# Skill: Docusaurus RAG Chatbot Builder

## Description
Expert-level skill for building a complete production-ready RAG (Retrieval-Augmented Generation) chatbot system for Docusaurus-based books and documentation. This skill scaffolds a full-stack solution with FastAPI backend, Neon Serverless Postgres, Qdrant vector store, OpenAI Agents SDK, and React frontend components.

## Purpose
Automate the creation of an intelligent AI chatbot that can:
- Answer questions about book/documentation content
- Use text selection for context-aware responses
- Maintain conversation history across sessions
- Stream responses in real-time
- Provide source citations with relevance scores
- Scale to production workloads

## When to Use
- Building AI-powered chatbot for technical books or documentation
- Implementing RAG system with conversation history
- Creating text-selection-based Q&A features
- Deploying chatbot for Docusaurus-based textbooks
- Hackathon projects requiring full-stack AI chatbot (like Physical AI & Humanoid Robotics textbook)

## Key Features

### Backend (FastAPI)
- ✅ Async FastAPI with modern Python patterns
- ✅ Neon Serverless Postgres for data persistence
- ✅ Qdrant Cloud integration for vector search
- ✅ OpenAI Agents SDK for conversational AI
- ✅ Server-Sent Events (SSE) for streaming
- ✅ Comprehensive error handling and logging
- ✅ Health checks for all services
- ✅ Pydantic validation throughout

### RAG Implementation
- ✅ Document chunking with configurable size/overlap
- ✅ OpenAI text-embedding-3-large (3072 dimensions)
- ✅ Semantic search with similarity thresholds
- ✅ Context injection into prompts
- ✅ Source citation with relevance scores
- ✅ Chapter-specific filtering
- ✅ Text selection-based retrieval

### Frontend (React/TypeScript)
- ✅ Beautiful floating chat widget
- ✅ Smooth animations and transitions
- ✅ Real-time streaming responses
- ✅ Source citations with expandable details
- ✅ Text selection detection
- ✅ Conversation history UI
- ✅ Mobile responsive design
- ✅ Easy Docusaurus integration

### Database Schema
- ✅ Conversations table (session management)
- ✅ Messages table (chat history)
- ✅ Documents table (ingested content)
- ✅ UUID primary keys
- ✅ Proper indexes for performance
- ✅ Metadata JSON fields for flexibility

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Docusaurus Frontend                   │
│  ┌──────────────────────────────────────────────────┐   │
│  │           ChatWidget Component (React)            │   │
│  │  • Text Selection Detection                       │   │
│  │  • Streaming Message Display                      │   │
│  │  • Source Citations                               │   │
│  └────────────────────┬─────────────────────────────┘   │
└────────────────────────┼─────────────────────────────────┘
                         │
                         │ HTTP/SSE
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   FastAPI Backend                        │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Chat API  │  Documents API  │  Health API       │   │
│  └──────┬──────────────┬─────────────────┬──────────┘   │
│         │              │                 │              │
│         ▼              ▼                 ▼              │
│  ┌──────────────┐ ┌──────────┐   ┌──────────┐         │
│  │ Agent Service│ │   RAG    │   │ Embedding│         │
│  │  (OpenAI)    │ │ Service  │   │ Service  │         │
│  └──────────────┘ └──────────┘   └──────────┘         │
└─────────┬──────────────┬─────────────────┬─────────────┘
          │              │                 │
          ▼              ▼                 ▼
┌─────────────┐  ┌──────────────┐  ┌──────────────┐
│    Neon     │  │   Qdrant     │  │   OpenAI     │
│  Postgres   │  │ Vector Store │  │     API      │
│ (Serverless)│  │  (Cloud)     │  │              │
└─────────────┘  └──────────────┘  └──────────────┘
```

## Usage

### Basic Usage
```bash
/sp.docusaurus-rag-chatbot
```

### With Parameters
```bash
/sp.docusaurus-rag-chatbot "Physical AI Textbook" vercel
```

### Arguments
- `book_title` (optional): Title of the book/documentation (default: "Interactive Book")
- `deployment_target` (optional): Deployment target - local/vercel/docker (default: "local")

## What Gets Created

### Backend Structure
```
backend/
├── app/
│   ├── main.py                      # FastAPI app with CORS, lifespan
│   ├── config.py                    # Pydantic settings
│   ├── models/
│   │   ├── conversation.py          # SQLAlchemy models
│   │   └── schemas.py               # Pydantic schemas
│   ├── services/
│   │   ├── rag_service.py           # RAG retrieval logic
│   │   ├── embedding_service.py     # OpenAI embeddings
│   │   ├── agent_service.py         # OpenAI Agents SDK
│   │   └── vector_store.py          # Qdrant operations
│   ├── api/
│   │   ├── chat.py                  # Chat endpoints
│   │   ├── documents.py             # Ingestion endpoints
│   │   └── health.py                # Health checks
│   └── database/
│       └── connection.py            # Neon Postgres setup
├── scripts/
│   └── ingest_documents.py          # Document ingestion script
├── tests/
│   ├── test_rag_service.py
│   └── test_chat_endpoint.py
├── requirements.txt
├── .env.example
└── README.md
```

### Frontend Structure
```
frontend/
└── src/
    └── components/
        ├── ChatWidget.tsx           # Main chat component
        ├── ChatMessage.tsx          # Message component
        ├── ChatInput.tsx            # Input component
        └── styles/
            └── chat.css             # Beautiful gradients & animations
