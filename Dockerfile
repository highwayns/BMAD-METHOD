# BMAD-METHOD Dockerfile
# Multi-stage build for optimized Node.js CLI application

# Stage 1: Build stage
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies (include dev so husky is available for "prepare")
RUN npm ci && \
    npm cache clean --force

# Stage 2: Production stage
FROM node:20-alpine

# Set environment variables
ENV NODE_ENV=production \
    NPM_CONFIG_LOGLEVEL=warn

# Create app user for security
RUN addgroup -g 1001 -S bmad && \
    adduser -S -D -H -u 1001 -h /app -s /sbin/nologin -G bmad -g bmad bmad

# Set working directory
WORKDIR /app

# Copy dependencies from builder
COPY --from=builder --chown=bmad:bmad /app/node_modules ./node_modules

# Copy application files
COPY --chown=bmad:bmad . .

# Switch to non-root user
USER bmad

# Set the entrypoint to the CLI
ENTRYPOINT ["node", "tools/cli/bmad-cli.js"]

# Default command shows help
CMD ["--help"]

# Health check (optional - adjust based on your needs)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node -e "console.log('healthy')" || exit 1

# Labels for metadata
LABEL maintainer="Brian (BMad) Madison" \
      version="6.0.0-alpha.0" \
      description="Breakthrough Method of Agile AI-driven Development" \
      org.opencontainers.image.source="https://github.com/bmad-code-org/BMAD-METHOD"
