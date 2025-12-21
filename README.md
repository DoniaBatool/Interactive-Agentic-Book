# 🤖 Physical AI & Humanoid Robotics Textbook

An interactive, multilingual textbook for learning Physical AI and Humanoid Robotics, built with modern web technologies. This project combines Docusaurus for content delivery, BetterAuth for authentication, and FastAPI for backend services.

## ✨ Features

### 🔐 Authentication & User Management
- **Email/Password Authentication**: Secure sign-up and sign-in with email verification
- **Social Login**: OAuth integration with Google and GitHub
- **Password Reset**: Forgot password functionality with email reset links
- **Session Management**: Secure session handling with BetterAuth
- **Admin Panel**: Role-based access control for administrators

### 🌍 Internationalization (i18n)
- **Multi-language Support**: English and Urdu (اردو) translations
- **RTL Support**: Right-to-left layout for Urdu content
- **Language Toggle**: Easy switching between languages
- **Dynamic Content Translation**: Real-time translation of course content

### 🎨 User Experience
- **Scroll Animations**: Smooth fade, slide, and scale animations on scroll
- **Responsive Design**: Mobile-first, works on all screen sizes
- **Modern UI/UX**: Clean, professional interface with smooth interactions
- **Personalization**: User profile customization with learning goals

### 📚 Course Features
- **Interactive Content**: Markdown-based course modules
- **Course Overview**: Comprehensive course structure and outcomes
- **Module-based Learning**: Organized into logical learning modules
- **RAG Chat**: AI-powered chat for course-related queries

## 🛠️ Tech Stack

### Frontend
- **Docusaurus v3**: React-based static site generator
- **TypeScript**: Type-safe development
- **React 19**: Modern React with latest features
- **CSS Modules**: Scoped styling
- **Prism**: Syntax highlighting for code blocks

### Backend Services
- **BetterAuth Server** (Port 8002): Authentication and user management
  - Express.js
  - PostgreSQL for user data
  - Email services (SendGrid/Nodemailer)
- **FastAPI Backend** (Port 8000): RAG, chat, and personalization
  - Python 3.11+
  - PostgreSQL for chat history
  - Qdrant for vector search

### Database
- **PostgreSQL**: Primary database for users, sessions, and chat history

