import { createAuthClient } from "better-auth/react";

// BetterAuth client configuration
export const authClient = createAuthClient({
  baseURL: "http://localhost:8002", // BetterAuth server (backend uses 8001)
});

// Export hooks and methods
export const {
  signIn,
  signUp,
  signOut,
  useSession,
  getSession,
} = authClient;

// Types
export type Session = typeof authClient.$Infer.Session;
export type User = typeof authClient.$Infer.Session.user;

