# Chapter Content Validation Script

**Purpose**: Validate chapter content structure and consistency  
**Created**: 2025-01-27  
**Status**: Documentation Only (No Real Execution)

## Prerequisites

Before running validation, ensure you have:

- [x] Chapter MDX files exist
- [x] Chapter metadata files exist
- [x] Chapter chunk files exist
- [x] All chapter content files are accessible

---

## Validation Steps

### Step 1: Check Section Count

**Action**: Verify each chapter has 7 sections

**Chapters to Check**:
- Chapter 1: `frontend/docs/chapters/chapter-1.mdx`
- Chapter 2: `frontend/docs/chapters/chapter-2.mdx`
- Chapter 3: `frontend/docs/chapters/chapter-3.mdx`

**What to Check**:
- Each chapter has exactly 7 H2 sections
- Section titles match expected structure
- Section order is correct

**Expected Result**: All chapters have 7 sections

**Expected Section Structure**:
1. Main content section 1
2. Main content section 2
3. Main content section 3
4. Main content section 4
5. Learning Objectives
6. Summary
7. Glossary

---

### Step 2: Check Placeholders

**Action**: Verify placeholders exist in chapter content

**What to Check**:
- AI block placeholders exist: `<!-- AI-BLOCK: ask-question -->`
- Diagram placeholders exist: `<!-- DIAGRAM: diagram-name -->`
- All placeholders are properly formatted
- Placeholders match expected types

**Expected Result**: All required placeholders exist

**Expected Placeholder Types**:
- `<!-- AI-BLOCK: ask-question -->`
- `<!-- AI-BLOCK: explain-like-i-am-10 -->`
- `<!-- AI-BLOCK: interactive-quiz -->`
- `<!-- AI-BLOCK: generate-diagram -->`
- `<!-- DIAGRAM: diagram-name -->`

---

### Step 3: Check Metadata Sync

**Action**: Verify MDX frontmatter matches Python metadata

**What to Check**:
- MDX frontmatter title matches Python metadata title
- MDX frontmatter description matches Python metadata summary
- Section IDs in MDX match section IDs in Python metadata
- Chapter IDs match

**Files to Compare**:
- `frontend/docs/chapters/chapter-1.mdx` ↔ `backend/app/content/chapters/chapter_1.py`
- `frontend/docs/chapters/chapter-2.mdx` ↔ `backend/app/content/chapters/chapter_2.py`
- `frontend/docs/chapters/chapter-3.mdx` ↔ `backend/app/content/chapters/chapter_3.py`

**Expected Result**: MDX frontmatter and Python metadata are synchronized

---

### Step 4: Check Glossary Structure

**Action**: Verify glossary structure is consistent

**What to Check**:
- Each chapter has a glossary section
- Glossary terms are properly formatted
- Glossary structure is consistent across chapters
- Terms are defined clearly

**Expected Result**: All chapters have consistent glossary structure

---

### Step 5: Check Section Ordering

**Action**: Verify section ordering is consistent

**What to Check**:
- Sections appear in expected order
- No sections are missing
- No duplicate sections
- Section IDs are unique

**Expected Result**: All sections are in correct order

---

### Step 6: Verify Chapter Chunks

**Action**: Verify chapter chunk files exist

**What to Check**:
- `backend/app/content/chapters/chapter_1_chunks.py` exists
- `backend/app/content/chapters/chapter_2_chunks.py` exists
- `backend/app/content/chapters/chapter_3_chunks.py` exists
- Chunk functions are defined
- Chunks are properly structured

**Expected Result**: All chapter chunk files exist and are accessible

---

## Expected Results Summary

- ✅ All chapters have 7 sections
- ✅ All placeholders exist
- ✅ Metadata is synchronized
- ✅ Glossary structure is consistent
- ✅ Section ordering is correct
- ✅ Chapter chunks exist

---

## Troubleshooting

**Issue**: Section count incorrect
- **Solution**: Check MDX files for section count, verify H2 headings

**Issue**: Placeholders missing
- **Solution**: Check MDX files for placeholder comments, verify format

**Issue**: Metadata not synced
- **Solution**: Compare MDX frontmatter with Python metadata, update as needed

**Issue**: Glossary structure inconsistent
- **Solution**: Check glossary sections in all chapters, standardize format

**Issue**: Section ordering incorrect
- **Solution**: Check section order in MDX files, verify against expected structure

---

## Notes

- This is a documentation-only validation script
- No real test execution is performed
- All steps are manual validation steps
- Future: Automated content validation

