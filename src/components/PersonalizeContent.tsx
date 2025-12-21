import React, { useState, useCallback } from 'react';
import { useAuth } from '../context/AuthContext';

interface PersonalizeContentProps {
  chapterTitle?: string;
}

// Backend URL
const getBackendUrl = (): string => {
  if (typeof window !== 'undefined' && (window as any).__BACKEND_URL__) {
    return (window as any).__BACKEND_URL__;
  }
  return 'http://localhost:8000';
};

export const PersonalizeContent: React.FC<PersonalizeContentProps> = ({ chapterTitle }) => {
  const { user } = useAuth();
  const [isPersonalizing, setIsPersonalizing] = useState(false);
  const [isPersonalized, setIsPersonalized] = useState(false);
  const [originalContent, setOriginalContent] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const backendUrl = getBackendUrl();

  // Get user's level for display
  const getLevelBadge = () => {
    if (!user?.profile) return null;
    const sw = user.profile.software_level || 'beginner';
    const hw = user.profile.hardware_level || 'none';
    
    const levelColors: Record<string, string> = {
      beginner: '#22c55e',
      intermediate: '#eab308',
      advanced: '#ef4444',
    };
    
    return (
      <span 
        className="personalize-level-badge"
        style={{
          backgroundColor: levelColors[sw] || '#6b7280',
          color: 'white',
          padding: '2px 8px',
          borderRadius: '12px',
          fontSize: '0.75rem',
          fontWeight: 600,
          marginLeft: '8px',
        }}
      >
        {sw.charAt(0).toUpperCase() + sw.slice(1)}
      </span>
    );
  };

  const personalizeContent = useCallback(async () => {
    if (!user?.profile) {
      setError('Please sign in and complete your profile to personalize content');
      return;
    }

    // Get the article content
    const articleElement = document.querySelector('article.markdown, .markdown, main article');
    if (!articleElement) {
      setError('Could not find chapter content to personalize');
      return;
    }

    // Save original content for restore
    if (!originalContent) {
      setOriginalContent(articleElement.innerHTML);
    }

    setIsPersonalizing(true);
    setError(null);

    try {
      // Get the text content (simplified - in production you'd want to preserve markdown)
      const content = articleElement.innerHTML;

      const response = await fetch(`${backendUrl}/personalize/content`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          content,
          software_level: user.profile.software_level || 'beginner',
          hardware_level: user.profile.hardware_level || 'none',
          technologies: user.profile.technologies || {},
          chapter_title: chapterTitle || document.querySelector('h1')?.textContent || 'Chapter',
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to personalize content');
      }

      const data = await response.json();
      
      // Replace article content with personalized version
      articleElement.innerHTML = data.content;
      setIsPersonalized(true);

    } catch (err: any) {
      console.error('Personalization error:', err);
      setError(err.message || 'Failed to personalize content');
    } finally {
      setIsPersonalizing(false);
    }
  }, [user, backendUrl, chapterTitle, originalContent]);

  const restoreOriginal = useCallback(() => {
    if (!originalContent) return;

    const articleElement = document.querySelector('article.markdown, .markdown, main article');
    if (articleElement) {
      articleElement.innerHTML = originalContent;
      setIsPersonalized(false);
    }
  }, [originalContent]);

  // Don't render if user is not logged in
  if (!user) {
    return (
      <div className="personalize-container personalize-login-prompt">
        <div className="personalize-icon">🎯</div>
        <div className="personalize-text">
          <a href="/auth/signin" className="personalize-link">Sign in</a> to personalize content for your skill level
        </div>
      </div>
    );
  }

  return (
    <div className="personalize-container">
      <div className="personalize-header">
        <span className="personalize-icon">🎯</span>
        <span className="personalize-label">
          Personalize for your level
          {getLevelBadge()}
        </span>
      </div>
      
      {error && (
        <div className="personalize-error">
          {error}
        </div>
      )}

      <div className="personalize-actions">
        {!isPersonalized ? (
          <button
            className="personalize-button personalize-button-primary"
            onClick={personalizeContent}
            disabled={isPersonalizing}
          >
            {isPersonalizing ? (
              <>
                <span className="personalize-spinner"></span>
                Personalizing...
              </>
            ) : (
              <>
                ✨ Personalize Content
              </>
            )}
          </button>
        ) : (
          <div className="personalize-done">
            <span className="personalize-success-icon">✓</span>
            <span>Content personalized for your level!</span>
            <button
              className="personalize-button personalize-button-secondary"
              onClick={restoreOriginal}
            >
              Restore Original
            </button>
          </div>
        )}
      </div>

      {!user.profile?.software_level && (
        <div className="personalize-profile-hint">
          <a href="/auth/profile">Complete your profile</a> for better personalization
        </div>
      )}
    </div>
  );
};

export default PersonalizeContent;

