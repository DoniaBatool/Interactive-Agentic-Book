<!--
SYNC IMPACT REPORT
Version: 0.0.0 → 1.0.0
Rationale: Initial constitution creation for AI-Native Physical AI & Robotics Textbook hackathon project

Modified Principles: N/A (initial creation)
Added Sections:
  - Core Principles (6 comprehensive principles)
  - AI Architecture Rules
  - Security & Authentication Requirements
  - Development Workflow
  - Governance

Removed Sections: N/A

Templates Status:
  ✅ .specify/templates/plan-template.md - validated, includes "Constitution Check" gate
  ✅ .specify/templates/spec-template.md - validated, TDD acceptance scenarios aligned
  ⚠️  .specify/templates/tasks-template.md - validated, NOTE: line 11 states "Tests are OPTIONAL" but Constitution Principle VI mandates TDD (NON-NEGOTIABLE). Template should be updated in future to reflect mandatory testing, but structure is otherwise aligned.
  ✅ .specify/templates/phr-template.prompt.md - aligned
  ✅ CLAUDE.md - primary source

Follow-up TODOs:
  - Consider updating tasks-template.md line 11 to mandate TDD instead of optional tests
  - Update all command files to reference this constitution for compliance checks
-->

# AI-Native Physical AI & Robotics Textbook Constitution

## Core Principles

### I. AI-Native Spec-Driven Development (NON-NEGOTIABLE)

ALL development MUST follow the Spec-Driven Development (SDD) methodology as taught at
https://ai-native.panaversity.org/. Every feature begins with structured specifications
created using Claude Code + Spec-Kit Plus workflow:

1. **Constitution First**: Establish project principles and constraints
2. **Specification**: Capture requirements in `specs/<feature>/spec.md`
3. **Architecture Planning**: Design decisions in `specs/<feature>/plan.md`
4. **Task Generation**: Testable implementation tasks in `specs/<feature>/tasks.md`
5. **TDD Implementation**: Red-Green-Refactor cycle with user approval gates

No code may be written without corresponding spec.md and plan.md artifacts. Claude Code
Subagents and Reusable Skills MUST be leveraged for all repetitive automation tasks.
Prompt History Records (PHRs) are mandatory for every development interaction.

**Rationale**: Ensures AI-assisted development is traceable, reproducible, and aligned
with hackathon requirements. Prevents scope creep and enables systematic quality gates.

### II. Docusaurus-First Documentation Strategy

The textbook MUST be built using Docusaurus as the primary documentation platform. All
content creation, organization, and rendering follows Docusaurus best practices:

- **Markdown-Native**: All educational content written in MDX format with React components
- **Structured Navigation**: Sidebar organization reflects learning progression and topic hierarchy
- **Version Control**: Content versioned alongside code in git repository
- **Static Generation**: Full static site generation for optimal performance and GitHub Pages deployment
- **Component-Based**: Reusable React components for interactive elements, code examples, diagrams
- **SEO Optimized**: Metadata, sitemap generation, and semantic HTML structure
- **Mobile-First**: Responsive design ensuring accessibility across devices

Docusaurus configuration MUST support plugin architecture for custom features including
the RAG chatbot integration, personalization engine, and translation system.

**Rationale**: Docusaurus provides production-ready documentation infrastructure with
React ecosystem integration, enabling rapid development while maintaining professional
quality and extensibility for AI-powered features.

### III. RAG-First Chatbot Architecture (NON-NEGOTIABLE)

The embedded AI chatbot MUST use Retrieval-Augmented Generation (RAG) as the foundational
architecture pattern. The system stack is strictly defined:

**Required Technology Stack:**
- **Backend**: FastAPI (Python) for REST API endpoints and WebSocket support
- **Vector Database**: Qdrant for semantic search and embedding storage
- **Relational Database**: Neon Serverless Postgres for user data, chat history, personalization profiles
- **AI Framework**: OpenAI Agents API + ChatKit for conversation management
- **Embedding Model**: OpenAI text-embedding-3-small or text-embedding-3-large
- **LLM**: GPT-4o or GPT-4o-mini for generation with streaming support

