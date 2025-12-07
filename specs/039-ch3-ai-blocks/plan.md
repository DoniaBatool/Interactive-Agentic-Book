# Implementation Plan: Chapter 3 — AI Blocks Integration

**Branch**: `039-ch3-ai-blocks` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/039-ch3-ai-blocks/spec.md` and Feature 037 specification

## Summary

This feature integrates all AI-interactive blocks into Chapter 3 MDX file at pedagogically aligned positions. The implementation replaces HTML comment placeholders with React components, adds component imports, and ensures components render correctly with placeholder UI. **No backend changes**—only frontend UI component placement following Chapter 1 and Chapter 2 patterns.

**Primary Deliverable**: `frontend/docs/chapters/chapter-3.mdx` (with React components integrated)
**Validation**: MDX compiles, components render, no TypeScript errors, build succeeds

---

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Components: React/TypeScript components (already exist)

**Primary Dependencies**:
- Feature 001 (Base Project Initialization) - Docusaurus frontend
- Feature 037 (Chapter 3 Content Specification) - Source for placement rules
- Feature 038 (Chapter 3 MDX Implementation) - MDX file with placeholders exists
- Feature 004 (Chapter 1 Interactive AI Blocks) - Components exist
- Frontend: Docusaurus 3.x (already installed)
- React components: Already exist in `frontend/src/components/ai/`

**Storage**: Static MDX file (no database)

**Testing**:
- Frontend: `npm run build` validation (Docusaurus build process)
- Browser: Visual verification of component rendering
- Manual: Component interaction testing (placeholder UI)

**Target Platform**:
- Frontend: Web browsers via Docusaurus static site

**Project Type**: Frontend MDX component integration

**Performance Goals**:
- Build time: Incremental build < 5 seconds
- No performance-critical operations (static component placement)

**Constraints**:
- MUST NOT add backend AI runtime logic (Feature 041 scope)
- MUST NOT modify Chapter 1 or Chapter 2 MDX files
- MUST NOT modify RAG or runtime engine files
- MUST follow Feature 037 specification exactly for placement
- Only frontend UI component placement

**Scale/Scope**:
- 1 MDX file (chapter-3.mdx)
- 4 React components integrated
- 4 placeholder replacements
- No backend changes

---

## 1. File Identification

### 1.1 MDX File to Modify

**Location**: `frontend/docs/chapters/chapter-3.mdx`
**Status**: Update existing file (placeholders exist from Feature 038)
**Action**: Replace HTML comment placeholders with React components, add imports

### 1.2 React Component Imports and Paths

**Component Paths**:
- `@site/src/components/ai/AskQuestionBlock`
- `@site/src/components/ai/ExplainLike10Block`
- `@site/src/components/ai/InteractiveQuizBlock`
- `@site/src/components/ai/GenerateDiagramBlock`

**Import Format**:
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
```

### 1.3 Mapping Registry File

**Location**: `frontend/src/mdx-components.ts`
**Status**: Verify exports exist (or use explicit imports)
**Action**: Verify all 4 components are exported (explicit imports also work)

---

## 2. Component Placement Map

### 2.1 Ask Question Block

**Placement**: Section 1 (What Is Perception in Physical AI?), at the end
**Replaces**: `<!-- AI-BLOCK: ask-question -->`
**Component**: `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />`
**Required Props**:
- `chapterId`: 3 (number)
- `sectionId`: "what-is-perception-in-physical-ai" (string)

### 2.2 Generate Diagram Block

**Placement**: Section 2 (Types of Sensors in Robotics), in the middle (after diagram placeholder)
**Replaces**: `<!-- AI-BLOCK: generate-diagram -->`
**Component**: `<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />`
**Required Props**:
- `chapterId`: 3 (number)
- `diagramType`: "sensor-types" (string, matches diagram placeholder name)

### 2.3 Explain Like 10 Block

**Placement**: Section 3 (Computer Vision & Depth Perception), in the middle (before diagram placeholder)
**Replaces**: `<!-- AI-BLOCK: explain-like-i-am-10 -->`
**Component**: `<ExplainLike10Block concept="computer-vision" chapterId={3} />`
**Required Props**:
- `chapterId`: 3 (number)
- `concept`: "computer-vision" (string)

### 2.4 Interactive Quiz Block

**Placement**: Section 4 (Signal Processing Basics for AI), at the end
**Replaces**: `<!-- AI-BLOCK: interactive-quiz -->`
**Component**: `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`
**Required Props**:
- `chapterId`: 3 (number)
- `numQuestions`: 5 (number)

