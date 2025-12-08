# 🚀 Local Testing - Quick Start

**Bilkul! Aap local system pe sab kuch test kar sakte hain bina deployment ke.**

---

## ⚡ Fastest Way (2 Commands)

### Option 1: Use Batch Script (Windows)

```bash
# Double-click this file or run in terminal:
start-local.bat
```

Ye script automatically:
- ✅ Backend start karega (port 8000)
- ✅ Frontend start karega (port 3000)
- ✅ Dono alag windows mein khulega

---

### Option 2: Manual Start (2 Terminals)

#### Terminal 1: Backend

```bash
cd backend
pip install -r requirements.txt  # Pehli baar hi
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Verify:** http://localhost:8000/docs (Swagger UI)

#### Terminal 2: Frontend

```bash
cd frontend
npm install  # Pehli baar hi
npm start
```

**Verify:** http://localhost:3000 (Homepage)

---

## ✅ Kya Test Kar Sakte Hain

### 1. **Backend API** (http://localhost:8000/docs)

- ✅ Health Check: `GET /api/health`
- ✅ Chapters: `GET /api/chapters`
- ✅ Signup: `POST /auth/signup`
- ✅ Personalization: `POST /api/personalize/chapter/1`
- ✅ Translation: `POST /api/translation/chapter/1`
- ✅ RAG: `POST /api/rag/selection`
- ✅ Progress: `GET /api/progress/`

### 2. **Frontend UI** (http://localhost:3000)

#### Chapter Pages:
- ✅ Chapter 1: http://localhost:3000/docs/chapters/chapter-1
- ✅ **Personalization Button** (top right) - Click karo, form fill karo
- ✅ **Translation Button** (top right) - Language select karo
- ✅ **AI Blocks** - Ask Question, Quiz, Diagram, etc.

#### Signup Form:
- ✅ Technical Background field
- ✅ Experience Level field
- ✅ Learning Goal field
- ✅ Domain Interests (multiple select)

### 3. **API Integration Testing**

Browser mein **F12** press karo → **Network Tab**:

1. Personalization button click → `POST /api/personalize/chapter/1` dikhega
2. Translation button click → `POST /api/translation/chapter/1` dikhega
3. Signup form submit → `POST /auth/signup` dikhega

**Expected:** Sab requests `http://localhost:8000` pe jayenge aur 200 OK milega (placeholder responses)

---

## 🔧 Configuration (Automatic)

### Backend:
- ✅ Port: `8000` (automatic)
- ✅ CORS: `http://localhost:3000` (already configured)
- ✅ API Docs: http://localhost:8000/docs

### Frontend:
- ✅ Port: `3000` (automatic)
- ✅ API URL: `http://localhost:8000` (automatic detection)
- ✅ No config needed!

---

## 🐛 Agar Koi Problem Aaye

### Backend Start Nahi Ho Raha?

```bash
# Check Python version
python --version  # Should be 3.11+

# Install dependencies
cd backend
pip install -r requirements.txt

# Try again
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Start Nahi Ho Raha?

```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

### CORS Error?

- ✅ Backend port 8000 pe chal raha hai?
- ✅ Frontend port 3000 pe chal raha hai?
- ✅ `backend/app/config/settings.py` mein `http://localhost:3000` hai?

### API Calls Fail Ho Rahi Hain?

1. Browser console check karo (F12)
2. Network tab mein request dekho
3. Backend terminal mein logs dekho
4. http://localhost:8000/docs pe ja kar manually test karo

---

## 📊 Testing Checklist

### Backend ✅
- [ ] Backend start ho gaya
- [ ] http://localhost:8000/docs khul raha hai
- [ ] Health endpoint kaam kar raha hai

### Frontend ✅
- [ ] Frontend start ho gaya
- [ ] http://localhost:3000 khul raha hai
- [ ] Chapter pages load ho rahi hain
- [ ] Personalization button dikh raha hai
- [ ] Translation button dikh raha hai

### Integration ✅
- [ ] Personalization button → API call successful
- [ ] Translation button → API call successful
- [ ] Signup form → API call successful
- [ ] No CORS errors in console

---

## 🎯 Expected Results

### ✅ Jo Kaam Karega (Placeholder Mode)
- Sab UI components render honge
- Sab buttons clickable honge
- Sab API calls backend tak jayenge
- Backend placeholder responses dega
- Console mein koi error nahi (except "TODO" messages)

### ⚠️ Jo Placeholder Hai (Expected)
- Authentication fake user data dega
- Personalization success message dega (no real logic)
- Translation success message dega (no real logic)
- RAG placeholder responses dega
- AI blocks "TODO" responses dega

### ❌ Jo Abhi Nahi Kaam Karega (To Be Implemented)
- Real authentication (login/signup)
- Real personalization logic
- Real translation logic
- Real RAG retrieval
- Real AI responses
- Real progress persistence

---

## 💡 Tips

1. **Dono terminals open rakho** - Backend ek mein, Frontend doosre mein
2. **`--reload` flag use karo** - Backend auto-reload hoga code changes pe
3. **Browser console check karo** (F12) - Frontend errors dikhenge
4. **Backend terminal check karo** - API requests dikhenge
5. **Swagger UI use karo** (http://localhost:8000/docs) - Direct API testing

---

## 📝 Quick Commands

```bash
# Backend
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Frontend
cd frontend
npm start

# Check backend health
curl http://localhost:8000/api/health
# OR open: http://localhost:8000/docs
```

---

**Happy Testing! 🎉**

Agar koi problem aaye, `LOCAL_TESTING_GUIDE.md` mein detailed troubleshooting hai.

