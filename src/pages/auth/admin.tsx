import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import { useAuth } from '../../context/AuthContext';
import { useTranslation } from '../../lib/i18n';
import { AUTH_SERVER_URL } from '../../config/env';

interface AdminUser {
  id: string;
  email: string;
  name?: string;
  emailVerified: boolean;
  role: string;
  isAdmin: boolean;
  createdAt: string;
  lastLogin?: string;
}

export default function AdminPage(): React.JSX.Element {
  const { user, loading: authLoading } = useAuth();
  const { t } = useTranslation();
  const [users, setUsers] = useState<AdminUser[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const authUrl = AUTH_SERVER_URL;

  // Check if user is admin
  useEffect(() => {
    if (!authLoading && user) {
      const isAdmin = (user as any).isAdmin || (user as any).role === 'admin';
      if (!isAdmin) {
        window.location.href = '/';
      }
    }
  }, [user, authLoading]);

  // Fetch users
  useEffect(() => {
    if (user && ((user as any).isAdmin || (user as any).role === 'admin')) {
      fetchUsers();
    }
  }, [user]);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch(`${authUrl}/api/auth/admin/users`, {
        credentials: 'include',
      });

      if (!response.ok) {
        // Try to parse error response
        let errorMessage = 'Failed to fetch users';
        try {
          const errorData = await response.json();
          errorMessage = errorData.error || errorData.message || errorMessage;
          console.error('Admin API error:', {
            status: response.status,
            statusText: response.statusText,
            error: errorData
          });
        } catch {
          errorMessage = `Server error: ${response.status} ${response.statusText}`;
        }
        setError(errorMessage);
        return;
      }

      const data = await response.json();
      setUsers(data.users || []);
    } catch (err: any) {
      console.error('Network error fetching users:', err);
      setError(`Network error: ${err.message || 'Please check if the server is running.'}`);
    } finally {
      setLoading(false);
    }
  };

  const toggleAdmin = async (userId: string, currentStatus: boolean) => {
    try {
      const response = await fetch(`${authUrl}/api/auth/admin/users/${userId}/toggle-admin`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ isAdmin: !currentStatus }),
      });

      if (response.ok) {
        fetchUsers(); // Refresh list
      } else {
        setError('Failed to update user');
      }
    } catch (err) {
      setError('Network error');
    }
  };

  const deleteUser = async (userId: string) => {
    if (!confirm('Are you sure you want to delete this user?')) {
      return;
    }

    try {
      const response = await fetch(`${authUrl}/api/auth/admin/users/${userId}`, {
        method: 'DELETE',
        credentials: 'include',
      });

      if (response.ok) {
        fetchUsers(); // Refresh list
      } else {
        setError('Failed to delete user');
      }
    } catch (err) {
      setError('Network error');
    }
  };

  if (authLoading || loading) {
    return (
      <Layout title="Admin Panel">
        <div className="auth-loading">{t('common.loading')}</div>
      </Layout>
    );
  }

  if (!user || (!(user as any).isAdmin && (user as any).role !== 'admin')) {
    return (
      <Layout title="Access Denied">
        <div className="auth-container">
          <div className="auth-card">
            <div className="auth-error">
              You don't have permission to access this page.
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout title="Admin Panel" description="User management">
      <div className="auth-container">
        <div className="auth-card" style={{ maxWidth: '1200px' }}>
          <div className="auth-header">
            <h1>Admin Panel</h1>
            <p>Manage users and permissions</p>
          </div>

          {error && (
            <div className="auth-error">{error}</div>
          )}

          <div className="admin-users-table">
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr>
                  <th>Email</th>
                  <th>Name</th>
                  <th>Verified</th>
                  <th>Role</th>
                  <th>Created</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {users.map((u) => (
                  <tr key={u.id}>
                    <td>{u.email}</td>
                    <td>{u.name || '-'}</td>
                    <td>{u.emailVerified ? '✅' : '❌'}</td>
                    <td>{u.isAdmin ? 'Admin' : 'User'}</td>
                    <td>{new Date(u.createdAt).toLocaleDateString()}</td>
                    <td>
                      <button
                        onClick={() => toggleAdmin(u.id, u.isAdmin)}
                        className="auth-submit"
                        style={{ marginRight: '8px', padding: '4px 12px', fontSize: '14px' }}
                      >
                        {u.isAdmin ? 'Remove Admin' : 'Make Admin'}
                      </button>
                      {u.id !== user.id && (
                        <button
                          onClick={() => deleteUser(u.id)}
                          className="auth-submit"
                          style={{ padding: '4px 12px', fontSize: '14px', backgroundColor: '#dc3545' }}
                        >
                          Delete
                        </button>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </Layout>
  );
}

