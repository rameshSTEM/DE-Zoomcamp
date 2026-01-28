FROM python:3.13-slim

# Python runtime behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Minimal system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# App setup
WORKDIR /app

# Install deps first (Docker cache win)
COPY pyproject.toml uv.lock ./
RUN uv pip install --system --frozen

# Copy source code
COPY src ./src

# Run the pipeline
CMD ["python", "-m", "pipeline.main"]
