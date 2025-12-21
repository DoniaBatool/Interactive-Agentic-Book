import React, { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react';

// Types
interface LanguageContextType {
  currentLanguage: 'en' | 'ur';
  toggleLanguage: () => void;
  translateChapter: (chapterPath: string, content: string) => Promise<string>;
  isTranslating: boolean;
  translationError: string | null;
  clearError: () => void;
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

import { BACKEND_URL } from '../config/env';

// Backend URL
const getBackendUrl = (): string => {
  if (typeof window !== 'undefined' && (window as any).__BACKEND_URL__) {
    return (window as any).__BACKEND_URL__;
  }
  return BACKEND_URL;
};

export const LanguageProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [currentLanguage, setCurrentLanguage] = useState<'en' | 'ur'>('en');
  const [isTranslating, setIsTranslating] = useState(false);
  const [translationError, setTranslationError] = useState<string | null>(null);
  
  const backendUrl = getBackendUrl();

  // Always default to English on mount - don't load from localStorage
  // User must manually toggle to Urdu on each page
  // IMPORTANT: Set document direction immediately on mount to prevent RTL flash
  useEffect(() => {
    if (typeof window !== 'undefined') {
      // Always set to English/LTR on mount
      setCurrentLanguage('en');
      document.documentElement.setAttribute('dir', 'ltr');
      document.documentElement.setAttribute('lang', 'en');
      document.documentElement.classList.remove('rtl-mode');
    }
  }, []);

  // Update document attributes when language changes
  // Don't save to localStorage - each page should default to English
  useEffect(() => {
    if (typeof window !== 'undefined') {
      // Update document attributes
      document.documentElement.setAttribute('lang', currentLanguage);
      document.documentElement.setAttribute('dir', currentLanguage === 'ur' ? 'rtl' : 'ltr');
      
      // Add/remove RTL class for styling
      if (currentLanguage === 'ur') {
        document.documentElement.classList.add('rtl-mode');
      } else {
        document.documentElement.classList.remove('rtl-mode');
      }
      
      // Load Urdu fonts if needed
      if (currentLanguage === 'ur') {
        loadUrduFonts();
      }
    }
  }, [currentLanguage]);

  const loadUrduFonts = useCallback(() => {
    // Check if fonts are already loaded
    const existingLink = document.querySelector('link[href*="Noto+Nastaliq+Urdu"]');
    if (existingLink) return;

    // Load Google Fonts for Urdu
    const link = document.createElement('link');
    link.href = 'https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;600;700&display=swap';
    link.rel = 'stylesheet';
    link.crossOrigin = 'anonymous';
    document.head.appendChild(link);
  }, []);

  const toggleLanguage = useCallback(() => {
    setCurrentLanguage(prev => prev === 'en' ? 'ur' : 'en');
    setTranslationError(null);
  }, []);

  const translateChapter = useCallback(async (chapterPath: string, content: string): Promise<string> => {
    setIsTranslating(true);
    setTranslationError(null);

    try {
      // Add timeout for translation request (increased for large content with chunking)
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 300000); // 5 minute timeout for large chapters

      const response = await fetch(`${backendUrl}/translate/chapter`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          chapter_path: chapterPath,
          content,
          target_language: 'ur',
          force_retranslate: false
        }),
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Translation failed: ${response.status}`);
      }

      const data = await response.json();
      
      // Log translation info
      const cacheStatus = data.cached ? 'cached' : 'fresh';
      const timeInfo = data.cached ? 'instant' : `${data.translation_time_ms}ms`;
      console.log(`Translation completed: ${cacheStatus}, time=${timeInfo}`);
      
      return data.translated_content;

    } catch (error: any) {
      let errorMessage = 'Translation failed';
      
      if (error.name === 'AbortError') {
        errorMessage = 'Translation timed out. Please try again.';
      } else if (error.message?.includes('fetch') || error.message?.includes('Network')) {
        errorMessage = 'Network error. Check if backend is running.';
      } else if (error.message?.includes('500')) {
        errorMessage = 'Server error. Please try again later.';
      } else if (error.message?.includes('400')) {
        errorMessage = 'Invalid request. Content may be too large or invalid.';
      } else {
        errorMessage = error.message || 'Translation failed';
      }
      
      setTranslationError(errorMessage);
      console.error('Translation error:', {
        chapterPath,
        errorName: error.name,
        errorMessage: error.message,
        errorStack: error.stack,
        response: error.response
      });
      throw new Error(errorMessage);
    } finally {
      setIsTranslating(false);
    }
  }, [backendUrl]);

  const clearError = useCallback(() => {
    setTranslationError(null);
  }, []);

  return (
    <LanguageContext.Provider
      value={{
        currentLanguage,
        toggleLanguage,
        translateChapter,
        isTranslating,
        translationError,
        clearError,
      }}
    >
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = (): LanguageContextType => {
  const context = useContext(LanguageContext);
  if (context === undefined) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};

export default LanguageContext;
