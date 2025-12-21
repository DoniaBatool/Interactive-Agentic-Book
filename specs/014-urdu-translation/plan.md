# Implementation Plan: Feature 014 - Urdu Translation Toggle

## Overview

Implement a comprehensive Urdu translation system with chapter-level caching, RTL support, and seamless language switching for the Physical AI textbook.

## Architecture Design

### **Translation Flow**
```
User clicks Urdu toggle
    ↓
Check translation cache
    ↓
If cached: Return instantly
If not cached: Translate via OpenAI
    ↓
Store in database cache
    ↓
Display Urdu content with RTL layout
```

### **Database Schema**

```sql
-- Translation cache table
CREATE TABLE translations (
    id SERIAL PRIMARY KEY,
    chapter_path VARCHAR(255) NOT NULL,
    source_language VARCHAR(10) DEFAULT 'en',
    target_language VARCHAR(10) NOT NULL,
    source_content TEXT NOT NULL,
    translated_content TEXT NOT NULL,
    content_hash VARCHAR(64) NOT NULL, -- For cache invalidation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(chapter_path, target_language, content_hash)
);

-- Translation metadata
CREATE TABLE translation_metadata (
    id SERIAL PRIMARY KEY,
    chapter_path VARCHAR(255) NOT NULL,
    total_words INTEGER,
    translation_time_ms INTEGER,
    translation_quality_score DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_translations_chapter_lang ON translations(chapter_path, target_language);
CREATE INDEX idx_translations_hash ON translations(content_hash);
```

### **API Design**

```python
# Translation endpoints
POST /translate/chapter
GET /translate/status/{chapter_path}
DELETE /translate/cache/{chapter_path}  # Admin only

# Request/Response schemas
class TranslationRequest:
    chapter_path: str
    content: str
    target_language: str = "ur"  # Urdu
    force_retranslate: bool = False

class TranslationResponse:
    translated_content: str
    cached: bool
    translation_time_ms: int
    word_count: int
```

## Implementation Strategy

### **Phase 1: Backend Translation Service**

#### **1.1 OpenAI Translation Integration**
```python
# backend/app/services/translation.py
class TranslationService:
    def __init__(self):
        self.openai_client = OpenAI()
        self.cache = TranslationCache()
    
    async def translate_chapter(
        self, 
        content: str, 
        chapter_path: str,
        target_lang: str = "ur"
    ) -> TranslationResult:
        # Check cache first
        cached = await self.cache.get_translation(chapter_path, content, target_lang)
        if cached:
            return cached
        
        # Translate via OpenAI
        translated = await self._translate_with_openai(content, target_lang)
        
        # Cache result
        await self.cache.store_translation(chapter_path, content, translated, target_lang)
        
        return translated
```

#### **1.2 Translation Prompt Engineering**
```python
def get_translation_prompt(content: str, target_lang: str) -> str:
    return f"""
You are an expert technical translator specializing in robotics, AI, and computer science content.

Translate the following English technical content to {target_lang} (Urdu):

IMPORTANT GUIDELINES:
1. Preserve all markdown formatting (headers, lists, code blocks, links)
2. Keep code blocks in English - only translate comments
3. Translate technical terms appropriately:
   - "Robot" → "روبوٹ"
   - "Artificial Intelligence" → "مصنوعی ذہانت"
   - "ROS 2" → "ROS 2" (keep as-is)
   - "Gazebo" → "Gazebo" (keep as-is)
4. Maintain mathematical formulas and equations exactly
5. Keep proper nouns and brand names in English
6. Ensure cultural appropriateness for Pakistani/Indian Urdu speakers
7. Use formal/academic Urdu register

Content to translate:
{content}

Translated content:
"""
```

