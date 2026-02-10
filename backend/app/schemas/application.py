from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ---------- Base ----------
class ApplicationBase(BaseModel):
    user_id: int
    job_id: int

# ---------- Create ----------
class ApplicationCreate(ApplicationBase):
    pass

# ---------- Update ----------
class ApplicationUpdate(BaseModel):
    status: str

# ---------- Response ----------
class ApplicationResponse(ApplicationBase):
    id: int
    status: str
    applied_at: datetime

    class Config:
        from_attributes = True
