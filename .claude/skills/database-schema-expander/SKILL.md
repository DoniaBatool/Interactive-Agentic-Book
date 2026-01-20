---
name: database-schema-expander
description: Add new tables to existing database schema with migrations, indexes, and backward compatibility (project)
---

# Skill: Database Schema Expander (Migrations + Backwards Compatibility)

## Description
Expert-level skill for evolving database schemas safely: migrations, backfills, indexes, constraints, and zero-downtime rollout patterns.

## When to Use
- Adding columns/tables/indexes
- Changing enums/constraints
- Introducing new relationships or multi-tenant boundaries

## Playbook (Expand/Contract)
1. **Expand**
   - Add new columns/tables nullable + defaults
2. **Backfill**
   - Batch job; idempotent; monitor locks + latency
3. **Dual-read / Dual-write (if needed)**
   - Deploy code compatible with both schemas
4. **Contract**
   - Remove old columns once fully migrated

## Zero-Downtime Checklist
- [ ] Additive change first (no breaking reads)
- [ ] Backfill avoids long table locks
- [ ] Indexes created safely (concurrent where supported)
- [ ] Rollback plan (including data considerations)

## Integration
- Works with: `transaction-management`, `connection-pooling`, `production-checklist`