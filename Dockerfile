# Dockerfile

# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if any are needed)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
# && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the application port
EXPOSE 8000

# Start the API with Uvicorn
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