**RAG Pipeline Requirements:**
1. Document ingestion: Chunk textbook content with metadata (chapter, section, difficulty level)
2. Embedding generation: Vector embeddings stored in Qdrant with appropriate indexes
3. Query processing: User questions embedded and semantic search executed
4. Context retrieval: Top-K relevant chunks retrieved with metadata filtering
5. Prompt construction: System prompt + retrieved context + user question + personalization data
6. Response generation: Streaming responses with source citations
7. Feedback loop: User interactions stored for improving retrieval quality

All chatbot responses MUST cite source chapters/sections. The RAG system MUST support
user-specific context filtering based on authentication state and personalization profile.

**Rationale**: RAG ensures factual accuracy grounded in textbook content, reduces
hallucinations, enables transparent sourcing, and supports continuous content updates
without model retraining.

### IV. Personalization & User-Centric Design

Every logged-in user MUST experience personalized content rendering based on their
background, experience level, and learning preferences. Personalization is powered by
BetterAuth authentication with extended user profiling:

**User Profile Data Collection:**
- Technical background (student, professional, researcher, hobbyist)
- Prior experience level (beginner, intermediate, advanced)
- Learning goals (academic, career transition, hobby, research)
- Preferred depth (high-level overview, detailed technical, research-level)
- Domain interests (hardware, software, AI algorithms, applications)

**Personalization Rules:**
1. **Content Adaptation**: Chapter sections dynamically adjust detail level based on user experience
2. **Example Selection**: Code examples and case studies matched to user's background
3. **Prerequisite Handling**: Advanced concepts show/hide prerequisites based on user knowledge
4. **Pacing Recommendations**: Learning path suggestions tailored to user goals
5. **Progress Tracking**: User-specific bookmarks, completion status, quiz results
6. **Chatbot Context**: AI assistant aware of user profile for contextual responses

**Implementation Requirements:**
- BetterAuth handles authentication with custom profile fields in Neon Postgres
- Signup flow MUST ask personalization questions before account creation
- User data encrypted at rest and in transit (see Security Requirements section)
- Personalization settings editable in user dashboard
- Default anonymous experience available with generic content for non-logged-in users

**Rationale**: Personalized learning significantly improves engagement, retention, and
learning outcomes. Capturing user context enables adaptive difficulty and relevant
examples, making the textbook valuable for diverse audiences from beginners to experts.

### V. Multilingual Support with On-Demand Translation

The textbook MUST support on-demand Urdu translation for all content to serve the
Pakistani educational market and global Urdu-speaking learners. Translation is
user-controlled and dynamically generated:

**Translation Architecture:**
- **Primary Language**: English (source content)
- **Secondary Language**: Urdu (on-demand translation)
- **Translation Engine**: OpenAI GPT-4o with specialized prompts for technical terminology
- **Caching Strategy**: Translated content cached per chapter/section in Neon Postgres
- **Quality Assurance**: Technical terms preserved in English with Urdu explanations
- **User Control**: Per-user language preference toggle with instant switching

**Translation Requirements:**
1. **Preserve Formatting**: Markdown structure, code blocks, and React components unchanged
2. **Technical Accuracy**: Domain-specific terms (robotics, AI, sensors) handled consistently
3. **Code Comments**: Code snippets optionally translated while preserving syntax
4. **Mathematical Notation**: LaTeX equations remain unchanged with Urdu context explanations
5. **Cultural Localization**: Examples and case studies adapted for regional relevance where appropriate

**Implementation Details:**
- Translation triggered on first user request per chapter
- Subsequent users receive cached translations (reducing API costs)
- Translation quality feedback mechanism for continuous improvement
- Admin dashboard for reviewing and editing machine translations
- Fallback to English if translation fails

**Rationale**: Urdu is spoken by 230+ million people globally. Providing native language
support significantly increases accessibility, comprehension, and adoption in Pakistan,
India, and diaspora communities, aligning with inclusive education goals.

### VI. Test-Driven Quality Gates (NON-NEGOTIABLE)

ALL features MUST pass comprehensive quality gates before deployment. Testing follows
strict Test-Driven Development (TDD) with Red-Green-Refactor cycles and multiple
validation layers:

**TDD Workflow (Mandatory):**
1. **Test First**: Write acceptance tests in `tasks.md` before implementation
2. **User Approval**: Obtain explicit user sign-off on test cases
3. **Red Phase**: Run tests to verify failure
4. **Green Phase**: Implement minimal code to pass tests
5. **Refactor Phase**: Improve code quality while maintaining green tests

