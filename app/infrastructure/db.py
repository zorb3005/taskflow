# app/infrastructure/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings  # настройки из .env

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # для SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Функция для создания сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
