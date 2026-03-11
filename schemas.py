from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str

class Task(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: str
    completed: bool