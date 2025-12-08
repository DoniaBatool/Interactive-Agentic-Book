# Test Report Format

**Feature**: 048-e2e-system-test-harness
**Created**: 2025-01-27
**Purpose**: Define test report structure for hackathon judges

## Report Structure

```yaml
TestReport:
  timestamp: string  # ISO 8601
  total_tests: int
  passed_tests: int
  failed_tests: int
  skipped_tests: int
  test_suites:
    - name: string
      tests: List[TestResult]
  coverage:
    chapters: Dict[int, ChapterCoverage]
    components: Dict[str, ComponentCoverage]
  build_status: "pass" | "fail"
  summary: string
```

## Test Result Structure

```yaml
TestResult:
  name: string
  status: "pass" | "fail" | "skip"
  duration_ms: float
  error_message: Optional[string]
  details: Dict[str, Any]
```

## Chapter Coverage

```yaml
ChapterCoverage:
  chapter_id: int
  content_validated: bool
  ai_blocks_tested: List[str]
  metadata_validated: bool
  sections_validated: bool
```

## Component Coverage

```yaml
ComponentCoverage:
  component_name: string
  tests_passed: int
  tests_total: int
  coverage_percentage: float
```

## Example Report

```json
{
  "timestamp": "2025-01-27T10:00:00Z",
  "total_tests": 50,
  "passed_tests": 48,
  "failed_tests": 2,
  "skipped_tests": 0,
  "test_suites": [
    {
      "name": "Chapter Content Validation",
      "tests": [...]
    },
    {
      "name": "RAG Pipeline",
      "tests": [...]
    },
    {
      "name": "AI Block Runtime",
      "tests": [...]
    },
    {
      "name": "Guardrails",
      "tests": [...]
    }
  ],
  "coverage": {
    "chapters": {
      "1": {"content_validated": true, "ai_blocks_tested": ["ask-question", "explain-like-el10", "interactive-quiz", "diagram-generator"]},
      "2": {...},
      "3": {...}
    },
    "components": {
      "rag_pipeline": {"tests_passed": 10, "tests_total": 10, "coverage_percentage": 100.0},
      "runtime_engine": {...},
      "guardrails": {...}
    }
  },
  "build_status": "pass",
  "summary": "48/50 tests passed. 2 failures in guardrail tests (expected - placeholder logic)."
}
```

