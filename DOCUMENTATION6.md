/sp.specify
feature-id: 006-diagram-generation-engine
title: "AI Diagram Generation Engine — Chapter Diagrams via AI → SVG → MDX"
type: backend-ai-infra
Generate spec.md FAST in small batches, not all at once

goal:
  Build the placeholder AI-powered diagram generation engine that converts
  conceptual inputs (like robot anatomy, physical-ai-overview) into
  generated diagrams (SVG/PNG/Mermaid). This feature creates the entire
  pipeline structure with TODO placeholders.

requirements:
  # 1 — Diagram Provider Interface
  - Create backend/app/ai/diagrams/base_diagram_provider.py
      - TODO: class BaseDiagramProvider with abstract generate_diagram(payload)
  - Create backend/app/ai/diagrams/openai_diagram_provider.py
      - TODO: scaffold for GPT-4o vision/output diagrams
  - Create backend/app/ai/diagrams/gemini_diagram_provider.py
      - TODO: scaffold for Gemini Flash/Image models

  # 2 — Diagram Pipeline
  - Create backend/app/ai/diagrams/pipeline.py
      - Steps (placeholder only):
          1. Validate diagram type
          2. Build prompt template
          3. Call provider
          4. Receive SVG or textual diagram description
          5. Format output
  
  # 3 — Diagram Templates
  - Create backend/app/ai/diagrams/templates/
      - anatomy_robot.txt
      - physical_ai_overview.txt
      - ai_robotics_stack.txt
      - core_concepts_flow.txt
      - Each file: placeholder explaining expected fields

  # 4 — API Endpoint Scaffold
  - Create backend/app/api/diagram_generation.py
      - POST /api/diagram/generate
      - Input: diagramType, chapterId, concepts[]
      - Output: placeholder JSON { svg: "<svg><!-- TODO --></svg>" }

  # 5 — Integrate Into AI Runtime Engine
  - Update backend/app/ai/runtime/engine.py
      - Add TODO: route diagram block → diagram pipeline

  # 6 — MDX Frontend Integration (scaffold only)
  - Create frontend/src/components/diagrams/DiagramRenderer.tsx
      - Accepts svgString prop
      - Renders placeholder <div> diagram goes here </div>

  # 7 — Env Vars
  - Update backend/app/config/settings.py:
      - DIAGRAM_MODEL
      - DIAGRAM_PROVIDER

  # 8 — Contracts
  - Create specs/006-diagram-generation-engine/contracts/diagram-api.yaml
      - Document the API contract, expected payloads, placeholder response schema

acceptance_criteria:
  - All scaffold modules, templates, and API stubs exist
  - No real AI logic implemented
  - Backend starts without errors
  - DiagramRenderer.tsx compiles
  - diagram-api.yaml created

success_message: |
  Diagram Generation Engine scaffolding successfully created.
  All providers, pipelines, templates, API stubs, and configuration blocks added.



/sp.plan
feature-id: 006-diagram-generation-engine
title: "Diagram Generation Engine — AI → SVG/PNG Diagram Pipeline"
Generate plan.md FAST in small batches, not all at once

Create a detailed architecture plan for implementing the diagram generation engine.
This plan must strictly follow these principles:

- Scaffold only (NO AI logic, NO API calls)
- Match folder structure defined in the spec
- Include implementation sequencing
- Define module responsibilities
- Describe data flow between providers → pipeline → runtime engine
- Describe integration points with RAG + AI Runtime Engine
- Include notes for future GPT/Gemini integration
- Include configuration blocks and env variable usage
- Include quickstart instructions for developers

Break the plan into:

1. System Overview  
2. Folder + Module Structure  
3. Diagram Provider Architecture  
4. Pipeline Architecture  
5. Template System  
6. API Routing & Request Flow  
7. Runtime Engine Integration  
8. Frontend Integration Scaffold  
9. Environment Variables  
10. Contracts Explanation  
11. Future Enhancements  
12. Implementation Sequencing (Phases 0–5)

Output: plan.md



/sp.tasks
feature-id: 006-diagram-generation-engine
title: "Diagram Generation Engine — Task Breakdown"

Generate a complete tasks.md file FAST in small batches, not all at once:

- Checkbox tasks
- Grouped by phases
- Explicit file paths
- No implementation logic (scaffold only)
- Matching the spec + plan EXACTLY
- Atomic tasks (1 file → 1 task)
- Developer-facing clear instructions

PHASES:

Phase 0 — Project Setup  
- Verify folder structure, imports, and settings.

Phase 1 — Providers  
- Create base diagram provider  
- Create OpenAI provider scaffold  
- Create Gemini provider scaffold

Phase 2 — Pipeline  
- Create pipeline module  
- Add placeholder flow steps (validate → prompt → provider → format output)

Phase 3 — Templates  
- Create 4 template files  
- Populate each with placeholder fields + TODO guidelines

Phase 4 — Backend API  
- Create /api/diagram/generate endpoint  
- Add request/response models  
- Add TODO placeholder implementation

Phase 5 — Runtime Engine Integration  
- Update ai/runtime/engine.py to include diagram routing

Phase 6 — Frontend Integration  
- Create DiagramRenderer.tsx  
- Add placeholder UI

Phase 7 — Configuration  
- Update settings.py  
- Update .env.example

Phase 8 — Validation  
- Backend should start without errors  
- Frontend should compile  
- All new modules import correctly

Output: tasks.md




/sp.implement
feature-id: 006-diagram-generation-engine
title: "Diagram Generation Engine — Implementation Phase"
 
Implement ONLY scaffolding for all tasks defined in tasks.md FAST in small batches, not all at once.

Rules:
- NO business logic
- NO real AI calls
- Only file creation, imports, class stubs, TODO markers
- Follow exact folder structure and filenames
- Do not rename or delete existing project files
- Add placeholder functions, classes, datatypes
- Ensure backend runs after scaffolding
- Ensure frontend builds after scaffolding

Implementation priorities:
1. Create all provider modules with base class + TODO comments
2. Create pipeline module with placeholder flow
3. Create template files containing placeholder instructions
4. Build API router for /api/diagram/generate (stub only)
5. Update runtime engine: add diagram handling block route
6. Add DiagramRenderer.tsx as placeholder component
7. Add new env variables to settings.py and .env.example
8. Validate import paths and fix any missing __init__.py files

Success criteria:
- All files created
- All imports resolve
- No runtime/backend/frontend errors
- Scaffold matches spec + plan + tasks exactly
