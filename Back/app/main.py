
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import os
import shutil
from typing import List

from database import SessionLocal, engine
import models
import schemas
import crud
from ml_model import PeopleCounter

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="People Counter", version="1.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

people_counter = PeopleCounter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#гл страница
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", "r") as f:
        return f.read()

@app.post("/analyze/")
async def analyze_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    is_video = file.filename.lower().endswith(('.mp4', '.avi', '.mov'))
    
    if is_video:
        result_data = people_counter.process_video_first_frame(file_path)
        file_type = "video"
    else:
        result_data = people_counter.process_image(file_path)
        file_type = "image"

    #сейв в бд
    db_result = schemas.AnalysisResultCreate(
        filename=file.filename,
        file_type=file_type,
        people_count=result_data["people_count"],
        confidence=result_data["confidence"]
    )
    
    created_result = crud.create_analysis_result(db, db_result)
    
    image_url = f"/static/results/{os.path.basename(result_data['image_path'])}"
    
    if os.path.exists(file_path):
        os.remove(file_path)
        ############################################################ dorabotka