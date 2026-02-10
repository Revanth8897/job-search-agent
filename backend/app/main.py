from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.jobs import router as job_router
from app.api.v1.resume import router as resume_router
from app.api.v1.external_jobs import router as external_jobs_router
from app.api.v1.recommendations import router as recommendations_router
from app.api.v1.application import router as application_router


app = FastAPI(title="Job Search Agent System")

# API Routers
app.include_router(auth_router)
app.include_router(job_router)
app.include_router(resume_router)
app.include_router(external_jobs_router)
app.include_router(recommendations_router)
app.include_router(application_router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
