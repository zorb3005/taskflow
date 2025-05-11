# app/services/task_service.py
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        if task_update.title:
            task.title = task_update.title
        if task_update.description:
            task.description = task_update.description
        if task_update.is_completed is not None:
            task.is_completed = task_update.is_completed
        db.commit()
        db.refresh(task)
    return task
