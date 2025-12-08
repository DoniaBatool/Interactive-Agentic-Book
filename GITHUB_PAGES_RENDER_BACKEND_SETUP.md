# 🌐 GitHub Pages (Frontend) + Render (Backend) Setup

**Frontend GitHub Pages pe, Backend Render pe - Perfect Combination!**

---

## ✅ Simple Answer

**Haan, bilkul same behavior hoga!**

- ✅ **Aap sirf GitHub Pages URL use karenge** (browser mein)
- ✅ **Frontend automatically Render backend ko call karega**
- ✅ **Aapko kuch extra nahi karna**

---

## 🎯 How It Works

### Current Setup (After Deployment)

```
┌─────────────────────────────────────────────────────────┐
│                    USER (Aap)                            │
│                                                          │
│  Browser mein sirf yeh URL open karo:                   │
│  👉 https://doniabatool.github.io/Interactive-Agentic-Book │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ (User sirf frontend use karta hai)
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│         FRONTEND (GitHub Pages)                          │
│  URL: https://doniabatool.github.io/Interactive-Agentic-Book │
│                                                          │
│  - Homepage                                              │
│  - Chapter pages                                         │
│  - Buttons (Personalization, Translation)                │
│  - Forms (Signup, Login)                                 │
│                                                          │
│  ✅ Configured to call Render backend automatically     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ (Automatic API calls)
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│         BACKEND (Render)                                 │
│  URL: https://ai-robotics-textbook-backend.onrender.com │
│                                                          │
│  - /api/personalize/chapter/1                            │
│  - /api/translation/chapter/1                            │
│  - /auth/signup                                          │
│  - /api/rag/selection                                    │
│                                                          │
│  ✅ CORS configured to accept GitHub Pages requests      │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 Configuration Required

### Step 1: Frontend Configuration (GitHub Pages)

**File**: `frontend/src/config/api.ts`

**Already configured!** Yeh file automatically:
- Development mein: `http://localhost:8000` use karegi
- Production mein: Environment variable check karegi

**GitHub Pages Deployment ke liye:**

**Option A: Build Time Environment Variable** (Recommended)

GitHub Actions ya build script mein:
```bash
REACT_APP_API_URL=https://ai-robotics-textbook-backend.onrender.com npm run build
```

**Option B: Runtime Configuration** (Better for GitHub Pages)

`frontend/src/config/api.ts` already supports `window.API_BASE_URL`:

```html
<!-- frontend/static/index.html (if exists) -->
<script>
  window.API_BASE_URL = 'https://ai-robotics-textbook-backend.onrender.com';
</script>
```

**Option C: Update api.ts for Production** (Easiest)

```typescript
// frontend/src/config/api.ts
const getApiBaseUrl = (): string => {
  // ... existing code ...
  
  // Priority 4: Production - GitHub Pages
  if (typeof window !== 'undefined') {
    // If on GitHub Pages, use Render backend
    if (window.location.hostname === 'doniabatool.github.io') {
      return 'https://ai-robotics-textbook-backend.onrender.com';
    }
  }
  
  return '';
};
```

---

### Step 2: Backend Configuration (Render)

**File**: `backend/app/config/settings.py`

**Already configured!** CORS origins include:

```python
cors_origins: list[str] = [
    "http://localhost:3000",  # Development
    "https://doniabatool.github.io",  # GitHub Pages
    "https://doniabatool.github.io/Interactive-Agentic-Book",  # With base path
]
```

**Render Dashboard mein Environment Variable:**

```
CORS_ORIGINS=https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book,http://localhost:3000
```

---

## 📝 Step-by-Step Setup

### Step 1: Deploy Backend to Render

1. **Go to Render Dashboard**
   - Create new Web Service
   - Connect GitHub repository
   - Root Directory: `backend`
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

2. **Set Environment Variables:**
   ```
   CORS_ORIGINS=https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book,http://localhost:3000
   ```

3. **Note Backend URL:**
   ```
   https://ai-robotics-textbook-backend.onrender.com
   ```

### Step 2: Update Frontend for Render Backend

**Option 1: Update api.ts** (Recommended)

```typescript
// frontend/src/config/api.ts
const getApiBaseUrl = (): string => {
  // Priority 1: Environment variable
  if (typeof process !== 'undefined' && process.env) {
    const envApiUrl = process.env.REACT_APP_API_URL;
    if (envApiUrl) return envApiUrl;
  }
  
  // Priority 2: Window variable
  if (typeof window !== 'undefined' && (window as any).API_BASE_URL) {
    return (window as any).API_BASE_URL;
  }
  
  // Priority 3: Development
  if (typeof window !== 'undefined') {
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      return 'http://localhost:8000';
    }
    
    // Priority 4: GitHub Pages → Render Backend
    if (window.location.hostname === 'doniabatool.github.io') {
      return 'https://ai-robotics-textbook-backend.onrender.com';
    }
  }
  
  return '';
};
```

**Option 2: Build Script** (Alternative)

```bash
# Before building for GitHub Pages
export REACT_APP_API_URL=https://ai-robotics-textbook-backend.onrender.com
npm run build
```

