from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db   
from app.models.external_jobs import ExternalJob
from app.models.resume import Resume
from app.services.recommendations import match_score

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.get("/{user_id}")
def recommend_jobs(user_id: int, db: Session = Depends(get_db)):
    resume = db.query(Resume).filter(Resume.user_id == user_id).first()

    if not resume:
        return {"message": "Resume not found"}

    jobs = db.query(ExternalJob).all()
    results = []

    for job in jobs:
        score = match_score(resume.raw_text, job.description)
        if score > 5:
            results.append({
                "job_id": job.id,
                "title": job.title,
                "company": job.company,
                "score": score
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:20]
