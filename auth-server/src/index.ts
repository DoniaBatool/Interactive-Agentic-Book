import express from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import { toNodeHandler } from "better-auth/node";
import { auth, pool } from "./auth.js";
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const app = express();
const PORT = process.env.AUTH_PORT || 8002; // Changed to 8002 to avoid conflict with backend

// Determine if we're in production (HTTPS)
const isProduction = process.env.AUTH_SERVER_URL?.startsWith('https://') || 
                     process.env.NODE_ENV === 'production';

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

// Root route handler - redirect OAuth errors to frontend and check admin status
app.get("/", async (req, res) => {
  const error = req.query.error;
  const frontendUrl = process.env.FRONTEND_URL || "http://localhost:3000";
  
  if (error) {
    // Check if it's our custom admin OAuth block error
    let errorMessage = error as string;
    if (errorMessage === 'ADMIN_OAUTH_BLOCKED' || errorMessage.includes('ADMIN_OAUTH_BLOCKED')) {
      errorMessage = 'Admin accounts cannot sign in via OAuth. Please use email/password login.';
    }
    
    // OAuth error - redirect to frontend signin page with error
    const redirectUrl = `${frontendUrl}/auth/signin?error=${encodeURIComponent(errorMessage)}`;
    res.redirect(redirectUrl);
    return;
  }
  
  // Check if user just signed in via OAuth and is admin
  try {
    const sessionToken = req.cookies?.['better-auth.session_token'] || 
                         req.headers.cookie?.match(/better-auth\.session_token=([^;]+)/)?.[1];
    
    if (sessionToken) {
      const baseToken = sessionToken.split('.')[0];
      const sessionResult = await pool.query(
        `SELECT s."userId", u."isAdmin", u.role, u.email 
         FROM "session" s 
         JOIN "user" u ON s."userId" = u.id 
         WHERE s.token = $1 AND s."expiresAt" > NOW()`,
        [baseToken]
      );
      
      if (sessionResult.rows.length > 0) {
        const user = sessionResult.rows[0];
        const isAdmin = user.isAdmin || user.role === 'admin';
        
        // Check if this session was just created (within last 5 seconds)
        // This indicates a fresh OAuth sign-in
        const sessionCreated = await pool.query(
          `SELECT "createdAt" FROM "session" WHERE token = $1`,
          [baseToken]
        );
        
        if (sessionCreated.rows.length > 0) {
          const createdAt = new Date(sessionCreated.rows[0].createdAt);
          const now = new Date();
          const secondsSinceCreation = (now.getTime() - createdAt.getTime()) / 1000;
          
          // If session was created within last 10 seconds and user is admin, sign them out
          if (secondsSinceCreation < 10 && isAdmin) {
            // Delete the session to sign out the admin
            await pool.query('DELETE FROM "session" WHERE token = $1', [baseToken]);
            
            // Clear the cookie
            res.clearCookie('better-auth.session_token');
            
            // Redirect to signin with error
            const redirectUrl = `${frontendUrl}/auth/signin?error=${encodeURIComponent('Admin accounts cannot sign in via OAuth. Please use email/password login.')}`;
            res.redirect(redirectUrl);
            return;
          }
        }
      }
    }
  } catch (error: any) {
    console.error('Error checking admin status in root route:', error);
    // Continue to redirect if there's an error
  }
  
  // No error - just redirect to frontend
  res.redirect(frontendUrl);
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

// Get current user with full details (including admin fields)
app.get("/api/auth/get-user", async (req, res) => {
  try {
    const sessionToken = req.cookies?.['better-auth.session_token'] || 
                         req.headers.cookie?.match(/better-auth\.session_token=([^;]+)/)?.[1];
    
    if (!sessionToken) {
      return res.status(401).json({ error: 'Unauthorized: No session token' });
    }
    
    const baseToken = sessionToken.split('.')[0];
    
    // Query user with all fields including admin fields
    const result = await pool.query(
      `SELECT u.* 
       FROM "session" s 
       JOIN "user" u ON s."userId" = u.id 
       WHERE s.token = $1 AND s."expiresAt" > NOW()`,
      [baseToken]
    );
    
    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'Unauthorized: Invalid or expired session' });
    }
    
    res.json({ user: result.rows[0] });
  } catch (error: any) {
    console.error('Error fetching user:', error);
    res.status(500).json({ error: error.message });
  }
});

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
    
    // Get current admin's user ID from session
    const currentAdminId = (req as any).user?.id;
    
    // Get user email to check if it's the protected admin
    const userResult = await pool.query('SELECT email FROM "user" WHERE id = $1', [userId]);
    if (userResult.rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    const userEmail = userResult.rows[0].email;
    const PROTECTED_ADMIN_EMAIL = 'donia1510aptech@gmail.com';
    
    // Prevent removing admin status from protected admin
    if (userEmail === PROTECTED_ADMIN_EMAIL && !isAdmin) {
      return res.status(403).json({ error: 'Cannot remove admin status from the primary admin account' });
    }
    
    // Prevent admin from removing their own admin status
    if (currentAdminId && userId === currentAdminId && !isAdmin) {
      return res.status(403).json({ error: 'You cannot remove your own admin status' });
    }
    
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
    
    // Get user email to check if it's the protected admin
    const userResult = await pool.query('SELECT email FROM "user" WHERE id = $1', [userId]);
    if (userResult.rows.length === 0) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    const userEmail = userResult.rows[0].email;
    const PROTECTED_ADMIN_EMAIL = 'donia1510aptech@gmail.com';
    
    // Prevent deletion of protected admin
    if (userEmail === PROTECTED_ADMIN_EMAIL) {
      return res.status(403).json({ error: 'Cannot delete the primary admin account' });
    }
    
    await pool.query('DELETE FROM "user" WHERE id = $1', [userId]);
    
    res.json({ success: true });
  } catch (error: any) {
    console.error('Error deleting user:', error);
    res.status(500).json({ error: error.message });
  }
});

