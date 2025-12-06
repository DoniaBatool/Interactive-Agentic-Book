# Data Model: Chapter 1 Quiz Engine

**Generated**: 2025-12-05
**Feature**: 007-ch1-quiz-engine

## Function Signatures

### Quiz Generator

```python
def generate_mcq(learning_outcomes: List[str]) -> List[Dict[str, Any]]:
    """
    Generate multiple choice questions from learning outcomes.
    
    Expected Input:
        learning_outcomes: List[str] - Learning objectives from chapter
    
    Expected Output:
        List of MCQ dictionaries:
        [
            {
                "id": str,                    # Question ID
                "question": str,               # Question text
                "options": List[str],         # Answer options (4 options)
                "correct_answer": str,         # Correct answer
                "explanation": str,           # Answer explanation
                "learning_outcome": str        # Related learning outcome
            },
            ...
        ]
    """
    # TODO: Implement MCQ generation
    return []
```

```python
def generate_true_false(learning_outcomes: List[str]) -> List[Dict[str, Any]]:
    """
    Generate true/false questions from learning outcomes.
    
    Expected Input:
        learning_outcomes: List[str] - Learning objectives from chapter
    
    Expected Output:
        List of true/false question dictionaries:
        [
            {
                "id": str,                    # Question ID
                "question": str,               # Question text
                "correct_answer": bool,        # True or False
                "explanation": str,           # Answer explanation
                "learning_outcome": str        # Related learning outcome
            },
            ...
        ]
    """
    # TODO: Implement true/false generation
    return []
```

```python
def generate_fill_blank(section_text: str) -> List[Dict[str, Any]]:
    """
    Generate fill-in-the-blank questions from section text.
    
    Expected Input:
        section_text: str - Text from chapter section
    
    Expected Output:
        List of fill-in-the-blank question dictionaries:
        [
            {
                "id": str,                    # Question ID
                "question": str,               # Question text with blanks
                "correct_answer": str,        # Correct answer
                "alternatives": List[str],    # Alternative acceptable answers
                "explanation": str,           # Answer explanation
                "section_id": str             # Source section ID
            },
            ...
        ]
    """
    # TODO: Implement fill-in-the-blank generation
    return []
```

### Quiz Validator

```python
def validate_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Validate user answer against correct answer.
    
    Expected Input:
        user_answer: str - User's answer
        correct_answer: str - Correct answer
    
    Expected Output:
        bool - True if answer is correct, False otherwise
    
    TODO: Implement answer validation
    TODO: Add case-insensitive matching
    TODO: Add fuzzy matching for partial credit
    """
    # TODO: Implement validation logic
    return False
```

```python
def score_quiz(answers_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Score quiz based on answer list.
    
    Expected Input:
        answers_list: [
            {
                "question_id": str,          # Question ID
                "user_answer": str,          # User's answer
                "correct_answer": str,       # Correct answer
                "is_correct": bool           # Validation result
            },
            ...
        ]
    
    Expected Output:
        {
            "total_questions": int,          # Total number of questions
            "correct_answers": int,         # Number of correct answers
            "incorrect_answers": int,        # Number of incorrect answers
            "score": float,                  # Score (0.0-1.0)
            "percentage": float              # Percentage score (0-100)
        }
    
    TODO: Implement scoring logic
    """
    # TODO: Implement scoring
    return {}
```

### Quiz Runtime

```python
async def run_quiz(chapter_id: int, num_questions: int) -> Dict[str, Any]:
    """
    Orchestrate quiz generation flow.
    
    Expected Input:
        chapter_id: int - Chapter identifier
        num_questions: int - Number of questions to generate
    
    Expected Output:
        {
            "questions": List[Dict[str, Any]],  # Generated questions
            "chapter_id": int,                  # Chapter ID
            "num_questions": int,               # Number of questions
            "metadata": Dict[str, Any]          # Additional metadata
        }
    
    Flow:
    1. Retrieve chapter chunks (RAG)
    2. Extract learning outcomes
    3. Generate questions (generator)
    4. Format questions (skills)
    5. Return structured quiz
    
    TODO: Implement orchestration
    """
    # TODO: Implement orchestration
    return {}
```

## API Request/Response Models

### Quiz Request (Existing)

```python
class QuizRequest(BaseModel):
    chapterId: int
    numQuestions: Optional[int] = 5
```

### Quiz Response (Updated)

```python
class QuizResponse(BaseModel):
    questions: List[Dict[str, Any]]  # Generated questions
    chapter_id: int
    num_questions: int
    metadata: Optional[Dict[str, Any]] = None
```

## Data Flow Contracts

### Quiz Generation Flow

1. **Request** → `POST /api/ai/quiz` → `QuizRequest`
2. **API** → `run_quiz(chapter_id, num_questions)` → Quiz Runtime
3. **Runtime** → `retrieve_quiz_context(chapter_id)` → RAG Pipeline
4. **Runtime** → `generate_mcq/generate_true_false/generate_fill_blank()` → Generator
5. **Runtime** → `format_mcq/format_true_false/format_fill_blank()` → Skills
6. **Runtime** → Returns structured quiz → API
7. **API** → Returns `QuizResponse` → Frontend

### Answer Validation Flow

1. **Request** → User submits answers
2. **Validator** → `validate_answer(user_answer, correct_answer)` → Boolean
3. **Validator** → `score_quiz(answers_list)` → Score dictionary
4. **Response** → Returns score and feedback

## Type Definitions

### Question Type Enum

```python
QuestionType = Literal["mcq", "true_false", "fill_blank"]
```

### Answer Format

```python
class Answer(BaseModel):
    question_id: str
    user_answer: str
    correct_answer: str
    is_correct: bool
```

