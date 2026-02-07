from pydantic import BaseModel
from typing import Optional


class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    company_name: str


class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    company_name: Optional[str] = None


class JobOut(JobCreate):
    id: int

    class Config:
        from_attributes = True
