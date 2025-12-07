# Implementation Plan: Chapter 3 — AI Blocks Integration Layer

**Branch**: `028-ch3-ai-blocks` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/028-ch3-ai-blocks/spec.md`

## Summary

This feature enables interactive AI blocks inside Chapter 3 by integrating React components into the MDX file. The implementation updates Chapter 3 MDX file with component imports, replaces HTML comment placeholders with React components, verifies component mapping, creates backend metadata stub, adds RAG preparation markers, and validates Docusaurus build. **No real AI logic is implemented**—only MDX integration and rendering scaffolding are established, mirroring the system used for Chapter 1 and Chapter 2.

**Primary Deliverable**: Chapter 3 MDX with 4 AI block components rendered correctly, backend metadata file, RAG chunking markers, and contract documentation
**Validation**: Docusaurus build succeeds, components render in correct positions, all imports resolve, backend metadata matches MDX structure

## Technical Context

**Language/Version**:
- Frontend: TypeScript + React 18+ with MDX (Docusaurus 3.x)
- Backend: Python 3.11+ (for metadata file)

**Primary Dependencies**:
- Frontend: React components from Feature 004 (Chapter 1 AI blocks) - already exist
- Chapter 3 content: Feature 017 or 018 (Chapter 3 Content) - already exists
- Docusaurus MDX configuration: Already configured from Feature 004
- Chapter 2 AI blocks: Feature 023 (reference for integration patterns)
- No new external dependencies required

**Storage**: 
- Frontend: React components (reused from Feature 004)
- MDX file: Component imports and usage (no database)
- Backend: Python metadata file (chapter_3.py - already exists, may need updates)
- Backend: Python chunks file (chapter_3_chunks.py - to be created)

**Testing**:
- Frontend: `npm run build` validation, manual component rendering test
- Backend: Python import test for metadata and chunks files
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Frontend: Web browsers via Docusaurus static site
- Backend: Python module (metadata and chunks)

**Project Type**: Web application (frontend MDX integration + backend metadata scaffolding)

**Performance Goals**:
- Component render time: < 100ms (reusing existing components)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST reuse existing components from Feature 004 (no new component creation)
- MUST NOT implement real AI logic (OpenAI API calls, RAG, embeddings)
- MUST NOT break existing Chapter 1 or Chapter 2 AI block functionality
- MUST follow same patterns used in Chapter 1 and Chapter 2 AI blocks integration
- MUST ensure Docusaurus build passes
- MUST ensure backend metadata matches MDX structure exactly

**Scale/Scope**:
- 1 MDX file update (chapter-3.mdx - add imports, replace 4 AI-BLOCK comments with components)
- 1 backend metadata file verification/update (chapter_3.py - verify structure matches MDX)
- 1 backend chunks file creation (chapter_3_chunks.py - placeholder function)
- 1 component mapping verification (mdx-components.ts - already configured)
- ~20-30 lines of new/modified code (imports and component calls)

## Constitution Check

*GATE: Must pass before implementation. Re-check after Phase 1 design.*

### ✅ PASS - Principle I: AI-Native Spec-Driven Development

**Status**: COMPLIANT

- Specification created: `specs/028-ch3-ai-blocks/spec.md` ✓
- Architecture planning: This plan document ✓
- SDD workflow followed: Spec → Plan → Tasks (next) → Implement ✓
- No code written without corresponding spec/plan artifacts ✓

### ✅ PASS - Principle II: Docusaurus-First Documentation Strategy

**Status**: COMPLIANT

- React components work within Docusaurus MDX (reusing from Feature 004) ✓
- MDX component mapping already configured (from Feature 004) ✓
- Components follow Docusaurus best practices (import from `@site/src/components/`) ✓
- Static generation supported (components are client-side React) ✓
- No breaking changes to existing Chapter 1, Chapter 2, or Chapter 3 content ✓
- Chapter 3 appears in sidebar at position 3 (after Chapter 2) ✓

### ⚠️ PARTIAL - Principle III: RAG-First Chatbot Architecture

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- Component props include `chapterId=3` for context ✓
- Components accept sectionId, concept, diagramType for future RAG integration ✓
- RAG chunking markers (`<!-- CHUNK: START -->` and `<!-- CHUNK: END -->`) present in MDX ✓
- Chapter 3 chunks file placeholder created ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No actual RAG pipeline for Chapter 3
  - No Qdrant vector search for Chapter 3
  - No OpenAI API calls for Chapter 3
  - No embedding generation for Chapter 3

**Justification**: This is a scaffolding feature extending Chapter 1 and Chapter 2 patterns to Chapter 3. RAG integration is explicitly planned for future features. Component structure is designed to accept RAG-ready parameters (chapterId=3, sectionId, concept). RAG chunking markers are added for future embedding generation.

### ✅ PASS - Principle IV: Personalization & User-Centric Design

**Status**: COMPLIANT (UI LAYER)

- Components accept Chapter 3 context props (chapterId=3, sectionId, concept) ✓
- UI is minimal but functional (learners can see where AI features will appear) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No user authentication
  - No personalization based on user profile
  - No adaptive content rendering

**Justification**: This feature extends UI foundation to Chapter 3. Personalization will be added in future features when BetterAuth and user profiles are implemented.

### ✅ PASS - Principle V: Multilingual Support with On-Demand Translation

**Status**: COMPLIANT (STRUCTURE)

- Component structure supports future translation (reusing from Feature 004) ✓
- No hard-coded English text in component logic ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No Urdu translation
  - No translation pipeline

**Justification**: Component structure is translation-ready (from Feature 004). Translation will be added in future features when translation system is implemented.

### ✅ PASS - Principle VI: Test-Driven Quality Gates

**Status**: COMPLIANT (MANUAL TESTING PHASE)

- Clear acceptance criteria defined in spec.md (10 success criteria) ✓
- Manual validation methods specified (build test, component rendering test, metadata validation) ✓
- **Not Yet Implemented** (automated testing out of scope for scaffolding):
  - No unit tests (components are reused, no new logic)
  - No integration tests (no real AI logic to test)
  - No E2E tests

**Justification**: This is a scaffolding feature with minimal new logic (mostly integration). Automated tests will be added in future features when real AI functionality is implemented.

---

### Constitution Check Summary

| Principle | Status | Notes |
|-----------|--------|-------|
| I. SDD Workflow | ✅ PASS | Full spec → plan → tasks workflow followed |
| II. Docusaurus-First | ✅ PASS | MDX component integration, reusing existing components |
| III. RAG-First | ⚠️ SCAFFOLDING | Component props support future RAG, chunking markers added, actual RAG in future |
| IV. Personalization | ✅ PASS | Component props support future personalization |
| V. Multilingual | ✅ PASS | Structure supports translation, implementation deferred |
| VI. TDD Quality Gates | ✅ PASS | Manual validation appropriate for scaffolding phase |

**Overall**: ✅ **APPROVED TO PROCEED**

---

## Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Docusaurus Frontend                       │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         frontend/docs/chapters/chapter-3.mdx         │  │
│  │                                                         │  │
│  │  import AskQuestionBlock from '@site/...'             │  │
│  │  import ExplainLike10Block from '@site/...'          │  │
│  │  import InteractiveQuizBlock from '@site/...'         │  │
│  │  import GenerateDiagramBlock from '@site/...'         │  │
│  │                                                         │  │
│  │  ## What Is Perception in Physical AI?                │  │
│  │  <AskQuestionBlock chapterId={3}                       │  │
│  │      sectionId="what-is-perception-in-physical-ai" />  │  │
│  │                                                         │  │
│  │  ## Types of Sensors in Robotics                      │  │
│  │  <GenerateDiagramBlock diagramType="sensor-types"      │  │
│  │      chapterId={3} />                                  │  │
│  │                                                         │  │
│  │  ## Computer Vision & Depth Perception                │  │
│  │  <ExplainLike10Block concept="computer-vision"         │  │
│  │      chapterId={3} />                                 │  │
│  │                                                         │  │
│  │  ## Signal Processing Basics for AI                   │  │
│  │  <InteractiveQuizBlock chapterId={3}                  │  │
│  │      numQuestions={5} />                              │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                   │
│                           │ Component Resolution              │
│                           ▼                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │     frontend/src/mdx-components.ts                    │  │
│  │                                                         │  │
│  │  export default {                                      │  │
│  │    AskQuestionBlock,                                    │  │
│  │    ExplainLike10Block,                                  │  │
│  │    InteractiveQuizBlock,                                │  │
│  │    GenerateDiagramBlock,                                │  │
│  │  };                                                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                   │
│                           │ Import                            │
│                           ▼                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  frontend/src/components/ai/*.tsx                    │  │
│  │  (Reused from Feature 004)                            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Metadata Sync
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend Metadata Layer                     │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  backend/app/content/chapters/chapter_3.py           │  │
│  │                                                         │  │
│  │  CHAPTER_METADATA = {                                  │  │
│  │    "id": 3,                                            │  │
│  │    "title": "Chapter 3 — ...",                        │  │
│  │    "sections": [...],                                 │  │
│  │    "ai_blocks": [...],                                │  │
│  │    "diagram_placeholders": [...]                      │  │
│  │  }                                                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                   │
│                           │ RAG Preparation                   │
│                           ▼                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  backend/app/content/chapters/chapter_3_chunks.py    │  │
│  │                                                         │  │
│  │  def get_chapter3_chunks(...) -> List[Dict]:          │  │
│  │    # TODO: Implement chunking                          │  │
│  │    return []                                           │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Component Flow

1. **MDX Processing**: Docusaurus processes `chapter-3.mdx` and encounters React component calls
2. **Component Resolution**: Docusaurus looks up components in `mdx-components.ts`
3. **Component Import**: Components are imported from `@site/src/components/ai/`
4. **Component Rendering**: React components render with Chapter 3 props (chapterId=3, sectionId, concept, diagramType)
5. **Metadata Sync**: Backend metadata file (`chapter_3.py`) matches MDX structure
6. **RAG Preparation**: Chunking markers and placeholder chunks function ready for future embedding

### Key Components

1. **Chapter 3 MDX File**: Contains frontmatter, imports, content sections, and AI block components
2. **Component Mapping**: `mdx-components.ts` exports all 4 AI block components
3. **React Components**: Reused from Feature 004 (AskQuestionBlock, ExplainLike10Block, InteractiveQuizBlock, GenerateDiagramBlock)
4. **Backend Metadata**: Python dictionary matching MDX structure
5. **RAG Chunks File**: Placeholder function for future chunking implementation

### Integration Points

- **Docusaurus MDX**: Processes MDX file and renders React components
- **Component Library**: Provides reusable AI block components
- **Backend Metadata**: Provides structured chapter information for RAG and analytics
- **RAG Pipeline** (Future): Will use chunking markers and chunks file for embedding generation

---

## Implementation Phases

### Phase 1: MDX File Update

**Goal**: Update Chapter 3 MDX file with component imports and replace placeholders with React components

**Files to Update**:
- `frontend/docs/chapters/chapter-3.mdx`

**Implementation Details**:
- Add import statements after frontmatter:
  ```mdx
  import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
  import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
  import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
  import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
  ```
- Replace `<!-- AI-BLOCK: ask-question -->` with:
  ```mdx
  <AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
  ```
- Replace `<!-- AI-BLOCK: generate-diagram -->` with:
  ```mdx
  <GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />
  ```
- Replace `<!-- AI-BLOCK: explain-like-i-am-10 -->` with:
  ```mdx
  <ExplainLike10Block concept="computer-vision" chapterId={3} />
  ```
- Replace `<!-- AI-BLOCK: interactive-quiz -->` with:
  ```mdx
  <InteractiveQuizBlock chapterId={3} numQuestions={5} />
  ```
- Verify frontmatter matches contract (title, description, sidebar_position, sidebar_label, tags)
- Ensure RAG chunking markers (`<!-- CHUNK: START -->` and `<!-- CHUNK: END -->`) are present

**Validation**:
- MDX file has all 4 component imports
- All 4 AI-BLOCK comments replaced with React components
- All components use `chapterId={3}`
- Frontmatter matches contract
- RAG chunking markers present

---

### Phase 2: Component Mapping Verification

**Goal**: Verify that `mdx-components.ts` exports all required AI block components

**Files to Check**:
- `frontend/src/mdx-components.ts`

**Implementation Details**:
- Verify file exists and exports all 4 components:
  - `AskQuestionBlock`
  - `ExplainLike10Block`
  - `InteractiveQuizBlock`
  - `GenerateDiagramBlock`
- If components not exported, add them (should already be present from Feature 004)

**Validation**:
- All 4 components are exported in `mdx-components.ts`
- Components are importable from `@site/src/components/ai/` paths

---

### Phase 3: Backend Metadata Verification

**Goal**: Verify that backend metadata file matches MDX structure exactly

**Files to Check/Update**:
- `backend/app/content/chapters/chapter_3.py`

**Implementation Details**:
- Verify `CHAPTER_METADATA` dictionary exists
- Verify `id` is 3
- Verify `title` matches MDX frontmatter exactly
- Verify `sections` list matches MDX H2 section titles in order (7 sections)
- Verify `ai_blocks` list matches component types in MDX (4 blocks)
- Verify `diagram_placeholders` list matches diagram names in MDX (4 diagrams)
- Update if needed to match MDX structure exactly

**Validation**:
- Metadata file exists and is importable
- All fields match MDX structure exactly
- `sections` list has 7 items matching MDX H2 headings
- `ai_blocks` list has 4 items: ["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]
- `diagram_placeholders` list has 4 items: ["perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline"]

---

### Phase 4: RAG Chunks File Creation

**Goal**: Create placeholder chunks file for future RAG implementation

**Files to Create**:
- `backend/app/content/chapters/chapter_3_chunks.py`

**Implementation Details**:
- Create file with placeholder function:
  ```python
  from typing import List, Dict, Any

  def get_chapter3_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
      """
      Get Chapter 3 chunks for RAG pipeline.
      
      Args:
          chapter_id: Chapter identifier (default: 3 for Chapter 3)
      
      Returns:
          List of chunk dictionaries with structure:
          [
              {
                  "id": str,
                  "text": str,
                  "chapter_id": 3,
                  "section_id": str,
                  "position": int,
                  "word_count": int,
                  "metadata": Dict[str, Any]
              },
              ...
          ]
      
      TODO: Implement chunking from Chapter 3 MDX content
      TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
      TODO: Implement chunking strategy (by section, by paragraph, or semantic)
      TODO: Extract metadata (section titles, positions, word counts)
      TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")
      TODO: Handle special content (glossary, diagrams, AI blocks)
      TODO: Cache chunks for performance
      TODO: Include Physical AI Perception-specific metadata
      """
      # Placeholder return - no real chunking implementation
      return []
  ```
- Add TODO comments for future implementation

**Validation**:
- File exists and is importable
- Function signature is correct
- Function has TODO comments
- Function returns empty list (placeholder)

---

### Phase 5: Build Validation

**Goal**: Validate that Docusaurus build succeeds and components render correctly

**Validation Steps**:
1. **Frontend Build Test**:
   - Run: `cd frontend && npm run build`
   - Expected: Build completes without errors
   - Check: No TypeScript compilation errors
   - Check: No missing component errors
   - Check: All imports resolve correctly

2. **Component Rendering Test**:
   - Start dev server: `cd frontend && npm run start`
   - Navigate to: `/docs/chapters/chapter-3`
   - Expected: All 4 AI block components render in correct positions
   - Check: No React errors in browser console
   - Check: Components display with correct props (chapterId=3)

3. **Backend Import Test**:
   - Run: `cd backend && python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; print('Import successful')"`
   - Expected: Import succeeds
   - Run: `cd backend && python -c "from app.content.chapters.chapter_3_chunks import get_chapter3_chunks; print('Import successful')"`
   - Expected: Import succeeds

