import React, { useState, useRef, useEffect } from 'react';
import { useHistory } from '@docusaurus/router';
import Link from '@docusaurus/Link';
import { useAuth } from '../context/AuthContext';
import { useTranslation } from '../lib/i18n';

const UserMenu: React.FC = () => {
  const { user, logout, loading } = useAuth();
  const { t } = useTranslation();
  const history = useHistory();
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

  // Show sign in/sign up buttons immediately if no user (even during loading)
  // This ensures buttons are visible on first page load
  // Only show loading if we have a cached user from localStorage (to avoid flash)
  if (!user) {
    // If loading and no cached user, show buttons immediately
    // If loading with cached user, wait a bit for session check
    if (loading) {
      // Check if there's cached user data
      const hasCachedUser = typeof window !== 'undefined' && localStorage.getItem('auth_user');
      if (!hasCachedUser) {
        // No cached user, show buttons immediately
        return (
          <div className="navbar__item user-menu-auth-links">
            <Link to="/auth/signin" className="user-menu-link">{t('common.signIn')}</Link>
            <Link to="/auth/signup" className="user-menu-link user-menu-link-primary">{t('common.signUp')}</Link>
          </div>
        );
      }
      // Has cached user, show loading briefly
      return (
        <div className="navbar__item user-menu-loading">
          <span className="user-menu-spinner"></span>
        </div>
      );
    }
    // Not loading and no user, show buttons
    return (
      <div className="navbar__item user-menu-auth-links">
        <Link to="/auth/signin" className="user-menu-link">{t('common.signIn')}</Link>
        <Link to="/auth/signup" className="user-menu-link user-menu-link-primary">{t('common.signUp')}</Link>
      </div>
    );
  }

  // Show loading spinner only if we have a user and still loading
  if (loading && user) {
    return (
      <div className="navbar__item user-menu-loading">
        <span className="user-menu-spinner"></span>
      </div>
    );
  }

  const handleLogout = async () => {
    setIsOpen(false);
    try {
      await logout();
      // Small delay to ensure state is cleared
      setTimeout(() => {
        history.push('/');
      }, 100);
    } catch (error) {
      console.error('Logout error:', error);
      // Force redirect even if logout fails
      history.push('/');
    }
  };

  const displayName = user.name || user.email.split('@')[0];
  const initials = displayName.slice(0, 2).toUpperCase();

  return (
    <div className="navbar__item user-menu" ref={menuRef}>
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
          <Link to="/auth/profile" className="user-menu-item" onClick={() => setIsOpen(false)}>
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
          </Link>
          {(() => {
            // Check multiple ways admin status might be stored
            const isAdmin = 
              (user as any).isAdmin === true || 
              (user as any).isAdmin === 'true' ||
              (user as any).role === 'admin' ||
              (user as any).role === 'Admin';
            
            // Debug: Log admin check with full user object
            console.log('🔍 Admin check in UserMenu:', {
              email: user.email,
              isAdmin: (user as any).isAdmin,
              isAdminType: typeof (user as any).isAdmin,
              role: (user as any).role,
              roleType: typeof (user as any).role,
              fullUser: user,
              result: isAdmin
            });
            
            return isAdmin;
          })() && (
            <Link to="/auth/admin" className="user-menu-item" onClick={() => setIsOpen(false)}>
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
            </Link>
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

