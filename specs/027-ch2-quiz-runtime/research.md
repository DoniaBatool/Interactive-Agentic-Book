# Research Notes: Chapter 2 Interactive Quiz Runtime Engine

**Feature**: 027-ch2-quiz-runtime
**Date**: 2025-01-27

## Problem Context

This feature establishes the scaffolding for AI-powered quiz generation runtime for Chapter 2. The system needs to generate ROS 2 quizzes using LLM reasoning, supporting future integrations with RAG pipeline, LLM providers, and the AI Runtime Engine.

**Key Challenge**: Ensuring all routing paths are documented, all files are created, and backend starts without errors while maintaining placeholder-only implementation that mirrors Feature 026 (Chapter 2 ELI10 Runtime).

---

## Industry References

### Quiz Generation Patterns

**Source**: Feature 026 (Chapter 2 ELI10 Runtime), Chapter 1 quiz patterns

**Key Findings**:
- Quiz runtime uses 6-step pipeline: Validate → Build Prompt → Retrieve Context → Call RAG → Call LLM → Format
- Prompt templates use variable substitution ({{variable}})
- Skills layer provides reusable functions for prompt building and formatting
- Runtime engine routes quiz requests based on block_type and chapterId

---

### LLM Reasoning + Quiz Generation

**Source**: Existing quiz_agent.py, quiz runtime

**Key Findings**:
- Quizzes generated using LLM reasoning with structured outputs
- Quiz structure: questions, answers, learning_objectives, metadata
- Agent methods: build prompt → call LLM → format response
- Question types: multiple choice, true/false, short answer

---

## Observations

### Chapter 1 Quiz Runtime

**Pattern Used**:
- Runtime module: `backend/app/ai/quiz/runtime.py`
- Prompt templates: (to be created for Chapter 2)
- Skills: `backend/app/ai/skills/prompt_builder_skill.py`, `formatting_skill.py`
- Routing: Runtime engine routes to quiz runtime

**Key Success Factors**:
- Clear 6-step pipeline
- Reusable skills functions
- Template-based prompt generation
- Structured quiz output

---

### Chapter 2 Requirements

**Differences from Chapter 1**:
- `chapter_id=2` instead of `chapter_id=1`
- ROS 2-specific learning objectives (topics, nodes, services, actions)
- ROS 2 examples and scenarios
- Chapter 2 prompt template (ch2_quiz_prompt.txt)
- Quiz-specific chunk retrieval (get_chapter2_quiz_chunks)

**Similarities**:
- Same 6-step pipeline structure
- Same skills pattern (build prompt, format output)
- Same routing pattern (runtime engine → quiz runtime)
- Same placeholder-only implementation

---

## Technical Decisions

### Decision 1: Create Chapter 2-Specific Runtime Module

**Rationale**: Clear separation between Chapter 1 and Chapter 2 logic, mirrors Feature 026 structure

**Alternative Considered**: Extend existing quiz runtime with Chapter 2 branches

**Chosen**: Create ch2_quiz_runtime.py as separate module

**Impact**: Clear separation, easier to implement Chapter 2-specific logic later

---

### Decision 2: Create Chapter 2 Prompt Template

**Rationale**: ROS 2-specific quizzes need different learning objectives and examples

**Alternative Considered**: Reuse Chapter 1 prompt template with variables

**Chosen**: Create ch2_quiz_prompt.txt with ROS 2-specific placeholders

**Impact**: Better prompt engineering for ROS 2 quizzes

---

### Decision 3: Placeholder-Only Implementation

**Rationale**: This is a scaffolding feature, no real AI logic should be implemented

**Alternative Considered**: Implement partial logic

**Chosen**: Placeholder-only with TODO comments

**Impact**: Clear separation between scaffolding and implementation phases

---

### Decision 4: Quiz-Specific Chunk Retrieval

**Rationale**: Quiz generation may need different chunk filtering than general RAG

**Alternative Considered**: Reuse general get_chapter_chunks() function

**Chosen**: Create get_chapter2_quiz_chunks() placeholder function

**Impact**: Flexibility for quiz-specific chunk filtering in future

---

## Implementation Notes

### File Creation Strategy

**New Files**:
- `ch2_quiz_runtime.py` - Mirror Feature 026 structure
- `ch2_quiz_prompt.txt` - ROS 2-specific template
- `quiz-contract.yaml` - Placeholder contract

**Modified Files**:
- `engine.py` - Add Chapter 2 quiz routing (comments only)
- `ai_blocks.py` - Add Chapter 2 routing comments
- `prompt_builder_skill.py` - Add build_quiz_prompt_ch2() placeholder
- `formatting_skill.py` - Add format_quiz_output_ch2() placeholder
- `chapter_2_chunks.py` - Add get_chapter2_quiz_chunks() placeholder

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
- Test Chapter 1 quiz functionality still works

---

### Risk 3: Incomplete Scaffolding

**Mitigation**:
- Follow Feature 026 patterns exactly
- Ensure all required files are created
- Verify all TODO comments are present

---

## Next Steps

1. **Implementation**: Create all required files with placeholders
2. **Validation**: Test backend startup and imports
3. **Documentation**: Update contract with actual file structures

---

## Summary

This feature creates complete quiz runtime scaffolding for Chapter 2. Key patterns:
- Chapter 2-specific runtime module (ch2_quiz_runtime.py)
- ROS 2-specific prompt template (ch2_quiz_prompt.txt)
- Quiz-specific chunk retrieval (get_chapter2_quiz_chunks)
- Placeholder-only implementation
- Structure parity with Feature 026

**Estimated Complexity**: Low (scaffolding only, no logic)
**Dependencies**: Feature 026 (Chapter 2 ELI10 Runtime), Feature 024 (Backend Runtime Wiring)
**Out of Scope**: Real AI logic, RAG implementation, LLM calls, quiz generation

