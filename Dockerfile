# Use an official Python slim image.
FROM python:3.9-slim

# Prevent Python from writing .pyc files and enable unbuffered stdout.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory.
WORKDIR /app

# Install dependencies.
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project.
COPY . /app/

# Expose port 5000 (for the web app) and 8000 (for the API) if needed.
EXPOSE 5000
EXPOSE 8000

# Default command to run the web app.
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5000"]
