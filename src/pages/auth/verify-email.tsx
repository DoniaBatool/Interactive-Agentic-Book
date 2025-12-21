import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import { useTranslation } from '../../lib/i18n';
import { AUTH_SERVER_URL } from '../../config/env';

export default function VerifyEmailPage(): React.JSX.Element {
  const { t } = useTranslation();
  const [token, setToken] = useState<string>('');
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const authUrl = AUTH_SERVER_URL;

  // Get token from URL
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      const tokenParam = params.get('token');
      if (tokenParam) {
        setToken(tokenParam);
        verifyEmail(tokenParam);
      } else {
        setError('Invalid verification link');
        setLoading(false);
      }
    }
  }, []);

  const verifyEmail = async (verificationToken: string) => {
    try {
      setLoading(true);
      setError(null);
      
      // Try GET first (BetterAuth standard)
      let response = await fetch(`${authUrl}/api/auth/verify-email?token=${encodeURIComponent(verificationToken)}`, {
        method: 'GET',
        credentials: 'include',
      });

      // If GET fails, try POST (some BetterAuth versions use POST)
      if (!response.ok && response.status === 404) {
        console.log('GET failed, trying POST...');
        response = await fetch(`${authUrl}/api/auth/verify-email`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
          body: JSON.stringify({ token: verificationToken }),
        });
      }

      let data: any = {};
      try {
        const text = await response.text();
        if (text) {
          data = JSON.parse(text);
        }
      } catch (e) {
        // If response is not JSON, that's okay
        console.log('Response is not JSON, status:', response.status);
      }

      if (response.ok) {
        setMessage('Email verified successfully! Redirecting to sign in...');
        setTimeout(() => {
          window.location.href = '/auth/signin';
        }, 2000);
      } else {
        const errorMessage = data.message || data.error?.message || `Failed to verify email (Status: ${response.status})`;
        setError(errorMessage);
        console.error('Verification error:', {
          status: response.status,
          statusText: response.statusText,
          url: `${authUrl}/api/auth/verify-email`,
          data
        });
      }
    } catch (err: any) {
      console.error('Network error during verification:', err);
      const errorMsg = err.message || 'Unknown error';
      setError(`Network error: ${errorMsg}. Please check if the auth server is running on ${authUrl}`);
    } finally {
      setLoading(false);
    }
  };

  const resendVerification = async () => {
    try {
      setError(null);
      setLoading(true);
      const response = await fetch(`${authUrl}/api/auth/resend-verification`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      });

      let data: any = {};
      try {
        const text = await response.text();
        if (text) {
          data = JSON.parse(text);
        }
      } catch (e) {
        console.error('Failed to parse response:', e);
      }

      if (response.ok) {
        setMessage(t('auth.verificationSent') || 'Verification email sent! Please check your inbox.');
      } else {
        const errorMessage = data.message || data.error?.message || 'Failed to resend verification email';
        setError(errorMessage);
        console.error('Resend verification error:', {
          status: response.status,
          statusText: response.statusText,
          data
        });
      }
    } catch (err: any) {
      console.error('Network error during resend:', err);
      setError(`Network error: ${err.message || 'Please check if the auth server is running'}`);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <Layout title={t('auth.verifyEmail')}>
        <div className="auth-container">
          <div className="auth-card">
            <div className="auth-loading">{t('common.loading')}</div>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout title={t('auth.verifyEmail')} description={t('auth.emailVerificationRequired')}>
      <div className="auth-container">
        <div className="auth-card">
          <div className="auth-header">
            <h1>{t('auth.verifyEmail')}</h1>
            <p>{t('auth.emailVerificationRequired')}</p>
          </div>

          {error && (
            <div className="auth-error">{error}</div>
          )}

          {message && (
            <div className="auth-success">{message}</div>
          )}

          {!message && (
            <div className="auth-footer">
              <p>{t('auth.checkYourEmail')}</p>
              <button
                onClick={resendVerification}
                className="auth-submit"
                style={{ marginTop: '1rem' }}
              >
                {t('auth.resendVerification')}
              </button>
            </div>
          )}
        </div>
      </div>
    </Layout>
  );
}

