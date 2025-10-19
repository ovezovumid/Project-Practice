from fastapi import FastAPI

app = FastAPI(title="ML Service")

@app.get("/")
def read_root():
    return {"Hello": "From ML Service"}

@app.get("/health")
def health_check():
    return {"status": "ok"}