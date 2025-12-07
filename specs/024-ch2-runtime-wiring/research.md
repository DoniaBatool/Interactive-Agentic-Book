# Research Notes: Chapter 2 Backend Runtime Wiring

**Feature**: 024-ch2-runtime-wiring
**Date**: 2025-01-27

## Problem Context

This feature wires Chapter 2 AI blocks into the backend runtime system. The goal is to create complete scaffolding for backend runtime routing, RAG layer, subagents, and skills extensions—all as placeholders with no real AI logic.

**Key Challenge**: Ensuring all routing paths are documented, all files are created, and backend starts without errors while maintaining placeholder-only implementation.

---

## Industry References

### Runtime Engine Patterns

**Source**: Feature 006 (AI Runtime Engine), Feature 022 (Chapter 2 Runtime Wiring)

**Key Findings**:
- Runtime engine uses chapter_id parameter for routing
- Chapter 2 routing should follow same patterns as Chapter 1
- Placeholder routing with TODO comments is acceptable for scaffolding phase

---

### Subagent Architecture

**Source**: Existing subagents (ask_question_agent.py, etc.)

**Key Findings**:
- Subagents follow consistent naming pattern
- Chapter 2 subagents should mirror Chapter 1 structure
- Empty scaffolds with TODO comments are appropriate for scaffolding

---

### Skills Layer Extension

**Source**: Existing skills (retrieval_skill.py, prompt_builder_skill.py, formatting_skill.py)

**Key Findings**:
- Skills are reusable across chapters
- Chapter 2 extensions should be comment-only (no logic)
- Placeholder routing comments document expected handling paths

---

## Observations

### Current Architecture

**Runtime Engine**:
- Already has Chapter 2 knowledge source mapping (from Feature 011)
- Has placeholder routing for chapterId=2 (from Feature 022)
- Needs subagent routing placeholders

**API Layer**:
- Already routes to runtime engine
- May need Chapter 2 routing comments
- Generic routing should handle chapterId=2

**RAG Layer**:
- Chapter 1 chunks structure exists
- Chapter 2 chunks file needs to be created
- Should match Chapter 1 structure

---

## Technical Decisions

### Decision 1: Create Chapter 2-Specific Subagent Files

**Rationale**: Clear separation between Chapter 1 and Chapter 2 logic, easier to maintain

**Alternative Considered**: Extend existing subagents with Chapter 2 branches

**Chosen**: Create ch2_*_agent.py files as empty scaffolds

---

### Decision 2: Comment-Only Skills Extensions

**Rationale**: Skills are reusable, only need to document Chapter 2 handling paths

**Alternative Considered**: Create Chapter 2-specific skills files

**Chosen**: Add placeholder routing comments to existing skills files

---

### Decision 3: Placeholder-Only Implementation

**Rationale**: This is a scaffolding feature, no real AI logic should be implemented

**Alternative Considered**: Implement partial logic

**Chosen**: Placeholder-only with TODO comments

---

## Implementation Notes

### File Creation Strategy

**New Files**:
- `chapter_2_chunks.py` - Match chapter_1_chunks structure
- `ch2_ask_question_agent.py` - Empty scaffold
- `ch2_explain_el10_agent.py` - Empty scaffold
- `ch2_quiz_agent.py` - Empty scaffold
- `ch2_diagram_agent.py` - Empty scaffold

**Modified Files**:
- `ai_blocks.py` - Add Chapter 2 routing comments
- `engine.py` - Add Chapter 2 routing placeholders (may already exist)
- `retrieval_skill.py` - Add Chapter 2 placeholder comments
- `prompt_builder_skill.py` - Add Chapter 2 placeholder comments
- `formatting_skill.py` - Add Chapter 2 placeholder comments

---

## Risks and Mitigations

### Risk 1: Import Errors

**Mitigation**: 
- Test all imports after file creation
- Ensure all files are syntactically correct
- Verify backend starts without errors

---

### Risk 2: Breaking Existing Functionality

**Mitigation**:
- Only add placeholders and comments
- Don't modify existing logic
- Test Chapter 1 functionality still works

---

### Risk 3: Incomplete Scaffolding

**Mitigation**:
- Follow Chapter 1 patterns exactly
- Ensure all required files are created
- Verify all TODO comments are present

---

## Next Steps

1. **Implementation**: Create all required files with placeholders
2. **Validation**: Test backend startup and imports
3. **Documentation**: Update contract with actual file structures

---

## Summary

This feature creates complete backend runtime scaffolding for Chapter 2. Key patterns:
- Chapter 2-specific subagent files (ch2_*_agent.py)
- Comment-only skills extensions
- Placeholder-only implementation
- Structure parity with Chapter 1

**Estimated Complexity**: Low (scaffolding only, no logic)
**Dependencies**: Feature 006 (Runtime Engine), Feature 023 (Frontend MDX)
**Out of Scope**: Real AI logic, RAG implementation, subagent logic