```

### Documentation
```
INTEGRATION_GUIDE.md                 # Step-by-step Docusaurus setup
README.md                            # Complete setup instructions
```

## API Endpoints

### Chat Endpoints
- `POST /api/v1/chat/message` - Send message, get response (non-streaming)
- `POST /api/v1/chat/stream` - Send message, get streaming response (SSE)
- `GET /api/v1/chat/history/{session_id}` - Get conversation history
- `DELETE /api/v1/chat/history/{session_id}` - Clear conversation

### Document Endpoints
- `POST /api/v1/documents/ingest` - Ingest document chapter
- `GET /api/v1/documents/list` - List all ingested documents

### Health Endpoint
- `GET /api/v1/health` - Check database, vector store, and OpenAI status

## Configuration

### Environment Variables (.env)
```env
# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-large

# Neon Postgres
DATABASE_URL=postgresql://user:password@host/dbname

# Qdrant
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-api-key

# RAG Settings
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_RESULTS=5
SIMILARITY_THRESHOLD=0.7
```

## Setup Workflow

1. **Run the skill** to scaffold the complete codebase
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Configure .env** with your API keys
4. **Create database tables**: SQLAlchemy auto-creates on startup
5. **Ingest documents**: `python scripts/ingest_documents.py ../docs`
6. **Start backend**: `uvicorn app.main:app --reload`
7. **Integrate frontend** into Docusaurus (see INTEGRATION_GUIDE.md)
8. **Test the chatbot** at http://localhost:3000

## Docusaurus Integration

### Step 1: Copy Components
```bash
cp -r frontend/src/components src/components/
```

### Step 2: Create Root Theme
Create `src/theme/Root.js`:
```javascript
import React from 'react';
import { ChatWidget } from '@site/src/components/ChatWidget';

