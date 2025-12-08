# Feature Specification: Multilingual Translation Engine — Urdu, Arabic, English, Roman Urdu

**Feature Branch**: `049-translation-engine`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-ai-translation-architecture
**Input**: User description: "Add a translation engine that enables all chapter content (MDX sections, glossary terms, explanations, quizzes, diagrams descriptions) to be translated into English (default), Urdu, Roman Urdu, and Arabic. Create translation APIs, provider abstraction, translation pipeline, translation glossary scaffolding, and runtime integration for future frontend UI usage."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Multilingual Content Access (Priority: P1)

As a user, I need to access chapter content in my preferred language (Urdu, Arabic, English, Roman Urdu), so I can learn effectively in my native language.

**Why this priority**: Multilingual support is essential for accessibility and user experience, especially for Urdu and Arabic speakers.

**Independent Test**: Can be fully tested by verifying translation APIs return translated content for all supported languages.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I request Chapter 1 content in Urdu, **Then** I receive translated MDX content in Urdu

2. **Given** the feature is implemented, **When** I request a glossary term translation, **Then** I receive the term translated to my selected language

3. **Given** the feature is implemented, **When** I request an AI block response translation, **Then** I receive the response translated to my selected language

4. **Given** the feature is implemented, **When** I request content in Roman Urdu, **Then** I receive content in Roman Urdu script

---

### User Story 2 - Developer Can Extend Translation (Priority: P1)

As a developer, I need a translation pipeline that supports multiple providers and languages, so I can easily add new languages or switch translation providers.

**Why this priority**: Flexibility is important for future expansion and provider selection.

**Independent Test**: Can be fully tested by verifying translation providers can be switched and new languages can be added.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I add a new language code, **Then** the translation pipeline supports it

2. **Given** the feature is implemented, **When** I switch translation providers, **Then** translations work with the new provider

---

### Edge Cases

- What happens when translation provider fails?
  - **Expected**: Return original content or error message
- What happens when language code is invalid?
  - **Expected**: Return error with valid language codes list
- What happens when content is too long for translation?
  - **Expected**: Chunk content and translate in batches

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Provider Architecture

- **FR-001.1**: System MUST create `backend/app/translation/providers/base_translation.py`:
  - Abstract base class for translation providers
  - Interface: `translate_text(text: str, target_language: str) -> str`
  - Interface: `translate_batch(texts: List[str], target_language: str) -> List[str]`
  - Interface: `supported_languages() -> List[str]`

- **FR-001.2**: System MUST create `backend/app/translation/providers/openai_translation.py`:
  - OpenAI provider implementation (placeholder)
  - Use OpenAI API for translation
  - Support languages: en, ur, ru, ar

- **FR-001.3**: System MUST create `backend/app/translation/providers/gemini_translation.py`:
  - Gemini provider implementation (placeholder)
  - Use Gemini API for translation
  - Support languages: en, ur, ru, ar

#### FR-002: Translation Pipeline

- **FR-002.1**: System MUST create `backend/app/translation/pipeline.py`:
  - Implement `translate_chapter(chapter_id: int, target_language: str) -> Dict[str, Any]`:
    - Step 1: Normalize chapter content
    - Step 2: Chunk paragraphs for translation
    - Step 3: Route to provider
    - Step 4: Reconstruct translated chapter
    - Step 5: Return structured dict
  - Implement `translate_snippet(text: str, target_language: str) -> str`:
    - Simple text translation
    - Use provider directly

#### FR-003: Translation Contracts

- **FR-003.1**: System MUST create `specs/049-translation-engine/contracts/translation-schema.yaml`:
  - Define allowed language codes: en, ur, ru, ar
  - Define translation output structure:
    ```yaml
    {
      "source": str,
      "translated": str,
      "language": str
    }
    ```

#### FR-004: Glossary Translation Support

- **FR-004.1**: System MUST create `backend/app/translation/glossary_mapper.py`:
  - Implement `translate_glossary_term(term: str, target_language: str) -> str` (placeholder)
  - Create placeholder dictionary structure for glossary translations
  - Support term-to-translation mapping

#### FR-005: API Endpoints

- **FR-005.1**: System MUST create `backend/app/api/translation.py`:
  - POST `/api/translate/chapter/{chapter_id}`:
    - Request: `{target_language: str}`
    - Response: Translated chapter content
  - POST `/api/translate/snippet`:
    - Request: `{text: str, target_language: str}`
    - Response: `{source: str, translated: str, language: str}`
  - GET `/api/translation/languages`:
    - Response: List of supported language codes

#### FR-006: Environment Variables

- **FR-006.1**: System MUST update `backend/app/config/settings.py`:
  - Add `TRANSLATION_PROVIDER: Optional[str] = None`
  - Add `TRANSLATION_MODEL: Optional[str] = None`

- **FR-006.2**: System MUST update `.env.example`:
  - Add `TRANSLATION_PROVIDER=openai`
  - Add `TRANSLATION_MODEL=gpt-4o-mini`

#### FR-007: Runtime Integration Stub

- **FR-007.1**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: "If translation needed, call translation pipeline before response"
  - Add placeholder for translation hook

## Non-Functional Requirements

### NFR-001: Performance
- Translation should complete in reasonable time (< 10 seconds per chapter)
- Batch translation should be efficient

### NFR-002: Reliability
- Translation failures should not break main functionality
- Fallback to original content if translation fails

### NFR-003: Maintainability
- Easy to add new languages
- Easy to switch providers
- Translation logic isolated from main code

## Acceptance Criteria

- [ ] All required modules exist
- [ ] No real translation logic is implemented (placeholders only)
- [ ] All imports resolve
- [ ] API endpoints respond successfully with mocked data
- [ ] Contracts/spec folder includes translation-schema.yaml
- [ ] Environment variables added
- [ ] Runtime integration stub added

## Success Message

Translation Engine scaffolding completed. Urdu, Arabic, English, and Roman Urdu translation pipelines, providers, contracts, glossary scaffolding, and API endpoints created successfully.

