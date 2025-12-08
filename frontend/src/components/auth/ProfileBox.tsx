/**
 * ProfileBox Component
 * 
 * Component for displaying current user profile and logout functionality.
 * Calls useAuth().getSession() on mount and useAuth().logout() on logout.
 * 
 * TODO: Real authentication logic will be implemented in a future feature.
 */

import React, { useState, useEffect } from 'react';
import { getSession, logout } from '../../auth/useAuth';

interface User {
  id: string;
  email: string;
  name?: string;
  role?: string;
  created_at?: string;
}

export default function ProfileBox() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [loggingOut, setLoggingOut] = useState(false);

  useEffect(() => {
    loadUser();
  }, []);

  const loadUser = async () => {
    setLoading(true);
    setError(null);
    try {
      const userData = await getSession();
      setUser(userData);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load user (placeholder)');
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    setLoggingOut(true);
    try {
      await logout();
      setUser(null);
      // TODO: Clear local state, redirect to login
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Logout failed (placeholder)');
    } finally {
      setLoggingOut(false);
    }
  };

  if (loading) {
    return (
      <div style={{ padding: '20px' }}>
        <p>Loading user profile...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ padding: '20px', color: 'red' }}>
        <p>Error: {error}</p>
      </div>
    );
  }

  if (!user) {
    return (
      <div style={{ padding: '20px' }}>
        <p>Not logged in (placeholder)</p>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '20px', border: '1px solid #ccc' }}>
      <h2>User Profile</h2>
      <div style={{ marginBottom: '15px' }}>
        <p><strong>Email:</strong> {user.email}</p>
        {user.name && <p><strong>Name:</strong> {user.name}</p>}
        {user.role && <p><strong>Role:</strong> {user.role}</p>}
        {user.created_at && <p><strong>Created:</strong> {user.created_at}</p>}
      </div>
      <button
        onClick={handleLogout}
        disabled={loggingOut}
        style={{
          width: '100%',
          padding: '10px',
          backgroundColor: '#dc3545',
          color: 'white',
          border: 'none',
          cursor: loggingOut ? 'not-allowed' : 'pointer',
        }}
      >
        {loggingOut ? 'Logging out...' : 'Logout'}
      </button>
      <p style={{ fontSize: '12px', color: '#666', marginTop: '10px' }}>
        (Placeholder - Real authentication coming soon)
      </p>
    </div>
  );
}

