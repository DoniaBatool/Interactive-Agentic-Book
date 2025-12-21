# API Contracts – Feature 014: Urdu Translation Toggle

## Endpoint: POST /translate/chapter

### Request

```json
{
  "chapter_path": "/docs/course-overview",
  "content": "<h1>Chapter Title</h1><p>Content to translate...</p>",
  "target_language": "ur",
  "force_retranslate": false
}
```

### Response (Success - 200)

```json
{
  "translated_content": "<h1>باب کا عنوان</h1><p>ترجمہ شدہ مواد...</p>",
  "cached": false,
  "translation_time_ms": 12500,
  "word_count": 450,
  "chapter_path": "/docs/course-overview",
  "target_language": "ur"
}
```

### Response (Cached - 200)

```json
{
  "translated_content": "<h1>باب کا عنوان</h1><p>ترجمہ شدہ مواد...</p>",
  "cached": true,
  "translation_time_ms": 15,
  "word_count": 450,
  "chapter_path": "/docs/course-overview",
  "target_language": "ur"
}
```

### Response (Error - 400)

```json
{
  "detail": "Content cannot be empty"
}
```

### Response (Error - 400)

```json
{
  "detail": "Content too large. Maximum size is 100KB."
}
```

### Response (Error - 500)

```json
{
  "detail": "Translation failed: OpenAI API error"
}
```

---

## Endpoint: GET /translate/status/{chapter_path}

### Request

```
GET /translate/status/docs/course-overview?target_language=ur
```

### Response (Success - 200)

```json
{
  "chapter_path": "/docs/course-overview",
  "target_language": "ur",
  "exists": true,
  "cached": true,
  "created_at": "2025-12-19T10:30:00Z",
  "word_count": 450,
  "translation_time_ms": 12500
}
```

### Response (Not Found - 200)

```json
{
  "chapter_path": "/docs/course-overview",
  "target_language": "ur",
  "exists": false,
  "cached": false,
  "created_at": null,
  "word_count": null,
  "translation_time_ms": null
}
```

---

## Endpoint: DELETE /translate/cache/{chapter_path}

### Request

```
DELETE /translate/cache/docs/course-overview?target_language=ur
```

### Response (Success - 200)

```json
{
  "message": "Translation cache cleared for /docs/course-overview",
  "chapter_path": "/docs/course-overview",
  "target_language": "ur"
}
```

### Response (Error - 500)

```json
{
  "detail": "Failed to clear translation cache"
}
```

---

## Endpoint: GET /translate/cache/stats

### Request

```
GET /translate/cache/stats
```

### Response (Success - 200)

```json
{
  "total_entries": 25,
  "expired_entries": 2,
  "active_entries": 23,
  "total_accesses": 150,
  "popular_chapters": [
    {
      "chapter_path": "/docs/course-overview",
      "access_count": 45
    },
    {
      "chapter_path": "/docs/intro",
      "access_count": 32
    }
  ]
}
```

---

## Endpoint: POST /translate/cache/cleanup

### Request

```
POST /translate/cache/cleanup
```

### Response (Success - 200)

```json
{
  "message": "Cleaned up 2 expired cache entries",
  "cleared_count": 2
}
```

---

## Endpoint: GET /translate/health

### Request

```
GET /translate/health
```

### Response (Success - 200)

```json
{
  "status": "ok",
  "service": "translation",
  "supported_languages": ["ur", "en"],
  "features": [
    "chapter_translation",
    "caching",
    "markdown_preservation",
    "technical_terminology"
  ]
}
```

---

## Request/Response Models

### TranslationRequest

```typescript
interface TranslationRequest {
  chapter_path: string;        // e.g., "/docs/course-overview"
  content: string;              // HTML/Markdown content to translate
  target_language: string;      // "ur" or "en"
  force_retranslate?: boolean;  // Force new translation even if cached
}
```

### TranslationResponse

```typescript
interface TranslationResponse {
  translated_content: string;   // Translated HTML/Markdown
  cached: boolean;               // Whether result was from cache
  translation_time_ms: number;  // Time taken in milliseconds
  word_count: number;            // Number of words in source
  chapter_path: string;          // Chapter path that was translated
  target_language: string;       // Target language code
}
```

### TranslationStatusResponse

```typescript
interface TranslationStatusResponse {
  chapter_path: string;
  target_language: string;
  exists: boolean;              // Whether translation exists
  cached: boolean;              // Whether translation is cached
  created_at?: string;          // ISO timestamp
  word_count?: number;
  translation_time_ms?: number;
}
```

### CacheStatsResponse

```typescript
interface CacheStatsResponse {
  total_entries: number;
  expired_entries: number;
  active_entries: number;
  total_accesses: number;
  popular_chapters: Array<{
    chapter_path: string;
    access_count: number;
  }>;
}
```

---

## Error Codes

| Status Code | Description |
|------------|-------------|
| 200 | Success |
| 400 | Bad Request (invalid input, content too large, etc.) |
| 404 | Not Found (chapter path not found) |
| 500 | Internal Server Error (translation service error, database error) |

---

## Rate Limiting

Currently no rate limiting implemented. Future enhancement:
- Rate limit: 10 requests per minute per IP
- Burst limit: 20 requests per 5 minutes

---

## Content Size Limits

- **Maximum content size**: 100KB (100,000 characters)
- **Recommended size**: <50KB for optimal performance
- **Large content warning**: >15KB triggers warning message

---

## Cache Behavior

- **Cache key**: `{chapter_path}_{content_hash}_{target_language}`
- **Cache invalidation**: Automatic on content hash change
- **Cache expiration**: Optional (configurable via `expires_at`)
- **Cache hit rate target**: >90% after initial translations

---

## Performance Expectations

- **First translation**: 10-30 seconds (depending on content size)
- **Cached translation**: <200ms (instant)
- **API response time**: <50ms (excluding translation time)
- **Database query time**: <10ms (with indexes)

