# Implementation Plan: Chapter 1 Quiz Engine — Question Generator, Validator, and Runtime

**Branch**: `007-ch1-quiz-engine` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/007-ch1-quiz-engine/spec.md`

## Summary

This feature creates the complete quiz engine scaffolding for Chapter 1 that generates quiz questions from chapter metadata, validates answers, and returns structured quiz results. The implementation establishes the architectural foundation for quiz generators (MCQ, true/false, fill-in-the-blank), validators (answer validation, scoring), runtime orchestrator, RAG pipeline integration, subagent updates, and formatting skills. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI quiz generation implementation.

**Primary Deliverable**: Complete quiz engine infrastructure scaffolding (generator, validator, runtime, skills, subagent updates, RAG hooks)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)

**Storage**:
- No persistent storage (scaffolding only)
- Future: Database for quiz questions and results

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend AI infrastructure scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no quiz generation)
- MUST maintain compatibility with Feature 005 (RAG pipeline, subagents, skills)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality

**Scale/Scope**:
- 6+ Python modules/files to create
- 2 files to update (quiz_agent.py, rag/pipeline.py, ai_blocks.py)
- ~400-600 lines of scaffolding code (mostly signatures and TODOs)
- 1 generator module, 1 validator module, 1 runtime module, 1 skill module

---

## 1. System Architecture

### Architecture Purpose

The quiz engine provides a unified system for generating quiz questions from chapter content, validating answers, and returning structured results. The system integrates with the existing RAG pipeline for context retrieval and uses subagents and skills for question generation and formatting.

### High-Level Data Flow

```
Frontend (Quiz Request)
  → POST /api/ai/quiz
  → Quiz Runtime Orchestrator
  → RAG Pipeline (Context Retrieval)
  → Quiz Generator (MCQ/TrueFalse/FillBlank)
  → Quiz Formatting Skills
  → Structured Quiz Response
  → Frontend
```

### Key Components

1. **Quiz Generator**: Generates questions (MCQ, true/false, fill-in-the-blank)
2. **Quiz Validator**: Validates answers and calculates scores
3. **Quiz Runtime**: Orchestrates quiz generation flow
4. **Quiz Agent**: Subagent blueprint for quiz generation
5. **Quiz Formatting Skill**: Formats questions for frontend
6. **RAG Integration**: Retrieves chapter context for question generation

### Integration Points

- **RAG Pipeline** (Feature 005): Retrieves chapter chunks and learning outcomes
- **Runtime Engine** (Feature 005): Routes quiz requests to quiz runtime
- **Subagents** (Feature 005): Quiz agent uses generator and validator
- **Skills** (Feature 005): Formatting skill formats questions
- **API Layer** (Feature 004): Quiz endpoint routes to quiz runtime

---

## 2. Module-Level Design

### 2.1 Quiz Generator Module

**File**: `backend/app/ai/quiz/generator.py`

**Purpose**: Generate quiz questions from learning outcomes and chapter content.

**Structure**:
```python
def generate_mcq(learning_outcomes: List[str]) -> List[Dict[str, Any]]:
    """
    Generate multiple choice questions from learning outcomes.
    
    TODO: Implement MCQ generation using LLM
    TODO: Use learning outcomes to generate relevant questions
    TODO: Generate 4 options per question with 1 correct answer
    TODO: Include distractors that are plausible but incorrect
    """
    # Placeholder return
    return []

def generate_true_false(learning_outcomes: List[str]) -> List[Dict[str, Any]]:
    """
    Generate true/false questions from learning outcomes.
    
    TODO: Implement true/false generation using LLM
    TODO: Use learning outcomes to generate clear true/false statements
    TODO: Ensure statements are unambiguous
    """
    # Placeholder return
    return []

def generate_fill_blank(section_text: str) -> List[Dict[str, Any]]:
    """
    Generate fill-in-the-blank questions from section text.
    
    TODO: Implement fill-in-the-blank generation using LLM
    TODO: Extract key concepts from section text
    TODO: Create blanks for important terms
    TODO: Generate alternative acceptable answers
    """
    # Placeholder return
    return []
