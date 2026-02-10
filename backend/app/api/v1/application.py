from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.base import Base
from app.db.session import get_db
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationResponse

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/", response_model=ApplicationResponse)
def apply_job(payload: ApplicationCreate, db: Session = Depends(get_db)):
    application = Application(**payload.dict())
    db.add(application)
    db.commit()
    db.refresh(application)
    return application



from typing import List

@router.get("/{user_id}", response_model=List[ApplicationResponse])
def get_user_applications(user_id: int, db: Session = Depends(get_db)):
    return db.query(Application).filter(Application.user_id == user_id).all()



from app.schemas.application import ApplicationUpdate

@router.put("/{app_id}", response_model=ApplicationResponse)
def update_status(app_id: int, payload: ApplicationUpdate, db: Session = Depends(get_db)):
    application = db.query(Application).filter(Application.id == app_id).first()
    application.status = payload.status
    db.commit()
    db.refresh(application)
    return application

