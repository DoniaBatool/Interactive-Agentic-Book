# Research Notes: Selection-Based RAG Engine

**Feature**: 051-selection-rag
**Date**: 2025-01-27

## Problem Context

Learners reading chapters often need clarification on specific passages. Currently, they must:
- Navigate away from the content
- Use general AI blocks that search entire chapter
- Lose context of what they were reading

Selection-based RAG solves this by:
- Allowing learners to highlight specific text
- Asking questions about only that selection
- Getting precise, contextual answers

## Industry References

### Text Selection Patterns
- **Medium's Highlight Feature**: Users can highlight text and add notes
- **Google Docs Comments**: Selection-based commenting system
- **Hypothesis Annotation**: Web annotation with selection-based context
- **Pocket Highlights**: Save and annotate selected text

### Contextual Q&A Systems
- **ChatGPT Selection**: Users can select text and ask questions
- **Notion AI**: Selection-based AI assistance
- **Obsidian AI**: Context-aware Q&A based on selected text

### RAG with Limited Context
- **Semantic Search on Subset**: Similarity search within selected text
- **Context Window Management**: Limiting context to relevant selection
- **Precision over Recall**: Focused answers vs. broad search

## Observations

### Current System Capabilities

**Existing RAG Pipeline** (from Feature 045):
- Full chapter embedding and search
- Context assembly from multiple chunks
- LLM integration ready

**Selection RAG Requirements**:
- Similar pipeline but limited to selected text
- No need to search entire chapter
- Faster, more focused responses

### Design Considerations

**Selection Text Processing**:
- Clean whitespace and formatting
- Handle special characters
- Normalize text for embedding

**Context Assembly**:
- Use selected text as primary context
- Optionally retrieve related chunks from chapter
- Balance between selection-only vs. selection+chapter context

**User Experience**:
- Minimal UI to avoid distraction
- Quick response time (future)
- Clear indication of what context is used

## Best Practices

### Selection Capture
- Minimum character threshold (e.g., 10 chars) to avoid noise
- Handle multi-line selections
- Preserve formatting context

### Context Management
- Limit context to selected text for precision
- Optionally include surrounding context
- Clear boundaries of what's included

### Error Handling
- Handle empty selections
- Handle very long selections
- Handle invalid chapter IDs
- Graceful degradation

## Implementation Considerations

### Pipeline Design
1. **Clean Selection**: Normalize selected text
2. **Embed Selection**: Generate embedding (future)
3. **Search Within Selection**: Find relevant parts (future)
4. **Build Context**: Assemble context from selection
5. **Call LLM**: Generate answer (future)

### Integration Points
- Frontend: Selection capture and UI
- API: Request/response handling
- Pipeline: Text processing and context building
- Runtime: Orchestration
- Subagent: Question answering logic

### Future Enhancements
- Real embedding generation
- Real similarity search within selection
- Real LLM calls
- Multi-selection support
- Selection history
- Selection sharing

## Technical Notes

### Selection Text Limits
- Minimum: 10 characters (to avoid accidental selections)
- Maximum: 10000 characters (to prevent abuse)
- Optimal: 100-1000 characters for best results

### Performance Considerations
- Selection-based RAG should be faster than full chapter search
- Limited context means faster LLM responses
- No need to search entire chapter vector store

### Security Considerations
- Validate selected text length
- Sanitize user input
- Rate limiting (future)
- Content filtering (future)

