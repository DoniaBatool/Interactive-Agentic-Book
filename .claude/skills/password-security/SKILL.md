---
name: password-security
description: Implement secure password hashing with bcrypt following industry best practices (Phase 2 pattern)
---

# Skill: Password Security (Hashing, Policies, Resets)

## Description
Expert-level skill for implementing password-based auth safely: hashing, policies, reset flows, and auditability—without leaking secrets or enabling account takeover.

## Non-Negotiables
- Never store plaintext passwords
- Never log passwords/reset tokens
- Always use a strong adaptive hash (bcrypt/argon2)

## Playbook
1. **Hashing**
   - Use bcrypt (or argon2) with appropriate cost
   - Store: `{hash, salt}` (bcrypt handles salt internally)
2. **Policies**
   - Minimum length; block common passwords; allow passphrases
3. **Login defense**
   - Rate limit; lockout/backoff; suspicious activity logging
4. **Reset flow**
   - One-time token, short expiry, invalidate after use
   - Email link points to frontend reset page
5. **Verification**
   - Tests for hash/verify; reset expiry; rate limiting

## Output Artifacts
- Password hashing module + tests
- Reset endpoints + email templates
- Security notes (threats + mitigations)

## Integration
- Works with: `security-engineer`, `jwt-authentication`, `production-checklist`