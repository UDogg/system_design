FROM python:3.10-slim-bullseye

# Update the system and install necessary packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential default-libmysqlclient-dev pkg-config

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Set the working directory and copy requirements
WORKDIR /app
COPY ./requirements.txt /app

# Install Python dependencies
RUN pip install --no-cache-dir --requirement /app/requirements.txt

# Copy the rest of your application
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run your application
CMD ["python3", "server.py"]
