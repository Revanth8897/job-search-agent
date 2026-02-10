from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    file_path = Column(String(255), nullable=False)
    raw_text = Column(Text, nullable=False)      # FULL resume text
    skills = Column(Text, nullable=True)         # comma-separated or JSON

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="resumes")
