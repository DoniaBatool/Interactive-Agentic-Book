# 🧪 Local Testing Guide

**Complete guide to test your project locally without deployment.**

---

## 📋 Prerequisites

- **Node.js** >= 18.0.0
- **Python** >= 3.11
- **pip** (Python package manager)

---

## 🚀 Quick Start (2 Steps)

### Step 1: Start Backend (Terminal 1)

```bash
# Navigate to backend directory
cd backend

# Install dependencies (first time only)
pip install -r requirements.txt
# OR if using pyproject.toml:
pip install -e .

# Start backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Expected Output:**
```
🚀 Starting AI Robotics Textbook API v0.1.0
📍 Environment: development
🔧 Backend Port: 8000
🌐 CORS Origins: ['http://localhost:3000']
```

**Verify Backend:**
- Open browser: http://localhost:8000/docs
- You should see FastAPI Swagger UI
- Test health endpoint: http://localhost:8000/api/health

---

### Step 2: Start Frontend (Terminal 2)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies (first time only)
npm install

# Start frontend development server
npm start
```

**Expected Output:**
```
[INFO] Starting the development server...
[SUCCESS] Docusaurus website is running at: http://localhost:3000/
```

**Verify Frontend:**
- Open browser: http://localhost:3000
- You should see the textbook homepage

---

## ✅ What to Test

### 1. **Backend API Endpoints**

Open http://localhost:8000/docs and test:

- ✅ **Health Check**: `GET /api/health`
- ✅ **Chapters**: `GET /api/chapters` (should return chapter list)
- ✅ **Authentication**: `POST /auth/signup`, `POST /auth/login`
- ✅ **Personalization**: `POST /api/personalize/chapter/{chapter_id}`
- ✅ **Translation**: `POST /api/translation/chapter/{chapter_id}`
- ✅ **RAG**: `POST /api/rag/selection`
- ✅ **Progress**: `GET /api/progress/`, `POST /api/progress/{chapter_id}/start`

### 2. **Frontend UI Components**

Navigate to http://localhost:3000 and test:

#### **Chapter Pages**
- ✅ Go to Chapter 1: http://localhost:3000/docs/chapters/chapter-1
- ✅ Check if **Personalization Button** appears (top right)
- ✅ Check if **Translation Button** appears (top right)
- ✅ Check if AI blocks are visible (Ask Question, Explain Like 10, Quiz, Diagram)

#### **Personalization Button**
1. Click "Personalize" button
2. Fill in the form:
   - Experience Level: Beginner/Intermediate/Advanced
   - Learning Goal: Research/Education/Industry
   - Preferred Depth: Overview/Detailed/Expert
   - Domain Interests: Select multiple
3. Click "Apply Personalization"
4. **Expected**: Success message (placeholder response from backend)

#### **Translation Button**
1. Click "Translate" button
2. Select a language (Urdu, Roman Urdu, Arabic)
3. **Expected**: Success message (placeholder response from backend)

#### **Signup Form**
1. Navigate to signup page (if available) or use API directly
2. Fill in:
   - Email
   - Password
   - Name (optional)
   - **Technical Background** (new field)
   - **Experience Level** (new field)
   - **Learning Goal** (new field)
   - **Preferred Depth** (new field)
   - **Domain Interests** (new field - multiple select)
3. Submit
4. **Expected**: User created message (placeholder response)

#### **AI Blocks** (Placeholder - will show "TODO" responses)
- ✅ **Ask Question Block**: Type a question → Click "Ask"
- ✅ **Explain Like 10 Block**: Click "Explain"
- ✅ **Quiz Block**: Click "Generate Quiz"
- ✅ **Diagram Block**: Enter description → Click "Generate"

### 3. **API Integration**

Open browser **Developer Tools** (F12) → **Network Tab**:

1. Click Personalization button → Check for `POST /api/personalize/chapter/1`
2. Click Translation button → Check for `POST /api/translation/chapter/1`
3. Submit Signup form → Check for `POST /auth/signup`
4. Click any AI block → Check for corresponding API calls

**Expected**: All requests should go to `http://localhost:8000` and return 200 OK (with placeholder responses)

---

## 🔧 Configuration

### Backend Configuration

The backend automatically:
- ✅ Runs on `http://localhost:8000`
- ✅ Allows CORS from `http://localhost:3000`
- ✅ Loads settings from `.env` file (if exists) or uses defaults

**Optional: Create `backend/.env` file:**
```env
# Optional - only if you have real API keys
OPENAI_API_KEY=your_key_here
QDRANT_URL=your_qdrant_url
DATABASE_URL=your_database_url

# CORS (already configured, but you can override)
CORS_ORIGINS=http://localhost:3000

# Backend Port (default: 8000)
BACKEND_PORT=8000
```

