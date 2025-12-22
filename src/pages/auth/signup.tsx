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
  const [showVerificationMessage, setShowVerificationMessage] = useState(false);

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
      // With email verification enabled, user needs to verify email before sign-in
      setShowVerificationMessage(true);
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

            <div className="auth-footer">
              Already have an account? <a href="/auth/signin">Sign In</a>
            </div>
          </form>
        </div>
      </div>
    </Layout>
  );
}

