# ✅ Backend Render Deployment - Step-by-Step Checklist

**Frontend already deployed on GitHub Pages. Ab backend Render pe deploy karte hain!**

---

## 📋 Prerequisites Check

Before starting, verify:

- [ ] GitHub repository connected to Render account
- [ ] Backend code pushed to GitHub
- [ ] `backend/requirements.txt` exists
- [ ] `backend/app/main.py` exists
- [ ] Render account created (free tier OK)

---

## 🚀 Step 1: Create Web Service on Render

### 1.1 Go to Render Dashboard

1. Visit: [dashboard.render.com](https://dashboard.render.com)
2. Login / Sign up (if not already)

### 1.2 Create New Web Service

1. Click **"New +"** button (top right)
2. Select **"Web Service"**

### 1.3 Connect GitHub Repository

1. **Connect GitHub** (if not connected):
   - Click "Connect GitHub"
   - Authorize Render
   - Select repository: `Interactive-Agentic-Book`
   - Click "Connect"

2. **Select Repository**:
   - Repository: `Interactive-Agentic-Book`
   - Branch: `main` (or your default branch)

---

## ⚙️ Step 2: Configure Backend Service

### 2.1 Basic Settings

Fill in these fields:

- **Name**: `ai-robotics-textbook-backend`
- **Environment**: `Python 3`
- **Region**: Choose closest to you (e.g., `Oregon (US West)`)
- **Branch**: `main` (or your default branch)
- **Root Directory**: `backend` ⚠️ **IMPORTANT!**

### 2.2 Build & Start Commands

- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```

- **Start Command**: 
  ```
  uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

### 2.3 Plan Selection

- **Plan**: `Free` (for now, can upgrade later)

---

## 🔧 Step 3: Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

### Required Variables:

1. **CORS_ORIGINS**
   ```
   https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book,http://localhost:3000
   ```
   ⚠️ **IMPORTANT**: No spaces after commas!

2. **ENVIRONMENT**
   ```
   production
   ```

3. **PYTHON_VERSION** (optional, but recommended)
   ```
   3.11.0
   ```

### Optional Variables (if you have):

4. **OPENAI_API_KEY**
   ```
   your_openai_api_key_here
   ```
   ⚠️ Mark as **"Secret"** (eye icon)

5. **QDRANT_URL**
   ```
   your_qdrant_url_here
   ```

6. **DATABASE_URL**
   ```
   your_neon_database_url_here
   ```

7. **BETTERAUTH_SECRET**
   ```
   your_betterauth_secret_here
   ```

---

## 🚀 Step 4: Deploy

1. **Review Settings**:
   - ✅ Name: `ai-robotics-textbook-backend`
   - ✅ Root Directory: `backend`
   - ✅ Build Command: `pip install -r requirements.txt`
   - ✅ Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - ✅ Environment Variables: CORS_ORIGINS set

2. **Click "Create Web Service"**

3. **Wait for Deployment**:
   - Build: ~5-10 minutes (first time)
   - Deploy: ~1-2 minutes
   - Watch logs in real-time

---

## ✅ Step 5: Verify Deployment

### 5.1 Check Deployment Status

- Status should show: **"Live"** (green)
- URL will be: `https://ai-robotics-textbook-backend.onrender.com`

### 5.2 Test Health Endpoint

Open in browser:
```
https://ai-robotics-textbook-backend.onrender.com/api/health
```

**Expected Response:**
```json
{"status":"healthy"}
```

### 5.3 Test API Docs

Open in browser:
```
https://ai-robotics-textbook-backend.onrender.com/docs
```

**Expected**: Swagger UI should open

---

## 🔗 Step 6: Update Frontend (If Needed)

### 6.1 Verify Frontend Config

Check `frontend/src/config/api.ts`:

```typescript
// Should automatically detect GitHub Pages and use Render backend
if (window.location.hostname === 'doniabatool.github.io') {
  return 'https://ai-robotics-textbook-backend.onrender.com';
}
```

### 6.2 Rebuild Frontend (If Config Changed)

```bash
cd frontend
npm run build
npm run deploy
```

---

## 🧪 Step 7: Test Integration

### 7.1 Open Frontend

1. Go to: `https://doniabatool.github.io/Interactive-Agentic-Book`
2. Open **Developer Tools** (F12)
3. Go to **Network** tab

### 7.2 Test API Calls

1. Navigate to Chapter 1
2. Click **"Personalize"** button
3. Check Network tab:
   - Should see: `POST https://ai-robotics-textbook-backend.onrender.com/api/personalize/chapter/1`
   - Status: `200 OK`

4. Click **"Translate"** button
5. Check Network tab:
   - Should see: `POST https://ai-robotics-textbook-backend.onrender.com/api/translation/chapter/1`
   - Status: `200 OK`

### 7.3 Check Console

- ❌ Should NOT see: CORS errors
- ✅ Should see: Successful API calls

---

## 🐛 Common Issues & Fixes

### Issue 1: Build Fails

**Error**: `ModuleNotFoundError: No module named 'app'`

**Fix**:
1. Check **Root Directory** is set to `backend` (not root)
2. Verify `backend/app/main.py` exists
3. Check build logs for exact error

### Issue 2: Service Won't Start

**Error**: `Application failed to respond`

**Fix**:
1. Check **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
2. Verify `$PORT` is used (Render provides this)
3. Check logs for errors

### Issue 3: CORS Errors

**Error**: `Access to fetch at ... has been blocked by CORS policy`

**Fix**:
1. Go to **Environment** tab
2. Check `CORS_ORIGINS` includes:
   ```
   https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book
   ```
3. No spaces after commas
4. Click **"Save Changes"** (auto-redeploys)

### Issue 4: 404 on Health Endpoint

**Error**: `404 Not Found`

**Fix**:
1. Check `/api/health` endpoint exists in `backend/app/api/health.py`
2. Verify router is included in `backend/app/main.py`
3. Check deployment logs

### Issue 5: Service Sleeps (Free Tier)

**Issue**: First request takes ~30 seconds

**Fix**:
- This is normal for free tier
- Service sleeps after 15 minutes of inactivity
- First request wakes it up (takes ~30 seconds)
- Upgrade to paid ($7/month) for always-on

---

## 📝 Quick Reference

### Backend URL
```
https://ai-robotics-textbook-backend.onrender.com
```

### Important Endpoints
- Health: `/api/health`
- API Docs: `/docs`
- Chapters: `/api/chapters`
- Personalization: `/api/personalize/chapter/{id}`
- Translation: `/api/translation/chapter/{id}`

### Environment Variables (Required)
```
CORS_ORIGINS=https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book,http://localhost:3000
ENVIRONMENT=production
```

---

## ✅ Final Checklist

- [ ] Backend deployed on Render
- [ ] Health endpoint works
- [ ] API docs accessible
- [ ] CORS configured correctly
- [ ] Frontend can call backend (tested)
- [ ] No CORS errors in browser console
- [ ] All API endpoints responding

---

## 🎯 Next Steps

1. ✅ Backend deployed
2. ✅ Tested endpoints
3. ✅ Frontend integration verified
4. 🎉 **Ready to use!**

---

**Deployment Complete! 🎉**

Agar koi problem aaye, mujhe batao - main help karunga!

