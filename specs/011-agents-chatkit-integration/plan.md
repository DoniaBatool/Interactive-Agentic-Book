# Architecture Plan: Agents/ChatKit Integration – Feature 011

## Overview

Goal: Upgrade the RAG chatbot from simple retrieval-augmented generation to an intelligent agent that uses OpenAI function calling to decide when and how to retrieve textbook context.

## High-Level Design

### Backend Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FastAPI Backend                          │
├─────────────────────────────────────────────────────────────┤
│  /chat/agent endpoint                                        │
│       │                                                      │
│       ▼                                                      │
│  ┌─────────────┐    ┌──────────────────┐                    │
│  │   Agent     │───▶│  OpenAI API      │                    │
│  │   Service   │    │  (Function Call) │                    │
│  └─────────────┘    └──────────────────┘                    │
│       │                     │                                │
│       │ tool_call           │ response                       │
│       ▼                     ▼                                │
│  ┌─────────────┐    ┌──────────────────┐                    │
│  │   RAG       │    │  Final Answer    │                    │
│  │   Service   │───▶│  + Citations     │                    │
│  └─────────────┘    └──────────────────┘                    │
│       │                                                      │
│       ▼                                                      │
│  ┌─────────────┐                                            │
│  │   Qdrant    │                                            │
│  │   Vector DB │                                            │
│  └─────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
```

### Agent Service (`agents.py`)

- **OpenAI Client**: Uses `openai.OpenAI` with function calling enabled.
- **System Prompt**: Describes the agent as a textbook assistant with access to the RAG tool.
- **Tool Definition**: `retrieve_book_context` function schema with parameters:
  - `query`: Search query for the textbook
  - `chapter_filter`: Optional chapter to prioritize
- **Flow**:
  1. Receive user question + optional chapter filter
  2. Send to OpenAI with tool definitions
  3. If tool_call received, execute RAG retrieval
  4. Send tool result back to OpenAI
  5. Return final answer with citations

### Frontend Integration

- **Mode Prop**: `RagChat` component accepts `mode: 'rag' | 'agent'`
- **Endpoint Routing**:
  - `mode="rag"` → POST `/chat`
  - `mode="agent"` → POST `/chat/agent`
- **Response Handling**: Both endpoints return same schema

## Data Flow

```
User Question
     │
     ▼
FloatingChatButton (mode="agent")
     │
     ▼
RagChat Component
     │
     ▼
POST /chat/agent
     │
     ▼
agents.py: generate_agent_answer()
     │
     ├──▶ OpenAI API (with tools)
     │         │
     │         ▼
     │    tool_call: retrieve_book_context?
     │         │
     │    ┌────┴────┐
     │    │  YES    │  NO (direct answer)
     │    ▼         │
     │  rag.py      │
     │  retrieve()  │
     │    │         │
     │    ▼         │
     │  Qdrant      │
     │    │         │
     └────┴─────────┘
              │
              ▼
     Final Answer + Citations
              │
              ▼
     ChatResponse JSON
```

## Error Handling Strategy

- **Tool Execution Failure**: Return graceful error message, log details.
- **No Context Found**: Agent responds with "I couldn't find relevant information in the textbook."
- **OpenAI API Error**: Return error response, maintain conversation state.

## Phased Implementation

1. **Phase 1 – Agent Service**
   - Create `agents.py` with OpenAI function calling
   - Implement `retrieve_book_context` tool
   - Add structured logging

2. **Phase 2 – API Endpoint**
   - Add `/chat/agent` endpoint
   - Wire to agent service
   - Maintain response schema compatibility

3. **Phase 3 – Frontend Integration**
   - Add `mode` prop to `RagChat`
   - Update `FloatingChatButton` default
   - Test both modes

## Dependencies / Config

- **OpenAI API**: `openai>=1.54.0` with function calling support
- **Backend**: Existing RAG service (`rag.py`) for tool execution
- **Environment**: `OPENAI_API_KEY` required

