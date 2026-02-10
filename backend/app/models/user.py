from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
import enum
from sqlalchemy.orm import relationship

class RoleEnum(enum.Enum):
    candidate = "candidate"
    recruiter = "recruiter"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    
    resumes = relationship("Resume", back_populates="user")
