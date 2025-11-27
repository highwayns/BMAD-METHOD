# Docker Usage Guide for BMAD-METHOD

This guide explains how to build and run BMAD-METHOD using Docker.

## Quick Start

### Build the Docker Image

```bash
docker build -t bmad-method:latest .
```

### Run the Container

```bash
# Show help
docker run --rm bmad-method:latest --help

# Run with specific command
docker run --rm bmad-method:latest status

# Run with mounted project directory
docker run --rm -v $(pwd):/workspace bmad-method:latest install
```

## Using Docker Compose

### Build and Run

```bash
# Build the image
docker-compose build

# Run a command
docker-compose run --rm bmad --help
docker-compose run --rm bmad status
docker-compose run --rm bmad install
```

### Interactive Mode

To run an interactive shell inside the container:

```bash
docker-compose run --rm --entrypoint /bin/sh bmad
```

## Advanced Usage

### Mount Configuration Files

```bash
docker run --rm \
  -v $(pwd):/workspace \
  -v ~/.bmad:/home/bmad/.bmad:ro \
  bmad-method:latest install
```

### Set Environment Variables

```bash
docker run --rm \
  -e NODE_ENV=development \
  -e DEBUG=true \
  bmad-method:latest status
```

### Network Access

If BMAD needs network access for external services:

```bash
docker run --rm \
  --network host \
  -v $(pwd):/workspace \
  bmad-method:latest install
```

## Build Options

### Development Build

For development with all dependencies:

```dockerfile
# In Dockerfile, change the npm install line to:
RUN npm ci && npm cache clean --force
```

Then rebuild:

```bash
docker build -t bmad-method:dev .
```

### Multi-Architecture Build

Build for multiple platforms:

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t bmad-method:latest \
  --push .
```

## Image Management

### View Built Images

```bash
docker images | grep bmad-method
```

### Remove Old Images

```bash
docker rmi bmad-method:old-tag
```

### Clean Up

```bash
# Remove all unused images
docker image prune -a

# Remove all unused containers, networks, and volumes
docker system prune -a --volumes
```

## Troubleshooting

### Container Won't Start

Check logs:
```bash
docker logs bmad-cli
```

### Permission Issues

Ensure mounted volumes have correct permissions:
```bash
chmod -R 755 /path/to/project
```

### Out of Memory

Increase memory limit in docker-compose.yml:
```yaml
deploy:
  resources:
    limits:
      memory: 4G
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Docker Build

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build Docker image
        run: docker build -t bmad-method:${{ github.sha }} .

      - name: Run tests
        run: docker run --rm bmad-method:${{ github.sha }} status
```

### GitLab CI Example

```yaml
build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

## Production Deployment

### Using Docker Hub

```bash
# Tag the image
docker tag bmad-method:latest username/bmad-method:6.0.0-alpha.0

# Push to Docker Hub
docker push username/bmad-method:6.0.0-alpha.0
```

### Using Private Registry

```bash
# Tag for private registry
docker tag bmad-method:latest registry.example.com/bmad-method:6.0.0-alpha.0

# Push to private registry
docker push registry.example.com/bmad-method:6.0.0-alpha.0
```

## Security Considerations

- The container runs as non-root user (`bmad`) for security
- Only production dependencies are installed
- Sensitive files are excluded via `.dockerignore`
- Health checks are enabled for monitoring

## Performance Optimization

### Layer Caching

The Dockerfile is optimized for layer caching:
1. Dependencies are installed first (changes less frequently)
2. Application code is copied last (changes more frequently)

### Image Size

Current image uses `node:20-alpine` for minimal size (~150MB).

To further reduce size:
```bash
docker build --squash -t bmad-method:slim .
```

## Support

For issues related to Docker setup, please check:
- [Docker Documentation](https://docs.docker.com/)
- [BMAD-METHOD Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues)
