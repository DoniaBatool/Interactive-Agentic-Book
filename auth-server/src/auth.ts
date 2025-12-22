import { betterAuth } from "better-auth";
import { Pool } from "pg";
import dotenv from "dotenv";
import crypto from "crypto";

dotenv.config({ path: "../.env" });

// Email service configuration
// Option 1: SendGrid (Recommended - 100 emails/day free, no domain verification needed)
// Option 2: Gmail SMTP (Completely free, uses your Gmail account)
// Option 3: Brevo (300 emails/day free)

// Email service setup (lazy initialization)
let sendEmail: ((to: string, subject: string, html: string) => Promise<void>) | null = null;
let emailServiceInitialized = false;

// Check if email service is configured
const hasEmailService = !!(process.env.SENDGRID_API_KEY || (process.env.GMAIL_USER && process.env.GMAIL_APP_PASSWORD));

// Initialize email service lazily (called when first email is sent)
async function initializeEmailService() {
  if (emailServiceInitialized) return;
  
  if (process.env.SENDGRID_API_KEY) {
    // Using SendGrid
    const sgMail = (await import('@sendgrid/mail')).default;
    sgMail.setApiKey(process.env.SENDGRID_API_KEY);
    
    sendEmail = async (to: string, subject: string, html: string) => {
      await sgMail.send({
        to,
        from: process.env.SENDGRID_FROM_EMAIL || 'noreply@example.com',
        subject,
        html,
      });
    };
    console.log('✅ Using SendGrid for email verification');
    emailServiceInitialized = true;
  } else if (process.env.GMAIL_USER && process.env.GMAIL_APP_PASSWORD) {
    // Using Gmail SMTP (Nodemailer)
    const nodemailer = (await import('nodemailer')).default;
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_APP_PASSWORD, // Gmail App Password (not regular password)
      },
    });
    
    sendEmail = async (to: string, subject: string, html: string) => {
      await transporter.sendMail({
        from: process.env.GMAIL_USER,
        to,
        subject,
        html,
      });
    };
    console.log('✅ Using Gmail SMTP for email verification');
    emailServiceInitialized = true;
  } else {
    console.warn('⚠️ No email service configured. Email verification will be disabled.');
    console.warn('💡 Options:');
    console.warn('   1. SendGrid: Add SENDGRID_API_KEY and SENDGRID_FROM_EMAIL to .env');
    console.warn('   2. Gmail: Add GMAIL_USER and GMAIL_APP_PASSWORD to .env');
    emailServiceInitialized = true; // Mark as initialized even if no service
  }
}

// PostgreSQL connection pool
export const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.DATABASE_URL?.includes("neon.tech")
    ? { rejectUnauthorized: false }
    : false,
});

// Determine if we're in production (HTTPS)
const isProduction = process.env.AUTH_SERVER_URL?.startsWith('https://') || 
                     process.env.NODE_ENV === 'production';

