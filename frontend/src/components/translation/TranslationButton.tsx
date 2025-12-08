import React, { useState } from 'react';
import styles from './styles.module.css';
import { apiCall } from '@site/src/config/api';

interface TranslationButtonProps {
  chapterId: number;
  currentLanguage?: string;
  onLanguageChange?: (language: string) => void;
}

const SUPPORTED_LANGUAGES = [
  { code: 'en', name: 'English', flag: '🇬🇧' },
  { code: 'ur', name: 'Urdu', flag: '🇵🇰' },
  { code: 'ru', name: 'Roman Urdu', flag: '📝' },
  { code: 'ar', name: 'Arabic', flag: '🇸🇦' },
];

const TranslationButton: React.FC<TranslationButtonProps> = ({
  chapterId,
  currentLanguage = 'en',
  onLanguageChange,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState(currentLanguage);

  const handleLanguageChange = async (languageCode: string) => {
    if (languageCode === currentLanguage) {
      setIsOpen(false);
      return;
    }

    setIsLoading(true);
    try {
      const response = await apiCall(`/api/translation/chapter/${chapterId}`, {
        method: 'POST',
        body: JSON.stringify({ 
          target_language: languageCode,
          source_language: currentLanguage,
        }),
      });

      if (!response.ok) {
        throw new Error('Translation request failed');
      }

      const data = await response.json();
      
      // Update the state
      setSelectedLanguage(languageCode);
      
      if (onLanguageChange) {
        onLanguageChange(languageCode);
      }
      
      // Show success message
      const langName = SUPPORTED_LANGUAGES.find(l => l.code === languageCode)?.name || languageCode;
      alert(data.message || `Content translated to ${langName}!`);
      setIsOpen(false);
    } catch (error) {
      console.error('Translation error:', error);
      alert('Failed to translate content. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const currentLang = SUPPORTED_LANGUAGES.find(l => l.code === selectedLanguage) || SUPPORTED_LANGUAGES[0];

  return (
    <div className={styles.translationContainer}>
      <button
        className={styles.translateButton}
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Translate Content"
        disabled={isLoading}
      >
        🌐 {currentLang.flag} {currentLang.name}
        {isLoading && ' (Translating...)'}
      </button>

      {isOpen && (
        <>
          <div className={styles.overlay} onClick={() => setIsOpen(false)} />
          <div className={styles.dropdown}>
            <div className={styles.dropdownHeader}>
              <h4>Select Language</h4>
              <button
                className={styles.closeButton}
                onClick={() => setIsOpen(false)}
                aria-label="Close"
              >
                ×
              </button>
            </div>
            <div className={styles.languageList}>
              {SUPPORTED_LANGUAGES.map((lang) => (
                <button
                  key={lang.code}
                  className={`${styles.languageOption} ${
                    selectedLanguage === lang.code ? styles.active : ''
                  }`}
                  onClick={() => handleLanguageChange(lang.code)}
                  disabled={isLoading}
                >
                  <span className={styles.flag}>{lang.flag}</span>
                  <span className={styles.languageName}>{lang.name}</span>
                  {selectedLanguage === lang.code && (
                    <span className={styles.checkmark}>✓</span>
                  )}
                </button>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default TranslationButton;

