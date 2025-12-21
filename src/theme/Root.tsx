import React, { useEffect } from 'react';
import { AuthProvider } from '../context/AuthContext';
import { LanguageProvider } from '../context/LanguageContext';
import FloatingChatButton from '../components/FloatingChatButton';

// This component wraps the entire Docusaurus app
export default function Root({ children }: { children: React.ReactNode }): React.JSX.Element {
  // Set initial document direction to LTR immediately (before React renders)
  // Always default to English - don't load from localStorage
  useEffect(() => {
    if (typeof window !== 'undefined' && typeof document !== 'undefined') {
      // Always set to English/LTR on initial load
      document.documentElement.setAttribute('dir', 'ltr');
      document.documentElement.setAttribute('lang', 'en');
      document.documentElement.classList.remove('rtl-mode');
    }
  }, []);

  return (
    <AuthProvider>
      <LanguageProvider>
        {children}
        <FloatingChatButton />
      </LanguageProvider>
    </AuthProvider>
  );
}
