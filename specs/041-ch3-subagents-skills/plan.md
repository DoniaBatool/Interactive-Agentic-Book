# Implementation Plan: Chapter 3 — Subagents + Skills Routing Integration

**Branch**: `041-ch3-subagents-skills` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/041-ch3-subagents-skills/spec.md` and Feature 024 (Chapter 2 Runtime Wiring) as reference pattern

## Summary

This feature adds subagent + skills scaffolding for Chapter 3 so that all four AI-interactive blocks (ask-question, explain-like-I-am-10, quiz, diagram) route through placeholder subagents and skills. **No business logic is implemented**—only placeholder scaffolding with TODO markers, following Chapter 2 subagents/skills patterns exactly.

**Primary Deliverable**: Complete subagent + skills scaffolding for Chapter 3
**Validation**: Backend starts without errors, all imports resolve, no real AI calls, API recognizes chapterId=3

---

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI
- Subagents: Python classes (scaffolding only)
- Skills: Python classes (scaffolding only)

**Primary Dependencies**:
- Feature 001 (Base Project Initialization) - Backend structure
- Feature 040 (Chapter 3 RAG + Runtime Integration) - RAG context available
- Feature 024 (Chapter 2 Runtime Wiring) - Reference pattern

**Storage**: 
- Subagents: Python files (ch3/ folder)
- Skills: Python files (ch3/ folder)
- Base interfaces: Python files (base_agent.py, base_skill.py)

**Testing**:
- Backend: `uvicorn app.main:app --reload` startup test
- Imports: Python import verification
- API: Manual API call with chapterId=3

**Target Platform**:
- Backend: FastAPI server (Python)

**Project Type**: Backend AI integration scaffolding

**Performance Goals**:
- Backend startup: < 5 seconds
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (scaffolding only)
- MUST NOT implement real subagent logic (placeholders only)
- MUST NOT implement real skills logic (placeholders only)
- MUST follow Chapter 2 subagents/skills patterns exactly
- MUST ensure backend boots successfully

**Scale/Scope**:
- 2 base interface files (base_agent.py, base_skill.py)
- 4 subagent files in ch3/ folder
- 3 skills files in ch3/ folder
- 1 runtime engine file updated (engine.py)
- 1 API file verified (ai_blocks.py)
- 1 contract document created

---

## 1. Folder Structure Layout

### 1.1 Subagents Folder Structure

**Directory**: `backend/app/ai/subagents/ch3/`
**Status**: Create new folder
**Files to Create**:
- `ask_question_agent.py`
- `explain_el10_agent.py`
- `quiz_agent.py`
- `diagram_agent.py`

### 1.2 Skills Folder Structure

**Directory**: `backend/app/ai/skills/ch3/`
**Status**: Create new folder
**Files to Create**:
- `retrieval_skill.py`
- `prompt_builder_skill.py`
- `formatting_skill.py`

### 1.3 Base Interface Files

**Directory**: `backend/app/ai/subagents/`
**File**: `base_agent.py`
**Status**: Create new file

**Directory**: `backend/app/ai/skills/`
**File**: `base_skill.py`
**Status**: Create new file

---

## 2. Subagent Responsibilities

### 2.1 Ask Question Agent

**File**: `backend/app/ai/subagents/ch3/ask_question_agent.py`
**Class**: `Ch3AskQuestionAgent`
**Inherits**: `BaseAgent`

**Responsibilities** (WHAT, not HOW):
- Answer questions about Physical AI concepts using Chapter 3 context
- Process questions with RAG context from Chapter 3 collection
- Generate formatted answers with source citations
- Return structured response

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

### 2.2 Explain ELI10 Agent

**File**: `backend/app/ai/subagents/ch3/explain_el10_agent.py`
**Class**: `Ch3ExplainEl10Agent`
**Inherits**: `BaseAgent`

**Responsibilities** (WHAT, not HOW):
- Generate simplified explanations of Physical AI concepts
- Use age-appropriate language (Explain Like I'm 10)
- Include analogies and real-world examples
- Return formatted explanation

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

### 2.3 Quiz Agent

**File**: `backend/app/ai/subagents/ch3/quiz_agent.py`
**Class**: `Ch3QuizAgent`
**Inherits**: `BaseAgent`

**Responsibilities** (WHAT, not HOW):
- Generate interactive quiz questions from Chapter 3 content
- Create diverse question types (multiple choice, true/false, short answer)
- Ensure questions cover learning objectives
- Return formatted quiz

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

### 2.4 Diagram Agent

**File**: `backend/app/ai/subagents/ch3/diagram_agent.py`
**Class**: `Ch3DiagramAgent`
**Inherits**: `BaseAgent`

**Responsibilities** (WHAT, not HOW):
- Generate visual diagrams for Physical AI concepts
- Create diagram descriptions/JSON for rendering
- Include diagram metadata
- Return formatted diagram

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

---

## 3. Skills Breakdown

### 3.1 Retrieval Skill

**File**: `backend/app/ai/skills/ch3/retrieval_skill.py`
**Class**: `Ch3RetrievalSkill`
**Inherits**: `BaseSkill`

**Purpose**: RAG context pulling for Chapter 3

**Methods** (Placeholder):
- `retrieve_content(query: str, chapter_id: int = 3, top_k: int = 5) -> List[Dict[str, Any]]`
- `retrieve_by_section(section_id: str, chapter_id: int = 3) -> List[Dict[str, Any]]`

**Flow** (Comment-only):
```
1. TODO: Call RAG pipeline with query and chapter_id=3
2. TODO: Filter chunks by section_id if provided
3. TODO: Return top-k most relevant chunks
```

### 3.2 Prompt Builder Skill

**File**: `backend/app/ai/skills/ch3/prompt_builder_skill.py`
**Class**: `Ch3PromptBuilderSkill`
**Inherits**: `BaseSkill`

**Purpose**: LLM prompt building for Chapter 3

**Methods** (Placeholder):
- `build_prompt(block_type: str, request_data: Dict[str, Any], context: Dict[str, Any]) -> str`
- `build_ask_question_prompt(question: str, context: str) -> str`
- `build_eli10_prompt(concept: str, context: str) -> str`
- `build_quiz_prompt(num_questions: int, context: str) -> str`
- `build_diagram_prompt(diagram_type: str, concepts: List[str], context: str) -> str`

**Flow** (Comment-only):
```
1. TODO: Select prompt template based on block_type
2. TODO: Inject context into prompt template
3. TODO: Add Physical AI-specific instructions
4. TODO: Return formatted prompt string
```

### 3.3 Formatting Skill

**File**: `backend/app/ai/skills/ch3/formatting_skill.py`
**Class**: `Ch3FormattingSkill`
**Inherits**: `BaseSkill`

**Purpose**: Structured response formatting for Chapter 3

**Methods** (Placeholder):
- `format_response(response: Dict[str, Any], block_type: str) -> Dict[str, Any]`
- `format_ask_question_response(answer: str, sources: List[str]) -> Dict[str, Any]`
- `format_eli10_response(explanation: str, analogies: List[str]) -> Dict[str, Any]`
- `format_quiz_response(questions: List[Dict]) -> Dict[str, Any]`
- `format_diagram_response(diagram: str, metadata: Dict) -> Dict[str, Any]`

**Flow** (Comment-only):
```
1. TODO: Select formatter based on block_type
2. TODO: Format response according to block type
3. TODO: Add metadata and structure
4. TODO: Return formatted response
```

---

## 4. Runtime Routing Design

### 4.1 Routing Map

**Flow**:
```
chapterId → blockType → subagent class
```

**Mapping**:
- `chapterId=3` + `blockType="ask-question"` → `Ch3AskQuestionAgent`
- `chapterId=3` + `blockType="explain-like-10"` → `Ch3ExplainEl10Agent`
- `chapterId=3` + `blockType="interactive-quiz"` → `Ch3QuizAgent`
- `chapterId=3` + `blockType="generate-diagram"` → `Ch3DiagramAgent`

### 4.2 Routing Pseudocode (Comment-only)

**File**: `backend/app/ai/runtime/engine.py`

**Location**: Inside `run_ai_block()` function

**Pseudocode**:
```python
# TODO: Chapter 3 routing
if chapter_id == 3:
    # TODO: Import Ch3 subagents
    # from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent
    # from app.ai.subagents.ch3.explain_el10_agent import Ch3ExplainEl10Agent
    # from app.ai.subagents.ch3.quiz_agent import Ch3QuizAgent
    # from app.ai.subagents.ch3.diagram_agent import Ch3DiagramAgent
    
    # TODO: Map block_type to Ch3*Agent classes
    # CH3_SUBAGENT_MAP = {
    #     "ask-question": Ch3AskQuestionAgent(),
    #     "explain-like-10": Ch3ExplainEl10Agent(),
    #     "interactive-quiz": Ch3QuizAgent(),
    #     "generate-diagram": Ch3DiagramAgent()
    # }
    
    # TODO: Get subagent from map
    # subagent = CH3_SUBAGENT_MAP.get(block_type)
    
    # TODO: Call RAG pipeline for Chapter 3 context
    # context = await run_rag_pipeline(query, chapter_id=3, top_k=5)
    
    # TODO: Call subagent with request_data + context
    # result = await subagent.run({**request_data, "context": context})
    
    # TODO: Return formatted response
    # return result
    
    pass
