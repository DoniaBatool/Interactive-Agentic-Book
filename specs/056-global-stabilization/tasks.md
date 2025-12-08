# Implementation Tasks: Global Platform Stabilization & Cross-Chapter Consistency Layer

**Feature**: 056-global-stabilization  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. AI Block Rules Tasks

- [ ] **T001**: Create `backend/app/ai/runtime/ai_block_rules.py`
  - Define AI_BLOCK_RULES dictionary with:
    - Formatting rules (markdown, diagrams, quizzes)
    - Token usage rules (max tokens, context limits)
    - Retry/backoff rules (max retries, backoff delay)
    - Context limits (max context length)
  - TODO markers for real rule enforcement
  - File: `backend/app/ai/runtime/ai_block_rules.py`

---

### B. Multi-Chapter Router Tasks

- [ ] **T002**: Update `backend/app/ai/rag/pipeline.py` with chapter scoring switch
  - Add function: `score_chapters_for_query(query_embedding) -> List[Dict]`
  - TODO: Score all chapters by relevance
  - Placeholder: Return placeholder scores
  - File: `backend/app/ai/rag/pipeline.py` (update existing)

- [ ] **T003**: Update `backend/app/ai/rag/pipeline.py` with chapter affinity routing
  - Add function: `route_to_best_chapter(query) -> int`
  - TODO: Route to best matching chapter
  - Placeholder: Return placeholder chapter ID
  - File: `backend/app/ai/rag/pipeline.py` (update existing)

- [ ] **T004**: Update `backend/app/ai/rag/pipeline.py` with fallback retrieval
  - Add function: `fallback_retrieval(query) -> List[Dict]`
  - TODO: Fallback if primary routing fails
  - Placeholder: Return placeholder results
  - File: `backend/app/ai/rag/pipeline.py` (update existing)

---

### C. Collections Tasks

- [ ] **T005**: Create `backend/app/ai/rag/collections.py`
  - Define constants:
    - `CH1_COLLECTION_NAME = "chapter_1_embeddings"`
    - `CH2_COLLECTION_NAME = "chapter_2_embeddings"`
    - `CH3_COLLECTION_NAME = "chapter_3_embeddings"`
  - TODO: auto-select collection from query
  - TODO: iterate over all collections
  - File: `backend/app/ai/rag/collections.py`

---

### D. Formatting Layer Tasks

- [ ] **T006**: Create `backend/app/ai/formatters/__init__.py`
  - Make formatters a package
  - File: `backend/app/ai/formatters/__init__.py`

- [ ] **T007**: Create `backend/app/ai/formatters/response_formatter.py`
  - Add function: `format_markdown(text) -> str`
    - TODO: Normalize markdown formatting
    - Placeholder: Return text as-is
  - Add function: `format_diagram(diagram_data) -> str`
    - TODO: Format diagram (Mermaid, PlantUML)
    - Placeholder: Return placeholder diagram
  - Add function: `format_quiz(quiz_data) -> str`
    - TODO: Format quiz consistently
    - Placeholder: Return placeholder quiz
  - File: `backend/app/ai/formatters/response_formatter.py`

---

### E. Cross-Chapter Validation Tasks

- [ ] **T008**: Create `backend/app/content/validation/__init__.py`
  - Make validation a package
  - File: `backend/app/content/validation/__init__.py`

- [ ] **T009**: Create `backend/app/content/validation/chapter_consistency.py`
  - Add function: `validate_ai_block_consistency() -> Dict`
    - TODO: Check number of AI blocks per chapter
    - Placeholder: Return placeholder validation result
  - Add function: `validate_section_ordering() -> Dict`
    - TODO: Check section order consistency
    - Placeholder: Return placeholder validation result
  - Add function: `validate_glossary_structure() -> Dict`
    - TODO: Check glossary structure consistency
    - Placeholder: Return placeholder validation result
  - File: `backend/app/content/validation/chapter_consistency.py`

---

### F. Build Stability Tasks

- [ ] **T010**: Create `scripts/pre_build_check.py`
  - Add function: `check_mdx_presence() -> bool`
    - TODO: Check MDX files exist for all chapters
    - Placeholder: Return True
  - Add function: `check_metadata_presence() -> bool`
    - TODO: Check metadata exists for all chapters
    - Placeholder: Return True
  - Add function: `check_ai_block_presence() -> bool`
    - TODO: Check AI blocks exist for all chapters
    - Placeholder: Return True
  - Add main execution block
  - File: `scripts/pre_build_check.py`

---

### G. Documentation Tasks

- [ ] **T011**: Create `docs/global/stabilization.md`
  - Describe stabilization goals
  - Describe multi-chapter routing rules
  - Describe formatting unification
  - Describe validation strategy
  - File: `docs/global/stabilization.md`

---

### H. Validation Tasks

- [ ] **T012**: Backend starts without errors
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T013**: Build script exists and is executable
  - Verify: `python scripts/pre_build_check.py` runs without errors
  - Check: Script returns placeholder results

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All functions must be placeholder implementations
- No real rule enforcement logic should be implemented
- No real validation logic should be implemented
- No real formatting logic should be implemented
- All responses are static placeholders
- Pipeline updates should not break existing functionality