**Validation Checklist**:
- [ ] Frontend build succeeds without errors
- [ ] All component imports resolve
- [ ] Components render in designated locations
- [ ] No console errors in browser
- [ ] Chapter 3 visible in sidebar at position 3
- [ ] Backend metadata file imports successfully
- [ ] Backend chunks file imports successfully

---

## Key Decisions

### Decision 1: Reuse Existing Components

**Rationale**: Components from Feature 004 are already tested and working. No need to create new components.

**Alternative Considered**: Create Chapter 3-specific components

**Chosen**: Reuse existing components with chapterId=3 prop

**Impact**: Faster implementation, consistent UI, less code to maintain

---

### Decision 2: Replace HTML Comments with React Components

**Rationale**: HTML comments are placeholders. React components provide actual UI foundation for future AI logic.

**Alternative Considered**: Keep HTML comments and add components separately

**Chosen**: Replace comments with components directly in MDX

**Impact**: Cleaner MDX file, components visible to learners, ready for future AI integration

---

### Decision 3: Match Backend Metadata to MDX Structure

**Rationale**: Backend metadata must match MDX structure exactly for RAG pipeline and analytics to work correctly.

**Alternative Considered**: Keep metadata separate from MDX

**Chosen**: Ensure metadata matches MDX structure exactly

