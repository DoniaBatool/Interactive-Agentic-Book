---
description: "Tasks for Urdu Translation Toggle – Feature 014"
---

# Tasks: Urdu Translation Toggle

**Input**: spec.md, plan.md  
**Tests**: Manual testing + Translation quality assessment + RTL rendering tests

## Phase 1: Backend Translation Service

### Database Schema
- [x] T014-001 Create translation tables in PostgreSQL:
  - `translations` table (chapter_path, source_content, translated_content, content_hash)
  - `translation_metadata` table (performance metrics, quality scores)
  - Indexes for efficient lookups

- [x] T014-002 Create database migration script:
  - Add translation tables to existing schema
  - Create indexes for performance
  - Add foreign key constraints if needed

### Translation API
- [x] T014-010 Create `backend/app/models/translation.py`:
  - Translation SQLAlchemy model
  - TranslationMetadata model
  - Proper relationships and constraints

- [x] T014-011 Create `backend/app/services/translation.py`:
  - `TranslationService` class with OpenAI integration
  - Context-aware translation for technical content
  - Markdown preservation logic
  - Error handling and retries

- [x] T014-012 Create `backend/app/services/translation_cache.py`:
  - `TranslationCache` class for database caching
  - Content hash-based cache invalidation
  - Efficient retrieval and storage methods
  - Cache statistics and monitoring

- [x] T014-013 Create `backend/app/api/translation.py`:
  - POST `/translate/chapter` - Translate chapter content
  - GET `/translate/status/{chapter_path}` - Check translation status
  - DELETE `/translate/cache/{chapter_path}` - Clear cache (admin)
  - Proper request/response schemas

- [x] T014-014 Register translation router in `main.py`:
  - Add translation API routes
  - Configure CORS for translation endpoints
  - Add rate limiting if needed

### OpenAI Integration
- [x] T014-020 Implement translation prompt engineering:
  - Technical content translation prompts
  - Markdown structure preservation
  - Code block handling (translate comments only)
  - Cultural adaptation guidelines

- [x] T014-021 Add translation quality assessment:
  - Post-translation validation
  - Technical term consistency checking
  - Markdown structure verification
  - Quality scoring system

## Phase 2: Frontend Language System

### Language Context
- [x] T014-030 Create `src/context/LanguageContext.tsx`:
  - Language state management (en/ur)
  - Translation request handling
  - Loading states and error handling
  - Language preference persistence

- [x] T014-031 Update `src/theme/Root.tsx`:
  - Wrap app with LanguageProvider
  - Set document language and direction attributes
  - Load language-specific fonts dynamically

### Language Toggle Component
- [x] T014-040 Create `src/components/LanguageToggle.tsx`:
  - Toggle button with Urdu/English labels
  - Loading spinner during translation
  - Accessibility attributes (aria-label, etc.)
  - Keyboard navigation support

- [x] T014-041 Create `src/components/TranslatableContent.tsx`:
  - Chapter content translation wrapper
  - Progressive loading (English first, then Urdu)
  - Error fallback to English
  - Translation caching in browser

### Integration Points
- [x] T014-050 Update `src/theme/DocItem/Content/index.tsx`:
  - Wrap content with TranslatableContent
  - Pass chapter path for translation
  - Handle translation loading states

- [x] T014-051 Add LanguageToggle to navbar:
  - Update navbar component to include toggle
  - Position toggle appropriately
  - Ensure visibility on all pages

## Phase 3: RTL Support & Typography

### CSS RTL Implementation
- [x] T014-060 Create `src/css/rtl-support.css`:
  - RTL layout rules for Urdu content
  - Directional adjustments for UI elements
  - Font family definitions for Urdu
  - Mixed content handling (LTR code in RTL text)

- [x] T014-061 Update existing CSS for RTL compatibility:
  - Use logical CSS properties (margin-inline-start, etc.)
  - Update navbar, sidebar, pagination for RTL
  - Ensure icons and buttons work in both directions
  - Test dark/light mode compatibility

### Font Integration
- [x] T014-070 Add Urdu font support:
  - Google Fonts integration (Noto Nastaliq Urdu)
  - Fallback fonts for different systems
  - Font loading optimization
  - Typography adjustments for readability

- [x] T014-071 Create Urdu typography styles:
  - Appropriate font sizes and line heights
  - Text spacing and kerning
  - Heading styles for Urdu content
  - Code block font handling

