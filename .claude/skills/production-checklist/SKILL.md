---
name: production-checklist
description: Comprehensive production readiness validation checklist covering security, performance, monitoring, and deployment (Phase 3)
---

# Skill: Production Checklist (Launch Readiness)

## Description
Expert-level pre-flight checklist for shipping production changes safely. Ensures reliability, security, observability, and rollback readiness.

## Before Deploy (P0)
- [ ] Environment variables validated; `.env.example` updated
- [ ] Health checks reflect real dependencies
- [ ] Timeouts set for all outbound calls
- [ ] Error messages are user-safe; logs have details
- [ ] Auth & RBAC verified for protected routes
- [ ] Rate limits / abuse controls on sensitive endpoints

## Deploy
- [ ] Prefer staged rollout (feature flags/canary) when risky
- [ ] Monitor p95 latency + error rate during rollout

## After Deploy (P0)
- [ ] Run smoke tests (critical user journeys)
- [ ] Confirm logs/metrics are flowing
- [ ] Confirm alerts configured and actionable

## Rollback Plan
- [ ] Know “last good deploy” identifier
- [ ] Clear rollback steps documented
- [ ] Data rollback considered (if schema changed)

## Integration
- Works with: `change-management`, `devops-engineer`, `structured-logging`, `security-engineer`