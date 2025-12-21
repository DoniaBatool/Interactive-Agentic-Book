/**
 * Environment configuration
 * Automatically detects production vs development
 */

const isProduction = typeof window !== 'undefined' && 
  (window.location.hostname !== 'localhost' && 
   window.location.hostname !== '127.0.0.1');

// Auth Server URL
// In production, this should be your deployed auth server URL
// You can override this by setting window.__AUTH_URL__ in your HTML
export const AUTH_SERVER_URL = (() => {
  if (typeof window !== 'undefined') {
    // Check for manual override (useful for testing)
    if ((window as any).__AUTH_URL__) {
      return (window as any).__AUTH_URL__;
    }
    
    // Production URL - Render auth server
    if (isProduction) {
      return 'https://interactive-agentic-book.onrender.com';
    }
  }
  
  // Development default
  return 'http://localhost:8002';
})();

// Backend API URL (FastAPI)
export const BACKEND_URL = (() => {
  if (typeof window !== 'undefined') {
    if ((window as any).__BACKEND_URL__) {
      return (window as any).__BACKEND_URL__;
    }
    
    if (isProduction) {
      // TODO: Replace with your actual backend URL when deployed to Render
      // For now, using localhost as backend is not deployed yet
      // When backend is deployed, update this to: 'https://your-backend.onrender.com'
      return 'http://localhost:8000'; // TODO: Update to production URL when backend is deployed
    }
  }
  
  return 'http://localhost:8000';
})();

// Frontend URL
export const FRONTEND_URL = (() => {
  if (typeof window !== 'undefined') {
    return window.location.origin;
  }
  return 'http://localhost:3000';
})();

