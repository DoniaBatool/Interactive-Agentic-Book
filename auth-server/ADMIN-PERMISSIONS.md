# Admin Permissions Guide

## Primary Admin (`donia1510aptech@gmail.com`)

The primary admin account has **full permissions** and **cannot be deleted or have admin status removed**.

### Permissions:
- ✅ View all users
- ✅ Make any user an admin
- ✅ Remove admin status from any user (except themselves)
- ✅ Delete any user (except themselves)
- ✅ Access admin panel
- ❌ Cannot delete their own account
- ❌ Cannot remove their own admin status

---

## Secondary Admins (Created by Primary Admin)

When the primary admin makes another user an admin, that user gets **the same permissions** as the primary admin, **EXCEPT**:

### Permissions:
- ✅ View all users
- ✅ Make any user an admin
- ✅ Remove admin status from any user (except primary admin and themselves)
- ✅ Delete any user (except primary admin and themselves)
- ✅ Access admin panel
- ❌ Cannot delete the primary admin (`donia1510aptech@gmail.com`)
- ❌ Cannot remove admin status from the primary admin
- ❌ Cannot delete their own account
- ❌ Cannot remove their own admin status

---

## Regular Users

Regular users have **no admin permissions**:
- ❌ Cannot access admin panel
- ❌ Cannot view other users
- ❌ Cannot modify user roles
- ✅ Can only manage their own profile

---

## Summary

| Action | Primary Admin | Secondary Admin | Regular User |
|--------|--------------|----------------|--------------|
| View all users | ✅ | ✅ | ❌ |
| Make user admin | ✅ | ✅ | ❌ |
| Remove admin (primary) | ❌ | ❌ | ❌ |
| Remove admin (secondary) | ✅ | ✅ (except self) | ❌ |
| Delete primary admin | ❌ | ❌ | ❌ |
| Delete secondary admin | ✅ | ✅ (except self) | ❌ |
| Delete regular user | ✅ | ✅ | ❌ |
| Delete own account | ❌ | ❌ | ❌ |

---

## Code Implementation

The protection is implemented in:
- **Backend**: `auth-server/src/index.ts` - `toggle-admin` and `delete-user` endpoints
- **Frontend**: `src/pages/auth/admin.tsx` - UI hides buttons for protected admin

