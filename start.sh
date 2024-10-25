#!/bin/bash

IMAGE_NAME="hadoop_python_image"
CONTAINER_NAME="hadoop_python"

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

if [ $? -ne 0 ]; then
    echo "Docker build failed. Exiting..."
    exit 1
fi

echo "Starting Docker container..."
docker run -d --name $CONTAINER_NAME \
    -p 9870:9870 \
    -v ./scripts:/scripts \
    $IMAGE_NAME

if [ $? -ne 0 ]; then
    echo "Failed to start Docker container. Exiting..."
    exit 1
fi

echo "Docker container started successfully!"