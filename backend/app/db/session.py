from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


USERNAME = "root"
PASSWORD = quote_plus("Revanth@8897") 
HOST = "localhost"
PORT = "3306"
DB_NAME = "job_search_agent"


DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


