from fastapi import APIRouter, HTTPException, status, Query
from app.schemas.task import TaskCreate, TaskUpdate

router = APIRouter()

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


@router.get("")
def get_tasks(
    subject: str = None,
    completed: bool = None,
    search: str = None,
    priority: str = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=20),
    sort_by: str = "title",
    order: str = "asc"
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

    if priority:
        filtered_tasks = [
            task for task in filtered_tasks
            if task["priority"] == priority
        ]

    if sort_by not in ["title", "estimated_minutes"]:
        raise HTTPException(
            status_code=400,
            detail="sort_by must be title or estimated_minutes"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="order must be asc or desc"
        )

    filtered_tasks = sorted(
        filtered_tasks,
        key=lambda task: task[sort_by],
        reverse=(order == "desc")
    )

    return filtered_tasks[skip:skip + limit]


@router.get("/summary")
def get_task_summary():
    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for task in tasks if task["completed"]
    )

    pending_tasks = total_tasks - completed_tasks

    total_estimated_minutes = sum(
        task["estimated_minutes"] for task in tasks
    )

    remaining_estimated_minutes = sum(
        task["estimated_minutes"]
        for task in tasks
        if not task["completed"]
    )

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "total_estimated_minutes": total_estimated_minutes,
        "remaining_estimated_minutes": remaining_estimated_minutes
    }

@router.get("/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@router.post("", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = task.model_dump()
    new_task["id"] = max(
        (item["id"] for item in tasks),
        default=0
    ) + 1

    tasks.append(new_task)
    return new_task


@router.put("/{task_id}")
def update_task(task_id: int, updated_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_data.model_dump())
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
