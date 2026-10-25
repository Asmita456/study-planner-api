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
