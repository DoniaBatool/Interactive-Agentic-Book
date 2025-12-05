# Data Model: Chapter 1 Interactive AI Blocks

**Feature**: 004-chapter-1-interactive-blocks
**Date**: 2025-12-05
**Purpose**: Define component props interfaces, API request/response schemas, and data structures for AI block scaffolding

## Overview

This feature implements scaffolding for AI-interactive blocks with no persistent data storage or database schemas. The "data model" consists of:

1. **Frontend Component Props**: TypeScript interfaces for React component properties
2. **Backend API Schemas**: Pydantic models for request/response validation
3. **Component State**: Local React state (no global state management)

**Note**: No user data, database tables, or persistent storage exists in this phase. Future features will add actual data models for chat history, user preferences, etc.

## Frontend Component Props Schemas

### 1. AskQuestionBlock Props

**Purpose**: Define props for the question-asking component

**TypeScript Interface**:
```typescript
interface AskQuestionBlockProps {
  chapterId?: number;    // Optional chapter ID for context
  sectionId?: string;    // Optional section ID for context
}
```

**Field Descriptions**:
- `chapterId`: Chapter identifier (e.g., 1 for Chapter 1). Used for future RAG context retrieval.
- `sectionId`: Section identifier within chapter (e.g., "what-is-physical-ai"). Used for future section-specific context.

**Usage Example**:
```mdx
<AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />
```

**Future Enhancement**: Will add `userId`, `preferences`, `history` props for personalization.

### 2. ExplainLike10Block Props

**Purpose**: Define props for the simplified explanation component

**TypeScript Interface**:
```typescript
interface ExplainLike10BlockProps {
  concept?: string;      // Optional concept name to explain
  chapterId?: number;   // Optional chapter ID for context
}
```

**Field Descriptions**:
- `concept`: Concept name to explain (e.g., "autonomy", "embodiment"). Used for future LLM prompt generation.
- `chapterId`: Chapter identifier for context retrieval.

**Usage Example**:
```mdx
<ExplainLike10Block concept="autonomy" chapterId={1} />
```

**Future Enhancement**: Will add `ageLevel`, `difficulty`, `examples` props for customization.

### 3. InteractiveQuizBlock Props

**Purpose**: Define props for the quiz generation component

**TypeScript Interface**:
```typescript
interface InteractiveQuizBlockProps {
  chapterId?: number;     // Optional chapter ID for quiz generation
  numQuestions?: number; // Optional number of questions (default: 5)
}
```

**Field Descriptions**:
- `chapterId`: Chapter identifier for quiz content generation.
- `numQuestions`: Number of quiz questions to generate (default: 5).

**Usage Example**:
```mdx
<InteractiveQuizBlock chapterId={1} numQuestions={5} />
```

**Future Enhancement**: Will add `difficulty`, `questionTypes`, `timeLimit` props for customization.

### 4. GenerateDiagramBlock Props

**Purpose**: Define props for the diagram generation component

**TypeScript Interface**:
```typescript
interface GenerateDiagramBlockProps {
  diagramType?: string;  // Optional diagram type identifier
  chapterId?: number;    // Optional chapter ID for context
}
```

**Field Descriptions**:
- `diagramType`: Type of diagram to generate (e.g., "robot-anatomy", "ai-robotics-stack"). Used for future diagram generation logic.
- `chapterId`: Chapter identifier for context.

**Usage Example**:
```mdx
<GenerateDiagramBlock diagramType="robot-anatomy" chapterId={1} />
```

**Future Enhancement**: Will add `concepts`, `style`, `format` props for customization.

## Backend API Request/Response Schemas

### 1. AskQuestionRequest Model

**Purpose**: Request schema for ask-question endpoint

**Pydantic Model**:
```python
class AskQuestionRequest(BaseModel):
    question: str
    chapterId: Optional[int] = None
    sectionId: Optional[str] = None
```

**Field Descriptions**:
- `question`: Required question text from user
- `chapterId`: Optional chapter ID for context (matches frontend prop)
- `sectionId`: Optional section ID for context (matches frontend prop)

**Validation Rules**:
- `question`: Must be non-empty string (min length: 1)
- `chapterId`: Must be positive integer if provided
- `sectionId`: Must be non-empty string if provided

**Example Request**:
```json
{
  "question": "What is Physical AI?",
  "chapterId": 1,
  "sectionId": "what-is-physical-ai"
}
```

### 2. ExplainLike10Request Model

**Purpose**: Request schema for explain-like-10 endpoint

**Pydantic Model**:
```python
class ExplainLike10Request(BaseModel):
    concept: str
    chapterId: Optional[int] = None
```

**Field Descriptions**:
- `concept`: Required concept name to explain
- `chapterId`: Optional chapter ID for context

**Validation Rules**:
- `concept`: Must be non-empty string (min length: 1)
- `chapterId`: Must be positive integer if provided

**Example Request**:
```json
{
  "concept": "autonomy",
  "chapterId": 1
}
```

### 3. QuizRequest Model

**Purpose**: Request schema for quiz endpoint

**Pydantic Model**:
```python
class QuizRequest(BaseModel):
    chapterId: int
    numQuestions: Optional[int] = 5
```

**Field Descriptions**:
- `chapterId`: Required chapter ID for quiz generation
- `numQuestions`: Optional number of questions (default: 5)

