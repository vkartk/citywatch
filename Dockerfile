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
    openssl-dev \
    bash \
    && pip install --upgrade pip

# Copy dependencies file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install runtime dependencies
RUN apk add --no-cache \
    mariadb-connector-c-dev \
    libffi \
    openssl

# Copy runtime Python dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port for Gunicorn
EXPOSE 8000

# Start the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "civic.wsgi:application"]