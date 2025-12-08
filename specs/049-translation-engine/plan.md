# Implementation Plan: Multilingual Translation Engine

**Branch**: `049-translation-engine` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature creates a translation engine supporting Urdu, Arabic, English, and Roman Urdu. It includes provider abstraction, translation pipeline, glossary support, and API endpoints. **All implementations are scaffolding only**—no real translation logic, just structure for future implementation.

**Primary Deliverable**: Translation engine with providers, pipeline, glossary support, and API endpoints
**Validation**: All modules exist, imports resolve, API endpoints respond with mocked data

---

## 1. Multi-Provider Architecture

### 1.1 Base Translation Provider

**Location**: `backend/app/translation/providers/base_translation.py`

**Interface**:
- `translate_text(text: str, target_language: str) -> str`
- `translate_batch(texts: List[str], target_language: str) -> List[str]`
- `supported_languages() -> List[str]`

### 1.2 OpenAI Translation Provider

**Location**: `backend/app/translation/providers/openai_translation.py`

**Implementation** (Placeholder):
- Use OpenAI API for translation
- Support languages: en, ur, ru, ar
- TODO: Real OpenAI translation API calls

### 1.3 Gemini Translation Provider

**Location**: `backend/app/translation/providers/gemini_translation.py`

**Implementation** (Placeholder):
- Use Gemini API for translation
- Support languages: en, ur, ru, ar
- TODO: Real Gemini translation API calls

---

## 2. Language Code Rules

### 2.1 Supported Languages

- **en**: English (default)
- **ur**: Urdu (Arabic script)
- **ru**: Roman Urdu (Latin script)
- **ar**: Arabic (Arabic script)

### 2.2 Language Code Validation

- Validate language codes against supported list
- Return error if invalid code provided
- Default to "en" if not specified

---

## 3. Translation Pipeline Flow

### 3.1 Chapter Translation Flow

```
Chapter Content (MDX)
  ↓
Normalize Content
  ↓
Chunk Paragraphs
  ↓
Route to Provider
  ↓
Translate in Batches
  ↓
Reconstruct Chapter
  ↓
Return Translated Content
```

### 3.2 Snippet Translation Flow

```
Text Snippet
  ↓
Route to Provider
  ↓
Translate
  ↓
Return Translated Text
```

---

## 4. Translation Storage Strategy

**Current**: No persistent storage (placeholder only)

**Future Considerations**:
- Cache translated content
- Store translations in database
- Version control for translations

---

## 5. Glossary Translation Process

### 5.1 Glossary Mapping

**Location**: `backend/app/translation/glossary_mapper.py`

**Structure** (Placeholder):
```python
GLOSSARY_TRANSLATIONS = {
    "en": {
        "term": "definition"
    },
    "ur": {
        "term": "ترجمہ شدہ تعریف"
    },
    # ... etc
}
```

**Process**:
1. Load glossary term
2. Look up translation in dictionary
3. Return translated definition

---

## 6. API Architecture Design

### 6.1 Endpoints

**POST `/api/translate/chapter/{chapter_id}`**:
- Request: `{target_language: str}`
- Response: Translated chapter content

**POST `/api/translate/snippet`**:
- Request: `{text: str, target_language: str}`
- Response: `{source: str, translated: str, language: str}`

**GET `/api/translation/languages`**:
- Response: `{languages: List[str]}`

---

## 7. Runtime Integration

### 7.1 Integration Point

**Location**: `backend/app/ai/runtime/engine.py`

**Integration** (Placeholder):
- Add TODO comment for translation hook
- Placeholder for calling translation pipeline before response
- Future: Check if translation needed, call pipeline

---

## 8. Future UI Usage

### 8.1 Language Switcher

**Frontend Integration** (Future):
- Language selector component
- Store selected language in user preferences
- Request translations on language change
- Cache translations for performance

---

## 9. Error-Handling Strategies

### 9.1 Provider Failure

- Return original content if translation fails
- Log error for monitoring
- Provide fallback message

### 9.2 Invalid Language Code

- Return error with valid codes list
- HTTP 400 status

### 9.3 Content Too Long

- Chunk content into smaller pieces
- Translate in batches
- Reconstruct translated content

---

## 10. File Structure

```
backend/app/
├── translation/
│   ├── __init__.py
│   ├── pipeline.py
│   ├── glossary_mapper.py
│   └── providers/
│       ├── __init__.py
│       ├── base_translation.py
│       ├── openai_translation.py
│       └── gemini_translation.py
└── api/
    └── translation.py

specs/049-translation-engine/
├── contracts/
│   └── translation-schema.yaml
└── README.md
```

