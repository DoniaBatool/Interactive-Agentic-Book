# Research Notes: Chapter 3 Diagram Generator Runtime Layer

**Feature**: 031-ch3-diagram-runtime
**Date**: 2025-01-27

## Problem Context

This feature establishes the scaffolding for AI-powered diagram generation runtime for Chapter 3. The system needs to generate Physical AI diagrams using LLM reasoning + structured outputs, supporting future integrations with SVG generators, JSON diagram structures, and the AI Runtime Engine.

**Key Challenge**: Ensuring all routing paths are documented, all files are created, and backend starts without errors while maintaining placeholder-only implementation that mirrors Feature 025 (Chapter 2 Diagram Runtime).

---

## Industry References

### Diagram Generation Patterns

**Source**: Feature 025 (Chapter 2 Diagram Runtime)

**Key Findings**:
- Diagram runtime uses 5-step pipeline: Validate → Build Prompt → Call RAG → Call LLM → Format
- Prompt templates use variable substitution ({{variable}})
- Skills layer provides reusable functions for prompt building and formatting
- Runtime engine routes diagram requests based on block_type and chapterId

---

### LLM Reasoning + Structured Outputs

**Source**: Feature 025 research

**Key Findings**:
- Diagrams generated using LLM reasoning with structured outputs
- Diagram structure: nodes, edges, SVG
- Schema models define request/response structures
- Subagent methods: ch3_diagram_agent() (from Feature 030)

---

## Observations

### Chapter 2 Diagram Runtime (Feature 025)

**Pattern Used**:
- Runtime module: `backend/app/ai/diagram/ch2_diagram_runtime.py`
- Prompt templates: `backend/app/ai/prompts/diagram/ch2_diagram_prompt.txt`
- Skills: `backend/app/ai/skills/prompt_builder_skill.py`, `formatting_skill.py`
- Routing: Runtime engine → ch2_diagram_runtime

**Key Success Factors**:
- Clear 5-step pipeline
- Reusable skills functions
- Template-based prompt generation
- Structured diagram output

---

### Chapter 3 Requirements

**Differences from Chapter 2**:
- `chapter_id=3` instead of `chapter_id=2`
- Physical AI-specific diagram types (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- Physical AI concepts (perception, sensors, computer-vision, signal-processing, feature-extraction)
- Chapter 3 prompt template (ch3_diagram_prompt.txt)
- Subagent already exists (ch3_diagram_agent from Feature 030)

**Similarities**:
- Same 5-step pipeline structure
- Same skills pattern (build prompt, format output)
- Same routing pattern (runtime engine → diagram runtime)
- Same placeholder-only implementation

---

## Technical Decisions

### Decision 1: Create Chapter 3-Specific Runtime Module

**Rationale**: Clear separation between Chapter 2 and Chapter 3 logic, mirrors Feature 025 structure

**Alternative Considered**: Extend existing diagram runtime with Chapter 3 branches

**Chosen**: Create ch3_diagram_runtime.py as separate module

**Impact**: Clear separation, easier to implement Chapter 3-specific logic later

---

### Decision 2: Create Chapter 3 Prompt Template

**Rationale**: Physical AI-specific prompts need different context and examples

**Alternative Considered**: Reuse Chapter 2 prompt template with variables

**Chosen**: Create ch3_diagram_prompt.txt with Physical AI-specific placeholders

**Impact**: Better prompt engineering for Physical AI diagrams

---

### Decision 3: Integrate with Existing Subagent

**Rationale**: ch3_diagram_agent already exists from Feature 030, runtime module orchestrates the flow

**Alternative Considered**: Create new subagent

**Chosen**: Use existing ch3_diagram_agent from Feature 030

**Impact**: Reuses existing subagent, runtime module orchestrates the diagram generation flow

---

### Decision 4: Placeholder-Only Implementation

**Rationale**: This is a scaffolding feature, no real AI logic should be implemented

**Alternative Considered**: Implement partial logic

**Chosen**: Placeholder-only with TODO comments

**Impact**: Clear separation between scaffolding and implementation phases

---

## Implementation Notes

### File Creation Strategy

**New Files**:
- `ch3_diagram_runtime.py` - Mirror ch2_diagram_runtime.py structure
- `ch3_diagram_prompt.txt` - Physical AI-specific template
- `diagram-api.yaml` - Placeholder contract

**Modified Files**:
- `engine.py` - Add Chapter 3 diagram routing (comments only)
- `ai_blocks.py` - Update `/ai/ch3/diagram` endpoint routing
- `prompt_builder_skill.py` - Add build_diagram_prompt_ch3() placeholder
- `formatting_skill.py` - Add format_diagram_output_ch3() placeholder
- `ch3_pipeline.py` - Add diagram context retrieval stub

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
- Test Chapter 1 and Chapter 2 diagram functionality still works

---

### Risk 3: Incomplete Scaffolding

**Mitigation**:
- Follow Feature 025 patterns exactly
- Ensure all required files are created
- Verify all TODO comments are present

---

### Risk 4: Subagent Integration

**Mitigation**:
- Verify ch3_diagram_agent exists from Feature 030
- Ensure runtime module calls subagent correctly (in TODO comments)
- Document integration in contract

---

## Next Steps

1. **Implementation**: Create all required files with placeholders
2. **Validation**: Test backend startup and imports
3. **Documentation**: Update contract with actual file structures

---

## Summary

This feature creates complete diagram runtime scaffolding for Chapter 3. Key patterns:
- Chapter 3-specific runtime module (ch3_diagram_runtime.py)
- Physical AI-specific prompt template (ch3_diagram_prompt.txt)
- Integration with existing ch3_diagram_agent subagent
- Placeholder-only implementation
- Structure parity with Feature 025

**Estimated Complexity**: Low (scaffolding only, no logic)
**Dependencies**: Feature 025 (Chapter 2 Diagram Runtime), Feature 030 (Chapter 3 AI Runtime Engine Integration)
**Out of Scope**: Real AI logic, RAG implementation, LLM calls, diagram generation

