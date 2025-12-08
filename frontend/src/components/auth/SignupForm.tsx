/**
 * SignupForm Component
 * 
 * Component for user registration with email, password, and optional name.
 * Calls useAuth().signup() on submit and displays placeholder response.
 * 
 * TODO: Real authentication logic will be implemented in a future feature.
 */

import React, { useState } from 'react';
import { signup } from '../../auth/useAuth';

export default function SignupForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [name, setName] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [user, setUser] = useState<any>(null);
  
  // User background questions (for personalization)
  const [technicalBackground, setTechnicalBackground] = useState('student');
  const [experienceLevel, setExperienceLevel] = useState('beginner');
  const [learningGoal, setLearningGoal] = useState('academic');
  const [preferredDepth, setPreferredDepth] = useState('overview');
  const [domainInterests, setDomainInterests] = useState<string[]>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setUser(null);

    // TODO: Validate password match
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      setLoading(false);
      return;
    }

    try {
      // Include user background for personalization
      const userProfile = {
        technicalBackground,
        experienceLevel,
        learningGoal,
        preferredDepth,
        domainInterests,
      };
      const response = await signup(email, password, name || undefined, userProfile as any);
      setUser(response.user);
      // TODO: Redirect to login or dashboard
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Signup failed (placeholder)');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '20px' }}>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            minLength={8}
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="confirmPassword">Confirm Password:</label>
          <input
            type="password"
            id="confirmPassword"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="name">Name (optional):</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>
        
        <div style={{ marginTop: '30px', paddingTop: '20px', borderTop: '2px solid #eee' }}>
          <h3 style={{ marginBottom: '15px', fontSize: '1.1rem' }}>Help Us Personalize Your Experience</h3>
          
          <div style={{ marginBottom: '15px' }}>
            <label htmlFor="technicalBackground">Technical Background:</label>
            <select
              id="technicalBackground"
              value={technicalBackground}
              onChange={(e) => setTechnicalBackground(e.target.value)}
              style={{ width: '100%', padding: '8px', marginTop: '5px' }}
            >
              <option value="student">Student</option>
              <option value="professional">Professional</option>
              <option value="researcher">Researcher</option>
              <option value="hobbyist">Hobbyist</option>
            </select>
          </div>
          
          <div style={{ marginBottom: '15px' }}>
            <label htmlFor="experienceLevel">Experience Level:</label>
            <select
              id="experienceLevel"
              value={experienceLevel}
              onChange={(e) => setExperienceLevel(e.target.value)}
              style={{ width: '100%', padding: '8px', marginTop: '5px' }}
            >
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
          </div>
          
          <div style={{ marginBottom: '15px' }}>
            <label htmlFor="learningGoal">Learning Goal:</label>
            <select
              id="learningGoal"
              value={learningGoal}
              onChange={(e) => setLearningGoal(e.target.value)}
              style={{ width: '100%', padding: '8px', marginTop: '5px' }}
            >
              <option value="academic">Academic</option>
              <option value="career">Career Transition</option>
              <option value="hobby">Hobby/Interest</option>
              <option value="research">Research</option>
            </select>
          </div>
          
          <div style={{ marginBottom: '15px' }}>
            <label htmlFor="preferredDepth">Preferred Depth:</label>
            <select
              id="preferredDepth"
              value={preferredDepth}
              onChange={(e) => setPreferredDepth(e.target.value)}
              style={{ width: '100%', padding: '8px', marginTop: '5px' }}
            >
              <option value="overview">High-Level Overview</option>
              <option value="detailed">Detailed Technical</option>
              <option value="research">Research-Level</option>
            </select>
          </div>
          
          <div style={{ marginBottom: '15px' }}>
            <label>Domain Interests (select all that apply):</label>
            <div style={{ marginTop: '8px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
              {['Hardware', 'Software', 'AI Algorithms', 'Applications', 'Robotics', 'Simulation'].map((interest) => (
                <label key={interest} style={{ display: 'flex', alignItems: 'center', gap: '5px', cursor: 'pointer' }}>
                  <input
                    type="checkbox"
                    checked={domainInterests.includes(interest)}
                    onChange={(e) => {
                      if (e.target.checked) {
                        setDomainInterests([...domainInterests, interest]);
                      } else {
                        setDomainInterests(domainInterests.filter(i => i !== interest));
                      }
                    }}
                  />
                  {interest}
                </label>
              ))}
            </div>
          </div>
        </div>
        
        {error && (
          <div style={{ color: 'red', marginBottom: '15px' }}>
            {error}
          </div>
        )}
        <button
          type="submit"
          disabled={loading}
          style={{
            width: '100%',
            padding: '10px',
            backgroundColor: '#28a745',
            color: 'white',
            border: 'none',
            cursor: loading ? 'not-allowed' : 'pointer',
          }}
        >
          {loading ? 'Signing up...' : 'Sign Up'}
        </button>
      </form>
      {user && (
        <div style={{ marginTop: '20px', padding: '10px', backgroundColor: '#f0f0f0' }}>
          <p>Account created: {user.email} (placeholder)</p>
        </div>
      )}
    </div>
  );
}

