# Implementation Plan: Chapter 2 — AI Block Rendering + MDX Integration

**Branch**: `023-ch2-ai-blocks` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/023-ch2-ai-blocks/spec.md`

## Summary

This feature enables interactive AI blocks inside Chapter 2 by integrating React components into the MDX file. The implementation updates Chapter 2 MDX file with component imports, replaces HTML comment placeholders with React components, verifies component mapping, and validates Docusaurus build. **No real AI logic is implemented**—only MDX integration and rendering scaffolding are established, mirroring the system used for Chapter 1.

**Primary Deliverable**: Chapter 2 MDX with 4 AI block components rendered correctly
**Validation**: Docusaurus build succeeds, components render in correct positions, all imports resolve

## Technical Context

**Language/Version**:
- Frontend: TypeScript + React 18+ with MDX (Docusaurus 3.x)

**Primary Dependencies**:
- Frontend: React components from Feature 004 (Chapter 1 AI blocks) - already exist
- Chapter 2 content: Feature 010 or 014 (Chapter 2 Content) - already exists
- Docusaurus MDX configuration: Already configured from Feature 004
- No new external dependencies required

**Storage**: 
- Frontend: React components (reused from Feature 004)
- MDX file: Component imports and usage (no database)

**Testing**:
- Frontend: `npm run build` validation, manual component rendering test
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Frontend: Web browsers via Docusaurus static site

**Project Type**: Web application (frontend MDX integration only)

**Performance Goals**:
- Component render time: < 100ms (reusing existing components)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST reuse existing components from Feature 004 (no new component creation)
- MUST NOT implement real AI logic (OpenAI API calls, RAG, embeddings)
- MUST NOT break existing Chapter 1 AI block functionality
- MUST follow same patterns used in Chapter 1 AI blocks integration
- MUST ensure Docusaurus build passes

**Scale/Scope**:
- 1 MDX file update (chapter-2.mdx - add imports, replace 4 AI-BLOCK comments with components)
- 1 component mapping verification (mdx-components.ts - already configured)
- ~20-30 lines of new/modified code (imports and component calls)

## Constitution Check

*GATE: Must pass before implementation. Re-check after Phase 1 design.*

### ✅ PASS - Principle I: AI-Native Spec-Driven Development

**Status**: COMPLIANT

- Specification created: `specs/023-ch2-ai-blocks/spec.md` ✓
- Architecture planning: This plan document ✓
- SDD workflow followed: Spec → Plan → Tasks (next) → Implement ✓
- No code written without corresponding spec/plan artifacts ✓

### ✅ PASS - Principle II: Docusaurus-First Documentation Strategy

**Status**: COMPLIANT

- React components work within Docusaurus MDX (reusing from Feature 004) ✓
- MDX component mapping already configured (from Feature 004) ✓
- Components follow Docusaurus best practices (import from `@site/src/components/`) ✓
- Static generation supported (components are client-side React) ✓
- No breaking changes to existing Chapter 1 or Chapter 2 content ✓

### ⚠️ PARTIAL - Principle III: RAG-First Chatbot Architecture

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- Component props include `chapterId=2` for context ✓
- Components accept sectionId, concept, diagramType for future RAG integration ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No actual RAG pipeline for Chapter 2
  - No Qdrant vector search for Chapter 2
  - No OpenAI API calls for Chapter 2
  - No embedding generation for Chapter 2

**Justification**: This is a scaffolding feature extending Chapter 1 patterns to Chapter 2. RAG integration is explicitly planned for future features. Component structure is designed to accept RAG-ready parameters (chapterId=2, sectionId, concept).

### ✅ PASS - Principle IV: Personalization & User-Centric Design

**Status**: COMPLIANT (UI LAYER)

- Components accept Chapter 2 context props (chapterId=2, sectionId, concept) ✓
- UI is minimal but functional (learners can see where AI features will appear) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No user authentication
  - No personalization based on user profile
  - No adaptive content rendering

**Justification**: This feature extends UI foundation to Chapter 2. Personalization will be added in future features when BetterAuth and user profiles are implemented.

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

- Clear acceptance criteria defined in spec.md (7 success criteria) ✓
- Manual validation methods specified (build test, component rendering test) ✓
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
| III. RAG-First | ⚠️ SCAFFOLDING | Component props support future RAG, actual RAG in future |
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
│  │         frontend/docs/chapters/chapter-2.mdx         │  │
│  │                                                         │  │
│  │  import AskQuestionBlock from '@site/...'             │  │
│  │  import ExplainLike10Block from '@site/...'          │  │
│  │  import InteractiveQuizBlock from '@site/...'         │  │
│  │  import GenerateDiagramBlock from '@site/...'         │  │
│  │                                                         │  │
│  │  ## Introduction to ROS 2                              │  │
│  │  <AskQuestionBlock chapterId={2}                       │  │
│  │      sectionId="introduction-to-ros2" />              │  │
│  │                                                         │  │
│  │  ## Nodes and Node Communication                      │  │
│  │  <GenerateDiagramBlock diagramType="..."              │  │
│  │      chapterId={2} />                                  │  │
│  │                                                         │  │
│  │  ## Topics and Messages                                │  │
│  │  <ExplainLike10Block concept="topics"                  │  │
│  │      chapterId={2} />                                 │  │
│  │                                                         │  │
│  │  ## Services and Actions                               │  │
│  │  <InteractiveQuizBlock chapterId={2}                  │  │
│  │      numQuestions={6} />                              │  │
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
```

