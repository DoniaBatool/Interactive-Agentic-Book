---
name: new-feature
description: Automatically scaffold a complete new feature with spec.md, plan.md, and tasks.md from a feature description
---

# Skill: New Feature Builder (Product → Shipping)

## Description
Expert-level skill to build a new feature end-to-end: clarify requirements, design API/UI, implement safely, and ship with monitoring and docs.

## When to Use
- Any new feature request
- Any multi-step change requiring coordination

## Playbook
1. **Clarify**
   - user story, acceptance criteria, non-goals
2. **Design**
   - contracts, states, error cases, UX flows
3. **Implement**
   - small commits; feature flags if risky
4. **Verify**
   - tests + smoke checks
5. **Ship**
   - deploy + monitor + document

## Definition of Done
- [ ] Feature works on fresh load and client-side navigation
- [ ] Error states are user-friendly
- [ ] Logged/observable in production
- [ ] Docs updated

## Integration
- Works with: `change-management`, `qa-engineer`, `production-checklist`