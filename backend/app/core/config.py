from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

USERNAME = "root"
PASSWORD = quote_plus("Revanth@8897")
HOST = "localhost"
PORT = "3306"
DB_NAME = "job_search_agent"

class Settings(BaseSettings):
    DATABASE_URL: str = (
        f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    )
    SECRET_KEY: str = "uygerafibdsjlvkcXNLkogf"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
