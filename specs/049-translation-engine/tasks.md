# Task List: Multilingual Translation Engine

**Feature**: 049-translation-engine
**Created**: 2025-01-27
**Status**: Draft

## Task Groups

### 1. Provider Tasks

- [ ] **T049-001** (P1) - Create `backend/app/translation/providers/__init__.py`
  - Create package initialization file
  - File: `backend/app/translation/providers/__init__.py`

- [ ] **T049-002** (P1) - Create `backend/app/translation/providers/base_translation.py`
  - Define abstract base class BaseTranslationProvider
  - Define translate_text() abstract method
  - Define translate_batch() abstract method
  - Define supported_languages() abstract method
  - File: `backend/app/translation/providers/base_translation.py`

- [ ] **T049-003** (P1) - Create `backend/app/translation/providers/openai_translation.py`
  - Implement OpenAITranslationProvider (placeholder)
  - Implement translate_text() (placeholder)
  - Implement translate_batch() (placeholder)
  - Implement supported_languages() (returns ["en", "ur", "ru", "ar"])
  - Add TODO comments for real OpenAI translation API calls
  - File: `backend/app/translation/providers/openai_translation.py`

- [ ] **T049-004** (P1) - Create `backend/app/translation/providers/gemini_translation.py`
  - Implement GeminiTranslationProvider (placeholder)
  - Implement translate_text() (placeholder)
  - Implement translate_batch() (placeholder)
  - Implement supported_languages() (returns ["en", "ur", "ru", "ar"])
  - Add TODO comments for real Gemini translation API calls
  - File: `backend/app/translation/providers/gemini_translation.py`

### 2. Pipeline Tasks

- [ ] **T049-010** (P1) - Create `backend/app/translation/__init__.py`
  - Create package initialization file
  - File: `backend/app/translation/__init__.py`

- [ ] **T049-011** (P1) - Create `backend/app/translation/pipeline.py`
  - Implement translate_chapter(chapter_id, target_language) (placeholder)
  - Step 1: Normalize chapter content (TODO)
  - Step 2: Chunk paragraphs for translation (TODO)
  - Step 3: Route to provider (TODO)
  - Step 4: Reconstruct translated chapter (TODO)
  - Step 5: Return structured dict (placeholder)
  - Implement translate_snippet(text, target_language) (placeholder)
  - Add TODO comments for real implementation
  - File: `backend/app/translation/pipeline.py`

### 3. Glossary Support Tasks

- [ ] **T049-020** (P1) - Create `backend/app/translation/glossary_mapper.py`
  - Implement translate_glossary_term(term, target_language) (placeholder)
  - Create placeholder dictionary structure GLOSSARY_TRANSLATIONS
  - Add TODO comments for real glossary mapping
  - File: `backend/app/translation/glossary_mapper.py`

### 4. API Endpoints Tasks

- [ ] **T049-030** (P1) - Create `backend/app/api/translation.py`
  - Create FastAPI router
  - Implement POST /api/translate/chapter/{chapter_id} (placeholder)
  - Implement POST /api/translate/snippet (placeholder)
  - Implement GET /api/translation/languages (placeholder)
  - Add TODO comments for real implementation
  - File: `backend/app/api/translation.py`

- [ ] **T049-031** (P1) - Add translation routes to main FastAPI router
  - Import translation router
  - Include router in main app
  - File: `backend/app/main.py` or router file

### 5. Config Tasks

- [ ] **T049-040** (P1) - Update `backend/app/config/settings.py`
  - Add TRANSLATION_PROVIDER: Optional[str] = None
  - Add TRANSLATION_MODEL: Optional[str] = None
  - File: `backend/app/config/settings.py`

- [ ] **T049-041** (P1) - Update `.env.example`
  - Add TRANSLATION_PROVIDER=openai
  - Add TRANSLATION_MODEL=gpt-4o-mini
  - File: `.env.example`

### 6. Contract Tasks

- [ ] **T049-050** (P1) - Create `specs/049-translation-engine/contracts/translation-schema.yaml`
  - Define allowed language codes: en, ur, ru, ar
  - Define translation output structure
  - Define chapter translation output structure
  - Define error handling
  - File: `specs/049-translation-engine/contracts/translation-schema.yaml`

### 7. Runtime Integration Tasks

- [ ] **T049-060** (P2) - Update `backend/app/ai/runtime/engine.py`
  - Add TODO comment: "If translation needed, call translation pipeline before response"
  - Add placeholder for translation hook
  - File: `backend/app/ai/runtime/engine.py`

---

## Implementation Notes

### Scaffolding Only
- All tasks create scaffolding/placeholders only
- No real translation logic implementation
- TODO comments indicate future implementation

### Priority Levels
- **P1**: Critical for feature completion
- **P2**: Optional enhancements (runtime integration)

### File Paths
- All file paths are relative to project root
- Use exact paths as specified

### Testing
- Manual testing recommended after each task group
- Verify imports resolve
- Verify API endpoints respond (with mocked data)

---

## Acceptance Criteria Checklist

- [ ] All required modules exist
- [ ] No real translation logic is implemented (placeholders only)
- [ ] All imports resolve
- [ ] API endpoints respond successfully with mocked data
- [ ] Contracts/spec folder includes translation-schema.yaml
- [ ] Environment variables added
- [ ] Runtime integration stub added