**Validation Rules**:
- `chapterId`: Must be positive integer (required)
- `numQuestions`: Must be between 1 and 20 if provided

**Example Request**:
```json
{
  "chapterId": 1,
  "numQuestions": 5
}
```

### 4. DiagramRequest Model

**Purpose**: Request schema for diagram endpoint

**Pydantic Model**:
```python
class DiagramRequest(BaseModel):
    diagramType: str
    chapterId: Optional[int] = None
    concepts: Optional[List[str]] = []
```

**Field Descriptions**:
- `diagramType`: Required diagram type identifier
- `chapterId`: Optional chapter ID for context
- `concepts`: Optional list of concept names to include

**Validation Rules**:
- `diagramType`: Must be non-empty string
- `chapterId`: Must be positive integer if provided
- `concepts`: Must be list of non-empty strings

**Example Request**:
```json
{
  "diagramType": "robot-anatomy",
  "chapterId": 1,
  "concepts": ["sensors", "actuators", "controllers"]
}
```

### 5. AIBlockResponse Model

**Purpose**: Unified response schema for all AI block endpoints (placeholder)

**Pydantic Model**:
```python
class AIBlockResponse(BaseModel):
    message: str
    received: dict
```

**Field Descriptions**:
- `message`: Placeholder message indicating scaffolding phase
- `received`: Echo of received request payload

**Example Response**:
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

**Future Enhancement**: Will be replaced with actual response structures:
- `AskQuestionResponse`: `{ answer: str, sources: List[str], confidence: float }`
- `ExplainLike10Response`: `{ explanation: str, examples: List[str] }`
- `QuizResponse`: `{ questions: List[Question], answers: List[str] }`
- `DiagramResponse`: `{ diagramUrl: str, diagramType: str, metadata: dict }`

## Component State Models

### Frontend Component State

**AskQuestionBlock State**:
```typescript
const [question, setQuestion] = useState<string>('');
```

**ExplainLike10Block State**:
```typescript
const [explanation, setExplanation] = useState<string | null>(null);
```

**InteractiveQuizBlock State**:
```typescript
const [quizStarted, setQuizStarted] = useState<boolean>(false);
```

**GenerateDiagramBlock State**:
```typescript
const [diagramGenerated, setDiagramGenerated] = useState<boolean>(false);
```

**State Management Strategy**:
- Use React `useState` hook for local component state
- No global state management (Redux, Context) needed for scaffolding
- State is ephemeral (resets on component unmount)
- Future features may add global state for user preferences, chat history

## Relationships & Dependencies

### Frontend-Backend Mapping

```
Frontend Component Props          Backend Request Model
─────────────────────────         ──────────────────────
AskQuestionBlockProps             AskQuestionRequest
  chapterId?: number      ──────>  chapterId: Optional[int]
  sectionId?: string      ──────>  sectionId: Optional[str]
  (question from state)   ──────>  question: str

ExplainLike10BlockProps           ExplainLike10Request
  concept?: string        ──────>  concept: str
  chapterId?: number      ──────>  chapterId: Optional[int]

InteractiveQuizBlockProps         QuizRequest
  chapterId?: number      ──────>  chapterId: int
  numQuestions?: number   ──────>  numQuestions: Optional[int]

GenerateDiagramBlockProps         DiagramRequest
  diagramType?: string    ──────>  diagramType: str
  chapterId?: number      ──────>  chapterId: Optional[int]
```

**Key Points**:
1. Frontend props match backend request fields (naming consistency)
2. Optional props in frontend map to optional fields in backend
3. Frontend state (question, concept) becomes required fields in backend
4. All endpoints return unified `AIBlockResponse` format (placeholder)

### Component-API Flow

```
MDX File
  │
  ├─> Import Component
  │
  ├─> Render Component with Props
  │
  ├─> User Interaction (click, submit)
  │
  ├─> Event Handler (console.log)
  │
  └─> [Future] API Call
         │
         └─> Backend Endpoint
               │
               └─> Placeholder Response
                     │
                     └─> Component State Update
```

## Constraints & Invariants

### Invariants

1. **No Persistent Storage**: All state is ephemeral (component-level only)
2. **Optional Context**: All context props (chapterId, sectionId) are optional
3. **Placeholder Responses**: All backend endpoints return placeholder format
4. **No Real AI Logic**: No OpenAI/Qdrant calls, only console.log and placeholder responses
5. **Type Safety**: All props and request/response models are strongly typed

### Constraints

1. **Component Props**: Must be optional to allow standalone usage
2. **Request Validation**: Backend validates all request fields with Pydantic
3. **Response Format**: All endpoints return consistent `AIBlockResponse` structure
4. **MDX Integration**: Components must work with Docusaurus 3.x MDX processing
5. **No Dependencies**: No new external dependencies beyond existing React/FastAPI

## Future Evolution

**Phase 2 (Not in this feature)**:
- User data models (UserProfile, ChatHistory)
- Content models (Chapter, Section, Content)
- Vector storage models (Embedding, Document)
- Quiz result models (QuizAttempt, Score, Feedback)

**Phase 3 (Not in this feature)**:
- Database schemas (SQLAlchemy models)
- Data persistence (PostgreSQL tables)
- Relationship models (User → ChatHistory, Chapter → Content)
- Migration scripts (Alembic)

**Note**: This scaffolding phase establishes the API contracts and component interfaces. Future features will add actual data persistence and business logic on top of this foundation.