### Step 3: Deploy Frontend to GitHub Pages

1. **Build Frontend:**
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy to GitHub Pages:**
   ```bash
   npm run deploy
   # OR
   git push origin main
   # (if GitHub Actions configured)
   ```

3. **Verify:**
   - Visit: `https://doniabatool.github.io/Interactive-Agentic-Book`
   - Open DevTools → Network tab
   - Click any button → Should see requests to Render backend

---

## ✅ Verification Checklist

### Backend (Render) ✅
- [ ] Backend deployed: `https://ai-robotics-textbook-backend.onrender.com`
- [ ] Health check works: `/api/health`
- [ ] CORS configured for GitHub Pages URL
- [ ] API docs accessible: `/docs`

### Frontend (GitHub Pages) ✅
- [ ] Frontend deployed: `https://doniabatool.github.io/Interactive-Agentic-Book`
- [ ] Homepage loads correctly
- [ ] Chapter pages accessible
- [ ] API calls go to Render backend (check Network tab)

### Integration ✅
- [ ] Personalization button → API call to Render backend
- [ ] Translation button → API call to Render backend
- [ ] Signup form → API call to Render backend
- [ ] No CORS errors in browser console

---

## 🎯 Real Example

### User Action:
1. Browser mein open karo:
   ```
   https://doniabatool.github.io/Interactive-Agentic-Book
   ```

2. Chapter 1 pe jao

3. "Personalize" button click karo

### What Happens (Automatic):
```
Frontend (GitHub Pages)
  ↓
  Button Click Event
  ↓
  API Call: POST https://ai-robotics-textbook-backend.onrender.com/api/personalize/chapter/1
  ↓
Backend (Render)
  ↓
  Response: { "message": "Personalized successfully" }
  ↓
Frontend (GitHub Pages)
  ↓
  Success message dikh jata hai
```

**User ko kya dikhega:**
- ✅ Success message
- ✅ Personalization applied
- ❌ Backend URL nahi dikhega (sirf frontend)

---

## 🔍 Testing

### Test 1: Check API Configuration

1. **Open GitHub Pages URL:**
   ```
   https://doniabatool.github.io/Interactive-Agentic-Book
   ```

2. **Open Browser DevTools** (F12)

3. **Go to Console tab:**
   ```javascript
   // Check API base URL
   console.log(window.API_BASE_URL);
   // Should show: https://ai-robotics-textbook-backend.onrender.com
   ```

### Test 2: Check API Calls

1. **Open Network tab** (DevTools)

2. **Click any button** (Personalization, Translation)

3. **Check Network requests:**
   - Should see: `POST https://ai-robotics-textbook-backend.onrender.com/api/...`
   - Status: `200 OK`
   - No CORS errors

### Test 3: Check CORS

1. **Open Console tab** (DevTools)

2. **Click any button**

3. **Check for errors:**
   - ❌ Should NOT see: "CORS policy blocked"
   - ✅ Should see: Successful API calls

---

## 🐛 Troubleshooting

### Issue 1: API Calls Fail

**Error**: `Network Error` or `Failed to fetch`

**Fix:**
1. Check `frontend/src/config/api.ts` has GitHub Pages detection
2. Verify backend URL is correct
3. Check backend is running on Render

### Issue 2: CORS Errors

**Error**: `Access to fetch at ... has been blocked by CORS policy`

**Fix:**
1. Check Render dashboard → Environment variables
2. Verify `CORS_ORIGINS` includes:
   ```
   https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book
   ```
3. Redeploy backend after updating CORS

### Issue 3: API URL Not Set

**Error**: API calls go to wrong URL or fail

**Fix:**
1. Update `frontend/src/config/api.ts` with GitHub Pages detection
2. Rebuild frontend: `npm run build`
3. Redeploy to GitHub Pages: `npm run deploy`

---

## 📊 Comparison: Different Setups

| Setup | Frontend | Backend | User URL |
|-------|----------|---------|----------|
| **Current** | GitHub Pages | Render | `github.io/...` |
| **Render Full** | Render | Render | `frontend.onrender.com` |
| **Local** | localhost:3000 | localhost:8000 | `localhost:3000` |

**All work the same way!** User sirf frontend URL use karta hai.

---

## ✅ Summary

### Question:
**Agar frontend GitHub Pages pe ho aur backend Render pe, to kya same behavior hoga?**

### Answer:
**✅ Haan, bilkul same behavior hoga!**

- ✅ **Aap sirf GitHub Pages URL use karenge**
- ✅ **Frontend automatically Render backend ko call karega**
- ✅ **Aapko kuch extra nahi karna**

### Configuration:
1. **Frontend**: Update `api.ts` to detect GitHub Pages and use Render backend URL
2. **Backend**: Set CORS to allow GitHub Pages domain

### Result:
- User experience: Same (sirf frontend URL)
- Technical: Frontend (GitHub Pages) → Backend (Render)
- Automatic: Sab kuch automatic hai

---

**Perfect Setup! 🎉**

GitHub Pages (free, always on) + Render (free tier) = Best combination!

