# syntax=docker/dockerfile:1
#
# Hardened example Dockerfile for the ticket-desk MCP server from Deep Dive A (Python, Streamable HTTP).
# This is a teaching example, not a product. Copy it, with .dockerignore, into the Deep Dive A lab folder
# (next to server.py, app.py and requirements.txt) and build from there. See README.md in this folder.
#
# What it shows, in order: a pinned base, a multi-stage build, no secrets, a non-root user, and nothing
# in the runtime stage that the server does not need.

# ---------- Build stage: has pip and build tools; nothing from here ships unless copied ----------
# Pin the base by digest. The tag is kept for humans; the digest is what Docker checks.
# Resolve the digest for the tag you choose, then paste it after the @:
#   docker buildx imagetools inspect python:3.13-slim --format '{{json .Manifest.Digest}}'
# Until you do, the line below builds from the tag alone. Step 1 of the walkthrough is to pin it.
ARG BASE_IMAGE=python:3.13-slim
FROM ${BASE_IMAGE} AS build

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Dependencies first, so this layer is cached until requirements.txt changes.
COPY requirements.txt .
# The lab pins exact versions. For production, generate hashes too and add --require-hashes:
#   pip-compile --generate-hashes requirements.in
RUN python -m venv /opt/venv && /opt/venv/bin/pip install -r requirements.txt

# Only the files the server needs. .dockerignore keeps tests, caches and local env files out of the context.
COPY server.py app.py ./

# ---------- Runtime stage: fresh base, only the virtual environment and the code ----------
FROM ${BASE_IMAGE}

# Metadata for traceability (CI fills these from the commit; see ci-pipeline.yml.example).
ARG GIT_SHA=unknown
LABEL org.opencontainers.image.title="ticket-desk" \
      org.opencontainers.image.description="Deep Dive A lab MCP server, hardened build example" \
      org.opencontainers.image.revision="${GIT_SHA}" \
      org.opencontainers.image.licenses="MIT"

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
# Host headers the server accepts. Behind a proxy, set this to your real host name at run time.
ENV MCP_ALLOWED_HOSTS="localhost:*,127.0.0.1:*"

WORKDIR /app
COPY --from=build /opt/venv /opt/venv
COPY --from=build /app/server.py /app/app.py ./

# Non-root. A numeric UID works without a passwd entry and matches the common "nonroot" convention (65532).
# The app writes nothing, so it also runs with a read-only root filesystem (docker run --read-only).
USER 65532:65532

EXPOSE 8000

# Listen on all interfaces inside the container; publish it to localhost only on the host:
#   docker run --rm --read-only -p 127.0.0.1:8000:8000 ticket-desk:dev
# The Host-header check in app.py still applies, so a request with Host: evil.example gets 421.
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Deliberately absent: API keys, .env files, a shell session, a package manager step in the runtime stage,
# and "RUN rm" of anything secret (deleting in a later layer does not remove it from an earlier one).