### Component Flow

1. **MDX File**: Chapter 2 MDX contains import statements and component calls
2. **Component Mapping**: `mdx-components.ts` exports components (already configured)
3. **Component Resolution**: Docusaurus resolves components via imports or mapping
4. **Component Rendering**: React components render with Chapter 2 props
5. **Build Validation**: Docusaurus build validates all imports and components

---

## Implementation Phases

### Phase 1: MDX Structure Verification

**Goal**: Confirm Chapter 2 MDX file exists and has correct structure

**Tasks**:
1. Verify `frontend/docs/chapters/chapter-2.mdx` exists
2. Check frontmatter structure (title, description, sidebar_position, etc.)
3. Identify sections where AI blocks should be placed
4. Document current placeholder locations (if any)

**Deliverables**:
- Confirmed MDX file structure
- List of sections for AI block placement
- Current placeholder inventory

**Validation**:
- MDX file exists and is readable
- Frontmatter is valid YAML
- Sections are properly structured

---

### Phase 2: Component Import Addition

**Goal**: Add component imports to Chapter 2 MDX file

**Tasks**:
1. Add import statements after frontmatter:
   ```mdx
   import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
   import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
   import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
   import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
   ```
2. Verify import paths are correct
3. Ensure imports are placed before content

**Deliverables**:
- Updated chapter-2.mdx with import statements
- All 4 components imported correctly

**Validation**:
- Imports are syntactically correct
- Import paths resolve to existing components
- No TypeScript errors

---

### Phase 3: Component Mapping Verification

**Goal**: Verify component mapping is configured correctly

**Tasks**:
1. Check `frontend/src/mdx-components.ts` exists
2. Verify all 4 components are exported:
   - AskQuestionBlock
   - ExplainLike10Block
   - InteractiveQuizBlock
   - GenerateDiagramBlock
3. Confirm export structure matches expected format
4. Document fallback swizzle path if needed (Docusaurus 3.x)

**Deliverables**:
- Verified component mapping configuration
- Documentation of mapping approach (direct imports vs. global mapping)

**Validation**:
- All 4 components are exported
- Export names match component names exactly
- Components are importable

---

### Phase 4: Placeholder Replacement

**Goal**: Replace HTML comment placeholders with React components

**Tasks**:
1. Replace `<!-- AI-BLOCK: ask-question -->` with:
   ```mdx
   <AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
   ```
2. Replace `<!-- AI-BLOCK: generate-diagram -->` with:
   ```mdx
   <GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />
   ```
3. Replace `<!-- AI-BLOCK: explain-like-i-am-10 -->` with:
   ```mdx
   <ExplainLike10Block concept="topics" chapterId={2} />
   ```
4. Replace `<!-- AI-BLOCK: interactive-quiz -->` with:
   ```mdx
   <InteractiveQuizBlock chapterId={2} numQuestions={6} />
   ```
5. Ensure components are placed at pedagogically correct positions
6. Verify props syntax (curly braces for numbers, quotes for strings)

**Deliverables**:
- Updated chapter-2.mdx with all 4 components
- Components placed at correct positions
- All props correctly formatted

**Validation**:
- All placeholders replaced with components
- Components are properly closed (self-closing syntax)
- Props match expected TypeScript interfaces
- Components placed at correct positions

---

### Phase 5: Build Validation

**Goal**: Ensure Docusaurus build succeeds with Chapter 2 AI blocks

**Tasks**:
1. Run `npm run build` in frontend directory
2. Check for TypeScript compilation errors
3. Check for missing component errors
4. Check for MDX syntax errors
5. Verify build output includes Chapter 2 page
6. Test in development server (`npm start`)
7. Navigate to `/docs/chapters/chapter-2` in browser
8. Verify all 4 components render correctly
9. Check browser console for React errors
10. Verify component props in DevTools

**Deliverables**:
- Successful Docusaurus build
- Components render in browser
- No console errors
- Props verified in DevTools

**Validation**:
- Build completes without errors
- All imports resolve correctly
- Components render in correct positions
- No React errors in console
- Component props are correct

---

## Key Decisions

### Decision 1: Use Direct Imports in MDX

**Rationale**: More reliable, explicit dependencies, works across Docusaurus versions

**Alternative Considered**: Global component mapping via `mdx-components.ts`

**Chosen**: Direct imports in chapter-2.mdx (same as Chapter 1)

