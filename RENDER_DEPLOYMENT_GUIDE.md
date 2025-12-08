# Render Deployment Guide - Backend API

**Complete step-by-step guide to deploy FastAPI backend on Render**

---

## 📋 Prerequisites

1. **GitHub Account** - Your code should be on GitHub
2. **Render Account** - Sign up at [render.com](https://render.com) (free tier available)
3. **Backend Code** - Your FastAPI backend in `backend/` folder

---

## 🚀 Step 1: Prepare Backend for Deployment

### 1.1 Verify Files Exist

Make sure these files exist in your `backend/` folder:
- ✅ `requirements.txt` (already created)
- ✅ `render.yaml` (already created)
- ✅ `app/main.py` (your FastAPI app)
- ✅ `pyproject.toml` (optional, but good to have)

### 1.2 Update CORS Settings

The backend needs to allow requests from your GitHub Pages domain.

**File**: `backend/app/config/settings.py`

Make sure CORS origins include your GitHub Pages URL:

```python
cors_origins: list[str] = [
    "http://localhost:3000",  # Development
    "https://doniabatool.github.io",  # Your GitHub Pages URL
    "https://doniabatool.github.io/Interactive-Agentic-Book",  # With base path
]
```

Or set it via environment variable in Render (recommended).

---

## 🎯 Step 2: Deploy to Render

### 2.1 Create New Web Service

1. **Go to Render Dashboard**: [dashboard.render.com](https://dashboard.render.com)
2. **Click "New +"** → **"Web Service"**
3. **Connect Repository**:
   - Select your GitHub repository
   - Choose the repository: `Interactive-Agentic-Book`

### 2.2 Configure Service

**Basic Settings**:
- **Name**: `ai-robotics-textbook-backend` (or any name you prefer)
- **Region**: Choose closest to you (e.g., `Oregon (US West)`)
- **Branch**: `main` (or your default branch)
- **Root Directory**: `backend` ⚠️ **IMPORTANT: Set this to `backend`**
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### 2.3 Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

**Required Variables**:
```
ENVIRONMENT=production
BACKEND_PORT=8000
CORS_ORIGINS=https://doniabatool.github.io,http://localhost:3000
```

**Optional Variables** (add if you have them):
```
OPENAI_API_KEY=your-openai-key
QDRANT_URL=your-qdrant-url
QDRANT_API_KEY=your-qdrant-key
DATABASE_URL=your-neon-db-url
GEMINI_API_KEY=your-gemini-key
```

**Note**: Render provides `$PORT` automatically, don't set it manually.

### 2.4 Deploy

1. Click **"Create Web Service"**
2. Render will:
   - Clone your repo
   - Install dependencies
   - Start your FastAPI app
3. Wait for deployment (usually 2-5 minutes)

### 2.5 Get Your Backend URL

After deployment, Render will give you a URL like:
```
https://ai-robotics-textbook-backend.onrender.com
```

**Save this URL** - you'll need it for frontend configuration!

---

## 🔧 Step 3: Update Frontend API Configuration

### 3.1 Update API Base URL

**File**: `frontend/src/config/api.ts`

The file is already updated to support environment variables. Now you need to set the API URL during build.

### 3.2 Option A: Set During Build (Recommended)

When building for production, set the API URL:

```bash
cd frontend
REACT_APP_API_URL=https://ai-robotics-textbook-backend.onrender.com npm run build
```

Or create a `.env.production` file in `frontend/`:

```env
REACT_APP_API_URL=https://ai-robotics-textbook-backend.onrender.com
```

Then build:
```bash
npm run build
```

### 3.3 Option B: Set in HTML (Alternative)

Add this script tag in `frontend/static/index.html` (if it exists) or in your Docusaurus config:

```html
<script>
  window.API_BASE_URL = 'https://ai-robotics-textbook-backend.onrender.com';
</script>
```

### 3.4 Rebuild and Redeploy Frontend

```bash
cd frontend
npm run build
```

Then commit and push to GitHub. GitHub Pages will automatically rebuild.

---

## ✅ Step 4: Verify Deployment

### 4.1 Test Backend Health

Visit your Render backend URL:
```
https://ai-robotics-textbook-backend.onrender.com/api/health
```

Should return:
```json
{
  "status": "healthy",
  "timestamp": "..."
}
```

### 4.2 Test API Docs

Visit:
```
https://ai-robotics-textbook-backend.onrender.com/docs
```

You should see Swagger UI with all your API endpoints.

### 4.3 Test from Frontend

1. Open your GitHub Pages site
2. Open browser DevTools (F12) → Network tab
3. Click "Personalize" or "Translate" button
4. Check Network tab - should see request to your Render backend URL
5. Should see success response (even if placeholder)

---

## 🐛 Troubleshooting

### Issue: Backend Not Starting

**Check Render Logs**:
1. Go to Render Dashboard
2. Click on your service
3. Click "Logs" tab
4. Look for errors

**Common Fixes**:
- Make sure `Root Directory` is set to `backend`
- Check `Start Command` is correct
- Verify `requirements.txt` exists

### Issue: CORS Errors

**Error**: `Access to fetch at '...' from origin '...' has been blocked by CORS policy`

**Fix**:
1. Go to Render Dashboard → Your Service → Environment
2. Add/Update `CORS_ORIGINS`:
   ```
   https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book,http://localhost:3000
   ```
3. Redeploy

### Issue: 404 on API Calls

**Check**:
1. Backend URL is correct in frontend config
2. API endpoint paths are correct (should start with `/api/`)
3. Backend is actually running (check Render logs)

### Issue: Frontend Not Updating

**Fix**:
1. Clear browser cache
2. Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
3. Check Network tab to see actual API calls

---

## 📊 Render Free Tier Limits

- **Sleep after 15 minutes** of inactivity (wakes up on first request)
- **750 hours/month** free (enough for always-on if you want)
- **512 MB RAM**
- **0.1 CPU**

**Note**: First request after sleep may take 30-60 seconds (cold start).

---

## 🔄 Continuous Deployment

Render automatically deploys when you push to your GitHub branch:
1. Push code to GitHub
2. Render detects changes
3. Automatically rebuilds and redeploys
4. Usually takes 2-5 minutes

---

## 🎯 Next Steps

### Optional: Custom Domain

1. Go to Render Dashboard → Your Service → Settings
2. Click "Custom Domains"
3. Add your domain
4. Update DNS records as instructed

### Optional: Database (Neon)

1. Create Neon database at [neon.tech](https://neon.tech)
2. Get connection string
3. Add to Render Environment Variables:
   ```
   DATABASE_URL=postgresql://user:pass@host/dbname
   ```

### Optional: Qdrant Cloud

1. Create Qdrant cluster at [cloud.qdrant.io](https://cloud.qdrant.io)
2. Get URL and API key
3. Add to Render Environment Variables:
   ```
   QDRANT_URL=https://your-cluster.qdrant.io
   QDRANT_API_KEY=your-api-key
   ```

---

## 📝 Summary

**Backend URL**: `https://ai-robotics-textbook-backend.onrender.com`  
**Frontend URL**: `https://doniabatool.github.io/Interactive-Agentic-Book`

**What Works Now**:
- ✅ Backend API endpoints accessible
- ✅ Personalization button → calls backend
- ✅ Translation button → calls backend
- ✅ Signup form → sends to backend
- ✅ All API calls working (even if placeholder responses)

**Still Placeholder** (but endpoints work):
- ⚠️ Real AI logic (needs API keys)
- ⚠️ Real RAG (needs Qdrant setup)
- ⚠️ Real translation (needs API keys)
- ⚠️ Real authentication (needs BetterAuth setup)

But at least **all buttons and forms will work** and return responses!

---

## 🆘 Need Help?

1. Check Render logs for errors
2. Check browser console for frontend errors
3. Check Network tab to see API calls
4. Verify CORS settings
5. Verify API URL in frontend config

---

**Generated**: 2025-01-27  
**Status**: Ready for Deployment ✅


