# Implementation Plan: End-to-End System Test Harness

**Branch**: `048-e2e-system-test-harness` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature creates a unified automated test harness that validates the entire AI Textbook System (Chapters 1, 2, and 3). Tests cover MDX compilation, AI Blocks routing, RAG retrieval pipelines, runtime engine stability, metadata correctness, build integrity, and end-to-end flow validation. **All implementations are scaffolding only**—placeholder tests, mocked providers, no real logic.

**Primary Deliverable**: Unified test harness with chapter content tests, RAG pipeline tests, AI block tests, guardrail tests, and build stability tests
**Validation**: All test files created, tests run without errors (placeholders OK), test report format defined

---

## 1. Test Infrastructure Architecture

### 1.1 Folder Structure

```
backend/tests/
└── e2e/
    ├── __init__.py
    ├── conftest.py (shared fixtures)
    ├── test_chapter_1_content.py
    ├── test_chapter_2_content.py
    ├── test_chapter_3_content.py
    ├── test_rag_pipeline.py
    ├── test_ai_blocks.py
    └── test_guardrails.py
```

### 1.2 Shared Fixtures

**Location**: `backend/tests/e2e/conftest.py`

**Fixtures**:
- `test_client`: FastAPI TestClient (placeholder)
- `mock_openai_provider`: Mock OpenAI provider
- `mock_gemini_provider`: Mock Gemini provider
- `mock_qdrant_client`: Mock Qdrant client
- `mock_embedding_client`: Mock embedding client

---

## 2. Chapter Content Validation Tests

### 2.1 Test Structure

**Location**: `backend/tests/e2e/test_chapter_{N}_content.py`

**Validations**:
- MDX file exists at `frontend/docs/chapters/chapter-{N}.mdx`
- Metadata file exists at `backend/app/content/chapters/chapter_{N}.py`
- Section count matches specification (7 for Ch1, varies for others)
- Placeholder count matches specification (AI-BLOCK, DIAGRAM)
- Metadata fields validated (ID, title match, glossary count)

**Test Functions** (Placeholder):
- `test_mdx_file_exists()`
- `test_metadata_file_exists()`
- `test_section_count()`
- `test_placeholder_count()`
- `test_metadata_fields()`

---

## 3. RAG Pipeline E2E Tests

### 3.1 Test Structure

**Location**: `backend/tests/e2e/test_rag_pipeline.py`

**Validations**:
- Chunk loader works (loads chapter chunks)
- Embedding generation works (mocked)
- Qdrant search works (mocked)
- Context assembly works
- No crashes with mocked providers

**Test Functions** (Placeholder):
- `test_chunk_loader()`
- `test_embedding_generation()`
- `test_qdrant_search()`
- `test_context_assembly()`
- `test_rag_pipeline_end_to_end()`

---

## 4. AI Block Runtime Tests

### 4.1 Test Structure

**Location**: `backend/tests/e2e/test_ai_blocks.py`

**Validations**:
- All 4 block types route correctly
- Response structure matches global contract
- All chapters work (1, 2, 3)
- Error handling works

**Test Functions** (Placeholder):
- `test_ask_question_routing()`
- `test_explain_el10_routing()`
- `test_quiz_routing()`
- `test_diagram_routing()`
- `test_response_structure()`
- `test_all_chapters()`

---

## 5. Guardrail Layer Tests

### 5.1 Test Structure

**Location**: `backend/tests/e2e/test_guardrails.py`

**Validations**:
- Guardrails receive input/output
- Prohibited content returns fallback
- Hallucination filter invoked (placeholder)
- Safety logging works (stub)

**Test Functions** (Placeholder):
- `test_input_safety_processing()`
- `test_output_safety_enforcement()`
- `test_prohibited_content_blocking()`
- `test_hallucination_filter()`
- `test_safety_logging()`

---

## 6. Build Stability Tests

### 6.1 Test Script

**Location**: `scripts/build_test.sh`

**Actions** (Placeholder):
- Run `npm run build` (frontend)
- Check backend server startup
- Validate no import errors
- Validate no runtime errors

---

## 7. Test Report Format

### 7.1 Report Structure

**Location**: `specs/048-e2e-system-test-harness/contracts/test-report-format.md`

**Components**:
- Test results summary
- Chapter coverage
- Component coverage
- Build status
- Summary message

---

## 8. Mocking Strategy

### 8.1 Provider Mocking

**OpenAI Provider**:
- Mock `generate()` to return placeholder response
- Mock API errors for error handling tests

**Gemini Provider**:
- Mock `generate()` to return placeholder response
- Mock API errors for error handling tests

### 8.2 Qdrant Mocking

**Qdrant Client**:
- Mock `similarity_search()` to return placeholder results
- Mock `upsert_vectors()` to return success
- Mock `create_collection()` to return success

### 8.3 Embedding Client Mocking

**Embedding Client**:
- Mock `generate_embedding()` to return placeholder vector
- Mock `batch_embed()` to return placeholder vectors

---

## 9. File Structure

```
backend/tests/
└── e2e/
    ├── __init__.py
    ├── conftest.py
    ├── test_chapter_1_content.py
    ├── test_chapter_2_content.py
    ├── test_chapter_3_content.py
    ├── test_rag_pipeline.py
    ├── test_ai_blocks.py
    └── test_guardrails.py

scripts/
└── build_test.sh

specs/048-e2e-system-test-harness/
├── contracts/
│   └── test-report-format.md
└── README.md
```

---

## 10. Risk Analysis

### 10.1 Top Risks

**Risk 1: Tests Too Slow**
- **Blast Radius**: All test execution
- **Mitigation**: Use mocks, run in parallel, optimize fixtures

**Risk 2: Flaky Tests**
- **Blast Radius**: Test reliability
- **Mitigation**: Deterministic mocks, no external dependencies

**Risk 3: Incomplete Coverage**
- **Blast Radius**: Missing validation
- **Mitigation**: Comprehensive test plan, regular review

---

## 11. Evaluation and Validation

### 11.1 Definition of Done

- [ ] All test files created
- [ ] All tests run without errors (placeholders OK)
- [ ] Build stability test works
- [ ] Test report format defined
- [ ] No import/runtime errors
- [ ] All chapters validated

### 11.2 Validation Criteria

- **Test Execution**: All tests run successfully
- **Coverage**: All chapters and components tested
- **Build**: Project builds cleanly
- **Reports**: Test reports generated correctly

