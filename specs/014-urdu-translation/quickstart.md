# Quickstart – Feature 014: Urdu Translation Toggle

## Prerequisites

- Python 3.11+ with venv
- Node.js 18+ (for frontend)
- Neon PostgreSQL database (from Feature 012)
- OpenAI API key for translation

## Architecture Overview

```
Frontend (Docusaurus :3000)
    │
    ├── LanguageToggle Component
    ├── TranslatableContent Component
    └── Locale Files (i18n/)
    │
    └── FastAPI Backend (:8000)
              │
              ├── /translate/chapter → OpenAI API
              └── Neon PostgreSQL ← Translation Cache
```

## Install Dependencies

### Backend Dependencies

```bash
cd C:\Users\Leo\interactive-agentic-book
venv\Scripts\activate
pip install openai sqlalchemy[asyncio] asyncpg
```

## Environment Variables

Add to `.env` in project root:

```env
# Database (Neon PostgreSQL)
DATABASE_URL=postgresql://user:password@ep-xxx.us-east-1.aws.neon.tech/textbook_db?sslmode=require

# OpenAI for translation
OPENAI_API_KEY=sk-proj-...

# Optional: Backend port
BACKEND_PORT=8000
```

## Database Setup

Translation tables are automatically created on backend startup. No manual migration needed.

### Tables Created:
- `translations` - Stores translated content
- `translation_metadata` - Performance metrics
- `translation_cache` - Cache management

## Start Servers

### 1. Start Backend (Terminal 1)

```bash
cd C:\Users\Leo\interactive-agentic-book
venv\Scripts\activate
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output**:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

### 2. Start Frontend (Terminal 2)

```bash
cd C:\Users\Leo\interactive-agentic-book
npm run start
```

**Expected Output**:
```
[INFO] Starting the development server...
[SUCCESS] Docusaurus website is running at: http://localhost:3000/
```

## Test Translation

### 1. Navigate to a Chapter

1. Open browser: `http://localhost:3000`
2. Navigate to any chapter (e.g., `/docs/course-overview`)

### 2. Toggle Language

1. Click **اردو** button in navbar (top right)
2. Wait for translation (10-30 seconds for first time)
3. Content will switch to Urdu with RTL layout

### 3. Verify Features

- ✅ **UI Elements**: All buttons/labels should be in Urdu
- ✅ **RTL Layout**: Text should be right-aligned
- ✅ **Urdu Font**: Noto Nastaliq Urdu font should load
- ✅ **Cache**: Switch back to English, then Urdu again (should be instant)

## API Endpoints

### Translate Chapter

```bash
POST http://localhost:8000/translate/chapter
Content-Type: application/json

{
  "chapter_path": "/docs/course-overview",
  "content": "<h1>Chapter Title</h1><p>Content...</p>"
}
```

**Response**:
```json
{
  "translated_content": "<h1>باب کا عنوان</h1><p>مواد...</p>",
  "cache_hit": false,
  "translation_time": 12.5
}
```

### Check Translation Status

```bash
GET http://localhost:8000/translate/status/docs/course-overview
```

**Response**:
```json
{
  "exists": true,
  "cached": true,
  "last_translated": "2025-12-19T10:30:00Z"
}
```

### Clear Cache

```bash
DELETE http://localhost:8000/translate/cache/docs/course-overview
```

### Cache Statistics

```bash
GET http://localhost:8000/translate/cache/stats
```

**Response**:
```json
{
  "total_translations": 15,
  "cache_hits": 120,
  "cache_misses": 15,
  "hit_rate": 0.89
}
```

## Troubleshooting

### Translation Not Working

1. **Check Backend Logs**:
   ```bash
   # Look for errors in backend terminal
   ```

2. **Check OpenAI API Key**:
   ```bash
   # Verify OPENAI_API_KEY in .env
   ```

3. **Check Database Connection**:
   ```bash
   # Verify DATABASE_URL in .env
   # Check backend logs for connection errors
   ```

### RTL Layout Issues

1. **Check CSS Loading**:
   - Verify `src/css/rtl-support.css` is imported
   - Check browser console for CSS errors

2. **Check Font Loading**:
   - Verify Noto Nastaliq Urdu font loads
   - Check Network tab in browser DevTools

### Slow Translation

1. **First Translation**: Normal (10-30 seconds)
2. **Cached Translation**: Should be instant (<200ms)
3. **Large Content**: May take 20-45 seconds

**Optimization Tips**:
- Use `gpt-4o-mini` (already configured)
- Enable caching (already enabled)
- Pre-translate popular chapters (future enhancement)

## Development Workflow

### Adding New Translations

1. **Add to Locale Files**:
   ```json
   // i18n/en/translations.json
   {
     "common": {
       "newKey": "New Text"
     }
   }
   
   // i18n/ur/translations.json
   {
     "common": {
       "newKey": "نیا متن"
     }
   }
   ```

2. **Use in Component**:
   ```tsx
   import { useTranslation } from '../lib/i18n';
   
   const { t } = useTranslation();
   <button>{t('common.newKey')}</button>
   ```

### Testing Translation

1. **Manual Testing**:
   - Toggle language on different pages
   - Check RTL layout
   - Verify cache behavior

2. **API Testing**:
   - Use Postman/curl for API endpoints
   - Check response times
   - Verify cache statistics

## Next Steps

- [ ] Add more UI translations (signup, profile pages)
- [ ] Implement translation preloading
- [ ] Add user feedback on translation quality
- [ ] Optimize for very large chapters

---

**For more details, see**:
- `specs/014-urdu-translation/spec.md` - Full specification
- `specs/014-urdu-translation/plan.md` - Implementation plan
- `specs/014-urdu-translation/LOCALE-FILES.md` - Locale files guide

