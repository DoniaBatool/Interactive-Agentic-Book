# Research Notes: Chapter 2 AI Block Rendering + MDX Integration

**Feature**: 023-ch2-ai-blocks
**Date**: 2025-01-27

## Problem Context

This feature enables interactive AI blocks inside Chapter 2 by integrating React components into MDX files. The goal is to render all 4 AI block types (Ask Question, Explain Like I'm 10, Interactive Quiz, Generate Diagram) in Chapter 2 with correct props and positioning.

**Key Challenge**: Ensuring MDX component integration works correctly with Docusaurus, maintaining consistency with Chapter 1 patterns, and validating that all components render without errors.

---

## Industry References

### Docusaurus MDX Integration

**Source**: Docusaurus Documentation
- MDX files support React components directly
- Components can be imported and used in MDX
- Component mapping via `mdx-components.ts` or swizzle approach
- Props can be passed using JSX syntax

**Key Findings**:
- Import statements must be at top of MDX file (after frontmatter)
- Components can be self-closing or properly closed
- Props use JSX syntax (curly braces for numbers, quotes for strings)
- Docusaurus 3.x may require swizzle approach for global component mapping

---

### React Component Props in MDX

**Pattern**: TypeScript interfaces for component props
- Optional props use `?:` syntax
- Required props have no `?`
- Props validation happens at runtime (TypeScript compile-time)

**Key Findings**:
- Props must match TypeScript interface exactly
- Optional props can be omitted
- Number props use curly braces: `{2}`
- String props use quotes: `"value"`

---

### MDX Component Mapping Patterns

**Pattern 1**: Direct imports in MDX file
- Each MDX file imports components it needs
- Explicit and clear dependencies
- Works reliably across Docusaurus versions

**Pattern 2**: Global component mapping
- Components exported from `mdx-components.ts`
- Components available without explicit imports
- May require swizzle in Docusaurus 3.x

**Key Findings**:
- Direct imports are more reliable
- Global mapping requires configuration
- Both patterns can coexist

---

## Observations

### Chapter 1 Implementation (Feature 004)

**Pattern Used**:
- Direct imports in chapter-1.mdx
- Components imported from `@site/src/components/ai/`
- Components used with props: `<AskQuestionBlock chapterId={1} sectionId="..." />`
- All 4 components successfully integrated

**Key Success Factors**:
- Clear import statements
- Correct prop syntax
- Proper component placement
- Build validation

---

### Chapter 2 Requirements

**Differences from Chapter 1**:
- `chapterId={2}` instead of `chapterId={1}`
- ROS 2-specific concepts (topics, nodes, services, actions)
- Chapter 2 section IDs (introduction-to-ros2, etc.)
- Chapter 2 diagram types (node-communication-architecture, etc.)

**Similarities**:
- Same 4 component types
- Same import patterns
- Same prop structure
- Same MDX integration approach

---

### Build Validation

**Docusaurus Build Process**:
1. Parse MDX files
2. Resolve imports
3. Compile TypeScript/JSX
4. Generate static HTML

**Common Issues**:
- Missing imports → Build fails
- Invalid props → TypeScript errors
- Component not found → Runtime errors
- MDX syntax errors → Build fails

**Validation Strategy**:
- Run `npm run build` to catch compilation errors
- Check browser console for runtime errors
- Verify components render in correct positions
- Test component props are passed correctly

---

## Technical Decisions

### Decision 1: Use Direct Imports

**Rationale**: More reliable, explicit dependencies, works across Docusaurus versions

**Alternative Considered**: Global component mapping via `mdx-components.ts`

**Chosen**: Direct imports in chapter-2.mdx

---

### Decision 2: Reuse Existing Components

**Rationale**: No need to create new components, consistency with Chapter 1, faster implementation

**Alternative Considered**: Create Chapter 2-specific components

**Chosen**: Reuse components from Feature 004 with Chapter 2 props

---

### Decision 3: Validate Build Early

**Rationale**: Catch errors before deployment, ensure components render correctly

**Alternative Considered**: Defer validation until later

**Chosen**: Run build validation as part of feature completion

---

## Implementation Notes

### Component Props Values

**Current Status**: Some props may use TODO placeholders if exact values not yet determined

**Future**: Replace TODO placeholders with actual values from Chapter 2 content

**Example**:
- Current: `sectionId="TODO"` or `sectionId="introduction-to-ros2"`
- Future: All props have actual values from Chapter 2 sections

---

### MDX File Structure

**Required Structure**:
1. Frontmatter (YAML)
2. Import statements
3. Content with embedded components

**Component Placement**:
- Components embedded at pedagogically correct positions
- Components don't break document flow
- Components properly closed

---

## Risks and Mitigations

### Risk 1: Components Don't Render

**Mitigation**: 
- Verify imports are correct
- Check component names match exactly
- Validate build succeeds
- Test in browser

---

### Risk 2: Props Don't Match Expected Interface

**Mitigation**:
- Use TypeScript interfaces for validation
- Check props syntax (curly braces for numbers, quotes for strings)
- Verify props match component expectations

---

### Risk 3: Build Fails

**Mitigation**:
- Run build early to catch errors
- Fix import paths
- Resolve TypeScript errors
- Validate MDX syntax

---

## Next Steps

1. **Implementation**: Add components to chapter-2.mdx with correct props
2. **Validation**: Run build and verify components render
3. **Testing**: Test component interactions (if any)
4. **Documentation**: Update contract with actual prop values

---

## Summary

This feature focuses on MDX integration for Chapter 2 AI blocks. Key patterns:
- Direct imports in MDX file
- Reuse existing components with Chapter 2 props
- Validate build early
- Follow Chapter 1 patterns for consistency

**Estimated Complexity**: Low (scaffolding only, no new logic)
**Dependencies**: Feature 004 (components), Feature 010/014 (Chapter 2 content)
**Out of Scope**: Backend integration, AI logic implementation