```

**Responsibilities**:
- Generate questions from learning outcomes
- Generate questions from section text
- Return structured question data
- Support multiple question types

**Integration**: Called by quiz runtime orchestrator

---

### 2.2 Quiz Validator Module

**File**: `backend/app/ai/quiz/validator.py`

**Purpose**: Validate user answers and calculate quiz scores.

**Structure**:
```python
def validate_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Validate user answer against correct answer.
    
    TODO: Implement answer validation logic
    TODO: Add case-insensitive matching
    TODO: Add fuzzy matching for partial credit (future)
    TODO: Handle multiple acceptable answers
    """
    # Placeholder return
    return False

def score_quiz(answers_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Score quiz based on answer list.
    
    TODO: Implement scoring logic
    TODO: Calculate total questions, correct answers, incorrect answers
    TODO: Calculate score (0.0-1.0) and percentage (0-100)
    TODO: Add per-question scoring breakdown
    """
    # Placeholder return
    return {}
```

**Responsibilities**:
- Validate individual answers
- Calculate quiz scores
- Return structured score data
- Support different question types

**Integration**: Called by quiz runtime or API endpoint

---

### 2.3 Quiz Runtime Orchestrator

**File**: `backend/app/ai/quiz/runtime.py`

**Purpose**: Orchestrate the complete quiz generation flow.

**Structure**:
```python
async def run_quiz(chapter_id: int, num_questions: int) -> Dict[str, Any]:
    """
    Orchestrate quiz generation flow.
    
    Flow:
    1. Retrieve chapter chunks (RAG)
    2. Extract learning outcomes
    3. Generate questions (generator)
    4. Format questions (skills)
    5. Return structured quiz
    
    TODO: Implement orchestration logic
    TODO: Step 1: Call RAG pipeline to retrieve chapter context
    TODO: Step 2: Extract learning outcomes from chapter metadata
    TODO: Step 3: Call generator functions to generate questions
    TODO: Step 4: Call formatting skills to format questions
    TODO: Step 5: Return structured quiz response
    """
    # Placeholder return
    return {}
