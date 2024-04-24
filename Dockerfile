# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install NLTK and its dependencies
RUN pip install --no-cache-dir nltk

# Download NLTK stop words
RUN python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "Script.py"]