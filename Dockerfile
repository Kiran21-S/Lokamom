# Use the official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Go back to the root project directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose port
EXPOSE 8000

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