export default function Root({children}) {
  return (
    <>
      {children}
      <ChatWidget apiUrl="http://localhost:8000/api/v1" />
    </>
  );
}
```

### Step 3: Configure
Add to `docusaurus.config.js`:
```javascript
customFields: {
  apiUrl: process.env.API_URL || 'http://localhost:8000/api/v1',
}
```

## Unique Features

### 1. Text Selection Context
- User selects text from the book
- Chatbot automatically uses it as context
- Provides focused, relevant answers
- Shows "Selected text will be used" indicator

### 2. Streaming Responses
- Real-time token-by-token display
- Better user experience for long answers
- Uses Server-Sent Events (SSE)
- Graceful error handling

### 3. Source Citations
- Every answer includes sources
- Chapter title and relevance score
- Expandable source snippets
- Helps users verify information

### 4. Chapter Filtering
- Filter RAG search by specific chapter
- Useful for chapter-specific questions
- Improves retrieval accuracy

## Production Deployment

### Backend Options
1. **Render**: Auto-deploy from GitHub, set env vars
2. **Railway**: One-click deploy, automatic scaling
3. **Docker**: Build container, deploy anywhere
4. **Vercel Serverless**: Use API routes (requires adaptation)

### Frontend (Docusaurus)
1. **Vercel**: Best for Next.js/React
2. **Netlify**: Great for static sites
3. **GitHub Pages**: Free hosting
4. **Cloudflare Pages**: Global CDN

### Database & Storage
- **Neon Postgres**: Serverless, auto-scaling
- **Qdrant Cloud**: Free tier available, 1GB storage
- **OpenAI API**: Pay per token

## Performance Considerations

### Optimization Tips
1. **Chunking**: Balance size (1000) vs overlap (200)
2. **Embedding Dimensions**: 3072 for best quality, 1536 for cost savings
3. **Top-K Results**: 5 is sweet spot for context vs token usage
4. **Similarity Threshold**: 0.7 filters low-quality matches
5. **Database Pooling**: Neon handles this automatically
6. **Caching**: Can add Redis for frequently asked questions

### Scalability
- **Concurrent Users**: FastAPI async handles 100s of connections
- **Vector Search**: Qdrant is optimized for millions of vectors
- **Database**: Neon serverless auto-scales
- **Rate Limits**: OpenAI API has per-minute limits

## Testing

### Run Tests
```bash
pytest tests/ -v
```

### Test Coverage
- RAG service retrieval
- Embedding generation
- Chat endpoint (streaming & non-streaming)
- Health checks
- Database operations

## Troubleshooting

### Common Issues

**1. Qdrant Connection Error**
- Check QDRANT_URL and QDRANT_API_KEY
- Verify collection exists
- Check firewall/network settings

**2. OpenAI Rate Limits**
- Implement exponential backoff
- Use lower-tier model for testing
- Add rate limiting middleware

**3. Database Connection Timeout**
- Verify DATABASE_URL format
- Check Neon dashboard for status
- Increase pool timeout settings

**4. Embedding Dimension Mismatch**
- Ensure consistent EMBEDDING_DIMENSIONS (3072)
- Re-create Qdrant collection if changed
- Re-ingest documents

## Bonus Features (For Hackathon)

This skill provides the **base 100 points**. To earn bonus points:

### +50 Points: Authentication (Better Auth)
- Integrate better-auth.com
- Add signup/signin at first chat
- Collect user background (software/hardware experience)
- Store in Conversations.metadata

### +50 Points: Content Personalization
- Add "Personalize Content" button per chapter
- Use user background to adjust complexity
- Simplify for beginners, add depth for experts
- Store preference in user profile

### +50 Points: Urdu Translation
- Add "Translate to Urdu" button per chapter
- Use OpenAI translation or Google Translate API
- Cache translations for performance
- Support both languages in chatbot

## Success Criteria

- [ ] Backend runs without errors
- [ ] All API endpoints respond correctly
- [ ] Neon Postgres connection works
- [ ] Qdrant vector search returns results
- [ ] OpenAI chat completion succeeds
- [ ] Document ingestion creates chunks
- [ ] Frontend chat widget renders
- [ ] Streaming responses work
- [ ] Text selection feature functional
- [ ] Conversation history persists
- [ ] Source citations display
- [ ] Health checks pass
- [ ] Tests pass
- [ ] Docusaurus integration complete

## Cost Estimates

### Development (per month)
- **Neon Postgres**: Free tier (3GB storage)
- **Qdrant Cloud**: Free tier (1GB, 100k vectors)
- **OpenAI API**: ~$10-30 (depends on usage)
- **Total**: ~$10-30/month

### Production (per month, 1000 users)
- **Neon Postgres**: ~$20 (Pro tier)
- **Qdrant Cloud**: ~$25 (1M vectors)
- **OpenAI API**: ~$100-500 (depends on chat volume)
- **Hosting**: ~$20 (Render/Railway)
- **Total**: ~$165-565/month

## Integration with Other Skills

### Works Well With
- `/sp.ai-agent-setup` - Enhanced agent configuration
- `/sp.chatbot-endpoint` - Alternative endpoint patterns
- `/backend-developer` - Backend optimization
- `/frontend-developer` - UI/UX improvements
- `/deployment-automation` - CI/CD setup

### Extends
- Base chatbot functionality → RAG-powered responses
- Simple Q&A → Context-aware conversations
- Static documentation → Interactive learning

## Example Usage Flow

### For Hackathon Project
```bash
# 1. Create RAG chatbot
/sp.docusaurus-rag-chatbot "Physical AI & Humanoid Robotics"

# 2. Configure environment
cd backend
cp .env.example .env
# Edit .env with API keys

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ingest book content
python scripts/ingest_documents.py ../docs

# 5. Start backend
uvicorn app.main:app --reload

# 6. In another terminal, start Docusaurus
cd ..
npm run start

# 7. Test at http://localhost:3000
# Click chat button, ask questions, select text!

# 8. Deploy
# Backend → Render/Railway
# Frontend → Vercel/Netlify
```

## Learning Outcomes

By using this skill, you will understand:
- RAG architecture and implementation
- Vector embeddings and semantic search
- Conversation state management
- Streaming responses with SSE
- FastAPI async patterns
- SQLAlchemy with Neon Postgres
- Qdrant vector database operations
- OpenAI Agents SDK integration
- React component design
- Docusaurus theme customization
- Production deployment strategies

## Resources

### Documentation
- [FastAPI](https://fastapi.tiangolo.com/)
- [Neon Postgres](https://neon.tech/docs)
- [Qdrant](https://qdrant.tech/documentation/)
- [OpenAI Agents SDK](https://platform.openai.com/docs/assistants)
- [Docusaurus](https://docusaurus.io/docs)

### Tutorials
- [RAG Explained](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)
- [Vector Databases Guide](https://www.pinecone.io/learn/vector-database/)
- [Streaming with FastAPI](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse)

## Version History

- **v1.0.0** (2025-01-20): Initial release
  - Complete RAG chatbot system
  - FastAPI + Neon + Qdrant + OpenAI
  - React frontend components
  - Text selection feature
  - Streaming responses
  - Comprehensive documentation

## License
MIT License - Free to use for hackathons and commercial projects

## Support
For issues or questions:
1. Check INTEGRATION_GUIDE.md
2. Review troubleshooting section
3. Test with /api/v1/health endpoint
4. Check backend logs for errors

---

**Built with ❤️ for the Physical AI & Humanoid Robotics Hackathon**

This skill represents expert-level full-stack AI engineering, combining modern backend architecture, vector search, conversational AI, and beautiful UX into a production-ready system.
