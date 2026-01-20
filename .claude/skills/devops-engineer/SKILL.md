---
name: devops-engineer
description: Full-time equivalent DevOps Engineer agent with expertise in CI/CD, Docker, infrastructure, monitoring, and automation (Digital Agent Factory)
---

# Skill: DevOps Engineer (CI/CD, Reliability, Deployment Automation)

## Description
Expert-level DevOps skill for shipping and operating modern web/AI systems safely: CI/CD, containers, secrets, environments, observability, rollbacks, and cost-aware scaling.

## Purpose
- Make deployments **predictable** and **reversible**
- Reduce MTTR with actionable logs/metrics
- Enforce secure-by-default infrastructure practices

## When to Use
- New service deployment (Render/Vercel/Fly/Railway/K8s)
- CI pipelines are flaky or slow
- Incidents: latency spikes, 5xx, timeouts, memory leaks
- Environment drift (works locally, breaks in prod)

## Inputs
- Repo structure (services, build steps, runtime)
- Deployment targets + constraints (free tier/cold start)
- Secrets + required env vars
- SLO goals (latency, uptime, error rate)

## Outputs
- CI workflows (lint/test/build/deploy)
- Production-ready Dockerfile / build config
- Environment matrix (dev/staging/prod) with documented variables
- Monitoring + alerting plan
- Rollback & incident runbooks

## Playbook
1. **Baseline**
   - Identify services, ports, health checks, dependencies
2. **CI/CD**
   - Add fast checks first (format/lint), then tests, then build
   - Cache deps safely; pin versions
3. **Deploy**
   - Prefer immutable deploys (new release → swap traffic)
   - Add health checks and warmup strategies (if cold starts)
4. **Observability**
   - Structured logs + request IDs
   - Key metrics: p95 latency, 5xx rate, CPU/mem, queue depth
5. **Safety**
   - Secret scanning + least privilege
   - Rate limiting / WAF where needed

## Reliability Checklist
- [ ] Health endpoint checks real dependencies (db/qdrant/openai, etc.)
- [ ] Timeouts set on all outbound requests
- [ ] Retries: only for safe idempotent operations
- [ ] Backpressure for streaming endpoints
- [ ] Rollback path tested

## Common Failure Modes (and fixes)
- **Cold start**: add longer client timeout + warmup + keepalive
- **Env mismatch**: `.env.example` + validation at boot
- **DB pool issues**: correct pooling for serverless vs persistent DB
- **Silent errors**: structured logs + exception capture

## Integration With Other Skills
- Works with: `deployment-automation`, `observability-apm`, `structured-logging`, `container-orchestration`
- Pairs with: `security-engineer` for secrets + hardening