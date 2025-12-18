# Contracts

API: `/chat` (POST)
- Body: { question: string, filters?: {chapter?: string, section?: string}, stream?: boolean }
- Response: { answer: string, citations: [{path, chapter, section?, score?}], stream?: boolean }
- Streaming: chunked text if stream=true.

