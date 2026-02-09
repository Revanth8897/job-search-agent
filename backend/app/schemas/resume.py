from pydantic import BaseModel

class ResumeOut(BaseModel):
    id: int
    file_path: str

    class Config:
        from_attributes = True
