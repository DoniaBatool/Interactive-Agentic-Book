# ⚡ Quick Deployment Guide

## 🚀 Frontend Deployment (GitHub Pages) - 5 Minutes

### Step 1: Update Auth Server URL (IMPORTANT!)

Before deploying, update the production auth server URL in `src/config/env.ts`:

```typescript
// In src/config/env.ts, line ~20
if (isProduction) {
  return 'https://your-actual-auth-server-url.railway.app'; // ← UPDATE THIS
}
```

### Step 2: Push to GitHub

```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### Step 3: Enable GitHub Pages

1. Go to: `https://github.com/doniabatool/Interactive-Agentic-Book/settings/pages`
2. Under **Build and deployment**:
   - **Source**: Select **"GitHub Actions"**
   - Click **Save**

### Step 4: Wait for Deployment

- Go to **Actions** tab in your repository
- Wait for the workflow to complete (green checkmark)
- Your site will be live at: `https://doniabatool.github.io/Interactive-Agentic-Book/`

---

## 🔐 Auth Server Deployment (Railway) - 10 Minutes

### Step 1: Sign Up on Railway

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select `Interactive-Agentic-Book`

### Step 2: Configure Service

1. **Settings** → **Root Directory**: Set to `auth-server`
2. **Settings** → **Build Command**: `npm install`
3. **Settings** → **Start Command**: `npm run start`

### Step 3: Add PostgreSQL Database

1. Click **"New"** → **"Database"** → **"Add PostgreSQL"**
2. Copy the connection string (DATABASE_URL)

### Step 4: Set Environment Variables

Go to **Variables** tab and add:

```env
AUTH_PORT=8002
BETTER_AUTH_URL=https://your-service-name.railway.app
BETTER_AUTH_SECRET=your-strong-secret-key-min-32-chars
DATABASE_URL=postgresql://... (from step 3)
FRONTEND_URL=https://doniabatool.github.io/Interactive-Agentic-Book
SENDGRID_API_KEY=your-key (optional)
GOOGLE_CLIENT_ID=your-id (optional)
GOOGLE_CLIENT_SECRET=your-secret (optional)
GITHUB_CLIENT_ID=your-id (optional)
GITHUB_CLIENT_SECRET=your-secret (optional)
```

### Step 5: Update OAuth Redirect URIs

**Google OAuth Console**:
- Add: `https://your-service-name.railway.app/api/auth/callback/google`

**GitHub OAuth Settings**:
- Add: `https://your-service-name.railway.app/api/auth/callback/github`

### Step 6: Update Frontend Config

Update `src/config/env.ts` with your Railway URL:

```typescript
if (isProduction) {
  return 'https://your-service-name.railway.app'; // ← Your Railway URL
}
```

Then push again to trigger frontend redeployment.

---

## ✅ Verification Checklist

- [ ] Frontend is accessible at GitHub Pages URL
- [ ] Auth server is accessible at Railway URL
- [ ] Sign up works
- [ ] Sign in works
- [ ] OAuth (Google/GitHub) works
- [ ] Password reset works
- [ ] Language toggle works

---

## 🆘 Troubleshooting

**Frontend shows 404 errors:**
- Check `baseUrl` in `docusaurus.config.ts` is `/Interactive-Agentic-Book/`

**Auth not working:**
- Verify `AUTH_SERVER_URL` in `src/config/env.ts` matches your Railway URL
- Check CORS settings in auth server
- Verify `FRONTEND_URL` in Railway environment variables

**OAuth not working:**
- Verify redirect URIs in Google/GitHub OAuth settings
- Check `BETTER_AUTH_URL` matches actual Railway URL

---

**Need more details?** See `DEPLOYMENT.md` for comprehensive guide.

