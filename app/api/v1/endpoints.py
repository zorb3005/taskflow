# app/api/v1/endpoints.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List  # Импортируем List
from app.infrastructure.db import get_db
from app.services.task_service import create_task, get_tasks, get_task, update_task
from app.schemas.task import TaskCreate, TaskUpdate, Task

router = APIRouter()

@router.post("/tasks/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/tasks/", response_model=List[Task])  # Теперь List определён
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, skip, limit)

@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return get_task(db, task_id)

@router.put("/tasks/{task_id}", response_model=Task)
def update_existing_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    return update_task(db, task_id, task_update)
