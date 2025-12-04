# Backend - FastAPI REST API

This directory contains the **FastAPI-powered backend** for the AI-Native Physical AI & Robotics Textbook.

## Quick Start

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e .

# Start server
uvicorn app.main:app --reload
```

**API Documentation**: http://localhost:8000/docs

## Structure

- `app/main.py` - FastAPI application entry point
- `app/api/` - API endpoints
- `app/config/` - Configuration management (see README there)
- `app/services/` - Business logic (Qdrant, OpenAI placeholders)
- `app/agents/` - AI agent orchestration (placeholder)
- `app/auth/` - Authentication (placeholder)
- `app/models/` - Database models (placeholder)
- `tests/` - Test suite (placeholder)

## Adding Features

### Create API Endpoint

```python
# app/api/example.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
async def example():
    return {"message": "Hello"}
```

Then include in `app/main.py`:
```python
from app.api.example import router
app.include_router(router, tags=["example"])
```

### Add Service

Create file in `app/services/` with business logic. See existing placeholders for examples.

## Testing

```bash
pytest
pytest --cov=app
pytest -v
```

## Configuration

See `app/config/README.md` for environment variable documentation.

## Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [Project README](../README.md)