// Middleware to prevent admin users from signing in via OAuth
// This runs BEFORE BetterAuth processes the callback
app.get("/api/auth/callback/google", async (req, res, next) => {
  try {
    const code = req.query.code as string;
    if (!code) {
      return next(); // No code, let BetterAuth handle it
    }
    
    // Get user info from Google using the code
    // First, we need to exchange the code for tokens
    // But BetterAuth does this internally, so we can't easily intercept
    
    // Instead, we'll check AFTER BetterAuth processes it in the root route
    // But we can add a check here to see if there's already a session
    // that was just created (indicating OAuth sign-in)
    
    next(); // Let BetterAuth process the callback first
  } catch (error: any) {
    console.error('Error in OAuth callback middleware:', error);
    next();
  }
});

app.get("/api/auth/callback/github", async (req, res, next) => {
  try {
    const code = req.query.code as string;
    if (!code) {
      return next(); // No code, let BetterAuth handle it
    }
    
    next(); // Let BetterAuth process the callback first
  } catch (error: any) {
    console.error('Error in OAuth callback middleware:', error);
    next();
  }
});

// Custom OAuth callback handler to block admin users
// This runs AFTER BetterAuth processes the callback
app.get("/api/auth/callback/google", async (req, res, next) => {
  // Let BetterAuth process the callback first
  // We'll check after in the root route handler
  next();
});

app.get("/api/auth/callback/github", async (req, res, next) => {
  // Let BetterAuth process the callback first
  // We'll check after in the root route handler
  next();
});

// BetterAuth handles all /api/auth/* routes (must be AFTER admin routes)
// We wrap it to catch responses and check for admin users
const authHandler = toNodeHandler(auth);
app.all("/api/auth/*", async (req, res, next) => {
  // Store original redirect function
  const originalRedirect = res.redirect.bind(res);
  
  // Override redirect to check admin status before redirecting
  res.redirect = function(url: string) {
    // Only check for OAuth callbacks
    if (req.path.includes('/callback/google') || req.path.includes('/callback/github')) {
      // Check if user is admin after OAuth callback
      setTimeout(async () => {
        try {
          const sessionToken = req.cookies?.['better-auth.session_token'] || 
                               req.headers.cookie?.match(/better-auth\.session_token=([^;]+)/)?.[1];
          
          if (sessionToken) {
            const baseToken = sessionToken.split('.')[0];
            const sessionResult = await pool.query(
              `SELECT s."userId", u."isAdmin", u.role, u.email, s."createdAt"
               FROM "session" s 
               JOIN "user" u ON s."userId" = u.id 
               WHERE s.token = $1 AND s."expiresAt" > NOW()`,
              [baseToken]
            );
            
            if (sessionResult.rows.length > 0) {
              const user = sessionResult.rows[0];
              const isAdmin = user.isAdmin || user.role === 'admin';
              
              // Check if session was just created (within last 5 seconds)
              const createdAt = new Date(user.createdAt);
              const now = new Date();
              const secondsSinceCreation = (now.getTime() - createdAt.getTime()) / 1000;
              
              if (secondsSinceCreation < 5 && isAdmin) {
                console.log(`🚫 Blocking OAuth sign-in for admin user: ${user.email}`);
                
                // Delete the session
                await pool.query('DELETE FROM "session" WHERE token = $1', [baseToken]);
                
                // Delete OAuth account link
                await pool.query('DELETE FROM "account" WHERE "userId" = $1 AND "createdAt" > NOW() - INTERVAL \'5 seconds\'', [user.userId]);
                
                // Clear cookie
                res.clearCookie('better-auth.session_token', {
                  httpOnly: true,
                  secure: isProduction,
                  sameSite: isProduction ? 'none' : 'lax',
                });
                
                // Redirect to signin with error
                const frontendUrl = process.env.FRONTEND_URL || "http://localhost:3000";
                return originalRedirect(`${frontendUrl}/auth/signin?error=${encodeURIComponent('Admin accounts cannot sign in via OAuth. Please use email/password login.')}`);
              }
            }
          }
        } catch (error: any) {
          console.error('Error checking admin status in OAuth callback:', error);
        }
      }, 100); // Small delay to ensure session is created
    }
    
    // Normal redirect
    return originalRedirect(url);
  };
  
  // Call BetterAuth handler
  authHandler(req, res, next);
});

// Start server
app.listen(PORT, () => {
  console.log(`🔐 BetterAuth server running on http://localhost:${PORT}`);
  console.log(`   Auth endpoints: http://localhost:${PORT}/api/auth/*`);
  console.log(`   Admin endpoints: http://localhost:${PORT}/api/auth/admin/*`);
});
