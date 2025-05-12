from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.services.task_service import get_tasks
from app.infrastructure.db import SessionLocal
from app.schemas.task import Task

app = FastAPI()

# Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = get_tasks(db=db, skip=skip, limit=limit)
    return tasks
