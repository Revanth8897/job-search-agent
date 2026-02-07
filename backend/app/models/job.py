from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(100))
    company_name = Column(String(255))
    recruiter_id = Column(Integer, ForeignKey("users.id"))