```

**Responsibilities**:
- Coordinate quiz generation flow
- Integrate with RAG pipeline
- Call generator functions
- Call formatting skills
- Return structured quiz

**Integration**: 
- Called by API endpoint
- Calls RAG pipeline
- Calls generator functions
- Calls formatting skills

---

### 2.4 Quiz Agent Subagent

**File**: `backend/app/ai/subagents/quiz_agent.py` (UPDATE existing file)

**Purpose**: High-level agent blueprint for quiz generation.

**Current Structure** (from Feature 005):
```python
async def quiz_agent(
    chapter_id: int,
    num_questions: int,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    # Existing placeholder
```

**Update Required**:
- Add TODO blueprint for generator selection
- Add TODO blueprint for returning structured results
- Update function to call quiz runtime
- Maintain existing function signature

**New Structure**:
```python
async def quiz_agent(
    chapter_id: int,
    num_questions: int,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Quiz generation agent blueprint.
    
    TODO: Implement generator selection logic
    TODO: Select appropriate generator based on question type distribution
    TODO: Call quiz runtime orchestrator
    TODO: Return structured quiz results
    """
    # TODO: Call quiz runtime
    # from app.ai.quiz.runtime import run_quiz
    # result = await run_quiz(chapter_id, num_questions)
    # return result
    
    # Placeholder return
    return {}
```

**Responsibilities**:
- Select appropriate generators
- Coordinate with quiz runtime
- Return structured quiz results
- Integrate with RAG context

**Integration**: Called by runtime engine for quiz blocks

---

### 2.5 Quiz Formatting Skill

**File**: `backend/app/ai/skills/quiz_formatting_skill.py` (NEW)

**Purpose**: Format quiz questions for frontend display.

**Structure**:
```python
def format_mcq(question_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format multiple choice question for frontend.
    
    TODO: Implement MCQ formatting
    TODO: Structure options for frontend display
    TODO: Add question metadata
    TODO: Format explanation
    """
    # Placeholder return
    return {}

def format_true_false(question_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format true/false question for frontend.
    
    TODO: Implement true/false formatting
    TODO: Structure for binary choice display
    TODO: Add question metadata
    TODO: Format explanation
    """
    # Placeholder return
    return {}

def format_fill_blank(question_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format fill-in-the-blank question for frontend.
    
    TODO: Implement fill-in-the-blank formatting
    TODO: Structure blanks for frontend display
    TODO: Add question metadata
    TODO: Format explanation and alternatives
    """
    # Placeholder return
    return {}
```

**Responsibilities**:
- Format questions for frontend
- Structure question data
- Add metadata
- Format explanations

**Integration**: Called by quiz runtime orchestrator

---

### 2.6 RAG Pipeline Integration

**File**: `backend/app/ai/rag/pipeline.py` (UPDATE existing file)

**Purpose**: Add TODO hooks for quiz context retrieval.

**Current Structure** (from Feature 005):
```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    # Existing placeholder
```

**Update Required**:
- Add TODO comment for quiz context retrieval
- Add TODO comment for quiz query embedding
- No breaking changes to existing functionality

**New Additions**:
```python
# TODO: retrieve_quiz_context(chapter_id)
# Function to retrieve chapter context specifically for quiz generation
# Should return learning outcomes, section text, and key concepts

# TODO: embed_quiz_query(question_text)
# Function to embed quiz question text for context matching
# Should use embedding client to generate query vector
```

**Responsibilities**:
- Provide quiz-specific context retrieval
- Support quiz query embedding
- Maintain existing RAG functionality

**Integration**: Called by quiz runtime orchestrator

---

## 3. File Paths

### Backend Structure

```
backend/app/
├── ai/
│   ├── quiz/                           # NEW: Quiz engine module
│   │   ├── __init__.py
│   │   ├── generator.py                 # Question generation
│   │   ├── validator.py                 # Answer validation and scoring
│   │   └── runtime.py                  # Orchestration
│   ├── rag/
│   │   └── pipeline.py                 # UPDATE: Add quiz hooks
│   ├── subagents/
│   │   └── quiz_agent.py               # UPDATE: Add generator selection
│   └── skills/
│       └── quiz_formatting_skill.py    # NEW: Question formatting
└── api/
    └── ai_blocks.py                     # UPDATE: Route to quiz runtime
```

### Specs Structure

```
specs/007-ch1-quiz-engine/
├── spec.md                              # ✅ Complete
├── plan.md                              # ✅ In progress
├── tasks.md                             # TODO
├── research.md                          # ✅ Complete
├── data-model.md                        # ✅ Complete
├── quickstart.md                        # ✅ Complete
├── checklists/
│   └── requirements.md                  # ✅ Complete
└── contracts/
    └── quiz-runtime.yaml                # ✅ Complete
```

---

## 4. Dependencies

### Internal Dependencies

- ✅ **Feature 001** (Base Project): Backend structure, FastAPI setup
- ✅ **Feature 004** (Chapter 1 Interactive Blocks): AI blocks API structure
- ✅ **Feature 005** (AI Runtime Engine): Runtime engine, RAG pipeline, subagents, skills

### External Dependencies

- ✅ **Python 3.11+**: Backend runtime
- ✅ **FastAPI 0.109+**: API framework
- ✅ **Pydantic 2.x**: Data validation

### Module Dependencies

- **Chapter Metadata Module**: For learning outcomes (future)
- **RAG Pipeline**: For context retrieval
- **Skills Architecture**: For formatting
- **Subagent Architecture**: For quiz agent

---

## 5. Success Criteria Mapping

| Success Criteria | Implementation Phase | Validation Method |
|------------------|---------------------|-------------------|
| **SC-001**: All scaffold modules exist | Generator, Validator, Runtime, Skills | File existence checks |
| **SC-002**: No real AI logic | All modules | Code review |
| **SC-003**: Backend starts successfully | All phases | Backend startup test |
| **SC-004**: API integration complete | API update | Endpoint routing test |
| **SC-005**: Documentation complete | ✅ Complete | File existence |

---

## 6. Risks

### Risk 1: Breaking Existing Features

**Risk**: Updates to existing files (quiz_agent.py, rag/pipeline.py, ai_blocks.py) may break existing functionality.

**Mitigation**: 
- Add new code as separate functions/comments
- Maintain existing function signatures
- Test all existing endpoints after updates
- No breaking changes to existing code

### Risk 2: Import Resolution Failures

**Risk**: New modules may have import errors.

**Mitigation**:
- Create all `__init__.py` files
- Test imports incrementally
- Fix errors immediately

### Risk 3: Interface Stability

**Risk**: Function signatures may need to change in future features.

**Mitigation**:
- Use comprehensive type hints
- Document expected input/output clearly
- Use placeholder return structures that match future implementation

### Risk 4: No Business Logic Allowed

**Risk**: Accidentally implementing real quiz generation logic.

**Mitigation**:
- All functions return placeholder values
- All logic marked with TODO comments
- Code review to ensure no real implementation

---

**Plan Generation Complete**: 2025-12-05
**Ready for Tasks**: Yes ✅