```

### 4.3 High-Level Flow Comments

**Flow** (Comment-only):
```
retrieval → prompt-building → formatting → LLM response
```

**Steps**:
1. TODO: Use retrieval_skill to get additional context if needed
2. TODO: Use prompt_builder_skill to construct LLM prompts
3. TODO: Call LLM provider with prompt + context
4. TODO: Use formatting_skill to format response
5. TODO: Return formatted response

---

## 5. Contract Document Planning

### 5.1 Contract Schema

**File**: `specs/041-ch3-subagents-skills/contracts/subagent-skill-contract.md`

**Content**:
- Expected inputs for each agent
- Expected outputs placeholder format
- Flow diagram (comment-only)
- TODO markers

**Structure**:
- Subagent Contract (4 agents)
- Skills Contract (3 skills)
- Runtime Routing Flow
- Base Interface Contracts

### 5.2 Interface Diagrams (ASCII)

**Flow Diagram** (Comment-only):
```
API Request (chapterId=3)
    │
    ▼
ai_blocks.py
    │
    ▼
engine.py::run_ai_block()
    │
    ├─► Check chapterId == 3
    │   │
    │   ├─► Map block_type to subagent
    │   ├─► Call RAG pipeline (chapter_id=3)
    │   ├─► Call subagent.run(request_data + context)
    │   │   │
    │   │   ├─► Use Ch3RetrievalSkill (if needed)
    │   │   ├─► Use Ch3PromptBuilderSkill
    │   │   ├─► Call LLM provider
    │   │   └─► Use Ch3FormattingSkill
    │   │
    │   └─► Return formatted response
    │
    └─► Response to frontend
