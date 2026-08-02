import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "DevMatch"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./devmatch.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

settings = Settings()
