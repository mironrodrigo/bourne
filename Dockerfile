# ✅ Versão otimizada com multi-stage build
# Build stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY pyproject.toml pdm.lock ./
RUN pip install pdm && \
    pdm install --prod --no-lock

# Runtime stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/__pypackages__/3.11/lib /usr/local/lib/python3.11/site-packages
COPY . .

# Instala dependências de runtime
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

CMD ["pdm", "run", "uvicorn", "bourne.main:app", "--host", "0.0.0.0"]