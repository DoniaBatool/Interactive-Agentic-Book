import React, { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react';
import { AUTH_SERVER_URL } from '../config/env';

// Types
interface UserProfile {
  software_level: string;
  hardware_level: string;
  technologies: Record<string, boolean>;
  learning_goals?: string;
}

interface User {
  id: string;
  email: string;
  name?: string;
  softwareLevel?: string;
  hardwareLevel?: string;
  technologies?: string; // JSON string
  learningGoals?: string;
  profile?: UserProfile; // Computed from user fields
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  error: string | null;
  login: (email: string, password: string, rememberMe?: boolean) => Promise<boolean>;
  signup: (data: SignupData) => Promise<boolean>;
  logout: () => Promise<void>;
  updateProfile: (profile: Partial<UserProfile>) => Promise<boolean>;
  clearError: () => void;
  refreshSession: () => Promise<void>;
}

interface SignupData {
  email: string;
  password: string;
  name?: string;
  profile?: Partial<UserProfile>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Helper to convert user data to profile
const userToProfile = (user: User): UserProfile => {
  let technologies: Record<string, boolean> = {};
  try {
    if (user.technologies) {
      technologies = JSON.parse(user.technologies);
    }
  } catch {
    technologies = {};
  }
  
  return {
    software_level: user.softwareLevel || 'beginner',
    hardware_level: user.hardwareLevel || 'none',
    technologies,
    learning_goals: user.learningGoals,
  };
};

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  // Initialize user from localStorage so that user info is immediately available
  // after a full page reload (e.g., after redirects on GitHub Pages)
  const [user, setUser] = useState<User | null>(() => {
    if (typeof window === 'undefined') return null;
    try {
      const stored = localStorage.getItem('auth_user');
      if (stored) {
        return JSON.parse(stored) as User;
      }
    } catch (e) {
      console.debug('Failed to read auth_user from localStorage:', e);
    }
    return null;
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  const authUrl = AUTH_SERVER_URL;

  // Check session on mount
  const refreshSession = useCallback(async () => {
    try {
      const response = await fetch(`${authUrl}/api/auth/get-session`, {
        credentials: 'include',
      });
      
      if (response.ok) {
        const data = await response.json();
        if (data.session && data.user) {
          const userData = {
            ...data.user,
            profile: userToProfile(data.user),
          };
          // Debug: Log user data to check admin fields
          console.log('🔍 User session data:', {
            email: userData.email,
            isAdmin: (userData as any).isAdmin,
            role: (userData as any).role,
            fullUser: userData
          });
          setUser(userData);
          try {
            localStorage.setItem('auth_user', JSON.stringify(userData));
          } catch (e) {
            console.debug('Failed to store auth_user in localStorage:', e);
          }
        } else {
          // Only clear user if we're sure there's no session
          // Don't clear if we have a cached user (might be a temporary network issue)
          const cachedUser = localStorage.getItem('auth_user');
          if (!cachedUser) {
            setUser(null);
            try {
              localStorage.removeItem('auth_user');
            } catch {
              // ignore
            }
          }
        }
      } else {
        // Only clear if status is 401/403 (unauthorized), not for other errors
        if (response.status === 401 || response.status === 403) {
          setUser(null);
          try {
            localStorage.removeItem('auth_user');
          } catch {
            // ignore
          }
        }
        // For other errors, keep cached user if available
      }
    } catch (err) {
      console.debug('Session check failed:', err);
      // Don't clear user on network errors - keep cached user
      // Only clear if we're sure there's no valid session
    } finally {
      setLoading(false);
    }
  }, [authUrl]);

  useEffect(() => {
    refreshSession();
  }, [refreshSession]);

  const login = useCallback(async (
    email: string,
    password: string,
    rememberMe: boolean = false
  ): Promise<boolean> => {
    setError(null);
    setLoading(true);

    try {
      const response = await fetch(`${authUrl}/api/auth/sign-in/email`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ 
          email, 
          password,
          rememberMe,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        if (data.user) {
          const userData = {
            ...data.user,
            profile: userToProfile(data.user),
          };
          setUser(userData);
          try {
            localStorage.setItem('auth_user', JSON.stringify(userData));
          } catch (e) {
            console.debug('Failed to store auth_user in localStorage after login:', e);
          }
          // Ensure loading is false after setting user
          setLoading(false);
          return true;
        }
        // Refresh session to get user data
        await refreshSession();
        setLoading(false);
        return true;
      } else {
        const errorData = await response.json().catch(() => ({}));
        setError(errorData.message || errorData.error || 'Login failed');
        return false;
      }
    } catch (err: any) {
      setError(err.message || 'Network error');
      return false;
    } finally {
      setLoading(false);
    }
  }, [authUrl, refreshSession]);

  const signup = useCallback(async (data: SignupData): Promise<boolean> => {
    setError(null);
    setLoading(true);

    try {
      // Prepare additional fields for BetterAuth
      const additionalFields: Record<string, any> = {
        name: data.name || '',
      };
      
      if (data.profile) {
        additionalFields.softwareLevel = data.profile.software_level || 'beginner';
        additionalFields.hardwareLevel = data.profile.hardware_level || 'none';
        additionalFields.technologies = JSON.stringify(data.profile.technologies || {});
        additionalFields.learningGoals = data.profile.learning_goals || '';
      }

      const response = await fetch(`${authUrl}/api/auth/sign-up/email`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({
          email: data.email,
          password: data.password,
          ...additionalFields,
        }),
      });

      let responseData: any = {};
      try {
        const text = await response.text();
        if (text) {
          responseData = JSON.parse(text);
        }
      } catch (e) {
        console.error('Failed to parse response:', e);
      }

      if (response.ok) {
        if (responseData.user) {
          const userData = {
            ...responseData.user,
            profile: userToProfile(responseData.user),
          };
          setUser(userData);
          try {
            localStorage.setItem('auth_user', JSON.stringify(userData));
          } catch (e) {
            console.debug('Failed to store auth_user in localStorage after signup:', e);
          }
        }
        return true;
      } else {
        // BetterAuth error format: { message: string } or { error: { message: string } }
        let errorMessage = 'Failed to create user';
        
        // Try different error formats
        if (responseData.message) {
          errorMessage = responseData.message;
        } else if (responseData.error) {
          if (typeof responseData.error === 'string') {
            errorMessage = responseData.error;
          } else if (responseData.error.message) {
            errorMessage = responseData.error.message;
          } else if (responseData.error.code) {
            errorMessage = `${responseData.error.code}: ${responseData.error.message || 'Unknown error'}`;
          }
        } else if (responseData.errors) {
          // Handle validation errors
          if (Array.isArray(responseData.errors)) {
            errorMessage = responseData.errors.map((e: any) => e.message || e).join(', ');
          } else if (typeof responseData.errors === 'object') {
            errorMessage = Object.values(responseData.errors).join(', ');
          }
        } else if (responseData.statusCode && responseData.message) {
          errorMessage = responseData.message;
        }
        
        // Log detailed error for debugging
        console.error('Signup error details:', {
          status: response.status,
          statusText: response.statusText,
          responseData: responseData,
          requestBody: {
            email: data.email,
            hasPassword: !!data.password,
            hasName: !!data.name,
            hasProfile: !!data.profile
          }
        });
        
        setError(errorMessage);
        return false;
      }
    } catch (err: any) {
      setError(err.message || 'Network error');
      return false;
    } finally {
      setLoading(false);
    }
  }, [authUrl]);

  const logout = useCallback(async () => {
    try {
      // Call BetterAuth sign-out endpoint
      const response = await fetch(`${authUrl}/api/auth/sign-out`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      // Check if logout was successful
      if (!response.ok) {
        console.error('Logout failed:', response.status, response.statusText);
      }

      // Clear user state immediately
      setUser(null);
      
      // Clear any local storage or session storage
      try {
        localStorage.removeItem('auth_user');
        sessionStorage.clear();
      } catch (e) {
        // Ignore storage errors
      }

      // Refresh session to ensure it's cleared
      await refreshSession();
      
    } catch (err) {
      console.error('Logout request failed:', err);
      // Even if request fails, clear local state
      setUser(null);
      try {
        localStorage.removeItem('auth_user');
        sessionStorage.clear();
      } catch (e) {
        // Ignore storage errors
      }
    }
  }, [authUrl, refreshSession]);

  const updateProfile = useCallback(async (profile: Partial<UserProfile>): Promise<boolean> => {
    setError(null);

    try {
      // BetterAuth uses update-user endpoint
      const updateData: Record<string, any> = {};
      
      if (profile.software_level !== undefined) {
        updateData.softwareLevel = profile.software_level;
      }
      if (profile.hardware_level !== undefined) {
        updateData.hardwareLevel = profile.hardware_level;
      }
      if (profile.technologies !== undefined) {
        updateData.technologies = JSON.stringify(profile.technologies);
      }
      if (profile.learning_goals !== undefined) {
        updateData.learningGoals = profile.learning_goals;
      }

      const response = await fetch(`${authUrl}/api/auth/update-user`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(updateData),
      });

      if (response.ok) {
        // Refresh session to get updated user
        await refreshSession();
        return true;
      } else {
        const errorData = await response.json().catch(() => ({}));
        setError(errorData.message || 'Profile update failed');
        return false;
      }
    } catch (err: any) {
      setError(err.message || 'Network error');
      return false;
    }
  }, [authUrl, refreshSession]);

  const clearError = useCallback(() => {
    setError(null);
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        error,
        login,
        signup,
        logout,
        updateProfile,
        clearError,
        refreshSession,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export default AuthContext;
