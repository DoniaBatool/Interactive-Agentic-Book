import React, { useState, useEffect } from 'react';
import { useHistory } from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import { useAuth } from '../../context/AuthContext';
import { useTranslation } from '../../lib/i18n';
import { AUTH_SERVER_URL } from '../../config/env';
import { authClient } from '../../lib/auth-client';

export default function SigninPage(): React.JSX.Element {
  const { login, user, loading, error, clearError, refreshSession } = useAuth();
  const { t } = useTranslation();
  const history = useHistory();
  const { siteConfig } = useDocusaurusContext();
  
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    rememberMe: false,
  });
  
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [oauthError, setOauthError] = useState<string | null>(null);

  // Handle OAuth callback - check if we're returning from OAuth
  useEffect(() => {
    if (typeof window !== 'undefined' && !loading) {
      const urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get('code');
      const error = urlParams.get('error');
      
      // If OAuth error, show error message
      if (error) {
        setOauthError(`OAuth error: ${error}. Please try again.`);
        // Clear error from URL
        window.history.replaceState({}, '', window.location.pathname);
        return;
      }
      
      // If OAuth callback with code, refresh session and check if user is admin
      if (code && !error) {
        // Refresh session to get user data from BetterAuth
        refreshSession().then(async () => {
          // Check if the user is admin - if so, sign them out
          try {
            const userResponse = await fetch(`${AUTH_SERVER_URL}/api/auth/get-user`, {
              credentials: 'include',
            });
            
            if (userResponse.ok) {
              const userData = await userResponse.json();
              if (userData.user) {
                const isAdmin = !!(userData.user.isAdmin) || userData.user.role === 'admin';
                
                if (isAdmin) {
                  // Admin users cannot sign in via OAuth - sign them out immediately
                  try {
                    // Call a custom endpoint to delete session and OAuth account link
                    await fetch(`${AUTH_SERVER_URL}/api/auth/block-admin-oauth`, {
                      method: 'POST',
                      credentials: 'include',
                    });
                  } catch (err) {
                    console.error('Error blocking admin OAuth:', err);
                  }
                  
                  // Also call standard sign-out
                  await fetch(`${AUTH_SERVER_URL}/api/auth/sign-out`, {
                    method: 'POST',
                    credentials: 'include',
                  });
                  
                  setOauthError('Admin accounts cannot sign in via OAuth. Please use email/password login.');
                  // Clear the code from URL
                  window.history.replaceState({}, '', window.location.pathname);
                  return;
                }
              }
            }
          } catch (err) {
            console.error('Error checking admin status:', err);
            // Continue with normal flow if check fails
          }
          
          // Wait a bit for session to be set, then redirect to home
          setTimeout(() => {
            const isProd =
              typeof window !== 'undefined' &&
              window.location.hostname === 'doniabatool.github.io';
            const target = isProd ? '/Interactive-Agentic-Book/' : '/';
            window.location.href = target;
          }, 1500); // Increased timeout to ensure session is set
        }).catch((err) => {
          console.error('OAuth callback error:', err);
          setOauthError('Failed to complete sign-in. Please try again.');
        });
      }
    }
  }, [loading, refreshSession, history]);

  // Redirect if already logged in
  useEffect(() => {
    if (user && !loading) {
      history.push('/');
    }
  }, [user, loading, history]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
    clearError();
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    clearError();
    setIsSubmitting(true);

    const success = await login(
      formData.email,
      formData.password,
      formData.rememberMe
    );

    setIsSubmitting(false);

    if (success) {
      // Small delay to ensure user state is set before redirect
      setTimeout(() => {
        const isProd =
          typeof window !== 'undefined' &&
          window.location.hostname === 'doniabatool.github.io';
        const target = isProd ? '/Interactive-Agentic-Book/' : '/';
        window.location.href = target;
      }, 100);
    }
  };

  if (loading) {
    return (
      <Layout title={t('common.signIn')}>
        <div className="auth-loading">{t('common.loading')}</div>
      </Layout>
    );
  }

  return (
    <Layout title={t('common.signIn')} description={t('auth.signInToContinue')}>
      <div className="auth-container">
        <div className="auth-card auth-card-signin">
          <div className="auth-header">
            <h1>{t('auth.welcomeBack')}</h1>
            <p>{t('auth.signInToContinue')}</p>
          </div>

          <form onSubmit={handleSubmit} className="auth-form">
              {error && (
                <div className="auth-error">{error}</div>
              )}

            <div className="auth-field">
              <label htmlFor="email">{t('auth.email')}</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                placeholder="your@email.com"
                autoComplete="email"
              />
            </div>

            <div className="auth-field">
              <label htmlFor="password">{t('auth.password')}</label>
              <div className="auth-password-wrapper">
                <input
                  type={showPassword ? "text" : "password"}
                  id="password"
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  required
                  placeholder={t('auth.password')}
                  autoComplete="current-password"
                />
                <button
                  type="button"
                  className="auth-password-toggle"
                  onClick={() => setShowPassword(!showPassword)}
                  aria-label={showPassword ? t('auth.hidePassword') : t('auth.showPassword')}
                >
                  {showPassword ? (
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/>
                      <line x1="1" y1="1" x2="23" y2="23"/>
                    </svg>
                  ) : (
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                      <circle cx="12" cy="12" r="3"/>
                    </svg>
                  )}
                </button>
              </div>
            </div>

            <div className="auth-options">
              <label className="auth-checkbox">
                <input
                  type="checkbox"
                  name="rememberMe"
                  checked={formData.rememberMe}
                  onChange={handleChange}
                />
                <span>{t('auth.rememberMe')}</span>
              </label>
              <a href="/auth/forgot-password" className="auth-forgot-link">
                {t('auth.forgotPassword')}
              </a>
            </div>

            <button
              type="submit"
              className="auth-submit"
              disabled={isSubmitting}
            >
              {isSubmitting ? t('auth.signingIn') : t('common.signIn')}
            </button>

            <div className="auth-footer">
              {t('auth.dontHaveAccount')} <a href="/auth/signup">{t('common.signUp')}</a>
            </div>
          </form>
        </div>
      </div>
    </Layout>
  );
}

