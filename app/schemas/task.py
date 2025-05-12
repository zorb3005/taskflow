# app/schemas/task.py
from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    is_completed: Optional[bool] = None

class Task(TaskBase):
    id: int
    is_completed: bool

    class Config:
        orm_mode = True
