from fastapi import FastAPI, HTTPException

app = FastAPI(title="cicd-demo")

TASKS = {1: "Learn CI", 2: "Learn CD"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return [{"id": task_id, "title": title} for task_id, title in TASKS.items()]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task_id, "title": TASKS[task_id]}
