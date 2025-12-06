# Quickstart: Chapter 2 Validation, Testing & Build Stability

**Feature**: 015-chapter-2-validation
**Created**: 2025-12-05
**Type**: Quality Assurance / Validation

## Prerequisites

1. **Feature Dependencies** (must be complete):
   - Feature 014: Chapter 2 Written Content — Structure, Metadata, Schema & Contracts
   - Feature 011: Chapter 2 AI Blocks Integration
   - Feature 012: Chapter 2 RAG Chunking, Embeddings & Qdrant Collection Setup
   - Feature 013: Chapter 2 AI Runtime Engine Integration

2. **Environment Setup**:
   - Frontend: Docusaurus installed and functional
   - Backend: FastAPI installed and functional
   - Python: 3.8+ with pytest available
   - Node.js: 16+ for frontend build

3. **Files Required**:
   - `frontend/docs/chapters/chapter-2.mdx`
   - `backend/app/content/chapters/chapter_2.py`
   - `backend/app/content/chapters/chapter_2_chunks.py`
   - `backend/app/api/ai_blocks.py`
   - `backend/app/ai/runtime/engine.py`
   - `backend/app/ai/rag/pipeline.py`

## Implementation Overview

This feature implements comprehensive validation for Chapter 2:
1. MDX structure validation
2. Metadata consistency validation
3. Chunk file validation
4. RAG & embedding readiness checks
5. AI runtime routing checks
6. API contract testing
7. Build stability validation
8. Validation report generation

**No new features are implemented** - only validation and testing.

## Step-by-Step Implementation

### Phase 1: MDX Structure Validation

1. **Validate MDX File Structure**:
   ```bash
   # Count H2 sections
   grep -c "^## " frontend/docs/chapters/chapter-2.mdx
   # Should return: 7
   
   # Count diagram placeholders
   grep -c "<!-- DIAGRAM:" frontend/docs/chapters/chapter-2.mdx
   # Should return: 4
   
   # Count AI-block components
   grep -c "chapterId={2}" frontend/docs/chapters/chapter-2.mdx
   # Should return: 4
   ```

2. **Validate YAML Frontmatter**:
   - Check `title`, `description`, `sidebar_position`, `sidebar_label`, `tags` exist
   - Verify values match expected format

3. **Validate Glossary**:
   - Check glossary section exists
   - Count glossary terms (should be 7)

### Phase 2: Metadata Consistency Validation

1. **Import Metadata**:
   ```python
   from app.content.chapters.chapter_2 import CHAPTER_METADATA
   
   # Verify import succeeds
   assert CHAPTER_METADATA["id"] == 2
   assert CHAPTER_METADATA["section_count"] == 7
   ```

2. **Compare with MDX**:
   - Compare `section_count` with actual MDX sections
   - Compare `ai_blocks` with MDX components
   - Compare `diagram_placeholders` with MDX placeholders
   - Compare `glossary_terms` with MDX glossary

3. **Validate Required Fields**:
   - Check all required fields present
   - Verify field types are correct

### Phase 3: Chunk File Validation

1. **Import Chunk File**:
   ```python
   from app.content.chapters.chapter_2_chunks import get_chapter_chunks
   
   # Verify import succeeds
   chunks = get_chapter_chunks(2)
   assert isinstance(chunks, list)
   ```

2. **Validate Function Signature**:
   - Check function exists
   - Verify signature is correct
   - Verify return type

### Phase 4: RAG & Embedding Readiness Checks

1. **Test Pipeline Import**:
   ```python
   from app.ai.rag.pipeline import run_rag_pipeline
   from app.content.chapters.chapter_2_chunks import get_chapter_chunks
   
   # Verify imports succeed
   # Verify pipeline can handle chapter_id=2
   ```

2. **Test Qdrant Collection**:
   - Verify `qdrant_store.py` accepts collection name for Chapter 2
   - Check collection name is "chapter_2"

3. **Test Embedding Methods**:
   ```python
   from app.ai.embeddings.embedding_client import generate_embedding, batch_embed
   
   # Verify methods exist (placeholder acceptable)
   ```

4. **Check for Circular Dependencies**:
   - Verify no circular imports
   - Check import graph is stable

### Phase 5: AI Runtime Routing Checks

1. **Test API Routing**:
   ```python
   from app.api.ai_blocks import router
   
   # Verify router exists
   # Verify routes are defined
   ```

2. **Test Runtime Engine**:
   ```python
   from app.ai.runtime.engine import run_ai_block
   
   # Verify function exists
   # Verify can handle chapter_id=2
   ```

3. **Test Stub Responses**:
   - Test all four AI block types return placeholder JSON
   - Verify chapterId=2 parameter is handled

