# Use the official Python image from the Docker Hub
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

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