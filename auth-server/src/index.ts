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
        
        // Check if this session was just created (within last 20 seconds)
        // This indicates a fresh OAuth sign-in
        const createdAt = new Date(user.createdAt);
        const now = new Date();
        const secondsSinceCreation = (now.getTime() - createdAt.getTime()) / 1000;
        
        // If session was created within last 20 seconds and user is admin, sign them out
        if (secondsSinceCreation < 20 && isAdmin) {
          console.log(`🚫 Blocking OAuth sign-in for admin user: ${user.email}`);
          
          // Delete the session to sign out the admin
          await pool.query('DELETE FROM "session" WHERE token = $1', [baseToken]);
          
          // Delete OAuth account link that was just created
          await pool.query('DELETE FROM "account" WHERE "userId" = $1 AND "createdAt" > NOW() - INTERVAL \'20 seconds\'', [user.userId]);
          
          // Clear the cookie
          res.clearCookie('better-auth.session_token', {
            httpOnly: true,
            secure: isProduction,
            sameSite: isProduction ? 'none' : 'lax',
          });
          
          // Redirect to signin with error
          const redirectUrl = `${frontendUrl}/auth/signin?error=${encodeURIComponent('Admin accounts cannot sign in via OAuth. Please use email/password login.')}`;
          res.redirect(redirectUrl);
          return;
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

// Intercept OAuth callbacks BEFORE BetterAuth processes them
// Check if the email belongs to an admin user and block if so
app.get("/api/auth/callback/google", async (req, res, next) => {
  const code = req.query.code as string;
  const state = req.query.state as string;
  
  if (!code) {
    return next(); // No code, let BetterAuth handle error
  }
  
  try {
    // Exchange code for access token from Google
    const tokenResponse = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        code: code,
        client_id: process.env.GOOGLE_CLIENT_ID || '',
        client_secret: process.env.GOOGLE_CLIENT_SECRET || '',
        redirect_uri: `${process.env.AUTH_SERVER_URL || 'http://localhost:8002'}/api/auth/callback/google`,
        grant_type: 'authorization_code',
      }),
    });
    
    if (!tokenResponse.ok) {
      console.error('Failed to exchange Google OAuth code:', await tokenResponse.text());
      return next(); // Let BetterAuth handle the error
    }
    
    const tokenData = await tokenResponse.json();
    const accessToken = tokenData.access_token;
    
    // Get user info from Google
    const userInfoResponse = await fetch('https://www.googleapis.com/oauth2/v2/userinfo', {
      headers: { 'Authorization': `Bearer ${accessToken}` },
    });
    
    if (!userInfoResponse.ok) {
      console.error('Failed to get Google user info:', await userInfoResponse.text());
      return next(); // Let BetterAuth handle the error
    }
    
    const userInfo = await userInfoResponse.json();
    const email = userInfo.email;
    
    if (email) {
      // Check if this email belongs to an admin user
      const userResult = await pool.query(
        'SELECT id, email, "isAdmin", role FROM "user" WHERE email = $1',
        [email]
      );
      
      if (userResult.rows.length > 0) {
        const user = userResult.rows[0];
        const isAdmin = user.isAdmin || user.role === 'admin';
        
        if (isAdmin) {
          console.log(`🚫 Blocking OAuth sign-in for admin user: ${email}`);
          const frontendUrl = process.env.FRONTEND_URL || "http://localhost:3000";
          return res.redirect(`${frontendUrl}/auth/signin?error=${encodeURIComponent('Admin accounts cannot sign in via OAuth. Please use email/password login.')}`);
        }
      }
    }
    
    // Not admin or new user - let BetterAuth process normally
    next();
  } catch (error: any) {
    console.error('Error checking admin status in Google OAuth callback:', error);
    // On error, let BetterAuth handle it
    next();
  }
});

app.get("/api/auth/callback/github", async (req, res, next) => {
  const code = req.query.code as string;
  const state = req.query.state as string;
  
  if (!code) {
    return next(); // No code, let BetterAuth handle error
  }
  
  try {
    // Exchange code for access token from GitHub
    const tokenResponse = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        client_id: process.env.GITHUB_CLIENT_ID || '',
        client_secret: process.env.GITHUB_CLIENT_SECRET || '',
        code: code,
        redirect_uri: `${process.env.AUTH_SERVER_URL || 'http://localhost:8002'}/api/auth/callback/github`,
      }),
    });
    
    if (!tokenResponse.ok) {
      console.error('Failed to exchange GitHub OAuth code:', await tokenResponse.text());
      return next(); // Let BetterAuth handle the error
    }
    
    const tokenData = await tokenResponse.json();
    const accessToken = tokenData.access_token;
    
    // Get user info from GitHub
    const userInfoResponse = await fetch('https://api.github.com/user', {
      headers: { 'Authorization': `Bearer ${accessToken}` },
    });
    
    if (!userInfoResponse.ok) {
      console.error('Failed to get GitHub user info:', await userInfoResponse.text());
      return next(); // Let BetterAuth handle the error
    }
    
    const userInfo = await userInfoResponse.json();
    // GitHub doesn't always return email in user endpoint, need to get from email endpoint
    let email = userInfo.email;
    
    if (!email) {
      // Try to get email from GitHub's email endpoint
      const emailResponse = await fetch('https://api.github.com/user/emails', {
        headers: { 'Authorization': `Bearer ${accessToken}` },
      });
      
      if (emailResponse.ok) {
        const emails = await emailResponse.json();
        const primaryEmail = emails.find((e: any) => e.primary) || emails[0];
        email = primaryEmail?.email;
      }
    }
    
    if (email) {
      // Check if this email belongs to an admin user
      const userResult = await pool.query(
        'SELECT id, email, "isAdmin", role FROM "user" WHERE email = $1',
        [email]
      );
      
      if (userResult.rows.length > 0) {
        const user = userResult.rows[0];
        const isAdmin = user.isAdmin || user.role === 'admin';
        
        if (isAdmin) {
          console.log(`🚫 Blocking OAuth sign-in for admin user: ${email}`);
          const frontendUrl = process.env.FRONTEND_URL || "http://localhost:3000";
          return res.redirect(`${frontendUrl}/auth/signin?error=${encodeURIComponent('Admin accounts cannot sign in via OAuth. Please use email/password login.')}`);
        }
      }
    }
    
    // Not admin or new user - let BetterAuth process normally
    next();
  } catch (error: any) {
    console.error('Error checking admin status in GitHub OAuth callback:', error);
    // On error, let BetterAuth handle it
    next();
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
