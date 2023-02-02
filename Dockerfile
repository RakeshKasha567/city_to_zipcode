# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the files to the container
COPY . .

# Expose port 5003 for the Flask application
EXPOSE 5003

# Run the command to start the Flask application
CMD ["python", "app.py"]


