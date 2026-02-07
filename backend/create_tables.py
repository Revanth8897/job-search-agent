from app.db.session import engine
from app.db.base import Base
from app.models.user import User
from app.models.job import Job


Base.metadata.create_all(bind=engine)
