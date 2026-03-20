# Use a lightweight Python base image
FROM python:3.12-slim

# Install 'uv' directly from Astral's official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY . /app

# Use uv for instant virtual environment creation and dependency resolution
RUN uv venv /opt/venv && \
    . /opt/venv/bin/activate && \
    uv pip install google-adk mcp[cli] fastmcp uvicorn

ENV PATH="/opt/venv/bin:$PATH"