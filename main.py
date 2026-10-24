from fastapi import FastAPI, HTTPException

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