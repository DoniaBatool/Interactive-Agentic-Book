/**
 * useAuth Hook
 * 
 * React hook for authentication operations (login, signup, logout, getSession).
 * All functions are placeholders that make API calls to backend endpoints.
 * 
 * TODO: Real authentication logic will be implemented in a future feature.
 * Currently returns placeholder responses.
 */

import { apiCall } from '@site/src/config/api';

interface User {
  id: string;
  email: string;
  name?: string;
  role?: string;
  created_at?: string;
}

interface LoginResponse {
  user: User;
  session_token: string;
}

interface SignupResponse {
  user: User;
  message: string;
}

interface MeResponse {
  user: User;
}

/**
 * Login with email and password.
 * 
 * @param email User's email address
 * @param password User's password
 * @returns Promise with user and session token
 */
export async function login(email: string, password: string): Promise<LoginResponse> {
  const response = await apiCall('/api/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    throw new Error('Login failed (placeholder)');
  }

  const data: LoginResponse = await response.json();
  return data;
}

/**
 * Signup with email, password, optional name, and user profile for personalization.
 * 
 * @param email User's email address
 * @param password User's password
 * @param name User's full name (optional)
 * @param userProfile User background/profile for personalization (optional)
 * @returns Promise with user and message
 */
export async function signup(
  email: string,
  password: string,
  name?: string,
  userProfile?: {
    technicalBackground?: string;
    experienceLevel?: string;
    learningGoal?: string;
    preferredDepth?: string;
    domainInterests?: string[];
  }
): Promise<SignupResponse> {
  const response = await apiCall('/api/auth/signup', {
    method: 'POST',
    body: JSON.stringify({ 
      email, 
      password, 
      name,
      user_profile: userProfile, // Include user background for personalization
    }),
  });

  if (!response.ok) {
    throw new Error('Signup failed (placeholder)');
  }

  const data: SignupResponse = await response.json();
  return data;
}

/**
 * Logout current user.
 * 
 * @returns Promise<void>
 */
export async function logout(): Promise<void> {
  // TODO: Clear session token from storage
  const response = await apiCall('/api/auth/logout', {
    method: 'POST',
    body: JSON.stringify({}),
  });

  if (!response.ok) {
    throw new Error('Logout failed (placeholder)');
  }

  // TODO: Clear local state, cookies, etc.
}

/**
 * Get current user session.
 * 
 * @returns Promise with user or null if not authenticated
 */
export async function getSession(): Promise<User | null> {
  // TODO: Include session token in request
  try {
    const response = await apiCall('/api/auth/me', {
      method: 'GET',
      // TODO: Add Authorization header with session token
    });

    if (!response.ok) {
      return null;
    }

    const data: MeResponse = await response.json();
    return data.user;
  } catch (error) {
    return null;
  }
}

