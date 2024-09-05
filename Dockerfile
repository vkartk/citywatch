FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the Django app will run on
EXPOSE 8000

# Define the command to run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "civic.wsgi:application"]