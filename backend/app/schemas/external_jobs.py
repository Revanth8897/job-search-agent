from pydantic import BaseModel
from typing import Optional

class ExternalJobBase(BaseModel):
    title: str
    company: str
    skills: Optional[str] = None
    url: str
    source: str


class ExternalJobResponse(ExternalJobBase):
    id: int
    job_id: str

    class Config:
        from_attributes = True   # SQLAlchemy → Pydantic