**Impact**: Future RAG pipeline can use metadata to understand chapter structure, analytics can track sections correctly

---

### Decision 4: Add RAG Chunking Markers

**Rationale**: Chunking markers prepare MDX for future embedding generation. Markers indicate where chunks should start and end.

**Alternative Considered**: Add chunking markers later when implementing RAG

**Chosen**: Add chunking markers now during MDX integration

**Impact**: MDX is ready for future RAG implementation, no need to modify MDX later

---

### Decision 5: Create Placeholder Chunks File

**Rationale**: Chunks file is needed for future RAG implementation. Creating placeholder now ensures structure is ready.

**Alternative Considered**: Create chunks file when implementing RAG

**Chosen**: Create placeholder chunks file now

**Impact**: Backend structure is ready for future RAG implementation, clear TODO markers for implementation

---

## Risk Analysis

### Risk 1: Component Import Errors

**Description**: Components may not import correctly if paths are wrong or components don't exist

**Probability**: Low

**Impact**: High (blocks frontend build)

**Mitigation**:
- Verify components exist in `frontend/src/components/ai/`
- Use exact import paths from Feature 004
- Test imports during build validation
- Check `mdx-components.ts` exports

**Status**: Mitigated by reusing existing components from Feature 004

---

### Risk 2: MDX Syntax Errors

