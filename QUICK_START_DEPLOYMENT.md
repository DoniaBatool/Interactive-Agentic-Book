# Quick Start: Deploy Backend to Render (5 Minutes) ⚡

**Fastest way to get your backend live**

---

## 🚀 Step 1: Deploy to Render (2 minutes)

1. **Go to**: [dashboard.render.com](https://dashboard.render.com)
2. **Click**: "New +" → "Web Service"
3. **Connect**: Your GitHub repo `Interactive-Agentic-Book`
4. **Configure**:
   - **Name**: `ai-robotics-backend`
   - **Root Directory**: `backend` ⚠️ **IMPORTANT**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. **Environment Variables**:
   - `CORS_ORIGINS` = `https://doniabatool.github.io,http://localhost:3000`
6. **Click**: "Create Web Service"
7. **Wait**: 2-5 minutes for deployment
8. **Copy**: Your backend URL (e.g., `https://ai-robotics-backend.onrender.com`)

---

## 🔧 Step 2: Update Frontend (1 minute)

**Option A: Build with API URL**
```bash
cd frontend
REACT_APP_API_URL=https://your-backend.onrender.com npm run build
git add .
git commit -m "Update API URL for production"
git push
```

**Option B: Create .env.production**
```bash
cd frontend
echo "REACT_APP_API_URL=https://your-backend.onrender.com" > .env.production
npm run build
git add .
git commit -m "Add production API URL"
git push
```

---

## ✅ Step 3: Test (1 minute)

1. **Backend**: Visit `https://your-backend.onrender.com/api/health`
2. **Frontend**: Visit your GitHub Pages site
3. **Test**: Click "Personalize" or "Translate" button
4. **Check**: Browser DevTools → Network tab → Should see API calls

---

## 🎉 Done!

Your backend is now live and frontend can communicate with it!

**Backend URL**: `https://your-backend.onrender.com`  
**Frontend URL**: `https://doniabatool.github.io/Interactive-Agentic-Book`

---

## 🐛 Quick Fixes

**CORS Error?**
- Add your GitHub Pages URL to `CORS_ORIGINS` in Render
- Format: `https://doniabatool.github.io,http://localhost:3000`

**404 on API?**
- Check backend URL is correct in frontend
- Check backend is running (visit `/api/health`)

**Frontend not updating?**
- Clear browser cache
- Hard refresh (Ctrl+Shift+R)

---

**Total Time**: ~5 minutes ⚡


