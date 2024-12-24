# Use an official Python runtime as the base image
FROM python:3.13.1-slim

# Set environment variables to prevent Python from writing .pyc files
# and to ensure stdout/stderr are logged
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app/

# Install Python dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django app
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
