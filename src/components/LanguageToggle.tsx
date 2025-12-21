import React from 'react';
import { useLocation } from '@docusaurus/router';
import { useLanguage } from '../context/LanguageContext';
import { useTranslation } from '../lib/i18n';

export const LanguageToggle: React.FC = () => {
  const { currentLanguage, toggleLanguage, isTranslating } = useLanguage();
  const { t } = useTranslation();
  const location = useLocation();

  return (
    <button
      className="language-toggle"
      onClick={toggleLanguage}
      disabled={isTranslating}
      aria-label={currentLanguage === 'en' ? t('common.switchToUrdu') : t('common.switchToEnglish')}
      title={currentLanguage === 'en' ? t('common.switchToUrdu') : t('common.switchToEnglish')}
    >
      {isTranslating ? (
        <span className="language-toggle-spinner">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
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
        </span>
      ) : (
        <span className="language-toggle-text">
          {currentLanguage === 'en' ? (
            <>
              <span className="language-label">{t('common.urdu')}</span>
              <span className="language-icon">🌐</span>
            </>
          ) : (
            <>
              <span className="language-label">{t('common.english')}</span>
              <span className="language-icon">🌐</span>
            </>
          )}
        </span>
      )}
    </button>
  );
};

export default LanguageToggle;
