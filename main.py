from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Literal


class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    subject: str = Field(min_length=2)
    priority: Literal["low", "medium", "high"]
    completed: bool = False
    estimated_minutes: int = Field(ge=1, le=480)


class TaskUpdate(BaseModel):
    title: str = Field(min_length=3)
    subject: str = Field(min_length=2)
    priority: Literal["low", "medium", "high"]
    completed: bool
    estimated_minutes: int = Field(ge=1, le=480)


app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Build calculator",
        "subject": "Python",
        "priority": "high",
        "completed": False,
        "estimated_minutes": 90
    },
    {
        "id": 2,
        "title": "Revise algebra",
        "subject": "Math",
        "priority": "medium",
        "completed": True,
        "estimated_minutes": 45
    },
    {
        "id": 3,
        "title": "Read API docs",
        "subject": "FastAPI",
        "priority": "high",
        "completed": False,
        "estimated_minutes": 60
    },
    {
        "id": 4,
        "title": "Practice loops",
        "subject": "Python",
        "priority": "low",
        "completed": False,
        "estimated_minutes": 30
    },
    {
        "id": 5,
        "title": "Solve equations",
        "subject": "Math",
        "priority": "high",
        "completed": True,
        "estimated_minutes": 75
    }
]

@app.get("/")
def home():
    return {"message" : "Welcome to Study Planner API"}

@app.get("/tasks")
def get_tasks(
    subject: str = None,
    completed: bool = None,
    search: str = None
):
    filtered_tasks = tasks

    if subject:
        filtered_tasks = [
            task for task in filtered_tasks
            if task["subject"].lower() == subject.lower()
        ]

    if completed is not None:
        filtered_tasks = [
            task for task in filtered_tasks
            if task["completed"] == completed
        ]

    if search:
        filtered_tasks = [
            task for task in filtered_tasks
            if search.lower() in task["title"].lower()
        ]

    return filtered_tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = task.model_dump()
    new_task["id"] = max(
        (item["id"] for item in tasks),
        default=0
    ) + 1

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_data.title
            task["subject"] = updated_data.subject
            task["priority"] = updated_data.priority
            task["completed"] = updated_data.completed
            task["estimated_minutes"] = updated_data.estimated_minutes

            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise HTTPException(status_code=404, detail="Task not found")