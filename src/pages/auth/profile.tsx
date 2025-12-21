import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import { useAuth } from '../../context/AuthContext';

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

export default function ProfilePage(): React.JSX.Element {
  const { user, loading, error, updateProfile, clearError } = useAuth();
  
  const [formData, setFormData] = useState({
    softwareLevel: 'beginner',
    hardwareLevel: 'none',
    technologies: {} as Record<string, boolean>,
    learningGoals: '',
  });
  
  const [isSaving, setIsSaving] = useState(false);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  // Initialize form data from user profile
  useEffect(() => {
    if (user?.profile) {
      setFormData({
        softwareLevel: user.profile.software_level || 'beginner',
        hardwareLevel: user.profile.hardware_level || 'none',
        technologies: user.profile.technologies || {},
        learningGoals: user.profile.learning_goals || '',
      });
    }
  }, [user]);

  // Redirect if not logged in
  useEffect(() => {
    if (!loading && !user) {
      window.location.href = '/auth/signin?redirect=/auth/profile';
    }
  }, [user, loading]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    setSuccessMessage(null);
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
    setSuccessMessage(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    clearError();
    setSuccessMessage(null);
    setIsSaving(true);

    const success = await updateProfile({
      software_level: formData.softwareLevel,
      hardware_level: formData.hardwareLevel,
      technologies: formData.technologies,
      learning_goals: formData.learningGoals || undefined,
    });

    setIsSaving(false);

    if (success) {
      setSuccessMessage('Profile updated successfully!');
    }
  };

  if (loading) {
    return (
      <Layout title="Profile">
        <div className="auth-loading">Loading...</div>
      </Layout>
    );
  }

  if (!user) {
    return (
      <Layout title="Profile">
        <div className="auth-loading">Redirecting to sign in...</div>
      </Layout>
    );
  }

  return (
    <Layout title="Profile" description="Your profile settings">
      <div className="auth-container">
        <div className="auth-card">
          <div className="auth-header">
            <h1>Your Profile</h1>
            <p>Manage your learning preferences</p>
          </div>

          <div className="profile-info">
            <div className="profile-avatar">
              {(user.name || user.email).slice(0, 2).toUpperCase()}
            </div>
            <div className="profile-details">
              <div className="profile-name">{user.name || 'No name set'}</div>
              <div className="profile-email">{user.email}</div>
            </div>
          </div>

          <form onSubmit={handleSubmit} className="auth-form">
            {error && (
              <div className="auth-error">{error}</div>
            )}
            {successMessage && (
              <div className="auth-success">{successMessage}</div>
            )}

            <div className="auth-section">
              <h3>Learning Background</h3>

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
                <label htmlFor="learningGoals">Learning Goals</label>
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
              disabled={isSaving}
            >
              {isSaving ? 'Saving...' : 'Save Changes'}
            </button>
          </form>
        </div>
      </div>
    </Layout>
  );
}

