---
name: pydantic-validation
description: Implement declarative input validation with Pydantic DTOs for FastAPI applications (Phase 2 pattern)
---

# Skill: Pydantic Validation (Schemas, Errors, Contracts)

## Description
Expert-level skill for building robust API contracts with Pydantic: strict validation, clean error messages, and safe parsing for external inputs.

## When to Use
- Any API endpoint accepting user input
- Config parsing from env vars
- Complex nested payloads (filters, tool calls)

## Playbook
1. **Model first**
   - Define request/response models; avoid `Any`
2. **Validation**
   - Use field constraints (min/max, regex) and custom validators
3. **Error mapping**
   - Convert validation errors into a consistent API format
4. **Security**
   - Enforce size limits; reject unexpected fields when appropriate

## Output Artifacts
- Typed schemas + examples
- Consistent error envelope
- `.env.example` + config validation

## Integration
- Works with: `api-contract-design`, `api-docs-generator`, `security-engineer`