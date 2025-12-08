# 🔧 Render Environment Variables Guide

**Kaunse Environment Variables Render mein add karne hain?**

---

## ✅ REQUIRED Variables (Must Add in Render)

Yeh variables **zaroor** add karne hain Render mein:

### 1. **CORS_ORIGINS** ⚠️ **MOST IMPORTANT**
```
Name: CORS_ORIGINS
Value: https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book,http://localhost:3000
```
**Why**: Frontend (GitHub Pages) se backend ko call karne ke liye CORS allow karna zaroori hai.

### 2. **ENVIRONMENT**
```
Name: ENVIRONMENT
Value: production
```
**Why**: Application ko production mode mein run karta hai.

### 3. **PYTHON_VERSION** (Optional but Recommended)
```
Name: PYTHON_VERSION
Value: 3.11.0
```
**Why**: Python version specify karta hai.

---

## ⚠️ OPTIONAL Variables (Add Only If You Have)

Agar aapke paas yeh services/keys hain, to add karo:

### AI Provider Keys

#### **OPENAI_API_KEY** (If using OpenAI)
```
Name: OPENAI_API_KEY
Value: sk-... (your OpenAI API key)
```
**Mark as Secret**: ✅ Yes (eye icon click karo)

#### **GEMINI_API_KEY** (If using Google Gemini)
```
Name: GEMINI_API_KEY
Value: your_gemini_api_key
```
**Mark as Secret**: ✅ Yes

### Vector Database - Qdrant

#### **QDRANT_URL** (If using Qdrant)
```
Name: QDRANT_URL
Value: https://your-cluster.qdrant.io
```

#### **QDRANT_API_KEY** (If Qdrant requires API key)
```
Name: QDRANT_API_KEY
Value: your_qdrant_api_key
```
**Mark as Secret**: ✅ Yes

#### **QDRANT_COLLECTION_CH1** (Optional)
```
Name: QDRANT_COLLECTION_CH1
Value: chapter_1_embeddings
```

### Database - Neon

#### **DATABASE_URL** (If using Neon PostgreSQL)
```
Name: DATABASE_URL
Value: postgresql://user:password@host:port/database
```
**Mark as Secret**: ✅ Yes

### Authentication - BetterAuth

#### **BETTERAUTH_SECRET** (If using BetterAuth)
```
Name: BETTERAUTH_SECRET
Value: your_secure_random_string_here
```
**Mark as Secret**: ✅ Yes

#### **BETTERAUTH_PUBLIC_KEY** (If using BetterAuth)
```
Name: BETTERAUTH_PUBLIC_KEY
Value: your_betterauth_public_key
```

#### **BETTERAUTH_SECRET_KEY** (If using BetterAuth)
```
Name: BETTERAUTH_SECRET_KEY
Value: your_betterauth_secret_key
```
**Mark as Secret**: ✅ Yes

### Email Configuration

#### **SMTP_HOST** (If sending emails)
```
Name: SMTP_HOST
Value: smtp.gmail.com
```

#### **SMTP_USER** (If sending emails)
```
Name: SMTP_USER
Value: your_email@gmail.com
```

#### **SMTP_PASSWORD** (If sending emails)
```
Name: SMTP_PASSWORD
Value: your_email_password
```
**Mark as Secret**: ✅ Yes

---

## 📋 Quick Checklist for Render

### Must Add (Required):
- [ ] **CORS_ORIGINS** - GitHub Pages URLs
- [ ] **ENVIRONMENT** - `production`

### Add If You Have:
- [ ] **OPENAI_API_KEY** - OpenAI API key (if using OpenAI)
- [ ] **QDRANT_URL** - Qdrant cluster URL (if using Qdrant)
- [ ] **DATABASE_URL** - Neon database URL (if using database)
- [ ] **BETTERAUTH_SECRET** - BetterAuth secret (if using auth)

### Don't Add (Not Needed):
- ❌ **BACKEND_PORT** - Render automatically provides `$PORT`
- ❌ **PYTHON_VERSION** - Optional (Render auto-detects)
- ❌ Model names (EMBEDDING_MODEL, LLM_MODEL, etc.) - Optional, defaults work
- ❌ Collection names - Optional, defaults work

---

## 🎯 Minimum Setup for Render (Recommended)

**For Basic Deployment (Placeholder Mode):**

Add only these 2 variables:

1. **CORS_ORIGINS**
   ```
   https://doniabatool.github.io,https://doniabatool.github.io/Interactive-Agentic-Book,http://localhost:3000
   ```

2. **ENVIRONMENT**
   ```
   production
   ```

**That's it!** Backend deploy ho jayega aur placeholder responses dega.

---

## 🔐 Security Best Practices

### Mark as Secret:
Always mark these as **Secret** (eye icon):
- ✅ OPENAI_API_KEY
- ✅ GEMINI_API_KEY
- ✅ QDRANT_API_KEY
- ✅ DATABASE_URL
- ✅ BETTERAUTH_SECRET
- ✅ BETTERAUTH_SECRET_KEY
- ✅ SMTP_PASSWORD

### Don't Mark as Secret:
These are safe to show:
- ❌ CORS_ORIGINS
- ❌ ENVIRONMENT
- ❌ PYTHON_VERSION
- ❌ AI_PROVIDER
- ❌ Model names

---

## 📝 Step-by-Step: Adding Variables in Render

1. **Go to Your Service** → **Environment** tab
2. **Click "Add Environment Variable"**
3. **Enter Name** (e.g., `CORS_ORIGINS`)
4. **Enter Value** (e.g., `https://doniabatool.github.io,...`)
5. **Mark as Secret** (if it's a key/password) - Click eye icon
6. **Click "Save Changes"** (auto-redeploys)

---

## ✅ Verification

After adding variables, check:

1. **Service Logs**: Should show configuration status
2. **Health Endpoint**: `https://your-backend.onrender.com/api/health`
3. **Startup Logs**: Should show which variables are configured

---

## 🐛 Common Issues

### Issue 1: CORS Errors
**Fix**: Make sure `CORS_ORIGINS` includes exact GitHub Pages URL (no trailing slash)

### Issue 2: API Keys Not Working
**Fix**: 
- Check if marked as Secret
- Verify no extra spaces in value
- Check service logs for errors

### Issue 3: Service Won't Start
**Fix**: 
- Check required variables are set
- Verify no typos in variable names
- Check logs for specific errors

---

## 📚 Reference

- **Full .env.example**: `backend/.env.example`
- **Settings File**: `backend/app/config/settings.py`
- **Render Docs**: [render.com/docs/environment-variables](https://render.com/docs/environment-variables)

---

**Summary**: 
- **Required**: CORS_ORIGINS, ENVIRONMENT
- **Optional**: API keys, database URLs, auth secrets (only if you have them)
- **Minimum**: Just CORS_ORIGINS and ENVIRONMENT for basic deployment!

