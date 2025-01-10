# Use a lightweight Python base image
FROM python:3.9-slim-bullseye

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application into the container
COPY ./app.py .

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=52032

# Expose Flask's default port
EXPOSE 52032

RUN mkdir -p /arq

# Run the Flask application
CMD ["python", "./app.py"]
