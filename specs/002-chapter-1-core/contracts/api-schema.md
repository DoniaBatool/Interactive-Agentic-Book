# API Contracts: Chapter 1 Core Implementation

**Feature**: 002-chapter-1-core
**Date**: 2025-12-05
**Purpose**: Define API contracts, request/response schemas, and validation rules

## Overview

This document specifies the data contracts for Chapter 1 Core API endpoints, including request parameters, response schemas, error handling, and validation rules.

---

## API Endpoint Contracts

### 1. GET /chapters/{chapter_id}

**Description**: Retrieve metadata for a specific chapter by ID.

**HTTP Method**: GET

**URL Pattern**: `/chapters/{chapter_id}`

**Path Parameters**:
| Parameter | Type | Required | Constraints | Description |
|-----------|------|----------|-------------|-------------|
| chapter_id | integer | Yes | ≥ 1 | Chapter number (1, 2, 3, ...) |

**Query Parameters**: None

**Request Headers**:
| Header | Required | Example |
|--------|----------|---------|
| Accept | No | application/json |

**Request Body**: None (GET request)

---

**Success Response (HTTP 200)**:

**Content-Type**: `application/json`

**Schema**:
```json
{
  "chapter": integer,
  "title": string,
  "summary": string,
  "sections": array<string>
}
```

**Example**:
```json
{
  "chapter": 1,
  "title": "Introduction to Physical AI & Robotics",
  "summary": "Placeholder summary for Chapter 1 introduction",
  "sections": []
}
```

**Field Specifications**:
- `chapter`: Integer ≥ 1, matches requested chapter_id
- `title`: String, 10-200 characters
- `summary`: String, 50-1000 characters
- `sections`: Array of strings (can be empty for scaffolding)

---

**Error Response (HTTP 404 - Not Found)**:

**Content-Type**: `application/json`

**Schema**:
```json
{
  "detail": string
}
```

**Example**:
```json
{
  "detail": "Chapter not found"
}
```

**When Returned**:
- Requested chapter_id does not exist (e.g., chapter 999)
- Chapter has been deleted or archived (future)

---

**Error Response (HTTP 422 - Validation Error)**:

**Content-Type**: `application/json`

**Schema**:
```json
{
  "detail": [
    {
      "loc": array<string>,
      "msg": string,
      "type": string
    }
  ]
}
```

**Example**:
```json
{
  "detail": [
    {
      "loc": ["path", "chapter_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

**When Returned**:
- chapter_id is not a valid integer (e.g., "abc", "1.5")
- chapter_id is negative or zero

---

**cURL Example**:
```bash
# Success case
curl -X GET "http://localhost:8000/chapters/1" -H "accept: application/json"

# Not found case
curl -X GET "http://localhost:8000/chapters/999" -H "accept: application/json"

# Validation error case
curl -X GET "http://localhost:8000/chapters/abc" -H "accept: application/json"
```

**Python Example (requests library)**:
```python
import requests

response = requests.get("http://localhost:8000/chapters/1")
if response.status_code == 200:
    data = response.json()
    print(f"Chapter {data['chapter']}: {data['title']}")
elif response.status_code == 404:
    print("Chapter not found")
else:
    print(f"Error: {response.status_code}")
```

---

### 2. GET /chapters/

**Description**: Retrieve a list of all available chapters.

**HTTP Method**: GET

**URL Pattern**: `/chapters/`

**Path Parameters**: None

**Query Parameters**: None (future: pagination, filtering)

**Request Headers**:
| Header | Required | Example |
|--------|----------|---------|
| Accept | No | application/json |

**Request Body**: None (GET request)

---

**Success Response (HTTP 200)**:

**Content-Type**: `application/json`

**Schema**:
```json
[
  {
    "chapter": integer,
    "title": string,
    "summary": string,
    "sections": array<string>
  }
]
```

**Example**:
```json
[
  {
    "chapter": 1,
    "title": "Introduction to Physical AI & Robotics",
    "summary": "Placeholder summary for Chapter 1 introduction",
    "sections": []
  }
]
```

**Field Specifications**:
- Returns array of ChapterMetadata objects
- Array can be empty if no chapters exist
- Chapters returned in numerical order (1, 2, 3...)

---

**cURL Example**:
```bash
curl -X GET "http://localhost:8000/chapters/" -H "accept: application/json"
```

**Python Example**:
```python
import requests

response = requests.get("http://localhost:8000/chapters/")
chapters = response.json()
print(f"Total chapters: {len(chapters)}")
for chapter in chapters:
    print(f"  - Chapter {chapter['chapter']}: {chapter['title']}")
```

---

## Pydantic Model Definition

### ChapterMetadata Model

**Module**: `backend/app/models/chapter.py`

**Definition**:
```python
from typing import List
from pydantic import BaseModel, Field

