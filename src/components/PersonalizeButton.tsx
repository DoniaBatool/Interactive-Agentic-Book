import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { useTranslation } from '../lib/i18n';

interface PersonalizeButtonProps {
  chapter?: string;
  onPersonalize?: (level: string) => void;
}

const PersonalizeButton: React.FC<PersonalizeButtonProps> = ({ chapter, onPersonalize }) => {
  const { user, loading } = useAuth();
  const { t } = useTranslation();
  const [isHovered, setIsHovered] = useState(false);

  if (loading) {
    return null;
  }

  // If user is not logged in, show a sign-in prompt
  if (!user) {
    return (
      <a
        href="/auth/signup"
        className="personalize-button personalize-button-signin"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        <svg
          width="16"
          height="16"
          viewBox="0 0 16 16"
          fill="none"
          className="personalize-icon"
        >
          <path
            d="M8 8a3 3 0 100-6 3 3 0 000 6zM2 14a6 6 0 0112 0H2z"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
        <span className="personalize-text">
          {isHovered ? t('common.signUpToPersonalize') : t('common.personalize')}
        </span>
      </a>
    );
  }

  // User is logged in - show their level and option to adjust
  const profile = user.profile;
  const level = profile?.software_level || 'beginner';
  const levelLabel = {
    beginner: t('profile.beginner'),
    intermediate: t('profile.intermediate'),
    advanced: t('profile.advanced'),
  }[level] || t('profile.beginner');

  const handleClick = () => {
    if (onPersonalize) {
      onPersonalize(level);
    } else {
      // Default: go to profile page
      window.location.href = '/auth/profile';
    }
  };

  return (
    <button
      className="personalize-button personalize-button-active"
      onClick={handleClick}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      title="Adjust content level"
    >
      <svg
        width="16"
        height="16"
        viewBox="0 0 16 16"
        fill="none"
        className="personalize-icon"
      >
        <path
          d="M13.5 4.5l-7.5 7.5-3-3M3 8l2 2 6-6"
          stroke="currentColor"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
      <span className="personalize-level">{levelLabel}</span>
      {isHovered && (
        <svg
          width="12"
          height="12"
          viewBox="0 0 12 12"
          fill="none"
          className="personalize-edit-icon"
        >
          <path
            d="M8.5 1.5l2 2L3 11H1v-2l7.5-7.5z"
            stroke="currentColor"
            strokeWidth="1"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      )}
    </button>
  );
};

export default PersonalizeButton;

