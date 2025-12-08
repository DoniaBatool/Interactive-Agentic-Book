# Deployment Checklist ✅

**Quick checklist to ensure everything is deployed correctly**

---

## ✅ Pre-Deployment

- [ ] Backend code is on GitHub
- [ ] Frontend code is on GitHub
- [ ] `backend/requirements.txt` exists
- [ ] `backend/render.yaml` exists (optional)
- [ ] CORS settings updated in `backend/app/config/settings.py`

---

## ✅ Backend Deployment (Render)

- [ ] Created Render account
- [ ] Created new Web Service on Render
- [ ] Connected GitHub repository
- [ ] Set Root Directory to `backend`
- [ ] Set Build Command: `pip install -r requirements.txt`
- [ ] Set Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- [ ] Added Environment Variables:
  - [ ] `ENVIRONMENT=production`
  - [ ] `CORS_ORIGINS=https://doniabatool.github.io,http://localhost:3000`
  - [ ] (Optional) `OPENAI_API_KEY`
  - [ ] (Optional) `QDRANT_URL`
  - [ ] (Optional) `DATABASE_URL`
- [ ] Deployment successful
- [ ] Backend URL saved: `https://...onrender.com`
- [ ] Tested health endpoint: `/api/health`
- [ ] Tested API docs: `/docs`

---

## ✅ Frontend Configuration

- [ ] Created `.env.production` file (or set during build)
- [ ] Set `REACT_APP_API_URL` to backend URL
- [ ] Rebuilt frontend: `npm run build`
- [ ] Committed and pushed to GitHub
- [ ] GitHub Pages rebuilt automatically

---

## ✅ Testing

- [ ] Backend health check works
- [ ] API docs accessible
- [ ] Frontend loads on GitHub Pages
- [ ] Personalization button works (check Network tab)
- [ ] Translation button works (check Network tab)
- [ ] Signup form works (check Network tab)
- [ ] No CORS errors in browser console
- [ ] API calls return responses (even if placeholder)

---

## ✅ Post-Deployment

- [ ] Updated `HACKATHON_PROGRESS_ANALYSIS.md` with backend URL
- [ ] Updated `RELEASE_PACKAGE.md` with backend URL
- [ ] Tested all features
- [ ] Documented any issues

---

## 🎯 Quick Test Commands

### Test Backend
```bash
curl https://your-backend.onrender.com/api/health
```

### Test Frontend API Call
Open browser DevTools → Network tab → Click any button → Check request URL

---

**Status**: Ready when all checked ✅