## Phase 4: Content Translation Features

### Chapter-Level Translation
- [x] T014-080 Implement chapter detection:
  - Extract chapter path from current URL
  - Get chapter content for translation
  - Handle different content types (markdown, MDX)
  - Preserve internal links and references

- [x] T014-081 Add translation status indicators:
  - Show translation progress
  - Display cache status (cached/fresh)
  - Error messages for failed translations
  - Retry mechanisms for failures

### Advanced Features
- [ ] T014-090 Implement translation preloading:
  - Background translation of popular chapters
  - Predictive translation based on user navigation
  - Batch translation capabilities
  - Translation queue management

- [ ] T014-091 Add translation quality features:
  - User feedback on translation quality
  - Manual translation corrections (admin)
  - Translation version management
  - A/B testing for translation improvements

## Phase 5: Performance & Optimization

### Caching Optimization
- [x] T014-100 Implement multi-level caching:
  - Database cache (PostgreSQL) ✅
  - Memory cache (Redis if available) ⏳ Future
  - Browser cache (localStorage) ✅
  - CDN cache for static translations ⏳ Future

- [x] T014-101 Add cache warming strategies:
  - Pre-translate popular chapters ⏳ Future
  - Background translation during low usage ⏳ Future
  - Cache invalidation on content updates ✅
  - Cache statistics and monitoring ✅

### Performance Monitoring
- [x] T014-110 Add translation metrics:
  - Translation request/response times ✅
  - Cache hit/miss rates ✅
  - Translation quality scores ✅
  - User language preferences analytics ⏳ Future

- [x] T014-111 Implement performance optimizations:
  - Lazy loading of translation features ✅
  - Debounced translation requests ✅
  - Compression for large translations ⏳ Future
  - Progressive enhancement for RTL ✅

## Phase 6: Testing & Quality Assurance

### Automated Testing
- [ ] T014-120 Unit tests for translation service:
  - Translation API functionality
  - Cache operations
  - Error handling scenarios
  - Performance benchmarks

- [ ] T014-121 Frontend component tests:
  - Language toggle functionality
  - RTL rendering tests
  - Translation loading states
  - Error boundary testing

### Manual Testing
- [x] T014-130 Translation quality assessment:
  - Technical accuracy verification ✅
  - Cultural appropriateness review ✅
  - Consistency across chapters ✅
  - Native speaker feedback ⏳ Future

- [x] T014-131 RTL usability testing:
  - Navigation in RTL mode ✅
  - Reading experience evaluation ✅
  - UI element positioning ✅
  - Cross-browser compatibility ✅

### Integration Testing
- [x] T014-140 End-to-end translation flow:
  - Complete user journey testing ✅
  - Performance under load ✅
  - Error recovery scenarios ✅
  - Cross-device compatibility ✅

## Phase 7: Documentation & Deployment

### Documentation
- [x] T014-150 Update documentation:
  - Translation system architecture ✅
  - API documentation ✅
  - User guide for language switching ✅
  - Admin guide for translation management ✅

- [x] T014-151 Create deployment guide:
  - Environment variable configuration ✅
  - Database migration instructions ✅
  - Performance tuning recommendations ✅
  - Monitoring setup guide ✅

### Production Readiness
- [ ] T014-160 Production deployment preparation:
  - Environment-specific configurations
  - Security considerations for translation API
  - Rate limiting and abuse prevention
  - Backup and recovery procedures

---

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend (:3000)                         │
│                         Docusaurus                              │
├─────────────────────────────────────────────────────────────────┤
│  LanguageContext │ LanguageToggle │ TranslatableContent │ RTL   │
└───────┬─────────────────────┬───────────────────────────────────┘
        │                     │
        ▼                     ▼
┌───────────────┐   ┌─────────────────────────────────────────────┐
│   FastAPI     │   │              OpenAI API                     │
│ /translate/*  │   │          Translation Service                │
│   (:8000)     │   │                                             │
└───────┬───────┘   └─────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────────────────┐
│                       PostgreSQL                               │
│         translations │ translation_metadata │ cache            │
└───────────────────────────────────────────────────────────────┘
```

**Estimated Timeline**: 3-4 days  
**Key Dependencies**: OpenAI API, PostgreSQL database  
**Success Metrics**: >90% cache hit rate, <5s translation time, Positive user feedback
