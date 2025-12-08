# 🚀 Render Full Stack Deployment Guide

**Complete guide to deploy both Frontend + Backend on Render**

---

## ✅ Can You Deploy Both on Render?

**Bilkul! Haan, aap poora project (Frontend + Backend) Render pe deploy kar sakte hain.**

Render supports:
- ✅ **Web Service** (Backend - FastAPI)
- ✅ **Static Site** (Frontend - Docusaurus)

---

## 📋 Prerequisites

1. **GitHub Account** - Code GitHub pe hona chahiye
2. **Render Account** - Sign up at [render.com](https://render.com) (free tier available)
3. **Project Structure** - Frontend aur Backend alag folders mein

---

## 🎯 Deployment Options

### Option 1: Using Render Blueprint (Recommended - Easiest)

**Single click se dono deploy!**

1. **Push `render.yaml` to GitHub**
   ```bash
   git add render.yaml
   git commit -m "Add Render Blueprint for full stack deployment"
   git push
   ```

2. **Go to Render Dashboard**
   - Visit: [dashboard.render.com](https://dashboard.render.com)
   - Click **"New +"** → **"Blueprint"**
   - Connect your GitHub repository
   - Select the repository: `Interactive-Agentic-Book`
   - Render will automatically detect `render.yaml`

3. **Review Services**
   - Backend: `ai-robotics-textbook-backend`
   - Frontend: `ai-robotics-textbook-frontend`
   - Click **"Apply"**

4. **Configure Environment Variables**
   - Backend service → Environment tab:
     - `CORS_ORIGINS`: Update with frontend URL (after deployment)
     - `OPENAI_API_KEY`: (optional, if you have)
     - `QDRANT_URL`: (optional)
     - `DATABASE_URL`: (optional)
   
   - Frontend service → Environment tab:
     - `REACT_APP_API_URL`: Update with backend URL (after deployment)

5. **Wait for Deployment**
   - Backend: ~5-10 minutes (first time)
   - Frontend: ~3-5 minutes (first time)

6. **Update URLs After Deployment**
   - Backend URL: `https://ai-robotics-textbook-backend.onrender.com`
   - Frontend URL: `https://ai-robotics-textbook-frontend.onrender.com`
   
   **Update CORS in Backend:**
   - Go to Backend service → Environment
   - Update `CORS_ORIGINS`: `https://ai-robotics-textbook-frontend.onrender.com,http://localhost:3000`
   
   **Update API URL in Frontend:**
   - Go to Frontend service → Environment
   - Update `REACT_APP_API_URL`: `https://ai-robotics-textbook-backend.onrender.com`
   - **Redeploy frontend** (Settings → Manual Deploy)

---

### Option 2: Manual Deployment (Step by Step)

#### Step 1: Deploy Backend

1. **Go to Render Dashboard**
   - Click **"New +"** → **"Web Service"**

2. **Connect GitHub**
   - Select your repository: `Interactive-Agentic-Book`
   - Click **"Connect"**

3. **Configure Backend Service**
   - **Name**: `ai-robotics-textbook-backend`
   - **Environment**: `Python 3`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

4. **Environment Variables** (Backend)
   ```
   PYTHON_VERSION=3.11.0
   ENVIRONMENT=production
   BACKEND_PORT=8000
   CORS_ORIGINS=http://localhost:3000
   ```

5. **Deploy**
   - Click **"Create Web Service"**
   - Wait for deployment (~5-10 minutes)
   - Note the URL: `https://ai-robotics-textbook-backend.onrender.com`

#### Step 2: Deploy Frontend

1. **Go to Render Dashboard**
   - Click **"New +"** → **"Web Service"** (yes, Web Service for Docusaurus)

2. **Connect GitHub** (same repo)

3. **Configure Frontend Service**
   - **Name**: `ai-robotics-textbook-frontend`
   - **Environment**: `Node`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npx serve -s build -l $PORT`

4. **Environment Variables** (Frontend)
   ```
   NODE_VERSION=18.20.0
   REACT_APP_API_URL=https://ai-robotics-textbook-backend.onrender.com
   BASE_URL=/
   ```

5. **Update Docusaurus Config** (if needed)
   - For Render, `baseUrl` should be `/` (not `/Interactive-Agentic-Book/`)
   - File: `frontend/docusaurus.config.ts`
   ```typescript
   url: 'https://ai-robotics-textbook-frontend.onrender.com',
   baseUrl: '/',
   ```

6. **Deploy**
   - Click **"Create Web Service"**
   - Wait for deployment (~3-5 minutes)
   - Note the URL: `https://ai-robotics-textbook-frontend.onrender.com`

#### Step 3: Update CORS and API URLs

1. **Update Backend CORS**
   - Go to Backend service → Environment
   - Update `CORS_ORIGINS`:
     ```
     https://ai-robotics-textbook-frontend.onrender.com,http://localhost:3000
     ```
   - Save (auto-redeploys)

2. **Update Frontend API URL** (if not set)
   - Go to Frontend service → Environment
   - Update `REACT_APP_API_URL`: `https://ai-robotics-textbook-backend.onrender.com`
   - Manual Deploy → Deploy latest commit

---

## 🔧 Configuration Updates Needed

### 1. Update Docusaurus Config for Render

**File**: `frontend/docusaurus.config.ts`

**For Render Deployment:**
```typescript
const config: Config = {
  url: 'https://ai-robotics-textbook-frontend.onrender.com',
  baseUrl: '/',  // Changed from '/Interactive-Agentic-Book/'
  // ... rest of config
};
```

**For GitHub Pages (keep this if you want both):**
```typescript
const config: Config = {
  url: 'https://doniabatool.github.io',
  baseUrl: '/Interactive-Agentic-Book/',
  // ... rest of config
};
```

**Solution**: Use environment variable or create separate config files.

### 2. Update Frontend API Configuration

**File**: `frontend/src/config/api.ts`

Already configured to use `REACT_APP_API_URL` environment variable, so no changes needed!

### 3. Update Backend CORS

**File**: `backend/app/config/settings.py`

Already configured to parse `CORS_ORIGINS` from environment variable, so no changes needed!

---

## ✅ Verification Checklist

### Backend ✅
- [ ] Backend deployed: `https://ai-robotics-textbook-backend.onrender.com`
- [ ] Health check works: `https://ai-robotics-textbook-backend.onrender.com/api/health`
- [ ] API docs accessible: `https://ai-robotics-textbook-backend.onrender.com/docs`
- [ ] CORS configured for frontend URL

### Frontend ✅
- [ ] Frontend deployed: `https://ai-robotics-textbook-frontend.onrender.com`
- [ ] Homepage loads correctly
- [ ] Chapter pages accessible
- [ ] API calls go to backend URL (check Network tab)

### Integration ✅
- [ ] Personalization button → API call succeeds
- [ ] Translation button → API call succeeds
- [ ] Signup form → API call succeeds
- [ ] No CORS errors in browser console

---

## 🐛 Troubleshooting

### Backend Issues

**Problem**: Backend deployment fails
- ✅ Check `requirements.txt` exists in `backend/` folder
- ✅ Check `app/main.py` exists
- ✅ Check build logs in Render dashboard

**Problem**: CORS errors
- ✅ Update `CORS_ORIGINS` with exact frontend URL
- ✅ Include protocol: `https://` not just domain
- ✅ No trailing slashes

### Frontend Issues

**Problem**: Frontend build fails
- ✅ Check `package.json` exists in `frontend/` folder
- ✅ Check Node version (18+)
- ✅ Check build logs for errors

**Problem**: Frontend shows 404 or blank page
- ✅ Check `baseUrl` in `docusaurus.config.ts` is `/` for Render
- ✅ Check `build` folder is generated correctly

**Problem**: API calls fail
- ✅ Check `REACT_APP_API_URL` is set correctly
- ✅ Check backend URL is accessible
- ✅ Check CORS is configured in backend

---

## 💰 Cost (Free Tier)

**Render Free Tier Includes:**
- ✅ 750 hours/month per service (enough for 24/7)
- ✅ Automatic SSL certificates
- ✅ Custom domains (optional)
- ✅ Auto-deploy on git push

**Limitations:**
- ⚠️ Services sleep after 15 minutes of inactivity (free tier)
- ⚠️ First request after sleep takes ~30 seconds (cold start)
- ⚠️ No persistent storage (use external DB like Neon)

**Upgrade to Paid:**
- $7/month per service for always-on (no sleep)
- Better performance
- More resources

---

## 🎯 Quick Comparison: Render vs GitHub Pages

| Feature | GitHub Pages | Render |
|---------|--------------|--------|
| **Frontend** | ✅ Free, Fast | ✅ Free, Fast |
| **Backend** | ❌ Not supported | ✅ Free tier available |
| **Auto-deploy** | ✅ On push | ✅ On push |
| **Custom Domain** | ✅ Free | ✅ Free |
| **SSL** | ✅ Automatic | ✅ Automatic |
| **Sleep** | ❌ Always on | ⚠️ Sleeps after 15min (free) |

**Recommendation:**
- **Frontend**: GitHub Pages (always on, faster)
- **Backend**: Render (required for API)
- **OR**: Both on Render (simpler, one platform)

---

## 📝 Quick Commands

```bash
# Push render.yaml to GitHub
git add render.yaml
git commit -m "Add Render Blueprint"
git push

# Or update Docusaurus config for Render
# Edit frontend/docusaurus.config.ts
# Change baseUrl from '/Interactive-Agentic-Book/' to '/'
```

---

## 🚀 Next Steps After Deployment

1. **Test Backend**: Visit `https://your-backend.onrender.com/docs`
2. **Test Frontend**: Visit `https://your-frontend.onrender.com`
3. **Update CORS**: Add frontend URL to backend CORS_ORIGINS
4. **Update API URL**: Set REACT_APP_API_URL in frontend
5. **Test Integration**: Click buttons, check Network tab

---

**Happy Deployment! 🎉**

Agar koi problem aaye, Render dashboard mein logs check karo ya mujhe batao!

