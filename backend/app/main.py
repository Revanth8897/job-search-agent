from fastapi import FastAPI

app = FastAPI(title="Job Search Agent System")

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
