from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os
from app.db.session import get_db
from app.models.resume import Resume
from app.models.user import User
from app.services.resume_parser import parse_resume
from app.services.skill_extractor import extract_skills
from app.core.deps import get_current_user

router = APIRouter(prefix="/resume", tags=["Resume"])

UPLOAD_DIR = "uploads/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Extract text
    extracted_text = parse_resume(file_path)

    # Extract skills
    skills = extract_skills(extracted_text)

    # Save to DB ✅
    resume = Resume(
        user_id=current_user.id,
        file_path=file_path,
        raw_text=extracted_text,
        skills=",".join(skills) if skills else None
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume.id,
        "skills": skills
    }


from app.services.job_matcher import match_job
from app.models.job import Job

@router.get("/match-jobs")
def match_jobs(resume_skills: list[str], db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    results = []

    for job in jobs:
        job_skills = job.skills.split(",") if job.skills else []

        match_result = match_job(resume_skills, job_skills)

        results.append({
            "job_id": job.id,
            "title": job.title,
            "company": job.company_name,
            **match_result
        })

    return sorted(results, key=lambda x: x["match_percentage"], reverse=True)
