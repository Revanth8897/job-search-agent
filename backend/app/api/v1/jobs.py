from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.job import Job
from app.schemas.job import JobCreate

router = APIRouter(prefix="/jobs", tags=["Jobs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(**job.dict(), recruiter_id=1)  # temp recruiter
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/")
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()
