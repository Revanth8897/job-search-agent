from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.external_jobs import ExternalJob
from app.schemas.external_jobs import ExternalJobResponse
from app.services.external_jobs import fetch_remotive_jobs

router = APIRouter(prefix="/external-jobs", tags=["External Jobs"])


@router.post("/fetch")
def fetch_jobs(db: Session = Depends(get_db)):
    fetch_remotive_jobs(db)
    return {"message": "External jobs fetched successfully"}


@router.get("/", response_model=List[ExternalJobResponse])
def list_external_jobs(db: Session = Depends(get_db)):
    return db.query(ExternalJob).limit(50).all()
