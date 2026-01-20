---
name: connection-pooling
description: Configure database connection pooling for optimal performance and resource management (Phase 2 pattern)
---

# Skill: Connection Pooling (DB + HTTP + Workers)

## Description
Expert-level skill to prevent production failures from **connection exhaustion** and poor pooling defaults. Covers Postgres, Redis, HTTP clients, and worker concurrency.

## When to Use
- “Too many connections” / random timeouts
- High concurrency (SSE, websockets, batch jobs)
- Serverless DBs (Neon/Supabase) + pooling quirks

## Core Principles
- Pool size must match infra limits and concurrency
- Serverless DBs often need **small pools** or **NullPool**
- Always set **timeouts** (connect/read/write)
- Retries only for **safe idempotent** operations

## Playbook
1. **Map connections**
   - DB, HTTP, vector DB, queues, background workers
2. **Pick strategy**
   - Serverless DB: NullPool or very small pool
   - Persistent DB: tuned pool_size/max_overflow/recycle
3. **Set budgets**
   - p95 latency target + max concurrent requests
4. **Load test**
   - Validate stability under realistic concurrency

## Output Artifacts
- Documented pool settings per environment
- Metrics to watch: active connections, pool wait time, timeouts

## Integration
- Works with: `devops-engineer`, `observability-apm`, `transaction-management`