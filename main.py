from fastapi import FastAPI

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
def get_tasks():
    return tasks

