FROM python:3.13-slim AS builder

# Minimal system deps (curl for healthcheck only)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip uv

# Copy project metadata & sources for build
COPY pyproject.toml ./
COPY README.md ./
COPY app ./app

# Build wheel & sdist into dist/
RUN uv build

FROM python:3.13-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip uv

# Copy built artifacts from builder stage
COPY --from=builder /app/dist /tmp/dist

# Install wheel (prefer wheel over sdist)
RUN uv pip install /tmp/dist/*.whl --system --no-cache

# Copy only runtime essentials (optional: keep README for transparency)
COPY README.md ./
COPY app ./app

# Expose port (Render sets $PORT; fastapi/uvicorn will bind to it)
EXPOSE 8000

# HEALTHCHECK (optional - Render has native health checks; still useful locally)
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f http://localhost:8000/health || exit 1

# Default command uses dynamic PORT with fallback
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