**Quality Gate Layers:**

**Layer 1: Unit Testing**
- Backend: pytest with 80%+ code coverage (FastAPI routes, RAG pipeline, auth)
- Frontend: Jest + React Testing Library for components
- Database: Postgres transaction tests with rollback
- Vector DB: Qdrant query accuracy validation

**Layer 2: Integration Testing**
- API contract tests (OpenAPI schema validation)
- RAG pipeline end-to-end tests (embedding → retrieval → generation)
- Authentication flow tests (signup, login, session management)
- Translation pipeline tests (English → Urdu → cache)
- Personalization engine tests (profile → content adaptation)

**Layer 3: End-to-End Testing**
- Playwright for critical user journeys (signup, chapter navigation, chatbot interaction)
- Cross-browser compatibility (Chrome, Firefox, Safari)
- Mobile responsiveness validation
- Performance budgets (Lighthouse scores: Performance > 90, Accessibility > 95)

**Layer 4: Manual Review Gates**
- Code review required for all PRs (2 approvals minimum for main branch)
- Content review for accuracy (subject matter expert validation)
- UI/UX review for design consistency
- Security review for authentication and data handling

**Continuous Integration:**
- GitHub Actions for automated testing on every PR
- Deployment blocked on failing tests
- Staging environment for pre-production validation
- Rollback procedures documented and tested

**Rationale**: Quality gates prevent regressions, ensure reliability, maintain user trust,
and enable rapid iteration without breaking existing functionality. TDD enforces clarity
of requirements and reduces debugging time.

## AI Architecture Rules

### Claude Code Subagents & Reusable Skills

ALL repetitive development tasks MUST leverage Claude Code automation:

**Mandatory Automation Targets:**
- Spec generation from user requirements
- Task list creation from architecture plans
- Test case generation from acceptance criteria
- Documentation generation from code
- ADR creation from architectural decisions
- PHR creation from development sessions

**Subagent Guidelines:**
- Create specialized subagents for domain-specific tasks (RAG pipeline, translation, auth)
- Encapsulate complex workflows in reusable skills
- Version control subagent definitions in `.specify/subagents/`
- Document skill usage in `docs/development/skills-guide.md`

### AgentKit + OpenAI ChatKit Integration

The RAG chatbot MUST use AgentKit as the orchestration layer with OpenAI ChatKit
for conversation management:

**AgentKit Responsibilities:**
- Multi-agent orchestration (retrieval agent, generation agent, feedback agent)
- Tool calling for external integrations (Qdrant, Postgres, translation API)
- State management across conversation turns
- Error handling and graceful degradation

**ChatKit Responsibilities:**
- Conversation history management
- Message threading and context window optimization
- Streaming response handling
- Token usage tracking and optimization

**Integration Contract:**
```
User Query → AgentKit Router → [
  Retrieval Agent (Qdrant search) →
  Context Agent (personalization filter) →
  Generation Agent (OpenAI GPT-4o) →
  Citation Agent (source linking)
] → ChatKit Response Manager → Streamed Response
```

### AI Model Usage Policies

**LLM Selection Matrix:**
- **Content Generation**: GPT-4o (high quality, creativity)
- **Chatbot Responses**: GPT-4o-mini (cost-effective, low latency)
- **Translation**: GPT-4o (nuanced technical translation)
- **Embeddings**: text-embedding-3-large (superior retrieval accuracy)
- **Classification**: GPT-4o-mini (user intent, sentiment analysis)

**Cost Optimization:**
- Cache embeddings in Qdrant (avoid regeneration)
- Cache translations in Postgres (per chapter/section)
- Use prompt caching for system prompts
- Implement rate limiting (100 requests/minute/user)
- Monitor token usage with alerts at 80% of budget

**Prompt Engineering Standards:**
- System prompts versioned in `prompts/` directory
- Use few-shot examples for consistent formatting
- Chain-of-thought prompting for complex reasoning
- Output format specifications in JSON schema
- Validate LLM outputs with Pydantic models

## Security & Authentication Requirements

### BetterAuth Integration

User authentication MUST use BetterAuth with the following configuration:

