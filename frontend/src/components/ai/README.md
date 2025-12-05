# AI Block Components

This directory contains React TypeScript components for AI-interactive blocks used in Chapter 1 of the AI-Native Physical AI & Robotics Textbook.

## Components

### 1. AskQuestionBlock

A component that allows learners to ask questions about chapter content.

**Props:**
- `chapterId?: number` - Optional chapter ID for context
- `sectionId?: string` - Optional section ID for context

**Usage in MDX:**
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';

<AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />
```

**Future Enhancement:**
- Integrate with RAG pipeline for retrieving relevant chapter content
- Add OpenAI API call for generating answers
- Add source citations from retrieved content

---

### 2. ExplainLike10Block

A component that generates simplified explanations of complex concepts at age-appropriate level.

**Props:**
- `concept?: string` - Optional concept name to explain
- `chapterId?: number` - Optional chapter ID for context

**Usage in MDX:**
```mdx
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';

<ExplainLike10Block concept="autonomy" chapterId={1} />
```

**Future Enhancement:**
- Integrate with LLM using ELI10 (Explain Like I'm 10) prompt
- Add concept context retrieval from chapter content
- Add analogies and examples for better understanding

---

### 3. InteractiveQuizBlock

A component that generates interactive quizzes based on chapter learning objectives.

**Props:**
- `chapterId?: number` - Optional chapter ID for quiz generation
- `numQuestions?: number` - Optional number of questions (default: 5)

**Usage in MDX:**
```mdx
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';

<InteractiveQuizBlock chapterId={1} numQuestions={5} />
```

**Future Enhancement:**
- Generate quiz questions from chapter learning objectives using LLM
- Ensure questions cover all learning objectives
- Add difficulty adjustment based on user performance
- Return structured quiz data with questions, answers, explanations

---

### 4. GenerateDiagramBlock

A component that generates visual diagrams from chapter concepts.

**Props:**
- `diagramType?: string` - Optional diagram type identifier
- `chapterId?: number` - Optional chapter ID for context

**Usage in MDX:**
```mdx
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

<GenerateDiagramBlock diagramType="robot-anatomy" chapterId={1} />
```

**Future Enhancement:**
- Generate diagrams using OpenAI vision API or diagram generation library
- Support multiple diagram types (flowcharts, concept maps, architecture diagrams)
- Return diagram URL or base64-encoded image
- Add diagram metadata (title, description, concepts included)

---

## Integration with MDX

All components can be used directly in MDX files by importing them:

```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

# Chapter Content

<AskQuestionBlock chapterId={1} sectionId="section-1" />

More content here...

<ExplainLike10Block concept="autonomy" chapterId={1} />
```

## Current Status

**Scaffolding Phase (Complete):**
- ✅ All 4 components created with minimal UI
- ✅ TypeScript interfaces defined
- ✅ Event handlers with console.log placeholders
- ✅ TODO comments for future AI integration
- ✅ Components integrated in Chapter 1 MDX

**Next Steps:**
- [ ] Integrate with backend API endpoints (`/api/ai/*`)
- [ ] Add RAG pipeline for content retrieval
- [ ] Add OpenAI API calls for AI features
- [ ] Add error handling and loading states
- [ ] Add user authentication and personalization

## Backend API Endpoints

All components will eventually call these backend endpoints:

- `POST /api/ai/ask-question` - Ask questions about chapter content
- `POST /api/ai/explain-like-10` - Generate simplified explanations
- `POST /api/ai/quiz` - Generate interactive quizzes
- `POST /api/ai/diagram` - Generate visual diagrams

See `backend/app/api/ai_blocks.py` for API documentation.

## Development Notes

- All components use inline styles for minimal UI (no external CSS dependencies)
- Components are designed to work standalone without real AI logic (scaffolding phase)
- Event handlers currently log to console; API integration is planned for future features
- Components follow Docusaurus 3.x MDX component patterns