#### **1.3 Caching System**
```python
# backend/app/services/translation_cache.py
class TranslationCache:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_translation(
        self, 
        chapter_path: str, 
        content: str, 
        target_lang: str
    ) -> Optional[str]:
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        
        result = await self.db.execute(
            select(Translation).where(
                Translation.chapter_path == chapter_path,
                Translation.target_language == target_lang,
                Translation.content_hash == content_hash
            )
        )
        
        translation = result.scalar_one_or_none()
        return translation.translated_content if translation else None
    
    async def store_translation(
        self, 
        chapter_path: str, 
        source_content: str, 
        translated_content: str, 
        target_lang: str
    ):
        content_hash = hashlib.sha256(source_content.encode()).hexdigest()
        
        translation = Translation(
            chapter_path=chapter_path,
            source_content=source_content,
            translated_content=translated_content,
            target_language=target_lang,
            content_hash=content_hash
        )
        
        self.db.add(translation)
        await self.db.commit()
```

### **Phase 2: Frontend Language Toggle**

#### **2.1 Language Context Provider**
```typescript
// src/context/LanguageContext.tsx
interface LanguageContextType {
  currentLanguage: 'en' | 'ur';
  toggleLanguage: () => void;
  translateChapter: (chapterPath: string, content: string) => Promise<string>;
  isTranslating: boolean;
  translationError: string | null;
}

export const LanguageProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [currentLanguage, setCurrentLanguage] = useState<'en' | 'ur'>('en');
  const [isTranslating, setIsTranslating] = useState(false);
  const [translationError, setTranslationError] = useState<string | null>(null);
  
  // Load language preference from localStorage
  useEffect(() => {
    const saved = localStorage.getItem('preferred-language');
    if (saved === 'ur' || saved === 'en') {
      setCurrentLanguage(saved);
    }
  }, []);
  
  // Save language preference
  useEffect(() => {
    localStorage.setItem('preferred-language', currentLanguage);
    document.documentElement.setAttribute('lang', currentLanguage);
    document.documentElement.setAttribute('dir', currentLanguage === 'ur' ? 'rtl' : 'ltr');
  }, [currentLanguage]);
  
  const toggleLanguage = useCallback(() => {
    setCurrentLanguage(prev => prev === 'en' ? 'ur' : 'en');
  }, []);
  
  const translateChapter = useCallback(async (chapterPath: string, content: string) => {
    setIsTranslating(true);
    setTranslationError(null);
    
    try {
      const response = await fetch('/api/translate/chapter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chapter_path: chapterPath,
          content,
          target_language: 'ur'
        })
      });
      
      if (!response.ok) throw new Error('Translation failed');
      
      const data = await response.json();
      return data.translated_content;
    } catch (error) {
      setTranslationError(error.message);
      throw error;
    } finally {
      setIsTranslating(false);
    }
  }, []);
  
  return (
    <LanguageContext.Provider value={{
      currentLanguage,
      toggleLanguage,
      translateChapter,
      isTranslating,
      translationError
    }}>
      {children}
    </LanguageContext.Provider>
  );
};
```

#### **2.2 Language Toggle Component**
```typescript
// src/components/LanguageToggle.tsx
export const LanguageToggle: React.FC = () => {
  const { currentLanguage, toggleLanguage, isTranslating } = useLanguage();
  
  return (
    <button
      className="language-toggle"
      onClick={toggleLanguage}
      disabled={isTranslating}
      aria-label={`Switch to ${currentLanguage === 'en' ? 'Urdu' : 'English'}`}
    >
      {isTranslating ? (
        <span className="translation-spinner">⟳</span>
      ) : (
        <span className="language-text">
          {currentLanguage === 'en' ? 'اردو' : 'English'}
        </span>
      )}
    </button>
  );
};
```

### **Phase 3: RTL Support & Typography**

#### **3.1 RTL CSS Implementation**
```css
/* src/css/rtl-support.css */
[dir="rtl"] {
  --ifm-font-family-base: 'Noto Nastaliq Urdu', 'Jameel Noori Nastaleeq', serif;
}

/* RTL layout adjustments */
[dir="rtl"] .navbar__items {
  flex-direction: row-reverse;
}

[dir="rtl"] .menu__list-item {
  text-align: right;
}

[dir="rtl"] .pagination-nav {
  flex-direction: row-reverse;
}

/* Keep code blocks LTR */
[dir="rtl"] pre,
[dir="rtl"] code {
  direction: ltr;
  text-align: left;
}

/* Urdu typography */
.urdu-content {
  font-family: 'Noto Nastaliq Urdu', 'Jameel Noori Nastaleeq', serif;
  font-size: 1.1em;
  line-height: 1.8;
  text-align: right;
}

/* Translation loading states */
.translation-loading {
  opacity: 0.6;
  pointer-events: none;
}

.translation-error {
  border: 1px solid #ff6b6b;
  background: rgba(255, 107, 107, 0.1);
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
}
```

