import { createAuthClient } from "better-auth/client";
import { AUTH_SERVER_URL } from "../config/env";

// BetterAuth client configuration
export const authClient = createAuthClient({
  baseURL: AUTH_SERVER_URL,
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

