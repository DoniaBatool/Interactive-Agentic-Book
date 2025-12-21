import React, { useState, useRef, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useTranslation } from '../lib/i18n';

const UserMenu: React.FC = () => {
  const { user, logout, loading } = useAuth();
  const { t } = useTranslation();
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  // Close menu when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  if (loading) {
    return (
      <div className="user-menu-loading">
        <span className="user-menu-spinner"></span>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="user-menu-auth-links">
        <a href="/auth/signin" className="user-menu-link">{t('common.signIn')}</a>
        <a href="/auth/signup" className="user-menu-link user-menu-link-primary">{t('common.signUp')}</a>
      </div>
    );
  }

  const handleLogout = async () => {
    setIsOpen(false);
    try {
      await logout();
      // Small delay to ensure state is cleared
      setTimeout(() => {
        window.location.href = '/';
      }, 100);
    } catch (error) {
      console.error('Logout error:', error);
      // Force redirect even if logout fails
      window.location.href = '/';
    }
  };

  const displayName = user.name || user.email.split('@')[0];
  const initials = displayName.slice(0, 2).toUpperCase();

  return (
    <div className="user-menu" ref={menuRef}>
      <button
        className="user-menu-trigger"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="User menu"
        aria-expanded={isOpen}
      >
        <span className="user-menu-avatar">{initials}</span>
        <span className="user-menu-name">{displayName}</span>
        <svg
          className={`user-menu-chevron ${isOpen ? 'open' : ''}`}
          width="12"
          height="12"
          viewBox="0 0 12 12"
          fill="none"
        >
          <path
            d="M2.5 4.5L6 8L9.5 4.5"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      </button>

      {isOpen && (
        <div className="user-menu-dropdown">
          <div className="user-menu-header">
            <span className="user-menu-email">{user.email}</span>
            {user.profile && (
              <span className="user-menu-level">
                {user.profile.software_level} · {user.profile.hardware_level}
              </span>
            )}
          </div>
          <div className="user-menu-divider"></div>
          <a href="/auth/profile" className="user-menu-item" onClick={() => setIsOpen(false)}>
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
              <path
                d="M8 8a3 3 0 100-6 3 3 0 000 6zM2 14a6 6 0 0112 0H2z"
                stroke="currentColor"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            {t('common.profile')}
          </a>
          {(() => {
            const isAdmin = (user as any).isAdmin || (user as any).role === 'admin';
            // Debug: Log admin check
            console.log('🔍 Admin check in UserMenu:', {
              email: user.email,
              isAdmin: (user as any).isAdmin,
              role: (user as any).role,
              result: isAdmin
            });
            return isAdmin;
          })() && (
            <a href="/auth/admin" className="user-menu-item" onClick={() => setIsOpen(false)}>
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path
                  d="M8 1L10.5 5.5L15.5 6.5L12 10L12.5 15L8 12.5L3.5 15L4 10L0.5 6.5L5.5 5.5L8 1Z"
                  stroke="currentColor"
                  strokeWidth="1.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
              {t('admin.adminPanel')}
            </a>
          )}
          <button className="user-menu-item user-menu-item-danger" onClick={handleLogout}>
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
              <path
                d="M6 14H3a1 1 0 01-1-1V3a1 1 0 011-1h3M11 11l3-3-3-3M14 8H6"
                stroke="currentColor"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            {t('common.signOut')}
          </button>
        </div>
      )}
    </div>
  );
};

export default UserMenu;

