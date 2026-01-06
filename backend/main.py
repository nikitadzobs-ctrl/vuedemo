from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import Task, TaskCreate, TaskUpdate
import json
from pathlib import Path
from datetime import datetime
from typing import List
import os

app = FastAPI(
    title="Task Manager API",
    description="API для управления задачами",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to data file
DATA_FILE = Path("tasks.json")

# Initialize data file if not exists
def init_data_file():
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps([], indent=2), encoding='utf-8')

# Read tasks from file
def read_tasks() -> List[dict]:
    try:
        content = DATA_FILE.read_text(encoding='utf-8')
        if not content:
            return []
        return json.loads(content)
    except Exception as e:
        print(f"Error reading tasks: {e}")
        return []

# Write tasks to file
def write_tasks(tasks: List[dict]):
    try:
        DATA_FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding='utf-8')
    except Exception as e:
        print(f"Error writing tasks: {e}")

# Get next ID
def get_next_id(tasks: List[dict]) -> int:
    if not tasks:
        return 1
    return max(task.get('id', 0) for task in tasks) + 1

@app.on_event("startup")
async def startup_event():
    init_data_file()

@app.get("/")
async def root():
    return {
        "name": "Task Manager API",
        "version": "1.0.0",
        "endpoints": [
            "GET /api/tasks",
            "GET /api/tasks/{id}",
            "POST /api/tasks",
            "PUT /api/tasks/{id}",
            "DELETE /api/tasks/{id}"
        ]
    }

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """Get all tasks"""
    tasks_data = read_tasks()
    return tasks_data

@app.get("/api/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Get a specific task by ID"""
    tasks_data = read_tasks()
    task = next((t for t in tasks_data if t.get('id') == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

@app.post("/api/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task_create: TaskCreate):
    """Create a new task"""
    tasks_data = read_tasks()
    
    task_dict = task_create.dict()
    task_dict['id'] = get_next_id(tasks_data)
    task_dict['completed'] = False
    task_dict['created_at'] = datetime.now().isoformat()
    task_dict['updated_at'] = datetime.now().isoformat()
    
    tasks_data.append(task_dict)
    write_tasks(tasks_data)
    
    return task_dict

@app.put("/api/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Update a task"""
    tasks_data = read_tasks()
    task_index = next((i for i, t in enumerate(tasks_data) if t.get('id') == task_id), None)
    
    if task_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    
    task = tasks_data[task_index]
    update_data = task_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        if value is not None:
            task[field] = value
    
    task['updated_at'] = datetime.now().isoformat()
    tasks_data[task_index] = task
    write_tasks(tasks_data)
    
    return task

@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """Delete a task"""
    tasks_data = read_tasks()
    task_index = next((i for i, t in enumerate(tasks_data) if t.get('id') == task_id), None)
    
    if task_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    
    tasks_data.pop(task_index)
    write_tasks(tasks_data)
    
    return None

@app.get("/api/stats")
async def get_stats():
    """Get tasks statistics"""
    tasks_data = read_tasks()
    completed = sum(1 for t in tasks_data if t.get('completed', False))
    pending = len(tasks_data) - completed
    
    return {
        "total": len(tasks_data),
        "completed": completed,
        "pending": pending
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