### Development Tools
- **TypeScript**: Type checking
- **Playwright**: End-to-end testing
- **ESBuild**: Fast bundling

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** ≥ 18.0 (recommended: use [nvm](https://github.com/nvm-sh/nvm))
- **npm** (bundled with Node.js)
- **Python** 3.11+ (for FastAPI backend)
- **PostgreSQL** 14+ (for database)
- **Git** (for version control)

### Optional (for production)
- **SendGrid API Key** (for email services)
- **Google OAuth Credentials** (for Google sign-in)
- **GitHub OAuth Credentials** (for GitHub sign-in)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd interactive-agentic-book
```

### 2. Install Frontend Dependencies

```bash
npm install
```

### 3. Install Auth Server Dependencies

```bash
cd auth-server
npm install
cd ..
```

### 4. Install Backend Dependencies

```bash
# Create virtual environment (Windows)
python -m venv venv
.\venv\Scripts\Activate

# Or (Linux/WSL)
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 5. Set Up Database

Create a PostgreSQL database:

```sql
CREATE DATABASE textbook_db;
```

Run migrations (if available) or use the SQL scripts in `auth-server/`:
- `create-tables.sql`: Create initial tables
- `add-role-columns.sql`: Add admin role columns
- `make-admin.sql`: Make a user admin (optional)

## ⚙️ Environment Setup

### Frontend Environment

Create a `.env` file in the root directory (if needed):

```env
# Frontend URL
FRONTEND_URL=http://localhost:3000
```

### Auth Server Environment

Create `auth-server/.env`:

```env
# Server Configuration
AUTH_PORT=8002
BETTER_AUTH_URL=http://localhost:8002
BETTER_AUTH_SECRET=your-secret-key-here-min-32-chars

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/textbook_db

# Frontend URL (for CORS)
FRONTEND_URL=http://localhost:3000

# Email Service (Choose one)
# Option 1: SendGrid
SENDGRID_API_KEY=your-sendgrid-api-key
SENDGRID_FROM_EMAIL=noreply@example.com

# Option 2: Gmail SMTP (for development)
GMAIL_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password

# OAuth Providers (Optional)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
```

### Backend Environment

Create `backend/.env` (if applicable):

```env
DATABASE_URL=postgresql://user:password@localhost:5432/textbook_db
QDRANT_URL=http://localhost:6333
```

## 🏃 Running the Project

### Development Mode

You need **3 separate terminals** to run all services:

#### Terminal 1: Frontend (Docusaurus)

```bash
npm start
```

Frontend will be available at `http://localhost:3000`

#### Terminal 2: Auth Server (BetterAuth)

```bash
cd auth-server
npm run dev
```

Auth server will be available at `http://localhost:8002`

#### Terminal 3: Backend (FastAPI)

**Windows:**
```bash
.\venv\Scripts\Activate
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

**Linux/WSL:**
```bash
source venv/bin/activate
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at `http://localhost:8000/docs`

### Quick Start Scripts

For convenience, you can use the scripts in `scripts/` directory (if available).

## 📁 Project Structure

```
interactive-agentic-book/
├── auth-server/              # BetterAuth authentication server
│   ├── src/
│   │   ├── auth.ts          # BetterAuth configuration
│   │   └── index.ts         # Express server setup
│   ├── package.json
│   └── .env                 # Auth server environment variables
│
├── backend/                  # FastAPI backend (RAG, chat)
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
│
├── docs/                     # Course content (Markdown)
│   ├── course-overview.md
│   └── modules/
│
├── src/                      # Frontend source code
│   ├── components/          # React components
│   │   ├── LanguageToggle.tsx
│   │   ├── TranslatableContent.tsx
│   │   ├── ScrollAnimate.tsx
│   │   ├── UserMenu.tsx
│   │   └── ...
│   ├── context/             # React contexts
│   │   ├── AuthContext.tsx
│   │   └── LanguageContext.tsx
│   ├── pages/               # Custom pages
│   │   ├── index.tsx       # Homepage
│   │   └── auth/           # Auth pages (signup, signin, etc.)
│   ├── css/                # Global styles
│   └── theme/              # Docusaurus theme overrides
│
├── i18n/                    # Internationalization
│   ├── en/                 # English translations
│   └── ur/                 # Urdu translations
│
├── static/                  # Static assets (images, etc.)
├── docusaurus.config.ts    # Docusaurus configuration
├── sidebars.ts             # Sidebar navigation
├── package.json
└── README.md
```

## 🔑 Key Features Explained

### Authentication Flow

1. **Sign Up**: User creates account with email/password or OAuth
2. **Email Verification**: Verification link sent to email (if enabled)
3. **Sign In**: User logs in with credentials
4. **Session**: BetterAuth manages secure sessions
5. **Admin Access**: Admins can access admin panel

### Internationalization

- **Default Language**: English (en)
- **Supported Languages**: English, Urdu (اردو)
- **Translation Files**: Located in `i18n/en/` and `i18n/ur/`
- **RTL Support**: Automatic right-to-left layout for Urdu
- **Language Persistence**: User preference saved in localStorage

### Scroll Animations

The homepage features smooth scroll-triggered animations:
- **Fade Up**: Elements fade in from bottom
- **Fade Left/Right**: Elements slide in from sides
- **Intersection Observer**: Efficient scroll detection

## 🧪 Testing

### Type Checking

```bash
npm run typecheck
```

### Content Structure Validation

```bash
npm test
```

This runs:
- Course structure validation (`tests/check-course-structure.mjs`)
- TypeScript type checking

### End-to-End Testing

```bash
# Install Playwright browsers (first time)
npx playwright install

# Run tests (if available)
npx playwright test
```

## 🏗️ Building for Production

### Build Frontend

```bash
npm run build
```

Output will be in `build/` directory.

### Serve Production Build

```bash
npm run serve
```

### Build Auth Server

```bash
cd auth-server
npm run build
npm run start
```

## 🚢 Deployment

### Frontend Deployment

The frontend can be deployed to:
- **Vercel**: Connect GitHub repo, auto-deploy
- **Netlify**: Connect GitHub repo, auto-deploy
- **GitHub Pages**: Use `npm run deploy`
- **Any static hosting**: Upload `build/` folder

### Auth Server Deployment

Deploy the auth server to:
- **Railway**: Connect GitHub, set environment variables
- **Render**: Connect GitHub, set environment variables
- **Heroku**: Use Procfile, set environment variables
- **VPS**: Use PM2 or systemd for process management

### Environment Variables for Production

Update all environment variables with production URLs:
- `BETTER_AUTH_URL`: Production auth server URL
- `FRONTEND_URL`: Production frontend URL
- `DATABASE_URL`: Production database URL
- OAuth redirect URIs: Update in Google/GitHub OAuth apps

## 👥 Admin Setup

To make a user an admin, run this SQL query:

```sql
UPDATE "user" 
SET 
    "isAdmin" = TRUE,
    "role" = 'admin'
WHERE "email" = 'your-email@example.com';
```

Or use the script: `auth-server/make-admin.sql`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow TypeScript best practices
- Use meaningful commit messages
- Test your changes locally
- Update documentation if needed
- Ensure translations are added for new UI text

## 📝 License

[Add your license here]

## 🙏 Acknowledgments

- [Docusaurus](https://docusaurus.io/) for the documentation framework
- [BetterAuth](https://better-auth.com/) for authentication
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation in `docs/`
- Review `START-SERVERS.md` for server setup help

---

**Built with ❤️ for Physical AI & Humanoid Robotics education**
