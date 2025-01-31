# Stage 1: Build stage
FROM python:3.11-alpine AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    build-base \
    mariadb-dev \
    musl-dev \
    libffi-dev \
    gcc \
    python3-dev \
    py3-pip \
    openssl-dev

# Copy dependencies file
COPY requirements.txt .

# Install Python dependencies
RUN python -m venv /app/venv && \
    . /app/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create non-root user
RUN adduser --disabled-password --no-create-home django-user

# Install runtime dependencies
RUN apk add --no-cache \
    mariadb-connector-c-dev \
    libffi \
    bash \
    openssl

# Set working directory
WORKDIR /app

# Copy runtime Python dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Set ownership to non-root user
RUN chown -R django-user:django-user /app

# Create and set permissions for static and media directories
RUN mkdir -p /app/static /app/media && \
    chown -R django-user:django-user /app/static /app/media

# Switch to non-root user
USER django-user

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 5000

# Start the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "civic.wsgi:application"]