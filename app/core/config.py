# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_expiration: int
    database_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"  # Указываем кодировку файла .env

settings = Settings()
