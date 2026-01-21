import React, { useState, useEffect, useCallback, ReactNode } from 'react';
import { useLanguage } from '../context/LanguageContext';
import { useTranslation } from '../lib/i18n';

interface TranslatableContentProps {
  chapterPath: string;
  children: ReactNode;
}

export const TranslatableContent: React.FC<TranslatableContentProps> = ({ 
  chapterPath, 
  children 
}) => {
  const { currentLanguage, translateChapter, translationError, clearError } = useLanguage();
  const { t } = useTranslation();
  const [translatedContent, setTranslatedContent] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [originalContent, setOriginalContent] = useState<string>('');

  // Note: Course-overview page is now included in translation
  // Only home page (/) is excluded via LanguageToggle component

  const handleTranslation = useCallback(async () => {
    if (!originalContent || isLoading) {
      console.log('Skipping translation:', { hasContent: !!originalContent, isLoading });
      return;
    }

    setIsLoading(true);
    clearError();

    try {
      // Extract text content for length check
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = originalContent;
      const textContent = tempDiv.textContent || tempDiv.innerText || '';
      
      console.log(`Translation request for ${chapterPath}: ${textContent.length} chars`);
      
      if (textContent.trim().length < 50) {
        // Content too short to translate meaningfully
        console.warn(`Content too short for ${chapterPath}, skipping translation`);
        setTranslatedContent(originalContent);
        setIsLoading(false);
        return;
      }

      // For very large content, show a warning
      if (textContent.length > 15000) {
        console.warn(`Large content detected for ${chapterPath}: ${textContent.length} chars, translation may take longer`);
      }

      const translated = await translateChapter(chapterPath, originalContent);
      setTranslatedContent(translated);
      console.log(`Translation successful for ${chapterPath}`);

    } catch (error: any) {
      console.error(`Translation failed for ${chapterPath}:`, error);
      console.error('Error details:', {
        chapterPath,
        contentLength: originalContent.length,
        errorMessage: error?.message,
        errorName: error?.name,
        errorStack: error?.stack
      });
      // Error is already set in LanguageContext
      setTranslatedContent(null);
    } finally {
      setIsLoading(false);
    }
  }, [chapterPath, originalContent, translateChapter, clearError, isLoading]);

  // Extract content when component mounts or chapter path changes
  useEffect(() => {
    if (typeof window !== 'undefined') {
      // Reset content when chapter changes
      setOriginalContent('');
      setTranslatedContent(null);
      clearError();
      
      // Wait for DOM to be ready
      const extractContent = () => {
        // For home page, extract from main or hero section
        if (chapterPath === '/' || chapterPath === '/index.html') {
          const mainElement = document.querySelector('main, .hero, [role="main"]');
          if (mainElement) {
            const content = mainElement.innerHTML;
            if (content && content.trim().length > 0) {
              setOriginalContent(content);
              console.log(`Home page content extracted: ${content.length} chars`);
              return;
            }
          }
        }
        
        // Try multiple selectors for different page types (docs pages)
        // IMPORTANT: Avoid extracting <main> for docs pages because it can include
        // non-doc UI (e.g., Personalize panel), which would then appear twice after translation.
        const selectors = [
          'article.markdown',
          'main article.markdown',
          '[role="main"] article.markdown',
          '.theme-doc-markdown',
          '.theme-doc-markdown article',
          '[itemprop="articleBody"]',
          'article'
        ];
        
        let articleElement: Element | null = null;
        for (const selector of selectors) {
          articleElement = document.querySelector(selector);
          if (articleElement) {
            console.log(`Found content element with selector: ${selector} for ${chapterPath}`);
            break;
          }
        }
        
        if (articleElement) {
          // Safety: strip UI blocks that should never be translated/injected as raw HTML
          // (prevents duplicates like Personalize panel showing twice).
          const tempDiv = document.createElement('div');
          tempDiv.innerHTML = articleElement.innerHTML;
          tempDiv.querySelectorAll('.personalize-container').forEach((el) => el.remove());

          const content = tempDiv.innerHTML;
          if (content && content.trim().length > 0) {
            setOriginalContent(content);
            console.log(`Content extracted for ${chapterPath}: ${content.length} chars`);
          } else {
            console.warn(`Empty content found for ${chapterPath}`);
          }
        } else {
          console.warn(`No article element found for ${chapterPath}. Selectors tried:`, selectors);
          // Do not fall back to extracting <main> for docs pages (causes duplicated UI after translation).
        }
      };
      
      // Try immediately
      extractContent();
      
      // Retry multiple times with increasing delays
      const timeout1 = setTimeout(extractContent, 100);
      const timeout2 = setTimeout(extractContent, 500);
      const timeout3 = setTimeout(extractContent, 1000);
      
      return () => {
        clearTimeout(timeout1);
        clearTimeout(timeout2);
        clearTimeout(timeout3);
      };
    }
  }, [chapterPath, clearError]);

  // Handle language change
  useEffect(() => {
    if (currentLanguage === 'ur' && !translatedContent && originalContent && !isLoading) {
      console.log(`Language changed to Urdu for ${chapterPath}, starting translation...`);
      handleTranslation();
    } else if (currentLanguage === 'en') {
      // Reset to original content when switching back to English
      console.log(`Language changed to English for ${chapterPath}, resetting content...`);
      setTranslatedContent(null);
      clearError();
    }
  }, [currentLanguage, originalContent, chapterPath, translatedContent, isLoading, handleTranslation, clearError]);

  const retryTranslation = useCallback(() => {
    setTranslatedContent(null);
    clearError();
    handleTranslation();
  }, [handleTranslation, clearError]);

  // Show loading state
  if (currentLanguage === 'ur' && isLoading) {
    return (
      <div className="translation-loading-container">
        <div className="translation-loading-overlay">
          <div className="translation-loading-spinner">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
              <circle
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeDasharray="32"
                strokeDashoffset="32"
              >
                <animate
                  attributeName="stroke-dasharray"
                  dur="2s"
                  values="0 32;16 16;0 32;0 32"
                  repeatCount="indefinite"
                />
                <animate
                  attributeName="stroke-dashoffset"
                  dur="2s"
                  values="0;-16;-32;-32"
                  repeatCount="indefinite"
                />
              </circle>
            </svg>
          </div>
          <div className="translation-loading-text">
            <div>{t('translation.translatingContent')}</div>
            <div style={{ fontSize: '0.875rem', opacity: 0.7, marginTop: '0.5rem' }}>
              {t('translation.expectedTime')}
            </div>
          </div>
        </div>
        <div className="translation-loading-content">
          {children}
        </div>
      </div>
    );
  }

  // Show error state
  if (currentLanguage === 'ur' && translationError) {
    return (
      <div className="translation-error-container">
        <div className="translation-error-banner">
          <div className="translation-error-icon">⚠️</div>
          <div className="translation-error-content">
            <div className="translation-error-title">
              {t('translation.translationError')}
            </div>
            <div className="translation-error-message">
              {translationError}
            </div>
            <button 
              className="translation-retry-button"
              onClick={retryTranslation}
            >
              {t('common.retry')}
            </button>
          </div>
        </div>
        <div className="translation-fallback-content">
          {children}
        </div>
      </div>
    );
  }

  // Show translated content for Urdu
  if (currentLanguage === 'ur' && translatedContent) {
    return (
      <div className="urdu-content-container">
        <div 
          className="urdu-content"
          dangerouslySetInnerHTML={{ __html: translatedContent }}
        />
      </div>
    );
  }

  // Show original content for English or when no translation available
  return <>{children}</>;
};

export default TranslatableContent;
