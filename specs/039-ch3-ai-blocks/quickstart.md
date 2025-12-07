# Quickstart Guide: Chapter 3 AI Blocks Integration

**Feature**: 039-ch3-ai-blocks
**Branch**: `039-ch3-ai-blocks`
**Estimated Time**: 30-45 minutes (MDX integration only, no backend logic)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 037 (Chapter 3 Content Specification) completed - Source for placement rules
- [x] Feature 038 (Chapter 3 MDX Implementation) completed - MDX file with placeholders exists
- [x] Feature 004 (Chapter 1 Interactive AI Blocks) completed - Components exist
- [x] Git branch `039-ch3-ai-blocks` checked out
- [x] Read `specs/039-ch3-ai-blocks/spec.md`
- [x] Read `specs/037-ch3-content-spec/spec.md` (Feature 037 for placement rules)

## Implementation Overview

**Total Steps**: 3 phases
**Primary Deliverable**: `frontend/docs/chapters/chapter-3.mdx` (with React components)
**Validation**: MDX compiles, components render, no TypeScript errors

---

## Phase 1: Add Component Imports (5 minutes)

### Step 1.1: Open Chapter 3 MDX File

**File**: `frontend/docs/chapters/chapter-3.mdx`

**Action**: Open file in editor

---

### Step 1.2: Add Import Statements

**Location**: After frontmatter (YAML block), before content

**Action**: Add the following import statements:

```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
```

**Validation**: 
- Save file
- Check for TypeScript/import errors
- Verify import paths are correct

---

## Phase 2: Replace Placeholders with Components (20 minutes)

### Step 2.1: Replace Ask Question Placeholder

**Location**: Section 1 (What Is Perception in Physical AI?), at the end

**Find**:
```mdx
<!-- AI-BLOCK: ask-question -->
```

**Replace with**:
```mdx
<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
```

---

### Step 2.2: Replace Generate Diagram Placeholder

**Location**: Section 2 (Types of Sensors in Robotics), in the middle (after diagram placeholder)

**Find**:
```mdx
<!-- AI-BLOCK: generate-diagram -->
```

**Replace with**:
```mdx
<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />
```

---

### Step 2.3: Replace Explain Like 10 Placeholder

**Location**: Section 3 (Computer Vision & Depth Perception), in the middle (before diagram placeholder)

**Find**:
```mdx
<!-- AI-BLOCK: explain-like-i-am-10 -->
```

**Replace with**:
```mdx
<ExplainLike10Block concept="computer-vision" chapterId={3} />
```

---

### Step 2.4: Replace Interactive Quiz Placeholder

**Location**: Section 4 (Signal Processing Basics for AI), at the end

**Find**:
```mdx
<!-- AI-BLOCK: interactive-quiz -->
```

**Replace with**:
```mdx
<InteractiveQuizBlock chapterId={3} numQuestions={5} />
```

---

## Phase 3: Validation (10 minutes)

### Step 3.1: Build Validation

**Action**: Run `npm run build` in frontend directory
**Expected**: Build succeeds with no errors

### Step 3.2: Browser Verification

**Action**: Run `npm start` and navigate to Chapter 3 page
**Expected**: All 4 AI blocks render visually

### Step 3.3: Component Interaction

**Action**: Interact with each AI block (click buttons, input fields)
**Expected**: Placeholder UI appears (no API calls)

---

## Success Criteria

- ✅ All 4 AI blocks appear visually in Chapter 3
- ✅ No TypeScript errors
- ✅ Correct ordering of components (matches Feature 037)
- ✅ No missing imports
- ✅ Build runs without warnings
- ✅ Components render with placeholder UI

---

## Troubleshooting

### Import Errors
- Verify import paths use `@site/src/components/ai/` prefix
- Check that component files exist in `frontend/src/components/ai/`
- Verify component names match exported names

### TypeScript Errors
- Check that props use correct types (numbers use {}, strings use "")
- Verify all required props are provided
- Check component prop interfaces match usage

### Build Errors
- Check MDX syntax (proper JSX formatting)
- Verify all components are imported
- Check for unclosed tags or syntax errors

---

## Notes

- This is frontend UI integration only—no backend changes
- Components show placeholder UI until Feature 041 runtime integration
- All components use chapterId={3} for Chapter 3 context
- Placement follows Feature 037 specification exactly

