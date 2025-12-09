# 🐛 Windows Local Testing - Port Error Fix

**Error**: `[WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions`

---

## 🔍 Problem

Port 8000 already use ho raha hai ya Windows firewall/antivirus block kar raha hai.

---

## ✅ Quick Fixes

### Fix 1: Different Port Use Karo (Easiest)

Port 8000 ki jagah 8001 ya 8080 use karo:

```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

**Frontend config update karo** (`frontend/src/config/api.ts`):
- Development mein automatically `localhost:8000` detect karta hai
- Agar 8001 use kar rahe ho, to manually update karo:

```typescript
// frontend/src/config/api.ts
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
  return 'http://localhost:8001'; // Change 8000 to 8001
}
```

---

### Fix 2: Check Port 8000 Already Use Ho Raha Hai

**Windows Command:**
```bash
netstat -ano | findstr :8000
```

Agar koi process dikhe, to usko kill karo:
```bash
taskkill /PID <PID_NUMBER> /F
```

Phir phir se try karo:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

### Fix 3: Firewall/Antivirus Check

1. **Windows Firewall**: Allow Python/uvicorn
2. **Antivirus**: Temporarily disable karke test karo
3. **Windows Defender**: Check if blocking

---

### Fix 4: Admin Rights

**Run Terminal as Administrator:**
1. Right-click on Terminal/CMD
2. "Run as administrator" select karo
3. Phir command run karo

---

### Fix 5: Use 127.0.0.1 Instead of 0.0.0.0

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🎯 Recommended Solution

**Step 1: Port 8001 Use Karo**

```bash
cd backend
uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```

**Step 2: Frontend Config Update (If Needed)**

Agar frontend se connect nahi ho raha, to `frontend/src/config/api.ts` update karo:

```typescript
// Priority 3: Development mode (localhost)
if (typeof window !== 'undefined') {
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    return 'http://localhost:8001'; // Changed from 8000 to 8001
  }
}
```

**Step 3: Test**

1. Backend: `http://localhost:8001/api/health`
2. Frontend: `http://localhost:3000`

---

## ✅ Verification

Backend start hone ke baad yeh dikhna chahiye:

```
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## 🐛 Still Not Working?

1. **Check Python version**: `python --version` (should be 3.11+)
2. **Check dependencies**: `pip install -r requirements.txt`
3. **Check firewall**: Temporarily disable
4. **Try different port**: 8002, 8080, 3001, etc.

---

**Try Fix 1 first (different port) - usually works!**

