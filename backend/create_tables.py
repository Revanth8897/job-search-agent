from app.db.session import engine
from app.db.base import Base
from app.models.user import User
from app.models.job import Job
from app.models.resume import Resume


Base.metadata.create_all(bind=engine)
