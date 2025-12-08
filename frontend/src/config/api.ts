/**
 * API Configuration
 * 
 * Centralized API base URL configuration for frontend.
 */

// Get API base URL from environment or use default
const getApiBaseUrl = (): string => {
  // Priority 1: Check for environment variable (set during build)
  // This allows setting REACT_APP_API_URL or NEXT_PUBLIC_API_URL during build
  if (typeof process !== 'undefined' && process.env) {
    const envApiUrl = process.env.REACT_APP_API_URL || 
                     process.env.NEXT_PUBLIC_API_URL || 
                     process.env.VITE_API_URL;
    if (envApiUrl) {
      return envApiUrl;
    }
  }
  
  // Priority 2: Check for window.API_BASE_URL (set via script tag in HTML)
  if (typeof window !== 'undefined' && (window as any).API_BASE_URL) {
    return (window as any).API_BASE_URL;
  }
  
  // Priority 3: Development mode (localhost)
  if (typeof window !== 'undefined') {
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      return 'http://localhost:8000';
    }
    
    // Priority 4: GitHub Pages → Render Backend
    // If deployed on GitHub Pages, automatically use Render backend
    if (window.location.hostname === 'doniabatool.github.io') {
      return 'https://ai-robotics-textbook-backend.onrender.com';
    }
  }
  
  // Priority 5: Production - use relative URLs (same origin) or default
  // If backend is on different domain, set REACT_APP_API_URL during build
  // Example: REACT_APP_API_URL=https://your-backend.onrender.com npm run build
  return '';
};

export const API_BASE_URL = getApiBaseUrl();

/**
 * Helper function to make API calls with proper base URL.
 */
export const apiCall = async (endpoint: string, options: RequestInit = {}): Promise<Response> => {
  const url = endpoint.startsWith('http') ? endpoint : `${API_BASE_URL}${endpoint}`;
  return fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });
};