class ChapterMetadata(BaseModel):
    """
    Metadata for a single chapter in the textbook.
    """

    chapter: int = Field(
        ...,
        description="Chapter number (e.g., 1, 2, 3)",
        ge=1,
        example=1
    )

    title: str = Field(
        ...,
        description="Full chapter title",
        min_length=10,
        max_length=200,
        example="Introduction to Physical AI & Robotics"
    )

    summary: str = Field(
        ...,
        description="Brief summary of chapter content",
        min_length=50,
        max_length=1000,
        example="Placeholder summary for Chapter 1 introduction"
    )

    sections: List[str] = Field(
        default_factory=list,
        description="List of section titles within the chapter",
        example=[]
    )

    class Config:
        schema_extra = {
            "example": {
                "chapter": 1,
                "title": "Introduction to Physical AI & Robotics",
                "summary": "Placeholder summary for Chapter 1 introduction",
                "sections": []
            }
        }
```

**Validation Rules**:
- `chapter`: Must be integer ≥ 1 (enforced by `ge=1`)
- `title`: Must be 10-200 characters (enforced by `min_length`, `max_length`)
- `summary`: Must be 50-1000 characters (enforced by `min_length`, `max_length`)
- `sections`: Default empty list if not provided

**Serialization**:
- Pydantic automatically serializes to JSON
- Datetime fields converted to ISO 8601 strings (future)
- None values excluded from response (future)

---

## Error Response Standards

### Error Schema

All errors follow FastAPI's standard error response format:

```json
{
  "detail": string | array<ValidationError>
}
```

**Simple Error** (404, 500):
```json
{
  "detail": "Chapter not found"
}
```

**Validation Error** (422):
```json
{
  "detail": [
    {
      "loc": ["path", "chapter_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

### HTTP Status Codes

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Successful retrieval of chapter(s) |
| 404 | Not Found | Chapter ID does not exist |
| 422 | Unprocessable Entity | Validation error (invalid chapter_id type) |
| 500 | Internal Server Error | Unexpected server error (future) |

---

## API Documentation (OpenAPI)

The API is documented using FastAPI's automatic OpenAPI generation:

**Swagger UI**: `http://localhost:8000/docs`
**ReDoc**: `http://localhost:8000/redoc`

**OpenAPI JSON**: `http://localhost:8000/openapi.json`

**Example OpenAPI Snippet**:
```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "AI Robotics Textbook API",
    "version": "0.1.0"
  },
  "paths": {
    "/chapters/{chapter_id}": {
      "get": {
        "summary": "Get chapter metadata",
        "operationId": "get_chapter",
        "parameters": [
          {
            "name": "chapter_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "minimum": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ChapterMetadata"
                }
              }
            }
          },
          "404": {
            "description": "Chapter not found"
          }
        }
      }
    }
  }
}
```

---

## Validation Checklist

### API Contract Validation

- [ ] All endpoints documented with request/response examples
- [ ] Path parameters typed and constrained (chapter_id ≥ 1)
- [ ] Success responses include all required fields
- [ ] Error responses follow standard format
- [ ] Status codes match HTTP semantics

### Pydantic Model Validation

- [ ] All fields have type annotations
- [ ] Required fields marked with `...`
- [ ] Optional fields have defaults
- [ ] Constraints specified (min_length, max_length, ge)
- [ ] Example data provided in Config

### Documentation Validation

- [ ] OpenAPI schema generated correctly
- [ ] Swagger UI displays all endpoints
- [ ] Example requests are valid cURL commands
- [ ] Response examples match actual API output

---

## Future API Endpoints (Out of Scope)

The following endpoints are **not implemented** in Feature 002 but documented for future reference:

### POST /chapters/{chapter_id}/embed
Generate and store embeddings for chapter content.

### GET /chapters/search?query={text}
Semantic search across all chapters.

### GET /chapters/{chapter_id}/related
Find chapters similar to the given chapter.

### GET /chapters/recommend?user_id={id}
Personalized chapter recommendations based on user progress.

### PATCH /chapters/{chapter_id}
Update chapter metadata (admin only).

### DELETE /chapters/{chapter_id}
Archive or delete a chapter (admin only).

---

## Summary

**2 API Endpoints Defined**:
1. `GET /chapters/{chapter_id}` - Retrieve single chapter
2. `GET /chapters/` - List all chapters

**1 Pydantic Model**:
- `ChapterMetadata` with 4 validated fields

**3 Error Types**:
- 404 Not Found
- 422 Validation Error
- 500 Internal Server Error (future)

**Key Contract Principles**:
- **Type Safety**: All fields strongly typed with Pydantic
- **Validation**: Constraints enforced at API boundary
- **Documentation**: OpenAPI auto-generated from code
- **Consistency**: All errors follow standard format
- **Extensibility**: Future endpoints planned but not implemented

---

**Next Steps**: Proceed to `quickstart.md` for step-by-step implementation guide.
