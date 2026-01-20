# Docusaurus RAG Chatbot - Quick Start Guide

## Overview
Expert-level skill that creates a complete production-ready RAG chatbot for your Docusaurus book in minutes.

## Quick Start

### 1. Run the Skill
```bash
/sp.docusaurus-rag-chatbot "Your Book Title"
```

This creates:
- ✅ Complete FastAPI backend with RAG
- ✅ Neon Postgres database setup
- ✅ Qdrant vector store integration
- ✅ OpenAI Agents SDK configuration
- ✅ React chat widget (beautiful UI)
- ✅ Document ingestion scripts
- ✅ Tests and documentation

### 2. Setup Backend (5 minutes)

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env - add your API keys:
# - OPENAI_API_KEY
# - DATABASE_URL (Neon Postgres)
# - QDRANT_URL and QDRANT_API_KEY

# Start server
uvicorn app.main:app --reload --port 8000
```

### 3. Ingest Your Book Content (2 minutes)

```bash
# From backend directory
python scripts/ingest_documents.py ../docs --api-url http://localhost:8000
```

This automatically:
- Reads all markdown files from your Docusaurus docs
- Chunks content into optimal sizes
- Generates embeddings
- Stores in Qdrant vector database
- Saves metadata in Postgres

### 4. Add to Docusaurus (3 minutes)

```bash
# Copy chat components
cp -r frontend/src/components src/components/

# Create src/theme/Root.js
```

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

### 5. Test!

```bash
npm run start
```

Visit http://localhost:3000 and click the chat button 💬

## Key Features You Get

### 🎯 Smart RAG System
- Semantic search across all book content
- Context-aware responses
- Source citations with relevance scores
- Chapter-specific filtering

### ✨ Text Selection Q&A
- Select any text in the book
- Ask questions about it
- AI uses selection as focused context
- **Unique feature that sets your chatbot apart!**

### 💬 Beautiful Chat UI
- Floating chat widget
- Smooth animations
- Real-time streaming responses
- Typing indicators
- Mobile responsive
- Purple gradient theme

### 📚 Conversation History
- Persists across page reloads
- Session-based tracking
- Can review past conversations
- Stored in Neon Postgres

### 🔄 Streaming Responses
- Token-by-token display
- Better UX for long answers
- Uses Server-Sent Events (SSE)
- Feels more natural and responsive

## API Endpoints Created

### Chat
- `POST /api/v1/chat/message` - Get AI response
- `POST /api/v1/chat/stream` - Stream AI response
- `GET /api/v1/chat/history/{session_id}` - View history
- `DELETE /api/v1/chat/history/{session_id}` - Clear history

### Documents
- `POST /api/v1/documents/ingest` - Add document
- `GET /api/v1/documents/list` - List all documents

### Health
- `GET /api/v1/health` - Check system status

## Tech Stack

### Backend
- **FastAPI**: Modern async Python framework
- **Neon Postgres**: Serverless database
- **Qdrant**: Vector search engine
- **OpenAI**: GPT-4o + text-embedding-3-large
- **SQLAlchemy**: ORM with async support
- **Pydantic**: Data validation

### Frontend
- **React**: UI components
- **TypeScript**: Type-safe code
- **CSS3**: Beautiful animations
- **Docusaurus**: Documentation framework

## For Hackathon (Physical AI Textbook)

### Base Requirements ✅ (100 points)
- ✅ AI/Spec-driven book creation (Docusaurus)
- ✅ RAG chatbot with OpenAI Agents SDK
- ✅ FastAPI backend
- ✅ Neon Serverless Postgres
- ✅ Qdrant Cloud Free Tier
- ✅ Answer questions about book content
- ✅ Text selection-based questions

### Bonus Features (150 extra points possible)

#### +50: Claude Code Subagents
- Use `/sp.docusaurus-rag-chatbot` skill (this one!)
- Create custom agent for content generation
- Demonstrate reusable intelligence

#### +50: Better Auth Integration
- Add signup/signin
- Collect user background (software/hardware)
- Personalize based on experience level

#### +50: Content Personalization
- Add "Personalize" button per chapter
- Adjust complexity for user level
- Use user background from signup

#### +50: Urdu Translation
- Add "Translate" button per chapter
- Real-time translation
- Support bilingual chatbot

## Deployment (Production)

### Backend (Choose One)

**Render** (Recommended)
```bash
# 1. Connect GitHub repo
# 2. Set environment variables
# 3. Deploy!
```

**Railway**
```bash
railway login
railway init
railway up
```

**Docker**
```bash
docker build -t rag-chatbot .
docker run -p 8000:8000 --env-file .env rag-chatbot
```

### Frontend

**Vercel** (Recommended)
```bash
vercel --prod
```

**Netlify**
```bash
netlify deploy --prod
```

**GitHub Pages**
```bash
npm run deploy
```

## Cost Breakdown

### Free Tier (Development)
- Neon Postgres: Free (3GB)
- Qdrant: Free (1GB)
- OpenAI: Pay-as-you-go (~$10/month)
- **Total: ~$10/month**

### Production (1000 users)
- Neon: ~$20/month
- Qdrant: ~$25/month
- OpenAI: ~$100-500/month
- Hosting: ~$20/month
- **Total: ~$165-565/month**

## Troubleshooting

### Qdrant Connection Error
```bash
# Check your .env file
QDRANT_URL=https://your-cluster.qdrant.io  # Must include https://
QDRANT_API_KEY=your-api-key
```

### OpenAI Rate Limit
```python
# In config.py, use lower-tier model for testing
OPENAI_MODEL = "gpt-4o-mini"  # Cheaper for testing
```

### Database Connection Timeout
```bash
# Verify DATABASE_URL format
postgresql://user:password@host.region.neon.tech/dbname?sslmode=require
```

### No Search Results
```python
# Lower similarity threshold in config.py
SIMILARITY_THRESHOLD = 0.5  # Was 0.7
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Test specific component
pytest tests/test_rag_service.py -v

