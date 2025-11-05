# 🐍 Backend Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose backend port
EXPOSE 5001

# Run Flask app
CMD ["python", "app.py"]