### Frontend Configuration

The frontend automatically:
- ✅ Detects `localhost` and uses `http://localhost:8000` as API base URL
- ✅ No configuration needed for local testing

**To verify API URL:**
1. Open browser console (F12)
2. Type: `window.API_BASE_URL` or check Network tab
3. Should show: `http://localhost:8000`

---

## 🐛 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'app'`
```bash
# Solution: Make sure you're in backend directory and install dependencies
cd backend
pip install -r requirements.txt
```

**Problem**: `Port 8000 already in use`
```bash
# Solution 1: Kill process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Solution 2: Use different port
uvicorn app.main:app --host 0.0.0.0 --port 8001
# Then update frontend/src/config/api.ts to use port 8001
```

**Problem**: `CORS error in browser`
- ✅ Check backend is running on port 8000
- ✅ Check frontend is running on port 3000
- ✅ Verify `backend/app/config/settings.py` has `cors_origins` including `http://localhost:3000`

### Frontend Issues

**Problem**: `npm start` fails
```bash
# Solution: Clear cache and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

**Problem**: API calls fail with `Network Error`
- ✅ Check backend is running: http://localhost:8000/docs
- ✅ Check browser console for CORS errors
- ✅ Verify `frontend/src/config/api.ts` returns `http://localhost:8000` in dev mode

**Problem**: Buttons don't appear on chapter pages
- ✅ Check if components are imported in `chapter-1.mdx`, `chapter-2.mdx`, `chapter-3.mdx`
- ✅ Check browser console for import errors

### API Integration Issues

**Problem**: API returns 404
- ✅ Check endpoint exists in `backend/app/main.py` (router included)
- ✅ Check endpoint path matches frontend call (e.g., `/api/personalize/chapter/1`)

**Problem**: API returns placeholder responses
- ✅ **This is expected!** All endpoints return placeholder data
- ✅ Check backend logs to see if request was received
- ✅ Real implementation will be added later

---

## 📊 Testing Checklist

### Backend ✅
- [ ] Backend starts without errors
- [ ] Health endpoint works: http://localhost:8000/api/health
- [ ] Swagger UI accessible: http://localhost:8000/docs
- [ ] All routers registered (check startup logs)
- [ ] CORS configured for localhost:3000

### Frontend ✅
- [ ] Frontend starts without errors
- [ ] Homepage loads: http://localhost:3000
- [ ] Chapter pages accessible
- [ ] Personalization button visible and clickable
- [ ] Translation button visible and clickable
- [ ] Signup form accessible (if route exists)
- [ ] AI blocks visible on chapter pages

### Integration ✅
- [ ] Personalization button → API call succeeds
- [ ] Translation button → API call succeeds
- [ ] Signup form → API call succeeds
- [ ] AI blocks → API calls succeed (placeholder responses)
- [ ] No CORS errors in browser console
- [ ] Network tab shows requests to `http://localhost:8000`

---

## 🎯 Expected Behavior

### ✅ What Works (Placeholder Mode)
- All UI components render
- All buttons are clickable
- All API calls are made
- Backend receives requests
- Backend returns placeholder responses
- No errors in console (except expected "TODO" messages)

### ⚠️ What's Placeholder (Expected)
- Authentication returns fake user data
- Personalization returns success message only
- Translation returns success message only
- RAG returns placeholder responses
- AI blocks return "TODO" responses
- Progress tracking returns mock data

### ❌ What Doesn't Work Yet (To Be Implemented)
- Real authentication (login/signup)
- Real personalization logic
- Real translation logic
- Real RAG retrieval
- Real AI responses
- Real progress persistence

---

## 🚀 Next Steps After Local Testing

1. **Verify all endpoints respond** (even with placeholders)
2. **Check UI components render** correctly
3. **Test API integration** (Network tab)
4. **Fix any CORS or routing issues**
5. **Ready for deployment** when real logic is implemented

---

## 📝 Quick Commands Reference

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Frontend
cd frontend
npm install
npm start

# Check backend health
curl http://localhost:8000/api/health

# Check backend docs
# Open: http://localhost:8000/docs
```

---

## 💡 Tips

1. **Keep both terminals open** - Backend in one, Frontend in another
2. **Use `--reload` flag** for backend auto-reload on code changes
3. **Check browser console** (F12) for frontend errors
4. **Check backend logs** in terminal for API requests
5. **Use Swagger UI** (http://localhost:8000/docs) to test APIs directly

---

**Happy Testing! 🎉**

