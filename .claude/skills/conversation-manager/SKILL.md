---
name: conversation-manager
description: Manage conversation state in database with message history, user isolation, and efficient querying (project)
---

# Skill: Conversation Manager (Context, Memory, and UX)

## Description
Expert-level skill to manage conversation state across sessions: context windows, summarization, grounding, and UX patterns that keep agents coherent over time.

## When to Use
- Any chat/agent feature with multi-turn interaction
- Adding history persistence or “session continuity”
- Reducing hallucinations via grounding and memory hygiene

## Core Concepts
- **Short-term context**: recent turns and task state
- **Long-term memory**: user preferences, durable facts (with consent)
- **Summaries**: compact representations to fit context limits
- **Grounding**: retrieved citations / tool outputs as sources of truth

## Playbook
1. **Define memory tiers**
   - transient (per request), session, user-profile
2. **Add summarization**
   - summarize when token budget exceeded
3. **Apply grounding**
   - cite sources; prefer retrieved context over prior beliefs
4. **Safety**
   - avoid storing secrets; allow user to clear history

## Output Artifacts
- Conversation schema (session_id, messages, metadata)
- Context assembly function (budgeting + ordering)
- UI affordances: clear chat, show citations, show current chapter

## Integration
- Works with: `chatbot-endpoint`, `user-isolation`, `structured-logging`