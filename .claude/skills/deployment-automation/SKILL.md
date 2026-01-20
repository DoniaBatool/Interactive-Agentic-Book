---
name: deployment-automation
description: Automate deployment workflow with Alembic migrations, environment setup, and staging/production deployment (Phase 3)
---

# Skill: Deployment Automation (CI/CD + Preview Envs + Rollbacks)

## Description
Expert-level skill to automate deployments safely: build pipelines, preview environments, environment promotion, and fast rollback strategies.

## When to Use
- Any repo that deploys to Render/Vercel/Netlify/K8s
- Teams hitting “it works locally” or manual deploy mistakes
- Need preview deployments for PRs

## Outputs
- CI workflow(s): lint → test → build → deploy
- Environment matrix (dev/staging/prod) with documented vars
- Rollback procedure (1-click or scripted)

## Playbook
1. **Define build + start commands**
2. **Add CI gates**
   - format/lint/typecheck/tests
3. **Preview deployments**
   - per-PR ephemeral envs where possible
4. **Promote**
   - deploy from artifact, not from local machine
5. **Rollback**
   - keep last known good; verify health after rollback

## Safety Checklist
- [ ] Secrets stored only in platform env vars
- [ ] Health checks configured (`/health`)
- [ ] Deploys are repeatable and pinned (lockfiles)
- [ ] Logs/metrics accessible immediately after deploy

## Integration
- Works with: `devops-engineer`, `production-checklist`, `structured-logging`