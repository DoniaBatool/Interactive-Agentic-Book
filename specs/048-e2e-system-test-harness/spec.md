# Feature Specification: End-to-End System Test Harness for All Chapters

**Feature Branch**: `048-e2e-system-test-harness`
**Created**: 2025-01-27
**Status**: Draft
**Type**: testing-architecture
**Input**: User description: "Build a unified automated test harness that validates the entire AI Textbook System (Chapters 1, 2, and 3). Tests must cover MDX compilation, AI Blocks routing, RAG retrieval pipelines, runtime engine stability, metadata correctness, build integrity, and end-to-end flow validation."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - System Validation (Priority: P1)

As a developer, I need automated tests that validate the entire system works correctly, so I can catch regressions and ensure quality before deployment.

**Why this priority**: Without automated tests, regressions can slip through and break the system. E2E tests provide confidence that all components work together.

**Independent Test**: Can be fully tested by running the test harness and verifying all tests pass.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I run the test harness, **Then** all chapter content validation tests pass

2. **Given** the feature is implemented, **When** I run the test harness, **Then** all RAG pipeline tests pass (with mocked providers)

3. **Given** the feature is implemented, **When** I run the test harness, **Then** all AI block routing tests pass

4. **Given** the feature is implemented, **When** I run the test harness, **Then** all guardrail tests pass

5. **Given** the feature is implemented, **When** I run the test harness, **Then** build stability tests pass

---

### User Story 2 - Hackathon Judges Can Validate System (Priority: P1)

As a hackathon judge, I need a test report that shows the system works correctly, so I can evaluate the project's completeness and quality.

**Why this priority**: Hackathon judges need clear evidence that the system works. Test reports provide this evidence.

**Independent Test**: Can be fully tested by running the test harness and generating a test report.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I run the test harness, **Then** a test report is generated in the specified format

2. **Given** the feature is implemented, **When** I review the test report, **Then** it clearly shows which tests passed and which failed

3. **Given** the feature is implemented, **When** I review the test report, **Then** it includes coverage information for all chapters

---

### Edge Cases

- What happens when a test fails?
  - **Expected**: Test report shows failure with details, test harness continues with other tests
- What happens when mocked providers fail?
  - **Expected**: Tests handle gracefully, report failure, continue with other tests
- What happens when build fails?
  - **Expected**: Build stability test fails, test report shows build error

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Test Infrastructure Setup

- **FR-001.1**: System MUST create `backend/tests/e2e/` folder
- **FR-001.2**: System MUST create `backend/tests/e2e/conftest.py`:
  - Shared fixtures (placeholder only)
  - TestClient setup for FastAPI (placeholder)
  - Mock providers setup (placeholder)
  - Mock Qdrant setup (placeholder)

#### FR-002: Chapter Content Validation Tests

- **FR-002.1**: System MUST create `backend/tests/e2e/test_chapter_1_content.py`:
  - Validate MDX file exists
  - Validate metadata file exists
  - Validate section count correct (7 sections)
  - Validate placeholder count correct (AI-BLOCK, DIAGRAM)
  - Validate metadata field rules (ID, title match, glossary count)

- **FR-002.2**: System MUST create `backend/tests/e2e/test_chapter_2_content.py`:
  - Same validations as Chapter 1
  - Chapter 2 specific validations

- **FR-002.3**: System MUST create `backend/tests/e2e/test_chapter_3_content.py`:
  - Same validations as Chapter 1
  - Chapter 3 specific validations

#### FR-003: RAG Pipeline E2E Tests

- **FR-003.1**: System MUST create `backend/tests/e2e/test_rag_pipeline.py`:
  - Validate placeholder flow: chunk loader → embed → search → return context
  - Ensure no crash when embeddings provider is mocked
  - Ensure no crash when Qdrant is mocked
  - Validate context structure

#### FR-004: AI Block Runtime Tests

- **FR-004.1**: System MUST create `backend/tests/e2e/test_ai_blocks.py`:
  - Test 4 block types: ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram
  - Validate correct routing to runtime engine (structure only)
  - Validate response structure matches global contract
  - Test all chapters (1, 2, 3)

#### FR-005: Guardrail Layer Tests

- **FR-005.1**: System MUST create `backend/tests/e2e/test_guardrails.py`:
  - Validate guardrails receive input/output
  - Validate prohibited content returns fallback
  - Validate hallucination filter invoked (placeholder)
  - Validate safety logging works (stub)

#### FR-006: Build Stability Tests

- **FR-006.1**: System MUST create `scripts/build_test.sh` (placeholder):
  - Run: `npm run build` (frontend)
  - Run: backend server startup check
  - Validate no import errors
  - Validate no runtime errors

#### FR-007: Test Reports

- **FR-007.1**: System MUST create `specs/048-e2e-system-test-harness/contracts/test-report-format.md`:
  - Define report structure for judges
  - Include test results, coverage, pass/fail counts
  - No real logic, just format definition

## Non-Functional Requirements

### NFR-001: Performance
- Test harness must complete in reasonable time (< 5 minutes)
- Tests should run in parallel where possible

### NFR-002: Reliability
- Tests must be deterministic (same input = same output)
- Tests must not depend on external services (use mocks)

### NFR-003: Maintainability
- Tests must be easy to extend for new chapters
- Tests must be easy to update when contracts change

## Acceptance Criteria

- [ ] All required test files created
- [ ] All tests run without logic (placeholders OK)
- [ ] Entire project builds cleanly under test harness
- [ ] No import/runtime error in RAG, runtime engine, metadata modules
- [ ] All chapters validated as per specification
- [ ] Test report format defined
- [ ] Build stability test works

## Success Message

End-to-End System Test Harness scaffolding completed successfully. All chapters, AI blocks, RAG runtime, and guardrail layers now have unified system-level validation.

