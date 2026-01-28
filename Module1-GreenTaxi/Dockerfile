FROM python:3.13-slim

# Python runtime behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV PATH="/root/.local/bin:$PATH"

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

#ignore the [dependency-groups] dev section
RUN uv sync --frozen --no-cache --no-install-project --no-dev

# Copy source code
COPY src ./src

# Make uv explicitly executable
RUN chmod +x /usr/local/bin/uv

# Run the pipeline
CMD ["uv", "run", "python", "src/pipeline.py"]
