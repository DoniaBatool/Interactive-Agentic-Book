# Implementation Plan: Real-Time AI Interaction Layer — Streaming

**Branch**: `050-live-ai-interaction` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements a real-time AI interaction framework with streaming support for all AI Blocks. It includes backend streaming infrastructure, API endpoints, frontend streaming client, React hooks, and component integration. **All implementations are scaffolding only**—mocked streaming, no real LLM streaming logic.

**Primary Deliverable**: Streaming infrastructure with backend APIs, frontend client, hooks, and component integration
**Validation**: Streaming endpoints return mocked chunks, frontend hooks work, components compile

---

## 1. Why Streaming Mode is Essential

### 1.1 User Experience Benefits

- **Progressive Display**: Users see content as it's generated, not after completion
- **Perceived Performance**: Faster perceived response time
- **Engagement**: Users stay engaged while waiting for complete responses
- **Feedback**: Users know the system is working

### 1.2 Technical Benefits

- **Lower Latency**: First token appears quickly
- **Better UX**: No blank screens during generation
- **Scalability**: Can handle long responses efficiently

---

## 2. Architecture Choice: SSE vs WebSockets

### 2.1 Server-Sent Events (SSE) - Recommended

**Advantages**:
- Simpler implementation
- Built-in reconnection
- HTTP-based (easier to debug)
- Unidirectional (server → client)

**Disadvantages**:
- Unidirectional only
- Limited browser support (but good enough)

### 2.2 WebSockets - Alternative

**Advantages**:
- Bidirectional communication
- Lower overhead
- Real-time updates

**Disadvantages**:
- More complex implementation
- Requires connection management
- More difficult to debug

### 2.3 Decision

**Initial Choice**: SSE (simpler, sufficient for streaming)
**Future**: Support both (placeholder for WebSocket option)

---

## 3. Streaming Manager Responsibilities

**Location**: `backend/app/ai/streaming/stream_manager.py`

**Responsibilities**:
- Manage streaming connections
- Generate streaming chunks (mocked for now)
- Handle SSE/WebSocket protocol
- Manage connection lifecycle
- Handle errors and cancellations

---

## 4. Required FastAPI Changes

### 4.1 Streaming Endpoint

**Location**: `backend/app/api/streaming.py`

**Endpoint**: `GET /api/stream/ai-block/{block_type}`

**Response**: `text/event-stream` with SSE format

**Implementation** (Placeholder):
- Return mocked streaming chunks
- Format as SSE events
- Send completion event

---

## 5. Frontend Streaming Flow

### 5.1 Component → Hook → Client Flow

```
AI Block Component
  ↓
useAIBlockStreaming(blockType)
  ↓
streamClient.connect(endpoint)
  ↓
EventSource (SSE) or WebSocket
  ↓
Event Listener (chunk, error, complete)
  ↓
Update Component State
  ↓
UI Updates in Real-Time
```

### 5.2 Hook Structure

**useAIStreaming()**:
- Manages streaming connection
- Provides chunks, error, complete states
- Handles reconnection

**useAIBlockStreaming(blockType)**:
- Block-specific streaming hook
- Calls appropriate endpoint
- Formats response for block type

---

## 6. Compatibility with Existing Runtime Engine

### 6.1 Integration Points

**Location**: `backend/app/ai/runtime/engine.py`

**Integration** (Placeholder):
- Add streaming mode check
- If streaming enabled, yield tokens instead of returning complete response
- TODO: Implement real token streaming from LLM providers

### 6.2 Backward Compatibility

- Non-streaming mode still works (default)
- Streaming is opt-in via configuration
- Existing endpoints unchanged

---

## 7. Token-by-Token Output Planning

### 7.1 Token Generation (Future)

**Process**:
1. LLM provider generates tokens
2. Stream manager receives tokens
3. Format as SSE chunks
4. Send to frontend
5. Frontend displays tokens progressively

### 7.2 Current (Placeholder)

- Mock token generation
- Simulate streaming with delays
- Return predefined chunks

---

## 8. How Future LLM Providers Enable Real Streaming

### 8.1 OpenAI Streaming

**Future Implementation**:
- Use `stream=True` in OpenAI API call
- Yield tokens from response stream
- Format as SSE chunks

### 8.2 Gemini Streaming

**Future Implementation**:
- Use streaming API in Gemini
- Yield tokens from response stream
- Format as SSE chunks

---

## 9. Testing Strategy

### 9.1 Mock Streaming Provider

- Mock token generation
- Simulate streaming delays
- Test chunk formatting

### 9.2 Frontend Fake Stream Simulator

- Simulate SSE events
- Test hook behavior
- Test component updates

---

## 10. File Structure

```
backend/app/
├── ai/
│   ├── streaming/
│   │   ├── __init__.py
│   │   └── stream_manager.py
│   └── runtime/
│       └── engine.py (updated: streaming hook)
└── api/
    └── streaming.py

frontend/src/
└── ai/
    ├── streamClient.ts
    └── streamHooks.ts

specs/050-live-ai-interaction/
├── contracts/
│   └── stream-schema.yaml
└── README.md
```

---

## 11. Risk Analysis

### 11.1 Top Risks

**Risk 1: Connection Management**
- **Blast Radius**: All streaming requests
- **Mitigation**: Proper connection lifecycle management, reconnection logic

**Risk 2: Performance Impact**
- **Blast Radius**: All AI block requests
- **Mitigation**: Efficient streaming, async processing

**Risk 3: Browser Compatibility**
- **Blast Radius**: Frontend streaming
- **Mitigation**: Use well-supported SSE, fallback to polling

---

## 12. Evaluation and Validation

### 12.1 Definition of Done

- [ ] Streaming backend infrastructure created
- [ ] Streaming API endpoints created (mocked)
- [ ] Frontend streaming client created
- [ ] Frontend streaming hooks created
- [ ] AI Block components updated
- [ ] Configuration variables added
- [ ] Contracts created
- [ ] Project starts without errors
- [ ] Streaming endpoints return mocked chunks
- [ ] Frontend components compile

### 12.2 Validation Criteria

- **Backend**: Streaming endpoints work (mocked)
- **Frontend**: Hooks work, components compile
- **Integration**: Components can consume streaming (mocked)
- **Configuration**: Settings work correctly

