# 🚀 Server Start Guide

## Servers ko start karne ka tareeqa (order matters!)

### **Step 1: Backend (FastAPI) - Port 8000**

#### **Windows (CMD/PowerShell):**

```cmd
# Terminal 1 mein
cd C:\Users\Leo\interactive-agentic-book

# Virtual environment activate karo:
.\venv\Scripts\Activate
# Ya PowerShell mein:
.\venv\Scripts\Activate.ps1

# Dependencies install (agar pehli baar):
pip install -r requirements.txt

# Backend start karo (Windows ke liye 127.0.0.1 use karo):
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

#### **Linux/WSL:**

```bash
# Terminal 1 mein
cd /mnt/c/Users/Leo/interactive-agentic-book

# Virtual environment activate karo:
source venv/bin/activate

# Dependencies install (agar pehli baar):
pip install -r requirements.txt

# Backend start karo:
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ **Check:** `http://localhost:8000/docs` pe API docs dikhne chahiye

⚠️ **Port 8000 pe error?** Alternative port try karo:
```cmd
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8001
```

---

### **Step 2: BetterAuth Server - Port 3000**

```bash
# Terminal 2 mein
cd /mnt/c/Users/Leo/interactive-agentic-book/auth-server

# Dependencies install (agar pehli baar):
npm install

# Environment variables check karo (.env file)
# Required: DATABASE_URL, BETTER_AUTH_SECRET, BETTER_AUTH_URL

# Auth server start karo:
npm run dev
```

✅ **Check:** `http://localhost:3000/api/auth/signin` pe signin page dikhna chahiye

---

### **Step 3: Frontend (Docusaurus) - Port 3001**

```bash
# Terminal 3 mein
cd /mnt/c/Users/Leo/interactive-agentic-book

# Dependencies install (agar pehli baar):
npm install

# Frontend start karo:
npm run start
```

✅ **Check:** Browser automatically open hoga `http://localhost:3001` pe

---

## 📋 Quick Reference

| Server | Port | Command | Terminal |
|--------|------|---------|----------|
| **Backend** | 8000 | `uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000` | Terminal 1 |
| **BetterAuth** | 3000 | `cd auth-server && npm run dev` | Terminal 2 |
| **Frontend** | 3001 | `npm run start` | Terminal 3 |

---

## 🔧 Troubleshooting

### Backend start nahi ho raha:

**Windows:**
- Virtual environment activate: `.\venv\Scripts\Activate` (CMD) ya `.\venv\Scripts\Activate.ps1` (PowerShell)
- Port permission error? `127.0.0.1` use karo `0.0.0.0` ki jagah
- Port already in use? Alternative port try karo: `--port 8001`
- Windows Firewall check karo - port block to nahi ho rahi?

**Linux/WSL:**
- Virtual environment activate: `source venv/bin/activate`
- Dependencies check: `pip install -r requirements.txt`

**Common:**
- Database connection check: `.env` mein `DATABASE_URL` sahi hai?
- Port check: `netstat -ano | findstr :8000` (Windows) ya `lsof -i :8000` (Linux)

### BetterAuth start nahi ho raha:
- `cd auth-server` karo pehle
- `npm install` karo
- `.env` file check karo (auth-server folder mein)

### Frontend start nahi ho raha:
- Root directory mein ho: `cd /mnt/c/Users/Leo/interactive-agentic-book`
- `npm install` karo
- Port 3001 already use ho raha hai? To automatically next port use hoga

---

## ⚡ One-Line Commands (3 separate terminals)

### **Windows (CMD/PowerShell):**

**Terminal 1 (Backend):**
```cmd
cd C:\Users\Leo\interactive-agentic-book && .\venv\Scripts\Activate && uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

**Terminal 2 (BetterAuth):**
```cmd
cd C:\Users\Leo\interactive-agentic-book\auth-server && npm run dev
```

**Terminal 3 (Frontend):**
```cmd
cd C:\Users\Leo\interactive-agentic-book && npm run start
```

### **Linux/WSL:**

**Terminal 1 (Backend):**
```bash
cd /mnt/c/Users/Leo/interactive-agentic-book && source venv/bin/activate && uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 (BetterAuth):**
```bash
cd /mnt/c/Users/Leo/interactive-agentic-book/auth-server && npm run dev
```

**Terminal 3 (Frontend):**
```bash
cd /mnt/c/Users/Leo/interactive-agentic-book && npm run start
```

---

## ✅ Verification

Sab servers start hone ke baad:

1. **Backend:** `http://localhost:8000/docs` - API documentation
2. **BetterAuth:** `http://localhost:3000/api/auth/signin` - Sign in page
3. **Frontend:** `http://localhost:3001` - Main website

Sab kaam kar rahe hain! 🎉

