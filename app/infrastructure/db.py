from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Создаем строку подключения из переменной окружения
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Инициализируем движок базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создаем базовый класс для моделей
Base = declarative_base()

# Создаем сессию для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
