from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate
from app.core.deps import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/", dependencies=[Depends(get_current_user)])
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_job = Job(
        **job.dict(),
        recruiter_id=current_user.id
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


@router.get("/")
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()


@router.put("/{job_id}")
def update_job(
    job_id: int,
    job_data: JobUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.recruiter_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    for key, value in job_data.dict(exclude_unset=True).items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job


@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.recruiter_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}
