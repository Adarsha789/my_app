# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=src.app
ENV FLASK_RUN_HOST=0.0.0.0

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the whole project
COPY . .

# Expose port for Flask
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run"]
