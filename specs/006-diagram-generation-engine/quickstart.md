# Quickstart: AI Diagram Generation Engine

**Feature**: 006-diagram-generation-engine

## Prerequisites

- Feature 001 (Base Project) complete
- Feature 005 (AI Runtime Engine) complete
- Backend: Python 3.11+, FastAPI 0.109+
- Frontend: Node.js 18+, Docusaurus 3.x

## Verification Steps

### Step 1: Verify Backend Structure

```bash
# Check diagram provider files exist
ls backend/app/ai/diagrams/base_diagram_provider.py
ls backend/app/ai/diagrams/openai_diagram_provider.py
ls backend/app/ai/diagrams/gemini_diagram_provider.py
ls backend/app/ai/diagrams/pipeline.py

# Check template files exist
ls backend/app/ai/diagrams/templates/anatomy_robot.txt
ls backend/app/ai/diagrams/templates/physical_ai_overview.txt
ls backend/app/ai/diagrams/templates/ai_robotics_stack.txt
ls backend/app/ai/diagrams/templates/core_concepts_flow.txt

# Check API endpoint exists
ls backend/app/api/diagram_generation.py
```

### Step 2: Verify Frontend Component

```bash
# Check DiagramRenderer component exists
ls frontend/src/components/diagrams/DiagramRenderer.tsx
```

### Step 3: Test Backend Imports

```bash
cd backend
python -c "from app.ai.diagrams.base_diagram_provider import BaseDiagramProvider; print('OK')"
python -c "from app.ai.diagrams.pipeline import run_diagram_pipeline; print('OK')"
python -c "from app.api.diagram_generation import router; print('OK')"
```

### Step 4: Test Frontend Compilation

```bash
cd frontend
npm run build
# Should compile without errors
```

### Step 5: Start Backend Server

```bash
cd backend
uvicorn app.main:app --reload
# Should start without import errors
```

### Step 6: Test API Endpoint (Placeholder)

```bash
curl -X POST http://localhost:8000/api/diagram/generate \
  -H "Content-Type: application/json" \
  -d '{
    "diagramType": "anatomy_robot",
    "chapterId": 1,
    "concepts": ["sensors", "actuators"]
  }'
# Should return placeholder response: {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}
```

## Common Issues

### Issue 1: Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'app.ai.diagrams'`

**Solution**: 
- Verify `backend/app/ai/diagrams/__init__.py` exists
- Check Python path includes backend directory
- Restart backend server

### Issue 2: Frontend Compilation Errors

**Symptom**: TypeScript errors in DiagramRenderer.tsx

**Solution**:
- Verify component has proper TypeScript types
- Check imports are correct
- Run `npm install` to ensure dependencies are installed

### Issue 3: API Endpoint Not Found

**Symptom**: `404 Not Found` when calling `/api/diagram/generate`

**Solution**:
- Verify router is included in `backend/app/main.py`
- Check endpoint route is correct
- Restart backend server

## Architecture Understanding

### Diagram Generation Flow

1. **Request**: Frontend calls `POST /api/diagram/generate` with diagramType, chapterId, concepts
2. **API**: Endpoint validates request and calls `run_diagram_pipeline()`
3. **Pipeline**: Validates diagram type, builds prompt, calls provider
4. **Provider**: Generates diagram (placeholder currently)
5. **Response**: Returns SVG string to frontend
6. **Frontend**: DiagramRenderer component renders SVG

### Module Responsibilities

- **BaseDiagramProvider**: Abstract interface for all providers
- **OpenAIDiagramProvider**: OpenAI-specific implementation (scaffold)
- **GeminiDiagramProvider**: Gemini-specific implementation (scaffold)
- **Pipeline**: Orchestrates diagram generation flow
- **Templates**: Prompt templates for different diagram types
- **API Endpoint**: RESTful interface for diagram generation
- **DiagramRenderer**: Frontend component for rendering diagrams

## Next Steps

1. **Future Feature**: Implement real AI diagram generation
   - Add OpenAI API calls
   - Add Gemini API calls
   - Implement template processing
   - Add diagram validation

2. **Future Feature**: Enhance diagram rendering
   - Implement SVG rendering
   - Add Mermaid support
   - Add diagram caching
   - Add error handling

3. **Future Feature**: Add diagram types
   - Create new template files
   - Add new diagram type validation
   - Update API contract

