# Data Model – Feature 014: Urdu Translation Toggle

## Database Schema

### Translations Table

Stores translated content with content hashing for cache invalidation.

```sql
CREATE TABLE translations (
    id SERIAL PRIMARY KEY,
    chapter_path VARCHAR(500) NOT NULL,
    source_content_hash VARCHAR(64) NOT NULL,
    source_content TEXT NOT NULL,
    translated_content TEXT NOT NULL,
    language VARCHAR(10) DEFAULT 'ur',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(chapter_path, source_content_hash, language)
);

CREATE INDEX idx_translations_chapter_path ON translations(chapter_path);
CREATE INDEX idx_translations_hash ON translations(source_content_hash);
CREATE INDEX idx_translations_language ON translations(language);
```

### Translation Metadata Table

Stores performance metrics and quality scores for translations.

```sql
CREATE TABLE translation_metadata (
    id SERIAL PRIMARY KEY,
    translation_id INTEGER UNIQUE NOT NULL REFERENCES translations(id) ON DELETE CASCADE,
    translation_time_seconds DECIMAL(10, 3),
    content_length INTEGER,
    quality_score DECIMAL(3, 2),
    model_used VARCHAR(50) DEFAULT 'gpt-4o-mini',
    cache_hit BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_translation_metadata_translation_id ON translation_metadata(translation_id);
CREATE INDEX idx_translation_metadata_quality ON translation_metadata(quality_score);
```

### Translation Cache Table

Manages cache statistics and invalidation.

```sql
CREATE TABLE translation_cache (
    id SERIAL PRIMARY KEY,
    chapter_path VARCHAR(500) NOT NULL,
    content_hash VARCHAR(64) NOT NULL,
    cache_key VARCHAR(100) NOT NULL,
    cached_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE,
    hit_count INTEGER DEFAULT 0,
    last_accessed TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(chapter_path, content_hash)
);

CREATE INDEX idx_translation_cache_path ON translation_cache(chapter_path);
CREATE INDEX idx_translation_cache_hash ON translation_cache(content_hash);
CREATE INDEX idx_translation_cache_expires ON translation_cache(expires_at);
```

## SQLAlchemy Models

### Translation Model

```python
# backend/app/models/translation.py
from sqlalchemy import Column, Integer, String, Text, DateTime, UniqueConstraint, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class Translation(Base):
    __tablename__ = "translations"
    
    id = Column(Integer, primary_key=True, index=True)
    chapter_path = Column(String(500), nullable=False, index=True)
    source_content_hash = Column(String(64), nullable=False, index=True)
    source_content = Column(Text, nullable=False)
    translated_content = Column(Text, nullable=False)
    language = Column(String(10), default='ur')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    metadata = relationship("TranslationMetadata", back_populates="translation", uselist=False)
    
    __table_args__ = (
        UniqueConstraint('chapter_path', 'source_content_hash', 'language', name='uq_translation'),
        Index('idx_translations_chapter_path', 'chapter_path'),
        Index('idx_translations_hash', 'source_content_hash'),
    )
```

### TranslationMetadata Model

```python
class TranslationMetadata(Base):
    __tablename__ = "translation_metadata"
    
    id = Column(Integer, primary_key=True, index=True)
    translation_id = Column(Integer, ForeignKey("translations.id", ondelete="CASCADE"), unique=True, nullable=False)
    translation_time_seconds = Column(Numeric(10, 3))
    content_length = Column(Integer)
    quality_score = Column(Numeric(3, 2))
    model_used = Column(String(50), default='gpt-4o-mini')
    cache_hit = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    translation = relationship("Translation", back_populates="metadata")
```

### TranslationCache Model

```python
class TranslationCache(Base):
    __tablename__ = "translation_cache"
    
    id = Column(Integer, primary_key=True, index=True)
    chapter_path = Column(String(500), nullable=False, index=True)
    content_hash = Column(String(64), nullable=False, index=True)
    cache_key = Column(String(100), nullable=False)
    cached_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)
    hit_count = Column(Integer, default=0)
    last_accessed = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        UniqueConstraint('chapter_path', 'content_hash', name='uq_translation_cache'),
        Index('idx_translation_cache_path', 'chapter_path'),
        Index('idx_translation_cache_hash', 'content_hash'),
        Index('idx_translation_cache_expires', 'expires_at'),
    )
```

## API Request/Response Models

### Translation Request

```python
# backend/app/api/translation.py
from pydantic import BaseModel

class TranslationRequest(BaseModel):
    chapter_path: str
    content: str
    language: str = "ur"
```

### Translation Response

```python
class TranslationResponse(BaseModel):
    translated_content: str
    cache_hit: bool
    translation_time: float
    chapter_path: str
```

### Translation Status Response

```python
class TranslationStatusResponse(BaseModel):
    exists: bool
    cached: bool
    last_translated: Optional[datetime]
    chapter_path: str
```

### Cache Statistics Response

```python
class CacheStatsResponse(BaseModel):
    total_translations: int
    cache_hits: int
    cache_misses: int
    hit_rate: float
```

## Frontend Data Models

### Language Context State

```typescript
// src/context/LanguageContext.tsx
interface LanguageState {
  currentLanguage: 'en' | 'ur';
  isTranslating: boolean;
  translationError: string | null;
}
```

### Translation Request

```typescript
interface TranslationRequest {
  chapter_path: string;
  content: string;
  language?: string;
}
```

### Translation Response

```typescript
interface TranslationResponse {
  translated_content: string;
  cache_hit: boolean;
  translation_time: number;
  chapter_path: string;
}
```

## Content Hashing

Content is hashed using SHA-256 for efficient cache lookup:

```python
import hashlib

def hash_content(content: str) -> str:
    """Generate SHA-256 hash of content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()
```

**Benefits**:
- Fast cache lookup (indexed hash column)
- Automatic cache invalidation on content change
- Efficient storage (64-char hash vs full content)

## Cache Strategy

### Cache Lookup Flow

```
1. User requests translation
2. Generate content hash
3. Check cache by (chapter_path, content_hash)
4. If found: Return cached translation (instant)
5. If not found: Call OpenAI API → Store in cache → Return
```

### Cache Invalidation

- **Automatic**: Content hash changes when source content changes
- **Manual**: DELETE `/translate/cache/{path}` endpoint
- **Time-based**: Optional `expires_at` for cache expiration

## Performance Considerations

### Indexes

- `chapter_path` - Fast lookup by chapter
- `source_content_hash` - Fast cache lookup
- `expires_at` - Efficient cache cleanup

### Query Optimization

```sql
-- Fast cache lookup
SELECT translated_content 
FROM translations 
WHERE chapter_path = ? 
  AND source_content_hash = ? 
  AND language = 'ur'
LIMIT 1;

-- Cache statistics
SELECT 
  COUNT(*) as total,
  SUM(CASE WHEN cache_hit THEN 1 ELSE 0 END) as hits
FROM translation_metadata;
```

---

**For implementation details, see**:
- `backend/app/models/translation.py` - Model definitions
- `backend/app/services/translation_cache.py` - Cache implementation
- `backend/app/api/translation.py` - API endpoints