**Authentication Features:**
- **Email/Password**: Primary authentication method with secure password hashing (bcrypt)
- **OAuth Providers**: Google, GitHub for social login
- **Session Management**: JWT tokens with refresh token rotation
- **MFA Support**: Optional two-factor authentication via TOTP
- **Password Reset**: Secure email-based password recovery flow
- **Email Verification**: Required before account activation

**Extended User Profile Schema:**
```typescript
interface UserProfile {
  id: string;
  email: string;
  emailVerified: boolean;
  createdAt: Date;
  updatedAt: Date;

  // Personalization fields
  fullName: string;
  technicalBackground: 'student' | 'professional' | 'researcher' | 'hobbyist';
  experienceLevel: 'beginner' | 'intermediate' | 'advanced';
  learningGoals: string[];
  preferredDepth: 'overview' | 'detailed' | 'research';
  domainInterests: string[];
  languagePreference: 'english' | 'urdu';

  // Privacy settings
  profileVisibility: 'public' | 'private';
  analyticsConsent: boolean;
  marketingConsent: boolean;
}
```

**Session Security:**
- Token expiration: 1 hour (access), 30 days (refresh)
- Automatic session refresh on user activity
- Device tracking for suspicious login detection
- Force logout on password change
- CSRF protection on all state-changing operations

### Data Protection & Privacy

**Encryption Requirements:**
- **In Transit**: TLS 1.3 for all HTTPS connections
- **At Rest**: AES-256 encryption for sensitive user data in Postgres
- **API Keys**: Environment variables, never in code, use secret management (e.g., GitHub Secrets)
- **Database Credentials**: Neon Serverless Postgres connection strings in `.env` only

**Data Privacy Compliance:**
- GDPR compliance for EU users (data export, right to deletion)
- User data minimization (collect only necessary profile information)
- Clear privacy policy and terms of service
- Cookie consent banner for analytics tracking
- User dashboard for data management (view, edit, delete account)

**PII Handling:**
- Email addresses hashed in logs
- User queries to chatbot NOT stored without explicit consent
- Personalization data isolated per user (no cross-user data leakage)
- Audit logs for admin access to user data

### API Security

**Backend API Protection:**
- Rate limiting: 100 requests/minute per user, 1000/minute globally
- API key authentication for service-to-service calls
- Input validation with Pydantic schemas on all endpoints
- SQL injection prevention (parameterized queries via SQLAlchemy)
- XSS protection (content security policy headers)
- CORS configuration (whitelist frontend domain only)

**Chatbot Security:**
- Prompt injection detection (filter malicious user inputs)
- Content filtering (block inappropriate queries)
- Source verification (citations link only to textbook content)
- Output validation (sanitize LLM responses before rendering)

### Secrets Management

**Required Secrets:**
- `OPENAI_API_KEY`: OpenAI API access
- `QDRANT_URL`, `QDRANT_API_KEY`: Vector database
- `DATABASE_URL`: Neon Postgres connection
- `BETTERAUTH_SECRET`: Session encryption key
- `SMTP_CREDENTIALS`: Email service for verification/password reset

**Management Protocol:**
- Development: `.env.local` (git-ignored)
- Staging/Production: GitHub Secrets or Vercel Environment Variables
- Rotation schedule: API keys rotated every 90 days
- Access control: Secrets accessible only to deployment pipeline and authorized developers
- Audit trail: Log all secret access attempts

## Development Workflow

### Pre-Implementation Checklist

Before writing any code, developers MUST:

1. **Verify Specification Exists**: Ensure `specs/<feature>/spec.md` is complete and approved
2. **Review Architecture Plan**: Study `specs/<feature>/plan.md` for design decisions
3. **Understand Tasks**: Read `specs/<feature>/tasks.md` with acceptance criteria
4. **Confirm Test Cases**: Verify test scenarios are comprehensive and approved
5. **Check Dependencies**: Identify external dependencies and integration points
6. **Review Constitution**: Confirm planned approach aligns with all principles

### Implementation Contract

For every implementation task:

1. **Red Phase**: Write tests first, run to verify failure
2. **Communicate**: Report test results to user, obtain approval to proceed
3. **Green Phase**: Implement minimal code to pass tests
4. **Verify**: Run tests again to confirm green status
5. **Refactor**: Improve code quality while maintaining test success
6. **Document**: Update relevant documentation (README, API docs, comments)
7. **Create PHR**: Generate Prompt History Record for the session
8. **Suggest ADR**: If architectural decision made, propose ADR creation

