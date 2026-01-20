---
name: edge-case-tester
description: Comprehensive edge case testing for features to ensure robustness and prevent broken functionality (project)
---

# Skill: Edge Case Tester (Break It Before Users Do)

## Description
Expert-level testing skill focused on **boundary conditions**, “weird inputs”, concurrency, and real-world failure modes that typical unit tests miss.

## When to Use
- User-reported bugs that are hard to reproduce
- Race conditions, timeouts, pagination bugs
- Multi-language/RTL rendering issues

## Playbook
1. **Inventory edge cases**
   - empty/null, huge payloads, invalid unicode, timeouts
2. **Property-based mindset**
   - define invariants (e.g., “never crash”, “never leak data”)
3. **Concurrency tests**
   - parallel requests, retries, aborts, streaming disconnects
4. **Failure injection**
   - simulate 500s, slow upstream, network errors

## Output Artifacts
- Edge-case test plan (bulleted)
- Regression test cases added for each bug
- “Known limits” documented (max sizes, timeouts)

## Integration
- Works with: `qa-engineer`, `observability-apm`, `chatbot-endpoint`