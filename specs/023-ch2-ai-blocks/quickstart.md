# Quickstart: Chapter 2 AI Block Rendering + MDX Integration

**Feature**: 023-ch2-ai-blocks
**Date**: 2025-01-27
**Purpose**: Step-by-step implementation guide for integrating AI blocks into Chapter 2 MDX

## Overview

This quickstart guide provides step-by-step instructions for enabling AI-interactive blocks in Chapter 2 (ROS 2 Fundamentals) MDX file. The implementation involves:

1. Adding component imports to chapter-2.mdx
2. Replacing HTML comment placeholders with React components
3. Ensuring correct props for each component
4. Validating Docusaurus build

**Estimated Time**: 30-45 minutes (MDX integration only, no backend logic)

---

## Prerequisites

- ✅ Feature 004 (Chapter 1 Interactive AI Blocks) - Components exist
- ✅ Feature 010 or 014 (Chapter 2 Content) - Chapter 2 MDX file exists
- ✅ Docusaurus frontend setup
- ✅ Git branch `023-ch2-ai-blocks` checked out (or appropriate branch)

---

## Phase 1: Add Component Imports (5 minutes)

### Step 1.1: Open Chapter 2 MDX File

**File**: `frontend/docs/chapters/chapter-2.mdx`

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

**Location**: After "Introduction to ROS 2" section

**Find**:
```mdx
<!-- AI-BLOCK: ask-question -->
```

**Replace with**:
```mdx
<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
```

**Validation**: Component should be placed at correct position

---

### Step 2.2: Replace Generate Diagram Placeholder

**Location**: After "Nodes and Node Communication" section

**Find**:
```mdx
<!-- AI-BLOCK: generate-diagram -->
```

**Replace with**:
```mdx
<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />
```

**Validation**: Component should be placed at correct position

---

### Step 2.3: Replace Explain Like 10 Placeholder

**Location**: Inside "Topics and Messages" section

**Find**:
```mdx
<!-- AI-BLOCK: explain-like-i-am-10 -->
```

**Replace with**:
```mdx
<ExplainLike10Block concept="topics" chapterId={2} />
```

**Validation**: Component should be placed at correct position

---

### Step 2.4: Replace Interactive Quiz Placeholder

**Location**: After "Services and Actions" section

**Find**:
```mdx
<!-- AI-BLOCK: interactive-quiz -->
```

**Replace with**:
```mdx
<InteractiveQuizBlock chapterId={2} numQuestions={6} />
```

**Validation**: Component should be placed at correct position

---

## Phase 3: Verify Component Mapping (5 minutes)

### Step 3.1: Check MDX Components File

**File**: `frontend/src/mdx-components.ts`

**Action**: Verify all 4 components are exported:

```typescript
export default {
  AskQuestionBlock,
  ExplainLike10Block,
  InteractiveQuizBlock,
  GenerateDiagramBlock,
};
```

**Validation**: 
- All 4 components should be exported
- Export names match component names exactly

---

## Phase 4: Build Validation (10 minutes)

### Step 4.1: Run Docusaurus Build

**Command**: `cd frontend && npm run build`

**Expected**: Build completes without errors

**Validation Checklist**:
- [ ] No TypeScript compilation errors
- [ ] No missing component errors
- [ ] MDX file compiles successfully
- [ ] All 4 AI block components imported correctly

---

### Step 4.2: Test in Development Server

**Command**: `cd frontend && npm start`

**Action**: Navigate to `/docs/chapters/chapter-2` in browser

**Validation Checklist**:
- [ ] All 4 AI block components render correctly
- [ ] Components appear in correct locations
- [ ] No React errors in browser console
- [ ] Components display placeholder UI (if no backend yet)

---

### Step 4.3: Verify Component Props

**Action**: Inspect each AI block component in browser DevTools

**Validation Checklist**:
- [ ] AskQuestionBlock has `chapterId={2}` and `sectionId="introduction-to-ros2"`
- [ ] GenerateDiagramBlock has `diagramType="node-communication-architecture"` and `chapterId={2}`
- [ ] ExplainLike10Block has `concept="topics"` and `chapterId={2}`
- [ ] InteractiveQuizBlock has `chapterId={2}` and `numQuestions={6}`

---

## Phase 5: Final Validation (5 minutes)

### Step 5.1: Review MDX File Structure

**File**: `frontend/docs/chapters/chapter-2.mdx`

**Validation Checklist**:
- [ ] Import statements at top (after frontmatter)
- [ ] All 4 components used with correct props
- [ ] Components placed at pedagogically correct positions
- [ ] No HTML comment placeholders remaining (or kept for reference)
- [ ] Components properly closed (self-closing syntax)

---

### Step 5.2: Check for Errors

**Validation Checklist**:
- [ ] No TypeScript errors
- [ ] No React errors in console
- [ ] No build errors
- [ ] All imports resolve correctly

---

## Completion Checklist

- [ ] Component imports added to chapter-2.mdx
- [ ] All 4 HTML comment placeholders replaced with React components
- [ ] All components have correct props (chapterId=2, appropriate sectionId/concept/diagramType)
- [ ] MDX components file exports all 4 components
- [ ] Docusaurus build succeeds
- [ ] Components render correctly in browser
- [ ] No React errors in console
- [ ] Component props verified in DevTools

---

## Troubleshooting

### Issue: Components don't render in chapter-2.mdx

**Solution**: 
- Check import statements are correct
- Verify component names match exactly
- Check Docusaurus build for errors
- Verify MDX component mapping is configured
- Ensure components are properly closed

---

### Issue: Build fails with import errors

**Solution**:
- Verify import paths use `@site/src/components/ai/` prefix
- Check component files exist in `frontend/src/components/ai/`
- Verify component names match exported names
- Check TypeScript compilation errors

---

### Issue: Props don't match expected interface

**Solution**:
- Verify props syntax (curly braces for numbers: `{2}`, quotes for strings: `"value"`)
- Check props match component TypeScript interfaces
- Ensure chapterId is 2 for all components
- Verify sectionId/concept/diagramType match Chapter 2 content

---

### Issue: Components render but props are wrong

**Solution**:
- Check props in browser DevTools
- Verify props match expected values
- Update props if needed
- Rebuild and test again

---

## Next Steps

After completing this quickstart:

1. **Content Review**: Verify component placement is pedagogically correct
2. **Props Refinement**: Update props with exact values from Chapter 2 content (if using TODO placeholders)
3. **Backend Integration**: Connect components to backend API (future feature)
4. **Testing**: Test component interactions (if any backend logic exists)

---

## Summary

This quickstart enables AI-interactive blocks in Chapter 2 by:
- ✅ Adding component imports to MDX file
- ✅ Replacing placeholders with React components
- ✅ Ensuring correct props for Chapter 2 context
- ✅ Validating build and rendering

**Estimated Total Time**: 30-45 minutes (MDX integration only)

**Key Success Factors**:
- Correct import paths
- Proper component syntax
- Accurate props values
- Build validation

