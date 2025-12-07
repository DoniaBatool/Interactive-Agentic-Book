---
id: 0002
title: Chapter 3 RAG + Embedding Preparation Layer Architecture Plan
stage: plan
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 029-ch3-rag-prep
branch: 003-chapter-1-content
user: Leo
command: /sp.plan
labels: ["chapter-3", "rag", "embeddings", "qdrant", "chunking", "planning", "architecture"]
links:
  spec: specs/029-ch3-rag-prep/spec.md
  plan: specs/029-ch3-rag-prep/plan.md
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/029-ch3-rag-prep/plan.md
tests:
  - Architecture plan completeness validation
  - Constitution check validation
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (646-677)

Feature details:
- feature-id: 029-ch3-rag-prep
- title: "Chapter 3 — RAG + Embedding Preparation Layer"
- goal: Produce a complete RAG architecture plan including:
  1. Chunking Strategy: How chapter 3 text will eventually be segmented, placeholder logic phases (syntactic, semantic, hybrid, RAG-marker-aware)
  2. Embeddings Strategy: Future embedding model choice (OpenAI text-embedding-3-small), batching plan, vector dimensional expectations, safety guidelines
  3. Qdrant Collection Design: Collection name (chapter3), vector schema (placeholder), metadata schema
  4. Retrieval Pipeline Flow: Query embedding, vector search placeholder, context window assembly, interface to runtime engine
  5. MDX RAG Markers: Strategy for adding RAG-CHUNK markers to Chapter 3 MDX
  6. File Creation Diagram: chapter_3_chunks.py, embedding_client.py extensions, qdrant_store scaffolding, ch3_pipeline.py creation, settings.py updates, chapter-3.mdx updates
  7. Risks: No real logic allowed at this stage, MDX marker interference, backend import errors, pattern inconsistency

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 3 RAG + Embedding Preparation Layer:

**Created Files:**
1. `specs/029-ch3-rag-prep/plan.md` - Complete architecture plan with:
   - Summary: RAG foundations for Chapter 3 (chunking, embeddings, Qdrant, pipeline, MDX markers, environment variables)
   - Technical Context: Python 3.11+, FastAPI, no new dependencies, scaffolding only
   - High-Level Architecture Overview: Architecture flow diagram, component responsibilities, data flow
   - Chunking Strategy: Multi-phase placeholder strategy with RAG markers (6 phases: syntactic, semantic, hybrid, heading-aware, RAG-marker-aware, overlapping windows)
   - Embeddings Strategy: OpenAI text-embedding-3-small (1536 dimensions), batching strategy, safety guidelines
   - Qdrant Collection Design: Collection "chapter3", vector schema (1536 dimensions), metadata schema with Physical AI concepts
   - Retrieval Pipeline Flow: Separate file ch3_pipeline.py with 5-step process (retrieve → embed → search → context → response)
   - MDX RAG Markers: Complementary to existing markers, wrap sections with RAG-CHUNK markers
   - Environment Variable Updates: QDRANT_COLLECTION_CH3, EMBEDDING_MODEL_CH3, settings.py fields
   - File Creation Diagram: 7 files to create/update (1 new file: ch3_pipeline.py)
   - Risks: 4 risks identified with mitigation strategies
   - Validation Steps: 5 validation checks (file existence, import resolution, backend startup, MDX build, environment variables)
   - Success Criteria: 10 criteria
   - Next Steps: Ready for /sp.tasks

**Key Architectural Decisions:**
1. **Separate Pipeline File**: Create ch3_pipeline.py for Chapter 3 (modularity, chapter-specific logic, isolation)
2. **RAG-Marker-Aware Chunking**: Respect `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers from MDX (explicit boundaries, complementary to existing markers)
3. **Chapter-Specific Embedding Functions**: Add embed_chapter3_chunks() and normalize_chapter3_embeddings() (chapter-specific logic, consistency with Chapter 2 pattern)
4. **Chapter-Specific Search Function**: Add similarity_search_ch3() (chapter-specific search logic, consistency)
5. **CH3_CHUNKS Constant**: Add placeholder constant CH3_CHUNKS = [] (explicit placeholder, matches Chapter 2 pattern)

**Pattern Consistency:**
- Follows Chapter 2 RAG prep patterns (Feature 012-chapter-2-rag) exactly
- Same placeholder-only approach
- Same structure and naming conventions
- Same validation steps
- Same risk mitigation strategies

**Key Differences from Chapter 2:**
- New file: ch3_pipeline.py (separate pipeline file for Chapter 3)
- New function: normalize_chapter3_embeddings() (optional normalization)
- MDX markers: RAG-CHUNK markers complement existing CHUNK markers
- Collection name: "chapter3" (from QDRANT_COLLECTION_CH3 env var)
- Concepts: Physical AI concepts (perception, sensors, vision, signal processing) instead of ROS 2 concepts

## Outcome

- ✅ Impact: Complete architecture plan ready for task generation. All Chapter 3 RAG preparation architecture decisions covered (chunking, embeddings, Qdrant, pipeline, MDX markers, environment variables). All files planned with placeholder-only approach. Architecture follows Chapter 2 RAG prep patterns for consistency. All validation steps defined. All risks identified with mitigation strategies.
- 🧪 Tests: Architecture plan completeness validation - PASS, Constitution check validation - PASS
- 📁 Files: 1 file created (plan.md)
- 🔁 Next prompts: Ready for /sp.tasks to generate implementation tasks
- 🧠 Reflection: Architecture plan follows established patterns for maintainability. Clear separation between scaffolding and future implementation ensures comprehensive coverage. All architectural decisions documented with rationale. Pattern consistency with Chapter 2 ensures developer familiarity. Note: This is an architecture plan extension - no actual implementation, only architectural decisions and blueprints. All decisions follow Chapter 2 patterns. Ready for task generation phase.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning phase completed successfully
- Graders run and results (PASS/FAIL): Architecture plan completeness - PASS, Constitution check - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Ready for /sp.tasks to generate implementation tasks

