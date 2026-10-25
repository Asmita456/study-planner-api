from fastapi import FastAPI
from app.routers.tasks import router as tasks_router

app = FastAPI(title="Study Planner API")

app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def home():
    return {"message": "Welcome to Study Planner API"}