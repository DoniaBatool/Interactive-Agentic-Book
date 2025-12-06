# Quickstart: Chapter 1 Validation, Testing & Build Stability Layer

**Feature**: 009-ch1-validation

## Prerequisites

- Feature 001 (Base Project) complete
- Feature 002 (Chapter 1 Core) complete
- Feature 003 (Chapter 1 Content) complete
- Feature 004 (Chapter 1 Interactive Blocks) complete
- Feature 005 (AI Runtime Engine) complete
- Feature 008 (Chapter 1 Diagram Runtime) complete
- Backend: Python 3.11+, FastAPI 0.109+
- Frontend: Node.js for test environment

## Verification Steps

### Step 1: Verify Frontend Validators Structure

```bash
# Check MDX structure validator exists
ls frontend/validators/mdx_structure.py

# Check AI blocks validator exists
ls frontend/validators/ai_blocks.py

# Check diagram validator exists
ls frontend/validators/diagrams.py

# Check glossary validator exists
ls frontend/validators/glossary.py
```

### Step 2: Verify Backend Validators Structure

```bash
# Check chapter metadata validator exists
ls backend/validators/chapter_metadata_validator.py

# Check RAG readiness validator exists
ls backend/validators/rag_readiness_validator.py
```

### Step 3: Test Backend Imports

```bash
cd backend
python -c "from app.validators.chapter_metadata_validator import validate_chapter_metadata; print('OK')"
python -c "from app.validators.rag_readiness_validator import validate_rag_readiness; print('OK')"
```

### Step 4: Verify Test Files

```bash
# Check frontend test file exists
ls frontend/tests/test_mdx_ch1_structure.js

# Check backend test file exists
ls backend/tests/test_chapter_1_validation.py
```

### Step 5: Start Backend Server

```bash
cd backend
uvicorn app.main:app --reload
# Should start without import errors
```

### Step 6: Verify Documentation

```bash
# Check validation guide exists
ls specs/009-ch1-validation/validation-guide.md

# Check build checklist exists
ls specs/009-ch1-validation/build-checklist.md

# Check CI script exists
ls scripts/validate_ch1.sh
```

## Common Issues

### Issue 1: Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'app.validators'`

**Solution**: 
- Verify `backend/app/validators/__init__.py` exists
- Check Python path includes backend directory
- Restart backend server

### Issue 2: Validator Functions Not Found

**Symptom**: `AttributeError: module has no attribute 'validate_mdx_structure'`

**Solution**:
- Verify validator functions are defined with correct signatures
- Check function names match expected names
- Ensure validators contain TODO placeholders

### Issue 3: Test Files Not Found

**Symptom**: Test files don't exist at expected paths

**Solution**:
- Verify test directories exist: `frontend/tests/`, `backend/tests/`
- Check test files are created with correct names
- Ensure test files contain TODO placeholders

## Architecture Understanding

### Validation Flow

1. **MDX Validation**: Frontend validators check MDX structure, AI blocks, diagrams, glossary, links
2. **Backend Validation**: Backend validators check metadata, RAG readiness
3. **Test Scaffolding**: Test files provide structure for future test implementation
4. **CI Integration**: Validation script placeholder for CI/CD pipeline

### Module Responsibilities

- **Frontend Validators**: MDX structure, AI blocks, diagrams, glossary, links validation
- **Backend Validators**: Chapter metadata, RAG readiness validation
- **Test Files**: Test scaffolding with TODO placeholders
- **Documentation**: Validation guide, build checklist
- **CI Script**: Validation pipeline placeholder

### Validation Response Structure

All validators return consistent structure:
```python
{
    "valid": bool,        # TODO: placeholder
    "errors": List[str],  # TODO: placeholder
    "warnings": List[str], # TODO: placeholder
    "details": Dict[str, Any] # TODO: placeholder
}
```

## Next Steps

1. **Future Feature**: Implement real validation logic
   - Add MDX parsing and structure validation
   - Implement AI block detection
   - Add link checking
   - Implement metadata comparison

2. **Future Feature**: Add CI/CD integration
   - Integrate validators into CI pipeline
   - Add automated build checks
   - Generate validation reports

3. **Future Feature**: Enhance validation coverage
   - Add more validation checks
   - Add validation reporting
   - Add auto-fix capabilities
