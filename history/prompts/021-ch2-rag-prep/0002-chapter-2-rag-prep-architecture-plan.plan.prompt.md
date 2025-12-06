---
id: 0002
title: Chapter 2 RAG Preparation Architecture Plan
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 021-ch2-rag-prep
branch: 021-ch2-rag-prep
user: Leo
command: /sp.plan
labels: ["chapter-2", "rag", "chunking", "embedding-prep", "architecture", "plan"]
links:
  spec: specs/021-ch2-rag-prep/spec.md
  plan: specs/021-ch2-rag-prep/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/021-ch2-rag-prep/plan.md
tests:
  - Plan completeness validation
  - Plan actionability validation
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (629-672)

Feature details:
- feature-id: 021-ch2-rag-prep
- title: "Chapter 2 — RAG Chunking, Embedding Prep & Knowledge Source Scaffolding"
- goal: Produce the architecture plan for chunking, embedding prep, and chapter-level RAG scaffolding for Chapter 2

Requirements:
1. MDX Layer: Identify ~6-8 semantic sections, place chunk markers before each major idea block, validate placeholder alignment
2. Chunking Rules: Chunk size 120-220 words, group by semantic topic, avoid breaking glossary, link diagram explanations
3. Backend Chunk Module: Create/update chapter_2_chunks.py with get_chapter_2_chunks() function
4. RAG Pipeline Integration: Append CH2 collection name, add TODO for registering embeddings, add TODO for local retrieval context builder
5. Contracts & Validation: rag-prep-schema.md already exists, include regex rules, specify embedding boundary rules, document RAG ingestion steps

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 2 RAG preparation:

**Created Files:**
1. `specs/021-ch2-rag-prep/plan.md` - Complete architecture plan with:
   - Summary (RAG preparation scaffolding for Chapter 2)
   - Technical context (dependencies, constraints, scale/scope)
   - High-level architecture overview (architecture flow, component responsibilities, data flow)
   - MDX Layer (semantic section identification, chunk marker placement strategy, placeholder alignment validation)
   - Chunking Rules (chunk size guidelines, semantic grouping strategy, glossary handling, diagram explanation linking)
   - Backend Chunk Module (chunking blueprint file structure, enhanced TODO comments, function signature)
   - RAG Pipeline Integration (collection name registration, embedding batch preparation, local retrieval context builder)
   - Contracts & Validation (RAG prep schema contract, regex rules, embedding boundary rules, RAG ingestion steps)
   - Integration points (Feature 005, 012, 014, 020)
   - Acceptance checks (5 validation categories)
   - Risk analysis (3 risks with mitigations)
   - Summary

**Key Plan Details:**
- MDX Layer: 7 chunk markers (one per section), placed before content placeholders
- Chunking Rules: 120-220 words per chunk, semantic grouping, glossary handling, diagram linking
- Backend Chunk Module: Enhanced `chapter_2_chunks.py` with comprehensive TODO comments
- RAG Pipeline Integration: TODO hooks for collection registration, embedding batch, search function
- Contracts: Existing `rag-prep-schema.md` with regex rules, embedding boundaries, RAG ingestion steps

**Chunk Marker Strategy:**
- Format: `<!-- CHUNK: x -->` (numbered format)
- Regex: `<!-- CHUNK: [0-9]+ -->`
- Placement: Before content placeholders in each section
- Count: 7 markers (one per section)
- Preservation: Existing diagram and AI-block markers preserved

**Chunking Strategy:**
- Chunk size: 120-220 words (target), 50-300 words (range)
- Semantic grouping: Group by topic, not paragraph count
- Glossary handling: Group as single chunks, don't break entries
- Diagram linking: Link explanations with adjacent text

**Pattern Consistency:**
- Follows Feature 012 (Chapter 2 RAG) and Feature 018 (Chapter 3 Plan) patterns
- Same scaffolding structure and format
- Adapted for Chapter 2 content (ROS 2)
- Includes chunk marker contract and embedding boundaries

## Outcome

- ✅ Impact: Complete architecture plan ready for task generation. All extension points defined (MDX chunk markers, chunking blueprint, RAG pipeline hooks, contracts). MDX layer clearly designed (7 sections, chunk marker placement, placeholder validation). Chunking rules comprehensive (size guidelines, semantic grouping, glossary handling, diagram linking). Backend chunk module detailed (enhanced TODO comments, function signature). RAG pipeline integration complete (collection registration, embedding batch, search function). Contracts validated (regex rules, embedding boundaries, RAG ingestion steps). Integration points documented. Acceptance checks defined. Plan is actionable and ready for direct conversion into tasks.
- 🧪 Tests: Plan completeness validation - PASS, Plan actionability validation - PASS
- 📁 Files: 1 plan file created (plan.md with comprehensive architecture plan)
- 🔁 Next prompts: `/sp.tasks` to create implementation tasks
- 🧠 Reflection: Plan follows established patterns for maintainability. Clear separation between MDX layer, chunking rules, backend module, and RAG integration ensures comprehensive coverage. Chunk marker format (numbered) is simpler than START/END pairs. Chunk size guidelines (120-220 words) balance context and precision. All TODO placeholders are descriptive and actionable. Note: This is a scaffolding extension - no actual chunking, embedding, or RAG logic implementation should be done, only scaffolding with TODO placeholders.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning phase completed successfully
- Graders run and results (PASS/FAIL): Plan completeness - PASS, Plan actionability - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to create implementation tasks
