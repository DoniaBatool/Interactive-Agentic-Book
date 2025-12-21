import React, { useState } from 'react';
import Layout from '@theme/Layout';
import { useTranslation } from '../../lib/i18n';

export default function ForgotPasswordPage(): React.JSX.Element {
  const { t } = useTranslation();
  const [email, setEmail] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const authUrl = typeof window !== 'undefined' 
    ? (window as any).__AUTH_URL__ || 'http://localhost:8002'
    : 'http://localhost:8002';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setMessage(null);
    setIsSubmitting(true);

    try {
      // BetterAuth uses /request-password-reset endpoint
      const response = await fetch(`${authUrl}/api/auth/request-password-reset`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ email }),
      });

      if (!response.ok) {
        // Try to parse error response
        let errorMessage = 'Failed to send reset email';
        try {
          const errorData = await response.json();
          errorMessage = errorData.message || errorData.error || errorMessage;
        } catch {
          errorMessage = `Server error: ${response.status} ${response.statusText}`;
        }
        setError(errorMessage);
        return;
      }

      const data = await response.json();
      setMessage('Password reset email sent! Please check your inbox.');
    } catch (err: any) {
      console.error('Forgot password error:', err);
      setError(`Network error: ${err.message || 'Please check if the server is running.'}`);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Layout title={t('auth.forgotPassword')} description={t('auth.resetPasswordDescription')}>
      <div className="auth-container">
        <div className="auth-card">
          <div className="auth-header">
            <h1>{t('auth.forgotPassword')}</h1>
            <p>{t('auth.enterEmailToReset')}</p>
          </div>

          <form onSubmit={handleSubmit} className="auth-form">
            {error && (
              <div className="auth-error">{error}</div>
            )}

            {message && (
              <div className="auth-success">{message}</div>
            )}

            <div className="auth-field">
              <label htmlFor="email">{t('auth.email')}</label>
              <input
                type="email"
                id="email"
                name="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                placeholder="your@email.com"
                autoComplete="email"
              />
            </div>

            <button
              type="submit"
              className="auth-submit"
              disabled={isSubmitting}
            >
              {isSubmitting ? t('auth.sending') : t('auth.sendResetLink')}
            </button>

            <div className="auth-footer">
              <a href="/auth/signin">{t('auth.backToSignIn')}</a>
            </div>
          </form>
        </div>
      </div>
    </Layout>
  );
}

