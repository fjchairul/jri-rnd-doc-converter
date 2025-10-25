# Use an official Python runtime as base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy backend and frontend build files to container
COPY backend backend
COPY jri-helper-doc-md/build jri-helper-doc-md/build

# Copy backend requirements
COPY backend/requirements.txt backend/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r backend/requirements.txt && \
    pip install pypandoc flask-cors

# Install pandoc
RUN apt-get update && apt-get install -y pandoc && apt-get clean

# Expose port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "backend/app.py"]
