---
name: performance-logger
description: Add performance monitoring and execution time logging to backend services with structured JSON output (Phase 3)
---

# Skill: Performance Logger (Metrics + Profiling + Budgeting)

## Description
Expert-level skill for measuring and improving performance with **instrumentation first**: latency metrics, timing spans, profiling, and performance budgets.

## When to Use
- Slow pages or slow API endpoints
- Timeouts (client or server)
- Cost spikes (token usage, vector queries)

## Playbook
1. **Instrument**
   - duration_ms for key operations (retrieval, embeddings, DB)
2. **Measure**
   - p50/p95/p99 latency; error rates; throughput
3. **Profile**
   - find hotspots (N+1 queries, heavy renders)
4. **Optimize**
   - caching, batching, indexes, memoization
5. **Set budgets**
   - enforce target p95 and max payload sizes

## Output Artifacts
- Metrics taxonomy + dashboards notes
- Performance regression tests (when practical)

## Integration
- Works with: `observability-apm`, `connection-pooling`, `devops-engineer`