from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
from app.infrastructure.db import engine
from app.models import user, task

# Создание таблиц в БД
user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api/v1", tags=["tasks and users"])
