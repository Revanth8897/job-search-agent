import requests
from sqlalchemy.orm import Session
from app.models.external_jobs import ExternalJob

REMOTIVE_URL = "https://remotive.com/api/remote-jobs"

def fetch_remotive_jobs(db: Session):
    response = requests.get(REMOTIVE_URL)
    data = response.json()

    for job in data["jobs"]:
        exists = db.query(ExternalJob).filter(
            ExternalJob.job_id == str(job["id"])
        ).first()

        if exists:
            continue

        new_job = ExternalJob(
            source="remotive",
            job_id=str(job["id"]),
            title=job["title"],
            company=job["company_name"],
            description=job["description"],
            skills=",".join(job.get("tags", [])),
            url=job["url"]
        )

        db.add(new_job)

    db.commit()
