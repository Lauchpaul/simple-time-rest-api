# Use an official lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY app.py .

# Expose port 5000 for network access
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
