# Quickstart: Chapter 1 Quiz Engine

**Feature**: 007-ch1-quiz-engine

## Prerequisites

- Feature 001 (Base Project) complete
- Feature 005 (AI Runtime Engine) complete
- Backend: Python 3.11+, FastAPI 0.109+

## Verification Steps

### Step 1: Verify Quiz Module Structure

```bash
# Check quiz generator file exists
ls backend/app/ai/quiz/generator.py

# Check quiz validator file exists
ls backend/app/ai/quiz/validator.py

# Check quiz runtime file exists
ls backend/app/ai/quiz/runtime.py
```

### Step 2: Verify Skills and Subagents

```bash
# Check quiz formatting skill exists
ls backend/app/ai/skills/quiz_formatting_skill.py

# Check quiz agent updated
ls backend/app/ai/subagents/quiz_agent.py
```

### Step 3: Test Backend Imports

```bash
cd backend
python -c "from app.ai.quiz.generator import generate_mcq, generate_true_false, generate_fill_blank; print('OK')"
python -c "from app.ai.quiz.validator import validate_answer, score_quiz; print('OK')"
python -c "from app.ai.quiz.runtime import run_quiz; print('OK')"
python -c "from app.ai.skills.quiz_formatting_skill import format_mcq, format_true_false, format_fill_blank; print('OK')"
```

### Step 4: Start Backend Server

```bash
cd backend
uvicorn app.main:app --reload
# Should start without import errors
```

### Step 5: Test API Endpoint (Placeholder)

```bash
curl -X POST http://localhost:8000/api/ai/quiz \
  -H "Content-Type: application/json" \
  -d '{
    "chapterId": 1,
    "numQuestions": 5
  }'
# Should return placeholder response
```

## Common Issues

### Issue 1: Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'app.ai.quiz'`

**Solution**: 
- Verify `backend/app/ai/quiz/__init__.py` exists
- Check Python path includes backend directory
- Restart backend server

### Issue 2: API Endpoint Not Found

**Symptom**: `404 Not Found` when calling `/api/ai/quiz`

**Solution**:
- Verify router is included in `backend/app/main.py`
- Check endpoint route is correct
- Restart backend server

### Issue 3: RAG Integration Missing

**Symptom**: Quiz runtime cannot retrieve context

**Solution**:
- Verify RAG pipeline TODO hooks are present
- Check quiz runtime calls RAG functions correctly
- Ensure Feature 005 (AI Runtime Engine) is complete

## Architecture Understanding

### Quiz Generation Flow

1. **Request**: Frontend calls `POST /api/ai/quiz` with chapterId and numQuestions
2. **API**: Endpoint validates request and calls `run_quiz()`
3. **Runtime**: Orchestrates chunk retrieval → question generation → formatting
4. **Generator**: Generates questions (MCQ, true/false, fill-in-the-blank)
5. **Skills**: Formats questions for frontend
6. **Response**: Returns structured quiz

### Module Responsibilities

- **Generator**: Question generation functions (MCQ, true/false, fill-in-the-blank)
- **Validator**: Answer validation and scoring
- **Runtime**: Orchestrates quiz generation flow
- **Skills**: Question formatting utilities
- **Subagent**: Quiz agent blueprint
- **RAG Integration**: Context retrieval for question generation

## Next Steps

1. **Future Feature**: Implement real AI quiz generation
   - Add LLM calls for question generation
   - Implement answer validation logic
   - Add scoring algorithms

2. **Future Feature**: Enhance quiz types
   - Add more question types
   - Support adaptive difficulty
   - Add question bank storage

3. **Future Feature**: Add analytics
   - Track quiz performance
   - Analyze learning outcomes
   - Generate reports

