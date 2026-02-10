from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT
from app.db.base import Base

class ExternalJob(Base):
    __tablename__ = "external_jobs"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(50))
    job_id = Column(String(100), unique=True)
    title = Column(String(255))
    company = Column(String(255))
    description = Column(LONGTEXT)   
    skills = Column(String(500))
    url = Column(String(500))
