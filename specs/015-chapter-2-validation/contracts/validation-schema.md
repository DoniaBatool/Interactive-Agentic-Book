# Validation Schema: Chapter 2 Validation, Testing & Build Stability

**Feature**: 015-chapter-2-validation
**Created**: 2025-12-05
**Type**: Quality Assurance / Validation

## Overview

This contract defines the validation schema for Chapter 2 quality assurance. All validations follow a consistent structure and validate Chapter 2 content, metadata, AI-block integrations, RAG pipeline, embeddings, runtime engine, and build stability.

## Validation Categories

### 1. MDX Structure Validation

**File**: `frontend/docs/chapters/chapter-2.mdx`

**Validations**:
- ✅ Exactly 7 H2 sections
- ✅ 4 diagram placeholders (all kebab-case):
  - `ros2-ecosystem-overview`
  - `node-communication-architecture`
  - `topic-pubsub-flow`
  - `services-actions-comparison`
- ✅ 4 AI-block React components (all with `chapterId={2}`):
  - `<AskQuestionBlock chapterId={2} sectionId="..." />`
  - `<GenerateDiagramBlock diagramType="..." chapterId={2} />`
  - `<ExplainLike10Block concept="..." chapterId={2} />`
  - `<InteractiveQuizBlock chapterId={2} numQuestions={5} />`
- ✅ Glossary section with 7 placeholder terms:
  - ROS 2
  - Node
  - Topic
  - Service
  - Action
  - Package
  - Launch File
- ✅ YAML frontmatter completeness:
  - `title: "Chapter 2 — ROS 2 Fundamentals"`
  - `description: "..."` (non-empty)
  - `sidebar_position: 2`
  - `sidebar_label: "Chapter 2: ROS 2 Fundamentals"`
  - `tags: ["ros2", "robotics", "programming", "beginner"]`
- ✅ No broken Markdown syntax
- ✅ All content is placeholder comments (no real text)

**Validation Response**:
```json
{
  "valid": true,
  "section_count": 7,
  "diagram_count": 4,
  "ai_block_count": 4,
  "glossary_term_count": 7,
  "errors": [],
  "warnings": []
}
```

---

### 2. Metadata Consistency Validation

**File**: `backend/app/content/chapters/chapter_2.py`

**Validations**:
- ✅ `section_count: 7` matches actual MDX sections
- ✅ `sections: [...]` list has 7 items matching MDX H2 headings
- ✅ `ai_blocks: 4` matches MDX AI-block components
- ✅ `diagram_placeholders: 4` matches MDX diagram placeholders
- ✅ `glossary_terms: 7` matches MDX glossary terms
- ✅ `learning_outcomes: [...]` exists and is non-empty
- ✅ `prerequisites: [1]` is correct
- ✅ `id: 2` is correct
- ✅ `title: "Chapter 2 — ROS 2 Fundamentals"` matches MDX frontmatter
- ✅ All required fields present
- ✅ File imports without errors

**Validation Response**:
```json
{
  "valid": true,
  "section_count_match": true,
  "ai_blocks_match": true,
  "diagram_placeholders_match": true,
  "glossary_terms_match": true,
  "import_successful": true,
  "errors": [],
  "warnings": []
}
```

---

### 3. Chunk File Validation

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Validations**:
- ✅ File exists
- ✅ File imports without errors
- ✅ Function `get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]` exists
- ✅ Function signature is correct
- ✅ Function returns `List[Dict[str, Any]]` (placeholder return acceptable)
- ✅ No syntax errors

**Validation Response**:
```json
{
  "valid": true,
  "file_exists": true,
  "import_successful": true,
  "function_exists": true,
  "signature_correct": true,
  "errors": [],
  "warnings": []
}
```

---

### 4. RAG & Embedding Readiness Checks

**Files**:
- `backend/app/ai/rag/pipeline.py`
- `backend/app/ai/rag/qdrant_store.py`
- `backend/app/ai/embeddings/embedding_client.py`

**Validations**:
- ✅ `pipeline.py` can import `chapter_2_chunks`
- ✅ `qdrant_store.py` accepts collection name for Chapter 2
- ✅ `embedding_client.py` placeholder methods exist:
  - `generate_embedding(text: str) -> List[float]`
  - `batch_embed(chunks: List[str]) -> List[List[float]]`
- ✅ No missing imports
- ✅ No circular dependencies
- ✅ RAG pipeline can handle `chapter_id=2` parameter

**Validation Response**:
```json
{
  "valid": true,
  "pipeline_import_successful": true,
  "qdrant_collection_supported": true,
  "embedding_methods_exist": true,
  "no_circular_dependencies": true,
  "errors": [],
  "warnings": []
}
```

---

### 5. AI Runtime Routing Checks

**Files**:
- `backend/app/api/ai_blocks.py`
- `backend/app/ai/runtime/engine.py`

