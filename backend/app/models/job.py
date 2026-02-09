from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    skills = Column(String(500))
    company_name = Column(String(200))
    recruiter_id = Column(Integer)