**Description**: Incorrect JSX syntax in MDX may cause build failures

**Probability**: Medium

**Impact**: High (blocks frontend build)

**Mitigation**:
- Follow exact syntax from Chapter 2 MDX file
- Use self-closing tags (`/>`)
- Ensure proper JSX prop syntax (curly braces for numbers, quotes for strings)
- Test build after each component addition

**Status**: Mitigated by following established patterns from Chapter 2

---

### Risk 3: Metadata Mismatch

**Description**: Backend metadata may not match MDX structure, causing issues in future RAG implementation

**Probability**: Medium

**Impact**: Medium (causes issues in future features)

**Mitigation**:
- Verify metadata matches MDX structure exactly
- Compare section titles, ai_blocks, and diagram_placeholders
- Update metadata if needed during implementation
- Document metadata structure in contract

**Status**: Mitigated by explicit validation step in Phase 3

---

### Risk 4: Breaking Existing Functionality

**Description**: Changes to MDX or components may break Chapter 1 or Chapter 2 functionality

**Probability**: Low

**Impact**: High (breaks existing features)

**Mitigation**:
- Only modify Chapter 3 MDX file
- Reuse existing components (no modifications)
- Test Chapter 1 and Chapter 2 still work
- Verify component mapping doesn't change

**Status**: Mitigated by only modifying Chapter 3 files and reusing components

