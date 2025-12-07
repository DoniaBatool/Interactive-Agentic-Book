# Research Notes: Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime

**Feature**: 026-ch2-explain-el10-runtime
**Date**: 2025-01-27

## Problem Context

This feature establishes the scaffolding for AI-powered ELI10 explanation runtime for Chapter 2. The system needs to generate age-appropriate explanations for ROS 2 concepts using LLM reasoning, supporting future integrations with RAG pipeline, LLM providers, and the AI Runtime Engine.

**Key Challenge**: Ensuring all routing paths are documented, all files are created, and backend starts without errors while maintaining placeholder-only implementation that mirrors Feature 025 (Chapter 2 Diagram Runtime).

---

## Industry References

### ELI10 Explanation Patterns

**Source**: Feature 025 (Chapter 2 Diagram Runtime), Chapter 1 ELI10 patterns

**Key Findings**:
- ELI10 runtime uses 5-step pipeline: Validate → Build Prompt → RAG Retrieve → Call LLM → Format
- Prompt templates use variable substitution ({{variable}})
- Skills layer provides reusable functions for prompt building and formatting
- Runtime engine routes ELI10 requests based on block_type and chapterId

---

### LLM Reasoning + Age-Appropriate Explanations

**Source**: Existing explain_el10_agent.py

**Key Findings**:
- Explanations generated using LLM reasoning with ELI10 prompt pattern
- Explanation structure: explanation, examples, analogies
- Agent methods: build prompt → call LLM → format response
- Age-appropriate language (10-year-old level)

---

## Observations

### Chapter 1 ELI10 Runtime

**Pattern Used**:
- Runtime module: `backend/app/ai/subagents/explain_el10_agent.py`
- Prompt templates: (to be created for Chapter 2)
- Skills: `backend/app/ai/skills/prompt_builder_skill.py`, `formatting_skill.py`
- Routing: Runtime engine routes to explain_el10_agent

**Key Success Factors**:
- Clear 5-step pipeline
- Reusable skills functions
- Template-based prompt generation
- Structured explanation output

---

### Chapter 2 Requirements

**Differences from Chapter 1**:
- `chapter_id=2` instead of `chapter_id=1`
- ROS 2-specific concepts (topics, nodes, services, actions)
- ROS 2 analogies (post office, restaurant, phone calls, package delivery)
- Chapter 2 prompt template (ch2_el10_prompt.txt)

**Similarities**:
- Same 5-step pipeline structure
- Same skills pattern (build prompt, format output)
- Same routing pattern (runtime engine → ELI10 runtime)
- Same placeholder-only implementation

---

## Technical Decisions

### Decision 1: Create Chapter 2-Specific Runtime Module

**Rationale**: Clear separation between Chapter 1 and Chapter 2 logic, mirrors Feature 025 structure

**Alternative Considered**: Extend existing ELI10 agent with Chapter 2 branches

**Chosen**: Create ch2_el10_runtime.py as separate module

**Impact**: Clear separation, easier to implement Chapter 2-specific logic later

---

### Decision 2: Create Chapter 2 Prompt Template

**Rationale**: ROS 2-specific explanations need different analogies and examples

**Alternative Considered**: Reuse Chapter 1 prompt template with variables

**Chosen**: Create ch2_el10_prompt.txt with ROS 2-specific placeholders

**Impact**: Better prompt engineering for ROS 2 explanations

---

### Decision 3: Placeholder-Only Implementation

**Rationale**: This is a scaffolding feature, no real AI logic should be implemented

**Alternative Considered**: Implement partial logic

**Chosen**: Placeholder-only with TODO comments

**Impact**: Clear separation between scaffolding and implementation phases

---

## Implementation Notes

### File Creation Strategy

**New Files**:
- `ch2_el10_runtime.py` - Mirror Feature 025 structure
- `ch2_el10_prompt.txt` - ROS 2-specific template
- `el10-contract.yaml` - Placeholder contract

**Modified Files**:
- `engine.py` - Add Chapter 2 ELI10 routing (comments only)
- `ai_blocks.py` - Add Chapter 2 routing comments
- `prompt_builder_skill.py` - Add build_el10_prompt_ch2() placeholder
- `formatting_skill.py` - Add format_el10_output_ch2() placeholder

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
- Test Chapter 1 ELI10 functionality still works

---

### Risk 3: Incomplete Scaffolding

**Mitigation**:
- Follow Feature 025 patterns exactly
- Ensure all required files are created
- Verify all TODO comments are present

---

## Next Steps

1. **Implementation**: Create all required files with placeholders
2. **Validation**: Test backend startup and imports
3. **Documentation**: Update contract with actual file structures

---

## Summary

This feature creates complete ELI10 runtime scaffolding for Chapter 2. Key patterns:
- Chapter 2-specific runtime module (ch2_el10_runtime.py)
- ROS 2-specific prompt template (ch2_el10_prompt.txt)
- Placeholder-only implementation
- Structure parity with Feature 025

**Estimated Complexity**: Low (scaffolding only, no logic)
**Dependencies**: Feature 025 (Chapter 2 Diagram Runtime), Feature 024 (Backend Runtime Wiring)
**Out of Scope**: Real AI logic, RAG implementation, LLM calls, explanation generation