### Post-Implementation Actions

After completing implementation:

1. **Run Full Test Suite**: Ensure no regressions introduced
2. **Update Specs**: Mark tasks as complete in `tasks.md`
3. **Update Documentation**: Sync README, API docs, user guides
4. **Create PHR**: Document the development session
5. **Commit Changes**: Following git commit message conventions
6. **Open Pull Request**: With comprehensive description and test evidence
7. **Request Review**: Tag appropriate reviewers

## Governance

### Constitutional Authority

This constitution is the **highest authority** for all development practices, architectural
decisions, and quality standards. In case of conflicts:

1. **Constitution > All Other Documents**: This document supersedes CLAUDE.md, templates,
   command files, and any other project guidance
2. **Principles Are Non-Negotiable**: Sections marked (NON-NEGOTIABLE) cannot be
   bypassed without constitutional amendment
3. **Deviations Require Justification**: Any deviation must be explicitly documented
   in PR description with reasoning and risk assessment
4. **Compliance Verification**: All PRs reviewed for constitutional compliance before merge

### Amendment Procedure

Constitution amendments follow strict semantic versioning and approval process:

**Version Increment Rules:**
- **MAJOR (X.0.0)**: Backward-incompatible changes (principle removal/redefinition, architecture pivot)
- **MINOR (x.Y.0)**: Additions (new principles, new sections, expanded requirements)
- **PATCH (x.y.Z)**: Clarifications (typo fixes, wording improvements, example additions)

**Amendment Workflow:**
1. **Proposal**: Document proposed change with rationale in GitHub issue
2. **Impact Analysis**: Identify affected templates, code, documentation
3. **Review**: Minimum 2 stakeholder approvals required
4. **Update Constitution**: Apply changes with version bump and sync impact report
5. **Propagate Changes**: Update all dependent templates and documentation
6. **Validate**: Ensure no broken references or inconsistencies
7. **Communicate**: Announce changes to team with migration guidance if needed

**Required Approvals:**
- PATCH: 1 approval (any core team member)
- MINOR: 2 approvals (including tech lead)
- MAJOR: 3 approvals (including project owner)

### Compliance Review Gates

**Pull Request Requirements:**
- ✅ Linked to spec/task in `specs/<feature>/`
- ✅ TDD cycle followed (tests written first, evidence of red → green)
- ✅ All tests passing (unit, integration, e2e)
- ✅ Code coverage maintained or improved (target: 80%+)
- ✅ No security vulnerabilities (CodeQL scan passes)
- ✅ PHR created in `history/prompts/`
- ✅ ADR created if architectural decision made
- ✅ Documentation updated
- ✅ No secrets or credentials in code
- ✅ Performance budgets met (Lighthouse scores)
- ✅ Accessibility standards met (WCAG AA)
- ✅ 2+ code review approvals

**Deployment Requirements:**
- ✅ All tests pass in CI/CD pipeline
- ✅ Staging deployment successful
- ✅ Manual smoke testing completed
- ✅ Performance benchmarks met
- ✅ Security scan clean (no HIGH/CRITICAL vulnerabilities)
- ✅ Database migrations tested (if applicable)
- ✅ Rollback procedure documented

### Quality Evolution

**Continuous Improvement:**
- Constitution reviewed quarterly for relevance and effectiveness
- Metrics tracked: test coverage, deployment frequency, bug escape rate, security incidents
- Retrospectives after major milestones to identify process improvements
- Template updates propagated within 1 week of constitutional changes

**Technical Debt Management:**
- Document known deviations in `docs/technical-debt.md`
- Prioritize debt repayment in quarterly planning
- No new debt without approved justification and repayment plan

### Accountability

**Roles and Responsibilities:**
- **Project Owner**: Constitutional compliance oversight, amendment approvals
- **Tech Lead**: Architecture alignment, code review quality, performance standards
- **Developers**: Principle adherence, TDD discipline, documentation maintenance
- **QA**: Test coverage verification, quality gate enforcement

**Enforcement:**
- PRs not meeting compliance requirements will be blocked from merge
- Repeated violations trigger architecture review and process improvement
- Emergency hotfixes may bypass gates with post-deployment compliance documentation

**Version**: 1.0.0 | **Ratified**: 2025-12-04 | **Last Amended**: 2025-12-04
