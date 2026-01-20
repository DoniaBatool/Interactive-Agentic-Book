---
name: jwt-authentication
description: Implement JWT-based stateless authentication with FastAPI for scalable, horizontally-scalable APIs (Phase 2 pattern)
---

# Skill: JWT Authentication (Secure Tokens + Cookies + Rotation)

## Description
Expert-level skill for implementing JWT auth safely: token issuance, validation, rotation, cookie vs header tradeoffs, CSRF protection, and RBAC-ready claims.

## When to Use
- Adding auth to an API
- Replacing “session only” with JWTs
- Multi-service authentication / gateway patterns

## Secure Defaults
- Short-lived access token + refresh token
- HttpOnly, Secure cookies when using cookies
- Audience/issuer checks; clock skew handling

## Playbook
1. **Decide transport**
   - Cookie (browser apps) vs Authorization header (APIs)
2. **Define claims**
   - `sub`, `exp`, `iat`, `iss`, `aud`, `role/scopes`
3. **Validate**
   - signature + issuer + audience + expiry
4. **Rotate**
   - refresh flow; revoke compromised refresh tokens
5. **Protect**
   - CSRF for cookie auth; rate limit login

## Output Artifacts
- Auth middleware/guards
- Token config (expiry, issuer, audience)
- Threat model notes for auth flows

## Integration
- Works with: `security-engineer`, `password-security`, `user-isolation`