---

## Validation Strategy

### Pre-Implementation Validation

- [ ] Specification reviewed and approved
- [ ] Architecture plan reviewed and approved
- [ ] Dependencies verified (Feature 004, Feature 017/018, Feature 023)
- [ ] Constitution check passed

### During Implementation Validation

- [ ] Each phase validated before proceeding
- [ ] MDX file updated with imports and components
- [ ] Component mapping verified
- [ ] Backend metadata verified/updated
- [ ] Chunks file created

### Post-Implementation Validation

- [ ] Frontend build succeeds
- [ ] Components render correctly
- [ ] No console errors
- [ ] Backend imports succeed
- [ ] Chapter 3 visible in sidebar
- [ ] Metadata matches MDX structure

---

## Success Criteria

- ✅ Chapter 3 MDX renders with all 4 AI blocks at designated positions
- ✅ Frontend build passes without errors (`npm run build`)
- ✅ Components imported correctly in chapter-3.mdx
- ✅ All components receive correct props (chapterId=3, appropriate sectionId/concept/diagramType)
- ✅ No real AI logic added (only MDX integration and rendering scaffolding)
- ✅ MDX component mapping includes all 4 AI block components
- ✅ Docusaurus can compile and render Chapter 3 with AI blocks
- ✅ Backend metadata file exists and matches MDX structure
- ✅ RAG chunking markers present in MDX
- ✅ Chapter 3 chunks file created with placeholder function

---

## Next Steps

1. **Task Generation**: Run `/sp.tasks` to generate atomic implementation tasks
2. **Implementation**: Execute tasks in order (Phase 1 → Phase 5)
3. **Validation**: Run validation checklist after each phase
4. **Documentation**: Update PHR after implementation

---

## Summary

This plan establishes the complete architecture for Chapter 3 AI blocks integration. The implementation follows Chapter 1 and Chapter 2 patterns, reuses existing components, updates MDX file with component imports and usage, verifies component mapping, ensures backend metadata matches MDX structure, adds RAG preparation markers, and validates Docusaurus build. All validation focuses on structure and rendering rather than functionality.

**Estimated Implementation Time**: 30-45 minutes (scaffolding only, no real AI logic)
**Complexity**: Low (scaffolding only, reusing existing components)
**Dependencies**: Feature 004 (Chapter 1 AI Blocks), Feature 017/018 (Chapter 3 Content), Feature 023 (Chapter 2 AI Blocks reference)
**Out of Scope**: Real AI logic, content writing, new component creation, RAG implementation

