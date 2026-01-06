from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
from enum import Enum

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class CategoryEnum(str, Enum):
    work = "Работа"
    personal = "Личное"
    study = "Учеба"
    other = "Другое"

class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None
    priority: PriorityEnum = "medium"
    category: str
    important: bool = False
    completed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @field_validator('title')
    @classmethod
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()

    @field_validator('category')
    @classmethod
    def category_valid(cls, v):
        valid_categories = ["Работа", "Личное", "Учеба", "Другое"]
        if v not in valid_categories:
            raise ValueError(f'Category must be one of {valid_categories}')
        return v

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None
    priority: PriorityEnum = "medium"
    category: str
    important: bool = False

    @field_validator('category')
    @classmethod
    def category_valid(cls, v):
        valid_categories = ["Работа", "Личное", "Учеба", "Другое"]
        if v not in valid_categories:
            raise ValueError(f'Category must be one of {valid_categories}')
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    description: Optional[str] = None
    priority: Optional[PriorityEnum] = None
    category: Optional[str] = None
    important: Optional[bool] = None
    completed: Optional[bool] = None