#### **3.2 Font Integration**
```typescript
// src/theme/Layout/index.tsx
export default function Layout(props) {
  const { currentLanguage } = useLanguage();
  
  useEffect(() => {
    // Load Urdu fonts dynamically
    if (currentLanguage === 'ur') {
      const link = document.createElement('link');
      link.href = 'https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;600;700&display=swap';
      link.rel = 'stylesheet';
      document.head.appendChild(link);
    }
  }, [currentLanguage]);
  
  return <OriginalLayout {...props} />;
}
```

### **Phase 4: Content Translation Integration**

#### **4.1 Chapter Translation Component**
```typescript
// src/components/TranslatableContent.tsx
export const TranslatableContent: React.FC<{ 
  chapterPath: string;
  children: ReactNode;
}> = ({ chapterPath, children }) => {
  const { currentLanguage, translateChapter } = useLanguage();
  const [translatedContent, setTranslatedContent] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
    if (currentLanguage === 'ur' && !translatedContent) {
      handleTranslation();
    }
  }, [currentLanguage, chapterPath]);
  
  const handleTranslation = async () => {
    setIsLoading(true);
    try {
      const content = document.querySelector('.markdown')?.innerHTML || '';
      const translated = await translateChapter(chapterPath, content);
      setTranslatedContent(translated);
    } catch (error) {
      console.error('Translation failed:', error);
    } finally {
      setIsLoading(false);
    }
  };
  
  if (currentLanguage === 'ur') {
    if (isLoading) {
      return <div className="translation-loading">{children}</div>;
    }
    
    if (translatedContent) {
      return (
        <div 
          className="urdu-content"
          dangerouslySetInnerHTML={{ __html: translatedContent }}
        />
      );
    }
  }
  
  return <>{children}</>;
};
```

## Performance Optimization

### **Caching Strategy**
1. **Database Caching**: Store translations in PostgreSQL
2. **Memory Caching**: Redis for frequently accessed translations
3. **Browser Caching**: LocalStorage for user's translated chapters
4. **Preemptive Translation**: Background translation of popular chapters

### **Loading Strategy**
1. **Progressive Loading**: Show English first, then replace with Urdu
2. **Skeleton Loading**: Show loading placeholders during translation
3. **Error Fallback**: Graceful degradation to English on translation failure
4. **Retry Logic**: Automatic retry for failed translations

## Testing Strategy

### **Unit Tests**
- Translation service functionality
- Cache hit/miss scenarios
- RTL CSS rendering
- Language toggle behavior

### **Integration Tests**
- End-to-end translation flow
- Database cache operations
- API error handling
- Performance benchmarks

### **User Testing**
- Urdu native speaker feedback
- RTL usability testing
- Translation quality assessment
- Performance on different devices

## Deployment Considerations

### **Environment Variables**
```env
# Translation settings
OPENAI_API_KEY=sk-...
TRANSLATION_CACHE_TTL=86400  # 24 hours
MAX_TRANSLATION_LENGTH=50000  # characters
SUPPORTED_LANGUAGES=en,ur

# Performance settings
TRANSLATION_BATCH_SIZE=5
TRANSLATION_TIMEOUT=30000  # 30 seconds
```

### **Database Migration**
```sql
-- Migration script for translation tables
-- Run this before deploying translation feature
```

### **Monitoring**
- Translation API response times
- Cache hit rates
- Translation quality scores
- User language preferences

---

**Estimated Timeline**: 3-4 days  
**Key Risks**: Translation quality, RTL complexity, Performance impact  
**Success Metrics**: >90% cache hit rate, <5s initial translation time, Positive user feedback
