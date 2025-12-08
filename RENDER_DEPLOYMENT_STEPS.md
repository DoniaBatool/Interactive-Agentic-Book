# 🚀 Render Deployment - Quick Steps

**Step-by-step guide to deploy Frontend + Backend on Render**

---

## ✅ Step 1: Prepare Files

### 1.1 Root `render.yaml` Already Created ✅
- File: `render.yaml` (root directory)
- Contains both backend and frontend services

### 1.2 Update Docusaurus Config (Optional)

**Option A: Keep GitHub Pages Config** (Recommended)
- Current config works for GitHub Pages
- For Render, we'll use environment variables

**Option B: Create Render-Specific Config**
- Copy `frontend/docusaurus.config.render.ts` to `frontend/docusaurus.config.ts`
- Only if you want to deploy ONLY on Render (not GitHub Pages)

**Recommended**: Keep current config, use environment variables in Render.

---

## 🎯 Step 2: Deploy Using Blueprint (Easiest)

### 2.1 Push to GitHub

```bash
git add render.yaml
git commit -m "Add Render Blueprint for full stack deployment"
git push origin main
```

### 2.2 Deploy on Render

1. **Go to Render Dashboard**
   - Visit: [dashboard.render.com](https://dashboard.render.com)
   - Sign up / Login

2. **Create Blueprint**
   - Click **"New +"** → **"Blueprint"**
   - Connect GitHub account
   - Select repository: `Interactive-Agentic-Book`
   - Render will detect `render.yaml` automatically

3. **Review Services**
   - ✅ Backend: `ai-robotics-textbook-backend`
   - ✅ Frontend: `ai-robotics-textbook-frontend`
   - Click **"Apply"**

4. **Wait for Deployment**
   - Backend: ~5-10 minutes (first time)
   - Frontend: ~3-5 minutes (first time)
   - You'll see build logs in real-time

---

## 🔧 Step 3: Configure Environment Variables

### 3.1 Backend Service

Go to **Backend Service** → **Environment** tab:

**Required:**
```
CORS_ORIGINS=https://ai-robotics-textbook-frontend.onrender.com,http://localhost:3000
```

**Optional (if you have):**
```
OPENAI_API_KEY=your_key_here
QDRANT_URL=your_qdrant_url
DATABASE_URL=your_neon_database_url
```

**Note**: After frontend deploys, update `CORS_ORIGINS` with actual frontend URL.

### 3.2 Frontend Service

Go to **Frontend Service** → **Environment** tab:

**Required:**
```
REACT_APP_API_URL=https://ai-robotics-textbook-backend.onrender.com
```

**Note**: After backend deploys, update `REACT_APP_API_URL` with actual backend URL.

---

## 🔄 Step 4: Update URLs After Deployment

### 4.1 Get Your URLs

After deployment completes:

- **Backend URL**: `https://ai-robotics-textbook-backend.onrender.com`
- **Frontend URL**: `https://ai-robotics-textbook-frontend.onrender.com`

### 4.2 Update Backend CORS

1. Go to **Backend Service** → **Environment**
2. Update `CORS_ORIGINS`:
   ```
   https://ai-robotics-textbook-frontend.onrender.com,http://localhost:3000
   ```
3. Save (auto-redeploys)

### 4.3 Update Frontend API URL

1. Go to **Frontend Service** → **Environment**
2. Update `REACT_APP_API_URL`:
   ```
   https://ai-robotics-textbook-backend.onrender.com
   ```
3. Go to **Manual Deploy** → **Deploy latest commit**

---

## ✅ Step 5: Verify Deployment

### 5.1 Test Backend

1. **Health Check:**
   ```
   https://ai-robotics-textbook-backend.onrender.com/api/health
   ```
   Expected: `{"status":"healthy"}`

2. **API Docs:**
   ```
   https://ai-robotics-textbook-backend.onrender.com/docs
   ```
   Expected: Swagger UI opens

### 5.2 Test Frontend

1. **Homepage:**
   ```
   https://ai-robotics-textbook-frontend.onrender.com
   ```
   Expected: Homepage loads

2. **Chapter 1:**
   ```
   https://ai-robotics-textbook-frontend.onrender.com/docs/chapters/chapter-1
   ```
   Expected: Chapter content loads

### 5.3 Test Integration

1. Open frontend in browser
2. Open **Developer Tools** (F12) → **Network Tab**
3. Click **Personalization Button**
4. Check Network tab → Should see request to backend
5. Check for CORS errors in Console

---

## 🐛 Common Issues & Fixes

### Issue 1: Backend Build Fails

**Error**: `ModuleNotFoundError: No module named 'app'`

**Fix**:
- Check `rootDir: backend` in render.yaml
- Verify `backend/app/main.py` exists
- Check build logs for exact error

### Issue 2: Frontend Build Fails

**Error**: `Cannot find module` or build errors

**Fix**:
- Check `rootDir: frontend` in render.yaml
- Verify `frontend/package.json` exists
- Check Node version (should be 18+)
- Review build logs

### Issue 3: CORS Errors

**Error**: `Access to fetch at ... has been blocked by CORS policy`

**Fix**:
1. Check backend `CORS_ORIGINS` includes exact frontend URL
2. Include protocol: `https://` not just domain
3. No trailing slashes
4. Redeploy backend after updating CORS

### Issue 4: API Calls Fail

**Error**: `Network Error` or `Failed to fetch`

**Fix**:
1. Check `REACT_APP_API_URL` is set correctly in frontend
2. Verify backend URL is accessible
3. Check backend logs for errors
4. Redeploy frontend after updating API URL

### Issue 5: Frontend Shows 404

**Error**: Blank page or 404 errors

**Fix**:
- Check `baseUrl` in `docusaurus.config.ts`
- For Render, should be `/` (not `/Interactive-Agentic-Book/`)
- Rebuild frontend

---

## 📝 Quick Reference

### Backend Service
- **Name**: `ai-robotics-textbook-backend`
- **Type**: Web Service
- **Root**: `backend/`
- **Build**: `pip install -r requirements.txt`
- **Start**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Frontend Service
- **Name**: `ai-robotics-textbook-frontend`
- **Type**: Web Service
- **Root**: `frontend/`
- **Build**: `npm install && npm run build`
- **Start**: `npx serve -s build -l $PORT`

### Environment Variables

**Backend:**
```
CORS_ORIGINS=https://ai-robotics-textbook-frontend.onrender.com,http://localhost:3000
```

**Frontend:**
```
REACT_APP_API_URL=https://ai-robotics-textbook-backend.onrender.com
```

---

## 🎯 Next Steps

1. ✅ Deploy both services
2. ✅ Update CORS and API URLs
3. ✅ Test all endpoints
4. ✅ Test UI components
5. ✅ Verify integration works

---

**Deployment Complete! 🎉**

Agar koi problem aaye, Render dashboard mein logs check karo ya detailed guide dekho: `RENDER_FULL_STACK_DEPLOYMENT.md`

