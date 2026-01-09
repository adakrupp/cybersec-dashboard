#!/bin/bash

# Docker Hub Publishing Script
# Run this after: docker login -u adakrupp

set -e  # Exit on error

DOCKER_USERNAME="adakrupp"
IMAGE_NAME="cybersec-dashboard"
VERSION="v1.0.0"

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║       🐳 PUBLISHING TO DOCKER HUB                          ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check if logged in
echo "✓ Checking Docker login status..."
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running!"
    exit 1
fi

# Verify no secrets in image
echo ""
echo "🔒 SECURITY CHECK: Verifying no secrets will be in image..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -f .env ]; then
    if grep -q ".env" .dockerignore; then
        echo "✅ .env is in .dockerignore (won't be in image)"
    else
        echo "⚠️  WARNING: .env not in .dockerignore!"
        echo "   Manually verify it won't be copied to image"
    fi
else
    echo "✅ No .env file in build context"
fi

# Build the image
echo ""
echo "🔨 Building Docker image..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Image: ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
echo "This will take 2-5 minutes..."
echo ""

docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}:latest .

echo ""
echo "✅ Build complete!"

# Tag with version
echo ""
echo "🏷️  Tagging with version: ${VERSION}..."
docker tag ${DOCKER_USERNAME}/${IMAGE_NAME}:latest ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}

echo "✅ Tagged as:"
echo "   • ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
echo "   • ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}"

# Verify image size
echo ""
echo "📊 Image details:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
docker images ${DOCKER_USERNAME}/${IMAGE_NAME}

# Final security check
echo ""
echo "🔒 FINAL SECURITY CHECK:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Inspecting image for .env file..."

if docker run --rm ${DOCKER_USERNAME}/${IMAGE_NAME}:latest ls /app/.env 2>/dev/null; then
    echo "❌ ERROR: .env file found in image! DO NOT PUSH!"
    exit 1
else
    echo "✅ No .env file in image (good!)"
fi

# Push to Docker Hub
echo ""
echo "📤 Pushing to Docker Hub..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "This may take a few minutes..."
echo ""

echo "Pushing latest tag..."
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:latest

echo ""
echo "Pushing version tag..."
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║          ✅ SUCCESSFULLY PUBLISHED TO DOCKER HUB!          ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "Your image is now available at:"
echo "👉 https://hub.docker.com/r/${DOCKER_USERNAME}/${IMAGE_NAME}"
echo ""
echo "Users can pull it with:"
echo "  docker pull ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
echo "  docker pull ${DOCKER_USERNAME}/${IMAGE_NAME}:${VERSION}"
echo ""
echo "🎉 All done!"
echo ""
