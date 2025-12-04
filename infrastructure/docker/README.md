# Docker Configuration

This directory contains Docker configuration files for containerizing the AI-Native Physical AI & Robotics Textbook platform.

## Files

- **`Dockerfile.frontend`**: Multi-stage build for Docusaurus frontend (Node.js → nginx)
- **`Dockerfile.backend`**: Python 3.11 image for FastAPI backend
- **`docker-compose.yml`**: Multi-container orchestration
- **`README.md`**: This file

## Quick Start

### Build Images

From repository root:

```bash
# Build frontend image
docker build -f infrastructure/docker/Dockerfile.frontend -t ai-textbook-frontend:latest .

# Build backend image
docker build -f infrastructure/docker/Dockerfile.backend -t ai-textbook-backend:latest .
```

### Run with Docker Compose

```bash
cd infrastructure/docker
docker-compose up
```

**Services**:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Stop Services

```bash
docker-compose down
```

## Configuration

### Environment Variables

The backend container reads from `../../.env` file. Ensure you have:

1. Copied `.env.example` to `.env`
2. Filled in required API keys and credentials

### Ports

- **Frontend**: 3000 (mapped from internal port 80)
- **Backend**: 8000 (mapped from internal port 8000)

To change ports, edit `docker-compose.yml`:
```yaml
ports:
  - "8080:80"  # Frontend on port 8080
  - "9000:8000"  # Backend on port 9000
```

## Architecture

### Frontend (Dockerfile.frontend)

**Stage 1 - Builder**:
- Base: `node:18-alpine`
- Install dependencies: `npm ci`
- Build static site: `npm run build`

**Stage 2 - Server**:
- Base: `nginx:alpine`
- Copy built files from builder
- Serve on port 80

**Benefits**:
- Small final image size (~25MB)
- Production-optimized nginx serving
- No Node.js in production image

### Backend (Dockerfile.backend)

- Base: `python:3.11-slim`
- Install system dependencies (gcc, postgresql-client)
- Install Python dependencies from `pyproject.toml`
- Copy application code
- Run with uvicorn ASGI server

**Benefits**:
- Slim base image (~150MB final size)
- Production-ready uvicorn server
- Hot reload disabled in production

## Troubleshooting

### Build Failures

**Problem**: "COPY failed: no source files were specified"

**Solution**: Ensure you're building from repository root, not from `infrastructure/docker/`:
```bash
cd ../../
docker build -f infrastructure/docker/Dockerfile.frontend -t ai-textbook-frontend:latest .
```

**Problem**: "npm install failed"

**Solution**: Check `frontend/package.json` and `package-lock.json` exist. Try:
```bash
cd frontend
npm install
cd ..
docker build -f infrastructure/docker/Dockerfile.frontend -t ai-textbook-frontend:latest .
```

### Runtime Issues

**Problem**: Backend container exits immediately

**Solution**: Check logs:
```bash
docker-compose logs backend
```

Common causes:
- Missing environment variables (check `.env` file)
- Port 8000 already in use (change port in docker-compose.yml)
- Import errors (ensure `backend/app/` structure is correct)

**Problem**: Frontend shows 502 Bad Gateway

**Solution**: Check if backend is running:
```bash
docker-compose ps
curl http://localhost:8000/health
```

**Problem**: "Cannot connect to database"

**Solution**: In initial scaffold phase, database is optional. The error is expected. Backend should still start with warnings.

### Network Issues

**Problem**: Frontend can't reach backend

**Solution**: docker-compose creates a network automatically. Services communicate via service names:
- Frontend → Backend: `http://backend:8000` (internal)
- External → Backend: `http://localhost:8000` (host)

## Production Deployment

These Dockerfiles are **placeholders for initial scaffold**. For production deployment:

1. **Security**:
   - Add health checks
   - Run as non-root user
   - Scan images for vulnerabilities

2. **Optimization**:
   - Use `.dockerignore` files
   - Multi-stage builds for smaller images
   - Layer caching optimization

3. **Orchestration**:
   - Use Kubernetes for scaling
   - Add load balancer
   - Configure auto-scaling

## References

- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Multi-stage Builds](https://docs.docker.com/build/building/multi-stage/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
