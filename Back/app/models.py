from sqlalchemy import Column, Integer, String, DateTime, Float
from .db import Base
from datetime import datetime, timezone

class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_type = Column(String)
    people_count = Column(Integer)
    confidence = Column(Float)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    processing_time = Column(Float)
    image_path = Column(String)