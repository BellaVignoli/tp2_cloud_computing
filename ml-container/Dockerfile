# Use a lightweight Python base image
FROM python:3.9-slim-bullseye

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rule generation code into the container
COPY recommendation_model.py .

RUN mkdir -p arq

# Set the default command to execute the rule generation script
CMD ["python", "recommendation_model.py"]
