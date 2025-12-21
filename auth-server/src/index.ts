import express from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import { toNodeHandler } from "better-auth/node";
import { auth, pool } from "./auth.js";
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const app = express();
const PORT = process.env.AUTH_PORT || 8002; // Changed to 8002 to avoid conflict with backend

// CORS configuration
const getAllowedOrigins = (): string[] => {
  const origins: string[] = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
  ];
  
  // Add FRONTEND_URL if set
  if (process.env.FRONTEND_URL) {
    origins.push(process.env.FRONTEND_URL);
  }
  
  // Add ALLOWED_ORIGINS if set (comma-separated)
  if (process.env.ALLOWED_ORIGINS) {
    const allowedOrigins = process.env.ALLOWED_ORIGINS.split(',').map(o => o.trim()).filter(Boolean);
    origins.push(...allowedOrigins);
  }
  
  return origins.filter(Boolean);
};

app.use(
  cors({
    origin: getAllowedOrigins(),
    credentials: true,
    methods: ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);

// Parse cookies and JSON
app.use(cookieParser());
app.use(express.json());

// Health check endpoint
app.get("/health", (req, res) => {
  res.json({ status: "ok", service: "better-auth-server" });
});

// Middleware to check admin status
const checkAdmin = async (req: express.Request, res: express.Response, next: express.NextFunction) => {
  try {
    // BetterAuth stores full session data in 'better-auth.session_data' cookie
    // The session_token is signed (baseToken.signature), but DB stores only baseToken
    // So we extract base token from signed token and query DB
    
    const sessionToken = req.cookies?.['better-auth.session_token'] || 
                         req.headers.cookie?.match(/better-auth\.session_token=([^;]+)/)?.[1];
    
    if (!sessionToken) {
      console.error('❌ Admin check failed: No session token');
      return res.status(401).json({ error: 'Unauthorized: No session token' });
    }
    
    // BetterAuth token format: baseToken.signature
    // Extract base token (part before the dot)
    const baseToken = sessionToken.split('.')[0];
    
    console.log('🔍 Admin check - Base token:', baseToken.substring(0, 20) + '...');
    
    // Query session table using base token
    const sessionResult = await pool.query(
      `SELECT s."userId", u."isAdmin", u.role, u.email 
       FROM "session" s 
       JOIN "user" u ON s."userId" = u.id 
       WHERE s.token = $1 AND s."expiresAt" > NOW()`,
      [baseToken]
    );
    
    if (sessionResult.rows.length === 0) {
      console.error('❌ Admin check failed: Invalid or expired session');
      return res.status(401).json({ error: 'Unauthorized: Invalid or expired session' });
    }
    
    const user = sessionResult.rows[0];
    const isAdmin = user.isAdmin || user.role === 'admin';
    
    console.log('🔍 Admin check - User:', {
      email: user.email,
      isAdmin: user.isAdmin,
      role: user.role,
      calculatedIsAdmin: isAdmin
    });
    
    if (!isAdmin) {
      console.error('❌ Admin check failed: User is not admin');
      return res.status(403).json({ error: 'Forbidden: Admin access required' });
    }
    
    console.log('✅ Admin check passed');
    (req as any).user = { id: user.userId, isAdmin, role: user.role };
    next();
  } catch (error: any) {
    console.error('❌ Admin check error:', error);
    res.status(401).json({ error: 'Unauthorized' });
  }
};

// Get all users (admin only)
app.get("/api/auth/admin/users", checkAdmin, async (req, res) => {
  try {
    const result = await pool.query('SELECT id, email, name, "emailVerified", role, "isAdmin", "createdAt" FROM "user" ORDER BY "createdAt" DESC');
    res.json({ users: result.rows });
  } catch (error: any) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: error.message });
  }
});

// Toggle admin status
app.post("/api/auth/admin/users/:userId/toggle-admin", checkAdmin, async (req, res) => {
  try {
    const { userId } = req.params;
    const { isAdmin } = req.body;
    
    await pool.query('UPDATE "user" SET "isAdmin" = $1, role = $2 WHERE id = $3', [
      isAdmin,
      isAdmin ? 'admin' : 'user',
      userId
    ]);
    
    res.json({ success: true });
  } catch (error: any) {
    console.error('Error updating user:', error);
    res.status(500).json({ error: error.message });
  }
});

// Delete user
app.delete("/api/auth/admin/users/:userId", checkAdmin, async (req, res) => {
  try {
    const { userId } = req.params;
    
    await pool.query('DELETE FROM "user" WHERE id = $1', [userId]);
    
    res.json({ success: true });
  } catch (error: any) {
    console.error('Error deleting user:', error);
    res.status(500).json({ error: error.message });
  }
});

// BetterAuth handles all /api/auth/* routes (must be AFTER admin routes)
app.all("/api/auth/*", toNodeHandler(auth));

// Start server
app.listen(PORT, () => {
  console.log(`🔐 BetterAuth server running on http://localhost:${PORT}`);
  console.log(`   Auth endpoints: http://localhost:${PORT}/api/auth/*`);
  console.log(`   Admin endpoints: http://localhost:${PORT}/api/auth/admin/*`);
});

