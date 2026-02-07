from fastapi import FastAPI
from app.api.v1.auth import router as auth_router

app = FastAPI(title="Job Search Agent System")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
