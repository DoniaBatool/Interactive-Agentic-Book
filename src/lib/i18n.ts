/**
 * i18n utility for accessing translations
 * Works with Docusaurus i18n and our custom LanguageContext
 */

import { useLanguage } from '../context/LanguageContext';

// Import translation files
import enTranslations from '../../i18n/en/translations.json';
import urTranslations from '../../i18n/ur/translations.json';

// Define translation keys more flexibly to support all keys
type TranslationKey = 
  | `common.${string}`
  | `auth.${string}`
  | `profile.${string}`
  | `translation.${string}`
  | `chat.${string}`
  | `admin.${string}`;

/**
 * Hook to get translated text based on current language
 * Uses LanguageContext for language detection
 */
export function useTranslation() {
  const { currentLanguage } = useLanguage();
  const translations = currentLanguage === 'ur' ? urTranslations : enTranslations;

  const t = (key: TranslationKey): string => {
    const [namespace, ...rest] = key.split('.');
    const translationKey = rest.join('.');
    
    const namespaceObj = translations[namespace as keyof typeof translations];
    if (!namespaceObj) return key;
    
    return (namespaceObj as Record<string, string>)[translationKey] || key;
  };

  return { t, currentLanguage };
}

/**
 * Get translation without hook (for use outside React components)
 */
export function getTranslation(key: TranslationKey, language: 'en' | 'ur' = 'en'): string {
  const translations = language === 'ur' ? urTranslations : enTranslations;
  const [namespace, ...rest] = key.split('.');
  const translationKey = rest.join('.');
  
  const namespaceObj = translations[namespace as keyof typeof translations];
  if (!namespaceObj) return key;
  
  return (namespaceObj as Record<string, string>)[translationKey] || key;
}

