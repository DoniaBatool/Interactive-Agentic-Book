import React, { useState, useEffect, useCallback } from 'react';
import { useLocation } from '@docusaurus/router';
import RagChat from './RagChat';

// Persist isOpen state in sessionStorage to survive page navigations
const STORAGE_KEY = 'rag-chat-panel-open';

function getChapterFromPath(pathname: string): string | undefined {
  if (pathname.includes('/modules/intro')) {
    return 'Introduction to Physical AI';
  } else if (pathname.includes('/modules/ros2')) {
    return 'ROS 2 Nervous System';
  } else if (pathname.includes('/modules/gazebo-unity')) {
    return 'Gazebo & Unity Digital Twin';
  } else if (pathname.includes('/modules/nvidia-isaac')) {
    return 'NVIDIA Isaac AI Brain';
  } else if (pathname.includes('/modules/vla-capstone')) {
    return 'Vision-Language-Action Capstone';
  } else if (pathname.includes('/course-overview')) {
    return 'Course Overview';
  }
  return undefined;
}

export const FloatingChatButton: React.FC = () => {
  const location = useLocation();
  const [isOpen, setIsOpen] = useState(false);
  const [currentChapter, setCurrentChapter] = useState<string | undefined>(undefined);
  const [mounted, setMounted] = useState(false);

  // Run only on client after mount
  useEffect(() => {
    setMounted(true);
    // Restore isOpen from sessionStorage
    const saved = sessionStorage.getItem(STORAGE_KEY);
    if (saved === 'true') {
      setIsOpen(true);
    }
    // Set initial chapter
    setCurrentChapter(getChapterFromPath(window.location.pathname));
  }, []);

  // Persist isOpen state to sessionStorage
  useEffect(() => {
    if (mounted) {
      sessionStorage.setItem(STORAGE_KEY, isOpen ? 'true' : 'false');
    }
  }, [isOpen, mounted]);

  // Update chapter when location changes
  useEffect(() => {
    if (!mounted) return;
    
    const updateChapter = () => {
      const path = window.location.pathname;
      let chapter = getChapterFromPath(path);
      
      // Fallback: try to get from page H1 if path doesn't match
      if (!chapter) {
        const h1 = document.querySelector('article h1, .markdown h1, h1');
        const title = h1?.textContent?.trim();
        if (title && title.length > 0 && title.length < 100) {
          chapter = title;
        }
      }
      
      setCurrentChapter(chapter);
    };
    
    // Update immediately
    updateChapter();
    
    // Also update after a short delay (for DOM to settle)
    const timeoutId = setTimeout(updateChapter, 200);
    
    return () => clearTimeout(timeoutId);
  }, [mounted, location.pathname, location.key]);

  // Toggle handler
  const handleToggle = useCallback(() => {
    setIsOpen(prev => !prev);
  }, []);

  // Close handler
  const handleClose = useCallback(() => {
    setIsOpen(false);
  }, []);

  // ALWAYS render the button (even during SSR) - just hide interactivity
  // This fixes the "button not appearing" issue
  return (
    <>
      {/* Floating Button - Bottom Right - ALWAYS VISIBLE */}
      <button
        className="floating-chat-button"
        onClick={handleToggle}
        aria-label={isOpen ? 'Close chat assistant' : 'Open chat assistant'}
        title="Chat with AI Assistant"
        style={{ display: mounted ? 'flex' : 'none' }}
      >
        {isOpen ? (
          // Close icon when open
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        ) : (
          // Chat icon when closed
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M12 2C6.48 2 2 6.48 2 12c0 1.54.36 2.98.97 4.29L1 23l6.71-1.97C9.02 21.64 10.46 22 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2zm0 18c-1.38 0-2.68-.35-3.81-.96L4 20l.96-4.19C4.35 14.68 4 13.38 4 12c0-4.41 3.59-8 8-8s8 3.59 8 8-3.59 8-8 8z"
              fill="currentColor"
            />
            <circle cx="9" cy="12" r="1.5" fill="currentColor" />
            <circle cx="15" cy="12" r="1.5" fill="currentColor" />
          </svg>
        )}
        {!isOpen && <span className="floating-chat-pulse"></span>}
      </button>

      {/* Chat Panel - Right Side Vertical Panel */}
      {mounted && isOpen && (
        <div 
          className="floating-chat-sidebar"
          style={{
            position: 'fixed',
            top: 0,
            right: 0,
            width: '400px',
            maxWidth: '100vw',
            height: '100vh',
            zIndex: 9999,
            display: 'flex',
            flexDirection: 'column',
            background: '#ffffff', // Solid white fallback
            backgroundColor: 'var(--ifm-background-color)',
            borderLeft: '1px solid var(--ifm-toc-border-color, #eee)',
            boxShadow: '-8px 0 30px rgba(0,0,0,0.2)',
          }}
        >
          <div 
            className="floating-chat-sidebar-header"
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              padding: '1rem 1.25rem',
              borderBottom: '1px solid var(--ifm-toc-border-color, #eee)',
              backgroundColor: 'var(--ifm-background-surface-color, #f8f9fa)',
              flexShrink: 0,
            }}
          >
            <h3 style={{ margin: 0, fontSize: '1rem', fontWeight: 600 }}>📚 AI Textbook Assistant</h3>
            <button
              className="floating-chat-close"
              onClick={handleClose}
              aria-label="Close chat"
              style={{
                background: 'transparent',
                border: 'none',
                fontSize: '1.75rem',
                cursor: 'pointer',
                padding: 0,
                width: '32px',
                height: '32px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              ×
            </button>
          </div>
          {currentChapter && (
            <div 
              className="floating-chat-chapter-badge"
              style={{
                padding: '0.5rem 1.25rem',
                backgroundColor: 'var(--ifm-color-primary-lightest, #e6f7f5)',
                color: 'var(--ifm-color-primary-darkest, #0f766e)',
                fontSize: '0.85rem',
                fontWeight: 500,
                borderBottom: '1px solid var(--ifm-toc-border-color, #eee)',
                flexShrink: 0,
              }}
            >
              📖 {currentChapter}
            </div>
          )}
          <div 
            className="floating-chat-sidebar-content"
            style={{
              flex: 1,
              overflow: 'hidden',
              display: 'flex',
              flexDirection: 'column',
            }}
          >
            <RagChat
              key={`chat-${currentChapter || 'default'}`}
              chapterFilter={currentChapter}
              useStreaming={false}
              showGreeting={true}
              mode="agent"
              hideHeader={true}
            />
          </div>
        </div>
      )}
    </>
  );
};

export default FloatingChatButton;