```

---

## 6. Validation Plan

### 6.1 Backend Boot Validation

**Command**: `uvicorn app.main:app --reload`
**Expected**: Backend starts without errors
**Validation**: Check startup logs for import errors

### 6.2 Import Path Validation

**Tests**:
- `from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent`
- `from app.ai.skills.ch3.retrieval_skill import Ch3RetrievalSkill`
- `from app.ai.subagents.base_agent import BaseAgent`
- `from app.ai.skills.base_skill import BaseSkill`

**Expected**: All imports resolve successfully

### 6.3 Circular Import Validation

**Test**: Import all subagents and skills in sequence
**Expected**: No circular import errors

### 6.4 Chapter 3 Agent Class Loading

**Test**: Instantiate each Ch3*Agent class
**Expected**: Classes instantiate without errors

### 6.5 API Routing Validation

**Test**: Make API call with chapterId=3
**Expected**: Request routes to Chapter 3 placeholder logic (no errors)

---

## 7. Constraints

### 7.1 No Real Logic

- **Constraint**: MUST NOT implement real AI logic
- **Rationale**: This is scaffolding phase only
- **Implementation**: All logic is TODO comments and placeholder returns

### 7.2 No Real Subagent Logic

- **Constraint**: MUST NOT implement real subagent logic
- **Rationale**: Subagent implementation is future feature
- **Implementation**: Classes return empty dicts/lists

### 7.3 No Real Skills Logic

- **Constraint**: MUST NOT implement real skills logic
- **Rationale**: Skills implementation is future feature
- **Implementation**: Methods return empty values

### 7.4 Follow Chapter 2 Patterns

- **Constraint**: MUST follow Chapter 2 subagents/skills patterns exactly
- **Rationale**: Maintains consistency across chapters
- **Implementation**: Replicate Chapter 2 structure for Chapter 3

---

## 8. Success Criteria

- ✅ All subagent + skill scaffolding exists in correct paths
- ✅ Runtime engine successfully imports and routes to chapter 3 placeholder classes
- ✅ ai_blocks endpoints work with chapterId=3 without errors
- ✅ No AI logic implemented (strictly scaffolding)
- ✅ Backend server starts cleanly
- ✅ All file paths exist and are auto-wired correctly

---

## 9. Dependencies + Risks

### Dependencies:
- Feature 001: Base Project Initialization
- Feature 040: Chapter 3 RAG + Runtime Integration
- Feature 024: Chapter 2 Runtime Wiring (reference pattern)

### Risks:
1. **Risk**: Import errors if ch3/ folders not created correctly
   - **Mitigation**: Verify folders exist, test imports, test backend startup
2. **Risk**: Backend startup fails if syntax errors
   - **Mitigation**: Test backend startup after each file creation
3. **Risk**: Circular imports between base classes and subagents
   - **Mitigation**: Test imports in sequence, verify no circular dependencies

---

## Summary

This plan establishes the complete architecture for Chapter 3 subagents + skills integration. The implementation follows Chapter 2 subagents/skills patterns exactly, creates all necessary scaffolding files, and ensures backend starts successfully. All logic is placeholder-only—no real subagent, skills, or AI operations.

**Estimated Implementation Time**: 45-60 minutes (scaffolding only, no real AI logic)
**Complexity**: Low (following existing patterns, placeholder implementation)
**Dependencies**: Feature 001, Feature 040, Feature 024
**Out of Scope**: Real subagent implementation, real skills implementation, real AI logic

