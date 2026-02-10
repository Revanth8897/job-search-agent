from app.db.session import engine
from app.db.base import Base
from app.models.user import User
from app.models.job import Job
from app.models.resume import Resume
from app.models.external_jobs import ExternalJob
from app.models.application import Application

Base.metadata.create_all(bind=engine)
print("Tables created")