**Impact**: Clear dependencies, easier debugging, consistent with Chapter 1 pattern

---

### Decision 2: Reuse Existing Components

**Rationale**: No need to create new components, consistency with Chapter 1, faster implementation

**Alternative Considered**: Create Chapter 2-specific components

**Chosen**: Reuse components from Feature 004 with Chapter 2 props

**Impact**: Faster implementation, consistent UI, easier maintenance

---

### Decision 3: Validate Build Early

**Rationale**: Catch errors before deployment, ensure components render correctly

**Alternative Considered**: Defer validation until later

**Chosen**: Run build validation as part of feature completion

**Impact**: Early error detection, confidence in implementation

---

### Decision 4: Use TODO Placeholders for Some Props

**Rationale**: Exact values may not be determined yet, allows flexibility

**Alternative Considered**: Require all props to have exact values

**Chosen**: Allow TODO placeholders for sectionId, concept, diagramType if needed

**Impact**: Flexible implementation, can refine props later

---

## Risk Analysis

### Risk 1: Components Don't Render

**Probability**: Low
**Impact**: High
**Mitigation**: 
- Verify imports are correct
- Check component names match exactly
- Validate build succeeds
- Test in browser

---

### Risk 2: Props Don't Match Expected Interface

**Probability**: Medium
**Impact**: Medium
**Mitigation**:
- Use TypeScript interfaces for validation
- Check props syntax (curly braces for numbers, quotes for strings)
- Verify props match component expectations
- Test in browser DevTools

---

### Risk 3: Build Fails

**Probability**: Low
**Impact**: High
**Mitigation**:
- Run build early to catch errors
- Fix import paths
- Resolve TypeScript errors
- Validate MDX syntax

---

### Risk 4: Component Mapping Not Working

**Probability**: Low
**Impact**: Medium
**Mitigation**:
- Verify `mdx-components.ts` exports all components
- Check Docusaurus version compatibility
- Use direct imports as fallback
- Test component resolution

---

## Non-Functional Requirements

### NFR-001: Code Quality

**Requirement**: Code must follow existing patterns and conventions

**Implementation**:
- Reuse components from Feature 004
- Follow same import patterns as Chapter 1
- Use consistent prop naming
- Add comments where needed

**Validation**: Code review, pattern consistency check

---

### NFR-002: Maintainability

**Requirement**: Code must be easy to understand and modify

**Implementation**:
- Clear import statements
- Explicit component usage
- Documented prop values
- Consistent structure

**Validation**: Code readability, documentation completeness

---

### NFR-003: Build Performance

**Requirement**: Docusaurus build must complete in reasonable time

**Implementation**:
- Reuse existing components (no new compilation)
- Minimal MDX changes
- No new dependencies

**Validation**: Build time measurement (< 2 minutes for full build)

---

## Success Criteria

- **SC-001**: Chapter 2 MDX renders with all 4 AI blocks at designated positions ✓
- **SC-002**: Frontend build passes without errors (`npm run build`) ✓
- **SC-003**: Components imported correctly in chapter-2.mdx ✓
- **SC-004**: All components receive correct props (chapterId=2, appropriate sectionId/concept/diagramType) ✓
- **SC-005**: No real AI logic added (only MDX integration and rendering scaffolding) ✓
- **SC-006**: MDX component mapping includes all 4 AI block components ✓
- **SC-007**: Docusaurus can compile and render Chapter 2 with AI blocks ✓

---

## Out of Scope

- ❌ Implementing real AI logic for Chapter 2
- ❌ Creating new AI block components
- ❌ Backend API integration
- ❌ RAG pipeline integration
- ❌ Runtime engine updates
- ❌ Subagent modifications
- ❌ Implementing diagram generation logic
- ❌ Creating quiz question generation logic
- ❌ Adding authentication or personalization

---

## Dependencies

- **Dependency 1**: Feature 004 (Chapter 1 Interactive AI Blocks) - Required for existing components and MDX mapping patterns
- **Dependency 2**: Feature 010 or 014 (Chapter 2 Content) - Required for Chapter 2 MDX file existence
- **Dependency 3**: Docusaurus MDX Configuration - Required for component rendering

---

## Next Steps

1. **Generate Tasks**: Run `/sp.tasks` to create atomic implementation tasks
2. **Implement Scaffolding**: Run `/sp.implement` to implement MDX integration
3. **Validate**: Run build and test component rendering
4. **Document**: Update contract with actual prop values (if using TODO placeholders)

---

## Summary

This plan establishes the architecture for integrating AI blocks into Chapter 2 MDX file. The implementation is straightforward: add imports, replace placeholders with components, verify mapping, and validate build. All components are reused from Chapter 1, ensuring consistency and faster implementation. The focus is on MDX integration only—no backend logic or AI implementation is included in this feature.

**Estimated Implementation Time**: 30-45 minutes (MDX integration only)
**Complexity**: Low (scaffolding only, reusing existing components)
**Risk Level**: Low (minimal changes, well-established patterns)

