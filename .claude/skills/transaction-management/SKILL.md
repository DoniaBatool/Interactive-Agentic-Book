---
name: transaction-management
description: Implement atomic database operations with proper transaction management and rollback handling (Phase 2 pattern)
---

# Skill: Transaction Management (Correctness Under Concurrency)

## Description
Expert-level skill to make database writes correct and reliable: transaction boundaries, isolation, idempotency, retries, and deadlock-safe patterns.

## When to Use
- Any multi-step write (create session + messages, admin updates)
- Concurrency bugs or inconsistent data
- Migrations/backfills that must be safe

## Playbook
1. **Define transaction boundaries**
   - What must be atomic vs eventually consistent
2. **Choose isolation**
   - Default usually OK; bump only when necessary
3. **Idempotency**
   - Use stable IDs; upserts; unique constraints
4. **Retries**
   - Retry only on safe transient errors; avoid double-writes

## Output Artifacts
- Transaction helper patterns
- Tests for concurrent writes
- Notes on retry behavior

## Integration
- Works with: `database-schema-expander`, `connection-pooling`, `qa-engineer`