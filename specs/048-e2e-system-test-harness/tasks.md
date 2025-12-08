# Task List: End-to-End System Test Harness

**Feature**: 048-e2e-system-test-harness
**Created**: 2025-01-27
**Status**: Draft

## Task Groups

### 1. Test Infrastructure Tasks

- [ ] **T048-001** (P1) - Create `backend/tests/e2e/` folder
  - Create directory structure
  - File: `backend/tests/e2e/`

- [ ] **T048-002** (P1) - Create `backend/tests/e2e/__init__.py`
  - Create package initialization file
  - File: `backend/tests/e2e/__init__.py`

- [ ] **T048-003** (P1) - Create `backend/tests/e2e/conftest.py`
  - Add shared fixtures (placeholder)
  - Add TestClient setup for FastAPI (placeholder)
  - Add mock providers setup (placeholder)
  - Add mock Qdrant setup (placeholder)
  - Add mock embedding client setup (placeholder)
  - File: `backend/tests/e2e/conftest.py`

### 2. Chapter Content Validation Tasks

- [ ] **T048-010** (P1) - Create `backend/tests/e2e/test_chapter_1_content.py`
  - Add test_mdx_file_exists() (placeholder)
  - Add test_metadata_file_exists() (placeholder)
  - Add test_section_count() (placeholder)
  - Add test_placeholder_count() (placeholder)
  - Add test_metadata_fields() (placeholder)
  - File: `backend/tests/e2e/test_chapter_1_content.py`

- [ ] **T048-011** (P1) - Create `backend/tests/e2e/test_chapter_2_content.py`
  - Same structure as Chapter 1
  - Chapter 2 specific validations
  - File: `backend/tests/e2e/test_chapter_2_content.py`

- [ ] **T048-012** (P1) - Create `backend/tests/e2e/test_chapter_3_content.py`
  - Same structure as Chapter 1
  - Chapter 3 specific validations
  - File: `backend/tests/e2e/test_chapter_3_content.py`

### 3. RAG Pipeline Tests

- [ ] **T048-020** (P1) - Create `backend/tests/e2e/test_rag_pipeline.py`
  - Add test_chunk_loader() (placeholder)
  - Add test_embedding_generation() (placeholder, mocked)
  - Add test_qdrant_search() (placeholder, mocked)
  - Add test_context_assembly() (placeholder)
  - Add test_rag_pipeline_end_to_end() (placeholder)
  - File: `backend/tests/e2e/test_rag_pipeline.py`

### 4. AI Block Runtime Tests

- [ ] **T048-030** (P1) - Create `backend/tests/e2e/test_ai_blocks.py`
  - Add test_ask_question_routing() (placeholder)
  - Add test_explain_el10_routing() (placeholder)
  - Add test_quiz_routing() (placeholder)
  - Add test_diagram_routing() (placeholder)
  - Add test_response_structure() (placeholder)
  - Add test_all_chapters() (placeholder)
  - File: `backend/tests/e2e/test_ai_blocks.py`

### 5. Guardrail Tests

- [ ] **T048-040** (P1) - Create `backend/tests/e2e/test_guardrails.py`
  - Add test_input_safety_processing() (placeholder)
  - Add test_output_safety_enforcement() (placeholder)
  - Add test_prohibited_content_blocking() (placeholder)
  - Add test_hallucination_filter() (placeholder)
  - Add test_safety_logging() (placeholder)
  - File: `backend/tests/e2e/test_guardrails.py`

### 6. Build Stability Tests

- [ ] **T048-050** (P1) - Create `scripts/build_test.sh`
  - Add npm run build check (placeholder)
  - Add backend server startup check (placeholder)
  - Add import error check (placeholder)
  - Add runtime error check (placeholder)
  - File: `scripts/build_test.sh`

### 7. Test Report Contract

- [ ] **T048-060** (P1) - Create `specs/048-e2e-system-test-harness/contracts/test-report-format.md`
  - Define report structure
  - Define test result structure
  - Define coverage structure
  - File: `specs/048-e2e-system-test-harness/contracts/test-report-format.md`

---

## Implementation Notes

### Scaffolding Only
- All tasks create scaffolding/placeholders only
- No real test logic implementation
- TODO comments indicate future implementation

### Priority Levels
- **P1**: Critical for feature completion

### File Paths
- All file paths are relative to project root
- Use exact paths as specified

### Testing
- Manual testing recommended after each task group
- Verify tests run without errors (placeholders OK)
- Verify no import/runtime errors

---

## Acceptance Criteria Checklist

- [ ] All required test files created
- [ ] All tests run without logic (placeholders OK)
- [ ] Entire project builds cleanly under test harness
- [ ] No import/runtime error in RAG, runtime engine, metadata modules
- [ ] All chapters validated as per specification
- [ ] Test report format defined