# Test with coverage
pytest --cov=app tests/
```

## Next Steps

1. ✅ Run the skill
2. ✅ Configure .env
3. ✅ Ingest documents
4. ✅ Test locally
5. 🎨 Customize chat UI colors
6. 🚀 Deploy to production
7. 📝 Add bonus features (auth, personalization, translation)
8. 🎥 Record demo video (<90 seconds)
9. 📤 Submit to hackathon

## Advanced Customization

### Change Chat Colors
Edit `frontend/src/components/styles/chat.css`:
```css
/* Change gradient */
background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
```

### Adjust Chunking
Edit `backend/app/config.py`:
```python
CHUNK_SIZE: int = 1500  # Larger chunks = more context
CHUNK_OVERLAP: int = 300  # More overlap = better continuity
TOP_K_RESULTS: int = 7  # More results = more context
```

### Custom System Prompt
Edit `backend/app/services/agent_service.py`:
```python
def _build_system_prompt(self, context: str, book_title: str) -> str:
    return f"""You are an expert tutor for {book_title}.

    Your personality: Friendly, encouraging, patient

    CONTEXT:
    {context}
    """
```

## Support

- 📖 Full documentation: See `SKILL.md`
- 🔧 Integration guide: See `INTEGRATION_GUIDE.md`
- 🐛 Issues: Check backend logs
- 💡 Questions: Review troubleshooting section

## What Makes This Special?

1. **Production-Ready**: Not a prototype, actual production code
2. **Text Selection**: Unique feature for focused Q&A
3. **Streaming**: Better UX with real-time responses
4. **Source Citations**: Builds trust with references
5. **Beautiful UI**: Professional-looking chat widget
6. **Easy Integration**: 10 minutes to add to Docusaurus
7. **Scalable**: Handles 1000s of users
8. **Well-Tested**: Includes test suite
9. **Documented**: Comprehensive guides

## Success Stories

Use this skill to:
- ✅ Build hackathon-winning chatbot in 1 hour
- ✅ Add AI to your documentation site
- ✅ Create interactive learning platform
- ✅ Launch AI-powered SaaS product
- ✅ Learn full-stack AI development

---

**Ready to build? Run: `/sp.docusaurus-rag-chatbot`**

🚀 **Let's make your book interactive!**
