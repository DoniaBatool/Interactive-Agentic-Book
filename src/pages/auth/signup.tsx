import React, { useState, useEffect } from 'react';
import { useHistory } from '@docusaurus/router';
import Layout from '@theme/Layout';
import { useAuth } from '../../context/AuthContext';
import { useTranslation } from '../../lib/i18n';
import { AUTH_SERVER_URL } from '../../config/env';
import { authClient } from '../../lib/auth-client';

const TECHNOLOGIES = [
  { key: 'python', label: 'Python' },
  { key: 'ros2', label: 'ROS 2' },
  { key: 'gazebo', label: 'Gazebo / Isaac Sim' },
  { key: 'isaac', label: 'NVIDIA Isaac' },
  { key: 'aiMl', label: 'AI/ML (TensorFlow, PyTorch)' },
  { key: 'unity', label: 'Unity' },
  { key: 'linux', label: 'Linux / Ubuntu' },
  { key: 'docker', label: 'Docker' },
];

export default function SignupPage(): React.JSX.Element {
  const { signup, user, loading, error, clearError } = useAuth();
  const { t } = useTranslation();
  const history = useHistory();
  
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    name: '',
    softwareLevel: 'beginner',
    hardwareLevel: 'none',
    technologies: {} as Record<string, boolean>,
    learningGoals: '',
  });
  
  const [formError, setFormError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  // Redirect if already logged in
  useEffect(() => {
    if (user && !loading) {
      history.push('/');
    }
  }, [user, loading, history]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    setFormError(null);
    clearError();
  };

  const handleTechChange = (key: string) => {
    setFormData(prev => ({
      ...prev,
      technologies: {
        ...prev.technologies,
        [key]: !prev.technologies[key],
      },
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormError(null);
    clearError();

    // Validation
    if (formData.password !== formData.confirmPassword) {
      setFormError('Passwords do not match');
      return;
    }
    if (formData.password.length < 8) {
      setFormError('Password must be at least 8 characters');
      return;
    }

    setIsSubmitting(true);

    const success = await signup({
      email: formData.email,
      password: formData.password,
      name: formData.name || undefined,
      profile: {
        software_level: formData.softwareLevel,
        hardware_level: formData.hardwareLevel,
        technologies: formData.technologies,
        learning_goals: formData.learningGoals || undefined,
      },
    });

    setIsSubmitting(false);

    if (success) {
      history.push('/');
    }
  };

  if (loading) {
    return (
      <Layout title="Sign Up">
        <div className="auth-loading">Loading...</div>
      </Layout>
    );
  }

  return (
    <Layout title="Sign Up" description="Create your account">
      <div className="auth-container">
        <div className="auth-card">
          <div className="auth-header">
            <h1>Create Account</h1>
            <p>Join us to personalize your learning experience</p>
          </div>

          <form onSubmit={handleSubmit} className="auth-form">
            {(formError || error) && (
              <div className="auth-error">{formError || error}</div>
            )}

            <div className="auth-section">
              <h3>Account Details</h3>
              
              <div className="auth-field">
                <label htmlFor="email">Email *</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  placeholder="your@email.com"
                />
              </div>

              <div className="auth-field">
                <label htmlFor="name">Name (optional)</label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  placeholder="Your name"
                />
              </div>

              <div className="auth-field">
                <label htmlFor="password">Password *</label>
                <div className="auth-password-wrapper">
                  <input
                    type={showPassword ? "text" : "password"}
                    id="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                    minLength={8}
                    placeholder="At least 8 characters"
                  />
                  <button
                    type="button"
                    className="auth-password-toggle"
                    onClick={() => setShowPassword(!showPassword)}
                    aria-label={showPassword ? "Hide password" : "Show password"}
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

              <div className="auth-field">
                <label htmlFor="confirmPassword">Confirm Password *</label>
                <div className="auth-password-wrapper">
                  <input
                    type={showConfirmPassword ? "text" : "password"}
                    id="confirmPassword"
                    name="confirmPassword"
                    value={formData.confirmPassword}
                    onChange={handleChange}
                    required
                    placeholder="Confirm your password"
                  />
                  <button
                    type="button"
                    className="auth-password-toggle"
                    onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                    aria-label={showConfirmPassword ? "Hide password" : "Show password"}
                  >
                    {showConfirmPassword ? (
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
            </div>

            <div className="auth-section">
              <h3>Your Background</h3>
              <p className="auth-section-desc">
                Help us personalize the content for you
              </p>

              <div className="auth-field">
                <label htmlFor="softwareLevel">Software Experience</label>
                <select
                  id="softwareLevel"
                  name="softwareLevel"
                  value={formData.softwareLevel}
                  onChange={handleChange}
                >
                  <option value="beginner">Beginner - New to programming</option>
                  <option value="intermediate">Intermediate - Comfortable with Python</option>
                  <option value="advanced">Advanced - Professional developer</option>
                </select>
              </div>

              <div className="auth-field">
                <label htmlFor="hardwareLevel">Hardware Experience</label>
                <select
                  id="hardwareLevel"
                  name="hardwareLevel"
                  value={formData.hardwareLevel}
                  onChange={handleChange}
                >
                  <option value="none">None - No robotics hardware experience</option>
                  <option value="some">Some - Basic Arduino/Raspberry Pi</option>
                  <option value="extensive">Extensive - Jetson, RealSense, professional robots</option>
                </select>
              </div>

              <div className="auth-field">
                <label>Technologies You Know</label>
                <div className="auth-checkboxes">
                  {TECHNOLOGIES.map(tech => (
                    <label key={tech.key} className="auth-checkbox">
                      <input
                        type="checkbox"
                        checked={formData.technologies[tech.key] || false}
                        onChange={() => handleTechChange(tech.key)}
                      />
                      <span>{tech.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              <div className="auth-field">
                <label htmlFor="learningGoals">Learning Goals (optional)</label>
                <textarea
                  id="learningGoals"
                  name="learningGoals"
                  value={formData.learningGoals}
                  onChange={handleChange}
                  rows={3}
                  placeholder="What do you want to learn from this course?"
                />
              </div>
            </div>

            <button
              type="submit"
              className="auth-submit"
              disabled={isSubmitting}
            >
              {isSubmitting ? 'Creating Account...' : 'Create Account'}
            </button>

            {/* OAuth Buttons */}
            {/* Note: OAuth providers can be enabled in BetterAuth config */}
            <div className="auth-divider">
              <span>{t('auth.orContinueWith')}</span>
            </div>
            <div className="auth-oauth-buttons">
              <button
                onClick={async (e) => {
                  e.preventDefault();
                  try {
                    // Detect if we're on GitHub Pages or Render
                    const isGitHubPages = typeof window !== 'undefined' && window.location.hostname === 'doniabatool.github.io';
                    const basePath = isGitHubPages ? '/Interactive-Agentic-Book' : '';
                    const callbackURL = window.location.origin + basePath + '/auth/signin';
                    
                    // Use POST to get OAuth redirect URL from BetterAuth
                    const response = await fetch(`${AUTH_SERVER_URL}/api/auth/sign-in/social`, {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      credentials: 'include',
                      body: JSON.stringify({
                        provider: 'google',
                        callbackURL: callbackURL,
                      }),
                    });
                    
                    const data = await response.json();
                    if (data.url) {
                      window.location.href = data.url;
                    } else {
                      console.error('No redirect URL in response:', data);
                    }
                  } catch (error) {
                    console.error('OAuth error:', error);
                  }
                }}
                className="auth-oauth-button auth-oauth-google"
                style={{ border: 'none', background: 'none', cursor: 'pointer', width: '100%' }}
              >
                <svg width="20" height="20" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                </svg>
                {t('auth.signUpWithGoogle')}
              </button>
              <button
                onClick={async (e) => {
                  e.preventDefault();
                  try {
                    // Detect if we're on GitHub Pages or Render
                    const isGitHubPages = typeof window !== 'undefined' && window.location.hostname === 'doniabatool.github.io';
                    const basePath = isGitHubPages ? '/Interactive-Agentic-Book' : '';
                    const callbackURL = window.location.origin + basePath + '/auth/signin';
                    
                    // Use POST to get OAuth redirect URL from BetterAuth
                    const response = await fetch(`${AUTH_SERVER_URL}/api/auth/sign-in/social`, {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      credentials: 'include',
                      body: JSON.stringify({
                        provider: 'github',
                        callbackURL: callbackURL,
                      }),
                    });
                    
                    const data = await response.json();
                    if (data.url) {
                      window.location.href = data.url;
                    } else {
                      console.error('No redirect URL in response:', data);
                    }
                  } catch (error) {
                    console.error('OAuth error:', error);
                  }
                }}
                className="auth-oauth-button auth-oauth-github"
                style={{ border: 'none', background: 'none', cursor: 'pointer', width: '100%' }}
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                {t('auth.signUpWithGitHub')}
              </button>
            </div>

            <div className="auth-footer">
              Already have an account? <a href="/auth/signin">Sign In</a>
            </div>
          </form>
        </div>
      </div>
    </Layout>
  );
}

