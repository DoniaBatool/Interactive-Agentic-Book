# Quickstart: Chapter 1 Diagram Generator Runtime

**Feature**: 008-chapter-1-diagram-runtime

## Prerequisites

- Feature 001 (Base Project) complete
- Feature 005 (AI Runtime Engine) complete
- Feature 006 (Diagram Generation Engine) complete
- Backend: Python 3.11+, FastAPI 0.109+

## Verification Steps

### Step 1: Verify Diagram Runtime Structure

```bash
# Check diagram runtime file exists
ls backend/app/ai/diagram/runtime.py

# Check diagram schema file exists
ls backend/app/ai/diagram/schema.py

# Check diagram agent updated
ls backend/app/ai/subagents/diagram_agent.py

# Check diagram skill exists
ls backend/app/ai/skills/diagram_skill.py

# Check RAG diagram retrieval exists
ls backend/app/ai/rag/diagram_retrieval.py
```

### Step 2: Test Backend Imports

```bash
cd backend
python -c "from app.ai.diagram.runtime import run_diagram_generator; print('OK')"
python -c "from app.ai.diagram.schema import DiagramRequest, DiagramNode, DiagramEdge, DiagramResponse; print('OK')"
python -c "from app.ai.subagents.diagram_agent import plan_diagram, create_structure, generate_svg_stub; print('OK')"
python -c "from app.ai.skills.diagram_skill import extraction_skill, layout_skill, svg_conversion_skill; print('OK')"
python -c "from app.ai.rag.diagram_retrieval import get_relevant_diagram_chunks; print('OK')"
```

### Step 3: Start Backend Server

```bash
cd backend
uvicorn app.main:app --reload
# Should start without import errors
```

### Step 4: Test API Endpoint (Placeholder)

```bash
curl -X POST http://localhost:8000/api/ai/diagram \
  -H "Content-Type: application/json" \
  -d '{
    "diagramType": "anatomy_robot",
    "chapterId": 1,
    "concepts": ["sensors", "actuators"]
  }'
# Should return placeholder response
```

## Common Issues

### Issue 1: Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'app.ai.diagram'`

**Solution**: 
- Verify `backend/app/ai/diagram/__init__.py` exists
- Check Python path includes backend directory
- Restart backend server

### Issue 2: API Endpoint Not Found

**Symptom**: `404 Not Found` when calling `/api/ai/diagram`

**Solution**:
- Verify router is included in `backend/app/main.py`
- Check endpoint route is correct
- Restart backend server

### Issue 3: Schema Validation Errors

**Symptom**: Pydantic validation errors

**Solution**:
- Verify schema models are properly defined
- Check request payload matches DiagramRequest model
- Ensure all required fields are provided

## Architecture Understanding

### Diagram Generation Flow

1. **Request**: Frontend calls `POST /api/ai/diagram` with diagramType, chapterId, concepts
2. **API**: Endpoint validates request and calls `run_diagram_generator()`
3. **Runtime**: Orchestrates validation → RAG retrieval → diagram agent → formatting
4. **Agent**: Plans → creates structure → generates SVG stub
5. **Skills**: Extract → layout → convert to SVG
6. **Response**: Returns structured diagram (nodes, edges, SVG)

### Module Responsibilities

- **Runtime**: Orchestrates diagram generation flow
- **Diagram Agent**: Plans, creates structure, generates SVG
- **Schema Models**: Type-safe data structures
- **Skills**: Extraction, layout, SVG conversion
- **RAG Retrieval**: Context retrieval for diagrams
- **API Integration**: Routes requests to runtime

## Next Steps

1. **Future Feature**: Implement real AI diagram generation
   - Add LLM calls for planning and structure creation
   - Implement SVG generation
   - Add layout algorithms

2. **Future Feature**: Enhance diagram types
   - Support more diagram types
   - Add diagram templates
   - Add diagram validation

3. **Future Feature**: Add diagram caching
   - Cache generated diagrams
   - Add diagram versioning
   - Add diagram editing

