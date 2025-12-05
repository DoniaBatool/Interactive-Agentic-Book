# Quickstart Guide: Chapter 1 Interactive AI Blocks

**Feature**: 004-chapter-1-interactive-blocks
**Date**: 2025-12-05
**Audience**: Developers implementing or testing AI block components and API endpoints

## Overview

This guide walks you through using and testing the AI-interactive block components and API endpoints for Chapter 1. After completing these steps, you'll be able to:

- ✅ View AI block components rendered in Chapter 1
- ✅ Test component interactions (buttons, forms)
- ✅ Test backend API endpoints with curl/Postman
- ✅ Verify MDX component integration
- ✅ Understand the scaffolding structure for future AI integration

**Estimated Time**: 5 minutes

## Prerequisites

Before starting, ensure you have:

1. **Feature 001 (Base Project)** complete - Frontend and backend running
2. **Feature 003 (Chapter 1 Content)** complete - Chapter 1 MDX file with AI-BLOCK placeholders
3. **Frontend running**: `cd frontend && npm start` → `http://localhost:3000`
4. **Backend running**: `cd backend && uvicorn app.main:app --reload` → `http://localhost:8000`

## Step-by-Step Guide

### Step 1: View Components in Chapter 1

1. **Navigate to Chapter 1**:
   - Open browser: `http://localhost:3000/docs/chapters/chapter-1`
   - Or navigate via sidebar: "Learn" → "Chapter 1: Intro to Physical AI"

2. **Verify Components Render**:
   - Scroll through Chapter 1 content
   - You should see 4 AI block components in these locations:
     - **Ask Question Block**: After "What is Physical AI?" section
     - **Generate Diagram Block**: After "What is a Robot?" section
     - **Explain Like I'm 10 Block**: In "AI + Robotics = Physical AI Systems" section
     - **Interactive Quiz Block**: After "Core Concepts" section

3. **Check Component UI**:
   - Each component should display minimal UI (input fields, buttons, placeholders)
   - Components should have distinct styling (different background colors)
   - No React errors in browser console (F12 → Console tab)

### Step 2: Test Component Interactions

1. **Test Ask Question Block**:
   - Type a question in the textarea: "What is Physical AI?"
   - Click "Submit Question" button
   - Open browser console (F12 → Console)
   - Verify console.log output: `AskQuestionBlock: Question submitted { question: "...", chapterId: 1, sectionId: "..." }`

2. **Test Explain Like I'm 10 Block**:
   - Click "Explain in Simple Terms" button
   - Verify placeholder explanation appears
   - Check console.log output: `ExplainLike10Block: Explanation requested { concept: "autonomy", chapterId: 1 }`

3. **Test Interactive Quiz Block**:
   - Click "Start Quiz" button
   - Verify quiz placeholder appears
   - Check console.log output: `InteractiveQuizBlock: Quiz started { chapterId: 1, numQuestions: 5 }`

4. **Test Generate Diagram Block**:
   - Click "Generate Diagram" button
   - Verify diagram placeholder appears
   - Check console.log output: `GenerateDiagramBlock: Diagram generation requested { diagramType: "robot-anatomy", chapterId: 1 }`

**Expected Behavior**: All interactions log to console, no API calls are made (scaffolding phase).

### Step 3: Test Backend API Endpoints

1. **Test Ask Question Endpoint**:
   ```bash
   curl -X POST http://localhost:8000/api/ai/ask-question \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Physical AI?", "chapterId": 1, "sectionId": "what-is-physical-ai"}'
   ```

   **Expected Response**:
   ```json
   {
     "message": "AI block placeholder",
     "received": {
       "question": "What is Physical AI?",
       "chapterId": 1,
       "sectionId": "what-is-physical-ai"
     }
   }
   ```

2. **Test Explain Like 10 Endpoint**:
   ```bash
   curl -X POST http://localhost:8000/api/ai/explain-like-10 \
     -H "Content-Type: application/json" \
     -d '{"concept": "autonomy", "chapterId": 1}'
   ```

   **Expected Response**:
   ```json
   {
     "message": "AI block placeholder",
     "received": {
       "concept": "autonomy",
       "chapterId": 1
     }
   }
   ```

3. **Test Quiz Endpoint**:
   ```bash
   curl -X POST http://localhost:8000/api/ai/quiz \
     -H "Content-Type: application/json" \
     -d '{"chapterId": 1, "numQuestions": 5}'
   ```

   **Expected Response**:
   ```json
   {
     "message": "AI block placeholder",
     "received": {
       "chapterId": 1,
       "numQuestions": 5
     }
   }
   ```

