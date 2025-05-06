# Use a Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install required dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Expose the relevant port (if needed)
EXPOSE 8080

# Set the default command to run the application
CMD ["python", "app.py"]
