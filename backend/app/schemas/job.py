from pydantic import BaseModel
from typing import Optional, List

class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    skills: Optional[List[str]] = None
    company_name: str

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[List[str]] = None
    company_name: Optional[str] = None

class JobOut(JobBase):
    id: int
    recruiter_id: int

    class Config:
        from_attributes = True