**Validations**:
- ✅ `ai_blocks.py` routes chapter-2 requests to runtime engine
- ✅ All four AI block types produce stub responses:
  - `ask-question` → returns placeholder JSON
  - `explain-el10` → returns placeholder JSON
  - `interactive-quiz` → returns placeholder JSON
  - `generate-diagram` → returns placeholder JSON
- ✅ Runtime engine can load Chapter 2 placeholders without error
- ✅ `chapterId=2` parameter is handled correctly

**Validation Response**:
```json
{
  "valid": true,
  "routing_works": true,
  "ask_question_stub_works": true,
  "explain_el10_stub_works": true,
  "interactive_quiz_stub_works": true,
  "generate_diagram_stub_works": true,
  "errors": [],
  "warnings": []
}
```

---

### 6. API Contract Testing

**Endpoints**:
- `POST /api/ai/blocks/ask-question`
- `POST /api/ai/blocks/explain-el10`
- `POST /api/ai/blocks/interactive-quiz`
- `POST /api/ai/blocks/generate-diagram`

**Validations**:
- ✅ All endpoints accept `chapterId=2` parameter
- ✅ All endpoints return valid JSON
- ✅ All endpoints return placeholder responses (no real logic required)
- ✅ Response structure matches expected schema

**Request Example**:
```json
{
  "question": "What is ROS 2?",
  "chapterId": 2,
  "sectionId": "introduction-to-ros2"
}
```

**Response Example** (Placeholder):
```json
{
  "message": "placeholder",
  "data": {}
}
```

**Validation Response**:
```json
{
  "valid": true,
  "ask_question_endpoint": "pass",
  "explain_el10_endpoint": "pass",
  "interactive_quiz_endpoint": "pass",
  "generate_diagram_endpoint": "pass",
  "errors": [],
  "warnings": []
}
```

---

### 7. Build Stability

**Frontend**:
- ✅ `npm run build` succeeds
- ✅ No build errors
- ✅ No build warnings (or acceptable warnings documented)

**Backend**:
- ✅ Server boots without import errors
- ✅ Server boots without runtime exceptions
- ✅ Import graph is stable (no circular dependencies)
- ✅ All imports resolve correctly

**Validation Response**:
```json
{
  "valid": true,
  "frontend_build": "pass",
  "backend_boot": "pass",
  "import_graph_stable": true,
  "errors": [],
  "warnings": []
}
```

---

## Validation Report Schema

**File**: `specs/015-chapter-2-validation/checklists/validation-report.md`

**Structure**:
```markdown
# Chapter 2 Validation Report

**Date**: YYYY-MM-DD
**Feature**: 015-chapter-2-validation

## Summary
- Total Validations: X
- Passed: Y
- Failed: Z
- Warnings: W

## Validation Results

### 1. MDX Structure Validation
- Status: PASS/FAIL
- Details: ...

### 2. Metadata Consistency Validation
- Status: PASS/FAIL
- Details: ...

### 3. Chunk File Validation
- Status: PASS/FAIL
- Details: ...

### 4. RAG & Embedding Readiness Checks
- Status: PASS/FAIL
- Details: ...

### 5. AI Runtime Routing Checks
- Status: PASS/FAIL
- Details: ...

### 6. API Contract Testing
- Status: PASS/FAIL
- Details: ...

### 7. Build Stability
- Status: PASS/FAIL
- Details: ...

## Recommendations
- ...
```

---

## Test Stub Schema

**File**: `tests/test_chapter_2_runtime.py`

**Structure**:
```python
import pytest
from app.api.ai_blocks import router
from app.content.chapters.chapter_2 import CHAPTER_METADATA

def test_chapter_2_metadata_imports():
    """Test that Chapter 2 metadata imports without errors."""
    assert CHAPTER_METADATA["id"] == 2
    assert CHAPTER_METADATA["section_count"] == 7

def test_ask_question_endpoint_stub():
    """Test ask-question endpoint returns placeholder JSON."""
    # TODO: Implement test stub
    pass

def test_explain_el10_endpoint_stub():
    """Test explain-el10 endpoint returns placeholder JSON."""
    # TODO: Implement test stub
    pass

def test_interactive_quiz_endpoint_stub():
    """Test interactive-quiz endpoint returns placeholder JSON."""
    # TODO: Implement test stub
    pass

def test_generate_diagram_endpoint_stub():
    """Test generate-diagram endpoint returns placeholder JSON."""
    # TODO: Implement test stub
    pass
```

---

## Validation Checklist

- [ ] MDX structure validation passes
- [ ] Metadata consistency validation passes
- [ ] Chunk file validation passes
- [ ] RAG & embedding readiness checks pass
- [ ] AI runtime routing checks pass
- [ ] API contract testing passes
- [ ] Frontend build succeeds
- [ ] Backend boots without errors
- [ ] Test stubs run without failure
- [ ] Validation report generated

---

## Notes

- All validations should use placeholder/stub responses where real logic is not yet implemented.
- Validation report should clearly indicate pass/fail status for each validation category.
- Test stubs should be minimal and focus on structure validation, not functionality testing.
- No new features should be implemented during validation phase.
