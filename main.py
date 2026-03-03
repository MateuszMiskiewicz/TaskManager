from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()

tasks = {}
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    if find_task(task.id):
        raise HTTPException(status_code=400, detail="Task with this ID already exists")
    tasks.append(task.dict())
    return task


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task)
