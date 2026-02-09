from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.jobs import router as job_router
from app.api.v1.resume import router as resume_router
from app.api.v1.resume import router as skill_extractor


app = FastAPI(title="Job Search Agent System")

app.include_router(auth_router)
app.include_router(job_router)
app.include_router(resume_router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
