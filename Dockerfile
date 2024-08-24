# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app.zip file from the current directory to the /app directory in the container
COPY app.zip .

# Install unzip utility to extract the app.zip file
RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

# Unzip the app.zip file into the /app directory
RUN unzip app.zip

# Install dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
