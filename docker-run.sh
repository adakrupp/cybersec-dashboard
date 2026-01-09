#!/bin/bash

# CyberSec Dashboard - Docker Startup Script
# This script helps you quickly start the dashboard with Docker Compose

set -e

echo "🔐 CyberSec Dashboard - Docker Setup"
echo "====================================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found. Creating from .env.example..."
    cp .env.example .env
    echo "✓ Created .env file"
    echo ""
    echo "⚙️  Please edit .env and configure:"
    echo "   - SECRET_KEY (generate a random one)"
    echo "   - REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET"
    echo "   - Other settings as needed"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo "✓ Found .env file"
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "✗ Docker is not running. Please start Docker and try again."
    exit 1
fi

echo "✓ Docker is running"
echo ""

# Check if docker-compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "✗ docker-compose not found. Please install docker-compose."
    exit 1
fi

echo "✓ docker-compose found"
echo ""

# Build and start containers
echo "🐳 Building and starting Docker containers..."
echo ""

docker-compose up --build -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

# Run migrations
echo ""
echo "📊 Running database migrations..."
docker-compose exec -T web python manage.py migrate

# Create superuser (optional)
echo ""
read -p "Do you want to create an admin superuser? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    docker-compose exec web python manage.py createsuperuser
fi

# Seed data
echo ""
read -p "Do you want to seed the database with initial data? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🌱 Seeding database..."
    docker-compose exec -T web python scripts/seed_data.py
fi

# Fetch initial news
echo ""
read -p "Do you want to fetch initial news articles? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📰 Fetching initial news (this may take a minute)..."
    docker-compose exec -T web python manage.py shell -c "from apps.news.tasks import fetch_all_news; fetch_all_news()"
fi

echo ""
echo "====================================="
echo "✅ CyberSec Dashboard is running!"
echo "====================================="
echo ""
echo "🌐 Access the dashboard at: http://localhost:8000"
echo "🔐 Admin panel at: http://localhost:8000/admin"
echo ""
echo "Useful commands:"
echo "  View logs:        docker-compose logs -f"
echo "  Stop services:    docker-compose stop"
echo "  Restart services: docker-compose restart"
echo "  Stop & remove:    docker-compose down"
echo ""