export const auth = betterAuth({
  baseURL: process.env.AUTH_SERVER_URL || "http://localhost:8002",
  basePath: "/api/auth",
  database: pool,
  // Cookie configuration for OAuth state management
  advanced: {
    defaultCookieAttributes: {
      sameSite: isProduction ? "none" : "lax", // 'none' for cross-site in production
      secure: isProduction, // HTTPS only in production
      httpOnly: true,
    },
  },
  emailAndPassword: {
    enabled: true,
    minPasswordLength: 8,
    requireEmailVerification: false, // Temporarily disabled for easier testing
    sendResetPassword: async ({ user, url, token }: { user: { email: string; name?: string }; url: string; token: string }) => {
      await initializeEmailService();
      
      // Use custom reset URL (frontend route) instead of auth server URL
      const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
      const resetUrl = `${frontendUrl}/auth/reset-password?token=${token}`;
      
      if (!sendEmail) {
        console.warn('⚠️ Email service not configured. Password reset link:', resetUrl);
        return;
      }

      try {
        const subject = 'Reset your password - Physical AI Textbook';
        const html = `
          <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #333;">Password Reset Request</h2>
            <p>Hello ${user.name || user.email},</p>
            <p>You requested to reset your password. Click the link below to reset it:</p>
            <p style="margin: 20px 0;">
              <a href="${resetUrl}" style="background-color: #4CAF50; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; display: inline-block;">
                Reset Password
              </a>
            </p>
            <p>Or copy and paste this link in your browser:</p>
            <p style="word-break: break-all; color: #666; background: #f5f5f5; padding: 10px; border-radius: 4px;">${resetUrl}</p>
            <p style="color: #999; font-size: 12px; margin-top: 30px;">This link will expire in 1 hour.</p>
            <p style="color: #999; font-size: 12px;">If you didn't request this, please ignore this email.</p>
          </div>
        `;

        await sendEmail(user.email, subject, html);
        console.log(`✅ Password reset email sent to ${user.email}`);
      } catch (error: any) {
        console.error('❌ Failed to send password reset email:', error);
        
        // Log SendGrid specific errors
        if (error.response?.body?.errors) {
          const errors = error.response.body.errors;
          console.error('📧 SendGrid Errors:');
          errors.forEach((err: any) => {
            console.error(`   - ${err.message || err}`);
          });
        } else {
          console.error('Error details:', error.message || error);
        }
        
        console.log(`📧 Fallback: Password reset link for ${user.email}: ${resetUrl}`);
      }
    },
  },
  emailVerification: {
    enabled: false, // Temporarily disabled - user can sign in without email verification
    sendOnSignUp: true,
    autoSignInAfterVerification: true,
    getVerificationUrl: async ({ token, user }: { token: string; user: { email: string } }) => {
      const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
      return `${frontendUrl}/auth/verify-email?token=${token}`;
    },
    sendVerificationEmail: async ({ user, url, token }: { user: { email: string; name?: string }; url: string; token: string }) => {
      await initializeEmailService();
      
      // Use custom verification URL (frontend route) instead of auth server URL
      const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
      const verificationUrl = `${frontendUrl}/auth/verify-email?token=${token}`;
      
      if (!sendEmail) {
        console.warn('⚠️ Email service not configured. Verification link:', verificationUrl);
        return;
      }

      try {
        const subject = 'Verify your email address - Physical AI Textbook';
        const html = `
          <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #333;">Welcome to Physical AI Textbook!</h2>
            <p>Hello ${user.name || user.email},</p>
            <p>Please verify your email address by clicking the link below:</p>
            <p style="margin: 20px 0;">
              <a href="${verificationUrl}" style="background-color: #4CAF50; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; display: inline-block;">
                Verify Email
              </a>
            </p>
            <p>Or copy and paste this link in your browser:</p>
            <p style="word-break: break-all; color: #666; background: #f5f5f5; padding: 10px; border-radius: 4px;">${verificationUrl}</p>
            <p style="color: #999; font-size: 12px; margin-top: 30px;">This link will expire in 24 hours.</p>
            <p style="color: #999; font-size: 12px;">If you didn't create this account, please ignore this email.</p>
          </div>
        `;

        await sendEmail(user.email, subject, html);
        console.log(`✅ Verification email sent to ${user.email}`);
      } catch (error: any) {
        console.error('❌ Failed to send verification email:', error);
        
        // Log SendGrid specific errors
        if (error.response?.body?.errors) {
          const errors = error.response.body.errors;
          console.error('📧 SendGrid Errors:');
          errors.forEach((err: any) => {
            console.error(`   - ${err.message || err}`);
          });
          
          // Check for common issues
          if (error.code === 403) {
            console.error('\n🔧 Fix: Verify your sender email in SendGrid:');
            console.error('   1. Go to https://app.sendgrid.com/settings/sender_auth/senders');
            console.error('   2. Click "Create New Sender"');
            console.error(`   3. Add and verify: ${process.env.SENDGRID_FROM_EMAIL || 'your-email@example.com'}`);
            console.error('   4. Check your email and click the verification link');
          }
        } else {
          console.error('Error details:', error.message || error);
        }
        
        // Use custom verification URL
        const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
        const verificationUrl = `${frontendUrl}/auth/verify-email?token=${token}`;
        console.log(`\n📧 Fallback: Verification link for ${user.email}:`);
        console.log(`   ${verificationUrl}`);
        // Don't throw - allow signup to continue even if email fails
      }
    },
  },
  forgotPassword: {
    enabled: true,
    getResetPasswordUrl: async ({ token }: { token: string }) => {
      const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
      return `${frontendUrl}/auth/reset-password?token=${token}`;
    },
    sendResetEmail: async ({ user, url, token }: { user: { email: string; name?: string }; url: string; token: string }) => {
      await initializeEmailService();
      
      // Use custom reset URL (frontend route) instead of auth server URL
      const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
      const resetUrl = `${frontendUrl}/auth/reset-password?token=${token}`;
      
      if (!sendEmail) {
        console.warn('⚠️ Email service not configured. Password reset link:', resetUrl);
        return;
      }

      try {
        const subject = 'Reset your password - Physical AI Textbook';
        const html = `
          <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #333;">Password Reset Request</h2>
            <p>Hello ${user.name || user.email},</p>
            <p>You requested to reset your password. Click the link below to reset it:</p>
            <p style="margin: 20px 0;">
              <a href="${resetUrl}" style="background-color: #4CAF50; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; display: inline-block;">
                Reset Password
              </a>
            </p>
            <p>Or copy and paste this link in your browser:</p>
            <p style="word-break: break-all; color: #666; background: #f5f5f5; padding: 10px; border-radius: 4px;">${resetUrl}</p>
            <p style="color: #999; font-size: 12px; margin-top: 30px;">This link will expire in 1 hour.</p>
            <p style="color: #999; font-size: 12px;">If you didn't request this, please ignore this email.</p>
          </div>
        `;

        await sendEmail(user.email, subject, html);
        console.log(`✅ Password reset email sent to ${user.email}`);
      } catch (error: any) {
        console.error('❌ Failed to send password reset email:', error);
        
        // Log SendGrid specific errors
        if (error.response?.body?.errors) {
          const errors = error.response.body.errors;
          console.error('📧 SendGrid Errors:');
          errors.forEach((err: any) => {
            console.error(`   - ${err.message || err}`);
          });
        } else {
          console.error('Error details:', error.message || error);
        }
        
        console.log(`📧 Fallback: Password reset link for ${user.email}: ${resetUrl}`);
      }
    },
  },
  socialProviders: {
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID || "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET || "",
      enabled: !!process.env.GOOGLE_CLIENT_ID,
      // Ensure OAuth users get default role, not admin
      mapProfileToUser: async (profile) => {
        return {
          email: profile.email,
          name: profile.name,
          image: profile.image,
          emailVerified: true,
          role: "user", // Explicitly set to user
          isAdmin: false, // Explicitly set to false
          softwareLevel: "beginner",
          hardwareLevel: "none",
          technologies: "{}",
        };
      },
    },
    github: {
      clientId: process.env.GITHUB_CLIENT_ID || "",
      clientSecret: process.env.GITHUB_CLIENT_SECRET || "",
      enabled: !!process.env.GITHUB_CLIENT_ID,
      // Ensure OAuth users get default role, not admin
      mapProfileToUser: async (profile) => {
        return {
          email: profile.email,
          name: profile.name,
          image: profile.image,
          emailVerified: true,
          role: "user", // Explicitly set to user
          isAdmin: false, // Explicitly set to false
          softwareLevel: "beginner",
          hardwareLevel: "none",
          technologies: "{}",
        };
      },
    },
  },
  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
    updateAge: 60 * 60 * 24, // 1 day
    cookieCache: {
      enabled: true,
      maxAge: 5 * 60, // 5 minutes
    },
  },
  user: {
    additionalFields: {
      name: {
        type: "string",
        required: false,
      },
      softwareLevel: {
        type: "string",
        required: false,
        defaultValue: "beginner",
      },
      hardwareLevel: {
        type: "string",
        required: false,
        defaultValue: "none",
      },
      technologies: {
        type: "string", // JSON string
        required: false,
        defaultValue: "{}",
      },
      learningGoals: {
        type: "string",
        required: false,
      },
      role: {
        type: "string",
        required: false,
        defaultValue: "user", // 'user' or 'admin'
      },
      isAdmin: {
        type: "boolean",
        required: false,
        defaultValue: false,
      },
    },
  },
  trustedOrigins: [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    process.env.FRONTEND_URL || "",
    "https://doniabatool.github.io",
    "https://doniabatool.github.io/Interactive-Agentic-Book",
    "https://interactive-agentic-book-frontend.onrender.com",
  ].filter(Boolean),
  // Redirect configuration for OAuth callbacks
  redirect: {
    onSignIn: process.env.FRONTEND_URL || "http://localhost:3000",
  },
});

export type Session = typeof auth.$Infer.Session;
export type User = typeof auth.$Infer.Session.user;

