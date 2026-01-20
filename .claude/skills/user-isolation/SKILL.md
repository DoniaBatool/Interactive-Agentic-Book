---
name: user-isolation
description: Enforce user isolation with ownership checks at database query level to prevent horizontal privilege escalation (Phase 2 pattern)
---

# Skill: User Isolation (Multi-Tenant Safety + Privacy)

## Description
Expert-level skill to ensure one user cannot access another user’s data. Covers authorization, row-level filtering, secure identifiers, and audit logging.

## When to Use
- Any feature storing user data (chat history, profiles, admin tools)
- Multi-tenant databases or shared resources
- “Session ID” based history endpoints

## Playbook
1. **Define tenant boundary**
   - user_id / org_id / session_id mapping
2. **Enforce authz**
   - checks at service layer AND query layer
3. **Secure identifiers**
   - UUIDs; avoid predictable IDs
4. **Audit**
   - log access patterns; alert on suspicious access

## Output Artifacts
- AuthZ policy notes
- Query patterns that always filter by tenant
- Tests for IDOR attempts

## Integration
- Works with: `security-engineer`, `conversation-manager`, `qa-engineer`