# cicd-demo

A tiny FastAPI app for learning CI/CD with GitHub Actions.

## Run locally

```
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/health

## Checks

```
.venv/bin/ruff check .
.venv/bin/pytest
```
