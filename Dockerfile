# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
# We'll install matplotlib and jupyterlab directly for this example.
RUN pip install --no-cache-dir matplotlib jupyterlab

# Make port 8888 available to the world outside this container
EXPOSE 8888