4. **Test Diagram Endpoint**:
   ```bash
   curl -X POST http://localhost:8000/api/ai/diagram \
     -H "Content-Type: application/json" \
     -d '{"diagramType": "robot-anatomy", "chapterId": 1, "concepts": ["sensors", "actuators", "controllers"]}'
   ```

   **Expected Response**:
   ```json
   {
     "message": "AI block placeholder",
     "received": {
       "diagramType": "robot-anatomy",
       "chapterId": 1,
       "concepts": ["sensors", "actuators", "controllers"]
     }
   }
   ```

### Step 4: Verify API Documentation

1. **Open Swagger UI**:
   - Navigate to: `http://localhost:8000/docs`
   - Find "ai-blocks" tag section

2. **Verify Endpoints**:
   - Should see 4 endpoints:
     - `POST /api/ai/ask-question`
     - `POST /api/ai/explain-like-10`
     - `POST /api/ai/quiz`
     - `POST /api/ai/diagram`

3. **Test via Swagger UI**:
   - Click on any endpoint
   - Click "Try it out"
   - Fill in request body (use examples from Step 3)
   - Click "Execute"
   - Verify response matches expected format

### Step 5: Verify Code Structure

1. **Check Frontend Components**:
   ```bash
   # From project root
   ls frontend/src/components/ai/
   # Should see:
   # - AskQuestionBlock.tsx
   # - ExplainLike10Block.tsx
   # - InteractiveQuizBlock.tsx
   # - GenerateDiagramBlock.tsx
   # - README.md
   ```

2. **Check MDX Integration**:
   ```bash
   # Check MDX components file
   cat frontend/src/mdx-components.ts
   # Should export all 4 components
   
   # Check Chapter 1 MDX
   grep -n "AskQuestionBlock\|ExplainLike10Block\|InteractiveQuizBlock\|GenerateDiagramBlock" frontend/docs/chapters/chapter-1.mdx
   # Should show component usage
   ```

3. **Check Backend API**:
   ```bash
   # Check API file
   cat backend/app/api/ai_blocks.py
   # Should contain 4 endpoints with Pydantic models
   
   # Check main.py integration
   grep -n "ai_blocks" backend/app/main.py
   # Should show router inclusion
   ```

## Verification Checklist

Before proceeding to next features, verify:

- [ ] All 4 components render in Chapter 1 without React errors
- [ ] Component interactions log to console correctly
- [ ] All 4 API endpoints respond with placeholder JSON
- [ ] API endpoints validate request structure (try invalid requests)
- [ ] Swagger UI shows all endpoints correctly
- [ ] No real AI logic present (no OpenAI/Qdrant imports)
- [ ] All TODO comments present for future implementation
- [ ] Docusaurus build succeeds: `cd frontend && npm run build`

## Common Issues

### Issue 1: Components Not Rendering

**Symptoms**: Chapter 1 shows but no AI block components visible

**Solutions**:
- Check browser console for React errors
- Verify MDX imports: `grep "import.*Block" frontend/docs/chapters/chapter-1.mdx`
- Verify components exist: `ls frontend/src/components/ai/`
- Rebuild frontend: `cd frontend && npm run build`

### Issue 2: API Endpoints Return 404

**Symptoms**: `curl` returns 404 Not Found

**Solutions**:
- Verify backend is running: `curl http://localhost:8000/health`
- Check router integration: `grep "ai_blocks" backend/app/main.py`
- Verify endpoint paths: Check `backend/app/api/ai_blocks.py` for correct paths
- Restart backend: Stop and run `uvicorn app.main:app --reload` again

### Issue 3: TypeScript Compilation Errors

**Symptoms**: `npm run build` fails with type errors

**Solutions**:
- Check component prop interfaces match usage
- Verify all imports use correct paths (`@site/src/components/`)
- Check for missing type definitions
- Run type check: `cd frontend && npm run typecheck`

## Next Steps

Once scaffolding is verified:

1. **Review Implementation**: Check `specs/004-chapter-1-interactive-blocks/plan.md` for architecture details
2. **Read API Contracts**: Review `specs/004-chapter-1-interactive-blocks/contracts/ai-blocks-api.yaml`
3. **Understand Data Models**: Review `specs/004-chapter-1-interactive-blocks/data-model.md`
4. **Future Features**: Prepare for RAG integration (Feature 005+)

## Resources

- **Component Documentation**: `frontend/src/components/ai/README.md`
- **API Documentation**: `http://localhost:8000/docs` (Swagger UI)
- **Feature Spec**: `specs/004-chapter-1-interactive-blocks/spec.md`
- **Implementation Plan**: `specs/004-chapter-1-interactive-blocks/plan.md`
- **Research Notes**: `specs/004-chapter-1-interactive-blocks/research.md`

---

**Success!** 🎉 AI block components and API endpoints are scaffolded and ready for future AI integration.

