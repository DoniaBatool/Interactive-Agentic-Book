# Research Notes: Chapter 2 Diagram Generator Runtime

**Feature**: 025-ch2-diagram-runtime
**Date**: 2025-01-27

## Problem Context

This feature establishes the scaffolding for AI-powered diagram generation runtime for Chapter 2. The system needs to generate ROS 2 diagrams using LLM reasoning + structured outputs, supporting future integrations with SVG generators, JSON diagram structures, and the AI Runtime Engine.

**Key Challenge**: Ensuring all routing paths are documented, all files are created, and backend starts without errors while maintaining placeholder-only implementation that mirrors Feature 008 (Chapter 1 Diagram Engine).

---

## Industry References

### Diagram Generation Patterns

**Source**: Feature 008 (Chapter 1 Diagram Engine)

**Key Findings**:
- Diagram runtime uses 5-step pipeline: Validate → Build Prompt → Call RAG → Call LLM → Format
- Prompt templates use variable substitution ({{variable}})
- Skills layer provides reusable functions for prompt building and formatting
- Runtime engine routes diagram requests based on block_type and chapterId

---

### LLM Reasoning + Structured Outputs

**Source**: Feature 008 research

**Key Findings**:
- Diagrams generated using LLM reasoning with structured outputs
- Diagram structure: nodes, edges, SVG
- Schema models define request/response structures
- Agent methods: plan_diagram(), create_structure(), generate_svg_stub()

---

## Observations

### Chapter 1 Diagram Runtime (Feature 008)

**Pattern Used**:
- Runtime module: `backend/app/ai/diagram/runtime.py`
- Prompt templates: `backend/app/ai/diagrams/templates/*.txt`
- Skills: `backend/app/ai/skills/diagram_skill.py`
- Schema: `backend/app/ai/diagram/schema.py`

**Key Success Factors**:
- Clear 5-step pipeline
- Reusable skills functions
- Template-based prompt generation
- Structured diagram output

---

### Chapter 2 Requirements

**Differences from Chapter 1**:
- `chapter_id=2` instead of `chapter_id=1`
- ROS 2-specific diagram types (ros2-ecosystem-overview, node-communication-architecture, etc.)
- ROS 2 concepts (nodes, topics, services, actions)
- Chapter 2 prompt template (ch2_diagram_prompt.txt)

**Similarities**:
- Same 5-step pipeline structure
- Same skills pattern (build prompt, format output)
- Same routing pattern (runtime engine → diagram runtime)
- Same placeholder-only implementation

---

## Technical Decisions

### Decision 1: Create Chapter 2-Specific Runtime Module

**Rationale**: Clear separation between Chapter 1 and Chapter 2 logic, mirrors Feature 008 structure

**Alternative Considered**: Extend existing diagram runtime with Chapter 2 branches

**Chosen**: Create ch2_diagram_runtime.py as separate module

**Impact**: Clear separation, easier to implement Chapter 2-specific logic later

---

### Decision 2: Create Chapter 2 Prompt Template

**Rationale**: ROS 2-specific prompts need different context and examples

**Alternative Considered**: Reuse Chapter 1 prompt template with variables

**Chosen**: Create ch2_diagram_prompt.txt with ROS 2-specific placeholders

**Impact**: Better prompt engineering for ROS 2 diagrams

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
- `ch2_diagram_runtime.py` - Mirror runtime.py structure
- `ch2_diagram_prompt.txt` - ROS 2-specific template
- `diagram-contract.yaml` - Placeholder contract

**Modified Files**:
- `engine.py` - Add Chapter 2 diagram routing (comments only)
- `ai_blocks.py` - Add Chapter 2 routing comments
- `prompt_builder_skill.py` - Add build_diagram_prompt_ch2() placeholder
- `formatting_skill.py` - Add format_diagram_output_ch2() placeholder

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
- Test Chapter 1 diagram functionality still works

---

### Risk 3: Incomplete Scaffolding

**Mitigation**:
- Follow Feature 008 patterns exactly
- Ensure all required files are created
- Verify all TODO comments are present

---

## Next Steps

1. **Implementation**: Create all required files with placeholders
2. **Validation**: Test backend startup and imports
3. **Documentation**: Update contract with actual file structures

---

## Summary

This feature creates complete diagram runtime scaffolding for Chapter 2. Key patterns:
- Chapter 2-specific runtime module (ch2_diagram_runtime.py)
- ROS 2-specific prompt template (ch2_diagram_prompt.txt)
- Placeholder-only implementation
- Structure parity with Feature 008

**Estimated Complexity**: Low (scaffolding only, no logic)
**Dependencies**: Feature 008 (Chapter 1 Diagram Engine), Feature 024 (Backend Runtime Wiring)
**Out of Scope**: Real AI logic, RAG implementation, LLM calls, diagram generation