---

## 3. Refactoring Plan

### 3.1 MDX Component Registry

**File**: `frontend/src/mdx-components.ts`
**Status**: Verify exports exist
**Action**: 
- Check that all 4 components are exported
- Verify export format matches Chapter 1/Chapter 2 pattern
- Note: Explicit imports in MDX also work if registry is not used

**Expected Exports**:
```typescript
export default {
  AskQuestionBlock,
  ExplainLike10Block,
  InteractiveQuizBlock,
  GenerateDiagramBlock,
};
```

### 3.2 Legacy Registry Check

**File**: `frontend/src/theme/MDXComponents.tsx` (if swizzled)
**Status**: Check if swizzled version exists
**Action**: 
- If swizzled, verify components are included
- If not swizzled, explicit imports in MDX work fine

---

## 4. Build Validation Plan

### 4.1 Commands to Test Build

**Build Command**: `npm run build` in `frontend/` directory
**Expected Result**: Build succeeds with no errors or warnings
**Validation**: 
- No TypeScript errors
- No MDX compilation errors
- No missing component errors

### 4.2 Browser-Level Checks

**Start Command**: `npm start` in `frontend/` directory
**Navigate To**: `/docs/chapters/chapter-3`
**Expected Result**: 
- All 4 AI blocks render visually
- Components appear in correct positions
- Placeholder UI displays (no API calls)

### 4.3 Error Expectations and Resolution

**Common Errors**:
1. **Import Error**: "Cannot find module '@site/src/components/ai/...'"
   - **Resolution**: Verify component files exist, check import paths
2. **TypeScript Error**: "Property 'X' is missing in type..."
   - **Resolution**: Verify all required props are provided
3. **MDX Error**: "Unexpected token"
   - **Resolution**: Check JSX syntax, verify component tags are properly closed

---

## 5. Constraints

### 5.1 No AI Runtime Implementation

- **Constraint**: MUST NOT add backend AI runtime logic
- **Rationale**: Runtime integration is Feature 041 scope
- **Implementation**: Components show placeholder UI only

### 5.2 No Backend Changes

- **Constraint**: MUST NOT modify backend files
- **Rationale**: This is frontend-only integration
- **Implementation**: Only modify `frontend/docs/chapters/chapter-3.mdx`

### 5.3 Strict Placeholder-to-Component Mapping

- **Constraint**: MUST replace placeholders exactly as specified
- **Rationale**: Ensures correct placement and props
- **Implementation**: Follow Feature 037 specification exactly

### 5.4 No Chapter 1 or Chapter 2 Modifications

- **Constraint**: MUST NOT modify Chapter 1 or Chapter 2 MDX files
- **Rationale**: Only Chapter 3 integration in this feature
- **Implementation**: Only modify chapter-3.mdx

---

## 6. Success Criteria

- ✅ All AI blocks appear visually in Chapter 3
- ✅ No TypeScript errors
- ✅ Correct ordering of components (matches Feature 037)
- ✅ No missing imports
- ✅ Build runs without warnings
- ✅ Components render with placeholder UI (no API calls)

---

## 7. Dependencies + Risks

### Dependencies:
- Feature 001: Base Project Initialization
- Feature 037: Chapter 3 Content Specification (placement rules)
- Feature 038: Chapter 3 MDX Implementation (MDX file with placeholders)
- Feature 004: Chapter 1 Interactive AI Blocks (components exist)

### Risks:
1. **Risk**: Component import paths may be incorrect
   - **Mitigation**: Verify paths match Chapter 1/Chapter 2 patterns
2. **Risk**: Props may not match component interfaces
   - **Mitigation**: Check component prop interfaces, verify all required props
3. **Risk**: Docusaurus build may fail
   - **Mitigation**: Test build early, fix errors incrementally

---

## Summary

This plan establishes the complete architecture for Chapter 3 AI blocks integration. The implementation follows Feature 037 specification exactly, replaces HTML comment placeholders with React components, and ensures components render correctly. All components are frontend UI only—no backend changes required.

**Estimated Implementation Time**: 30-45 minutes (MDX integration only, no backend logic)
**Complexity**: Low (following existing patterns, explicit component placement)
**Dependencies**: Feature 001, Feature 037, Feature 038, Feature 004
**Out of Scope**: Backend AI runtime integration, RAG pipeline, real API calls