### Phase 6: API Contract Testing

1. **Create Test Stubs**:
   ```bash
   # Create test file
   touch tests/test_chapter_2_runtime.py
   ```

2. **Add Test Stubs**:
   ```python
   import pytest
   from app.api.ai_blocks import router
   
   def test_ask_question_endpoint_stub():
       # TODO: Implement test stub
       pass
   
   def test_explain_el10_endpoint_stub():
       # TODO: Implement test stub
       pass
   
   def test_interactive_quiz_endpoint_stub():
       # TODO: Implement test stub
       pass
   
   def test_generate_diagram_endpoint_stub():
       # TODO: Implement test stub
       pass
   ```

3. **Run Test Stubs**:
   ```bash
   pytest tests/test_chapter_2_runtime.py -v
   ```

4. **Test API Endpoints**:
   - Test `/api/ai/blocks/ask-question` with chapterId=2
   - Test `/api/ai/blocks/explain-el10` with chapterId=2
   - Test `/api/ai/blocks/interactive-quiz` with chapterId=2
   - Test `/api/ai/blocks/generate-diagram` with chapterId=2
   - Verify all return valid JSON

### Phase 7: Build Stability

1. **Test Frontend Build**:
   ```bash
   cd frontend
   npm run build
   # Verify build succeeds
   ```

2. **Test Backend Boot**:
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload
   # Verify server starts without errors
   ```

3. **Check Import Graph**:
   - Verify no circular dependencies
   - Check all imports resolve correctly

### Phase 8: Validation Report Generation

1. **Run All Validations**:
   - Execute all validation checks
   - Collect results

2. **Generate Report**:
   - Update `specs/015-chapter-2-validation/checklists/validation-report.md`
   - Fill in all validation results
   - Add recommendations

3. **Verify All Pass**:
   - Check all validations pass
   - Address any failures
   - Re-run validations until all pass

## Validation Checklist

- [ ] MDX structure validation passes
- [ ] Metadata consistency validation passes
- [ ] Chunk file validation passes
- [ ] RAG & embedding readiness checks pass
- [ ] AI runtime routing checks pass
- [ ] API contract testing passes
- [ ] Frontend build succeeds
- [ ] Backend boots without errors
- [ ] Test stubs run without failure
- [ ] Validation report generated

## Success Criteria

1. ✅ All MDX structure validations pass
2. ✅ All metadata consistency validations pass
3. ✅ Chunk file validation passes
4. ✅ RAG pipeline readiness checks pass
5. ✅ AI runtime routing checks pass
6. ✅ All API endpoints return valid JSON
7. ✅ Frontend build succeeds
8. ✅ Backend boots without errors
9. ✅ Test stubs run without failure
10. ✅ Validation report generated with all results

## Troubleshooting

### Issue: MDX Structure Validation Fails

**Symptoms**: Section count, diagram count, or AI-block count doesn't match expected values.

**Solution**:
1. Check `frontend/docs/chapters/chapter-2.mdx` structure
2. Verify exactly 7 H2 sections
3. Verify 4 diagram placeholders (all kebab-case)
4. Verify 4 AI-block components (all with chapterId={2})
5. Verify glossary has 7 terms

### Issue: Metadata Consistency Validation Fails

**Symptoms**: Metadata doesn't match MDX structure.

**Solution**:
1. Check `backend/app/content/chapters/chapter_2.py`
2. Verify `section_count: 7` matches actual sections
3. Verify `ai_blocks: 4` matches MDX components
4. Verify `diagram_placeholders: 4` matches MDX placeholders
5. Verify `glossary_terms: 7` matches MDX glossary

### Issue: Import Errors

**Symptoms**: Backend imports fail.

**Solution**:
1. Check all required files exist
2. Verify import paths are correct
3. Check for circular dependencies
4. Verify Python environment is correct

### Issue: Build Failures

**Symptoms**: Frontend or backend build fails.

**Solution**:
1. Check for syntax errors
2. Verify all dependencies are installed
3. Check for missing files
4. Verify environment configuration

### Issue: API Endpoint Failures

**Symptoms**: API endpoints return errors instead of placeholder JSON.

**Solution**:
1. Check API routing is correct
2. Verify runtime engine can handle chapterId=2
3. Check request/response models
4. Verify placeholder responses are implemented

## Next Steps

After validation is complete:
1. Address any validation failures
2. Re-run validations until all pass
3. Update validation report with final results
4. Proceed to next feature (content writing or RAG implementation)

## Notes

- All validations should use placeholder/stub responses where real logic is not yet implemented.
- Validation report should clearly indicate pass/fail status for each validation category.
- Test stubs should be minimal and focus on structure validation, not functionality testing.
- No new features should be implemented during validation phase.
