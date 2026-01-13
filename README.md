# CyberSecHub - Cybersecurity Dashboard

A comprehensive, self-hosted cybersecurity dashboard built with Django and HTMX. Stay updated with the latest security news, access curated learning resources, explore security tools, and track CVEs—all in one place.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

### 📰 News Aggregator
- Automatically fetch and display the latest cybersecurity news
- Multiple RSS feed sources:
  - Krebs on Security, BleepingComputer, The Hacker News
  - Dark Reading, SecurityWeek, Naked Security by Sophos
  - Graham Cluley, Threatpost
- Background updates every 30 minutes via Celery
- Filter by source and search functionality

### 📚 Learning Resources
- Curated catalog of cybersecurity learning materials
- Popular certifications (Security+, CEH, CISSP, OSCP, GIAC)
- Free and paid courses (Cybrary, TryHackMe, HackTheBox)
- Practice labs and CTF platforms
- Documentation (OWASP, NIST, CIS Controls)
- Filter by category, difficulty, and price

### 🛠️ Security Tools Directory
- Comprehensive catalog of 84 essential security tools
- 9 Categories: Network Analysis, Pentesting, Password Cracking, Web Security, Forensics, OSINT, Reverse Engineering, Vulnerability Scanning, Online Security Analysis
- Includes: Wireshark, Nmap, Metasploit, Burp Suite, OWASP ZAP, John the Ripper, Hashcat, and more
- Online analysis tools: VirusTotal, Cisco Talos Intelligence, URLhaus, Hybrid Analysis, AbuseIPDB, Have I Been Pwned, SSL Labs, and more
- Filter by category, platform, and open-source status
- Links to official sites and GitHub repositories

### 🗺️ Learning Paths
- Interactive skill trees for structured cybersecurity learning
- Prerequisite tracking shows learning dependencies
- Curated learning resources for each skill (courses, books, tutorials, documentation)
- Links to related tools and certifications
- Available paths: Web Security Fundamentals (more coming soon)
- Difficulty levels: Beginner, Intermediate, Advanced

### 🐛 CVE Tracker
- Search and track Common Vulnerabilities and Exposures
- Real-time integration with NVD (National Vulnerability Database) API
- Displays recent CVEs, CVSS scores, and severity levels
- Shows affected products and references
- Caches results for performance
- Track popular searches

## Tech Stack

- **Backend**: Django 5.0 + Django REST Framework
- **Frontend**: HTMX + TailwindCSS (modern, responsive design)
- **Database**: PostgreSQL (production) / SQLite (development)
- **Task Queue**: Celery + Redis (background news fetching)
- **Deployment**: Docker + Docker Compose
- **APIs**: RSS feeds (feedparser), NVD CVE API

## System Requirements

### Minimum Requirements (Development/Personal Use)
- **RAM**: 2 GB (1 GB for containers + 1 GB for OS)
- **Disk Space**: 2 GB free space
- **CPU**: 1-2 cores (any modern CPU)
- **OS**: Linux, macOS, or Windows with Docker support

### Recommended for Production
- **RAM**: 4-8 GB
- **Disk Space**: 10-20 GB (for logs, database growth, backups)
- **CPU**: 2-4 cores
- **OS**: Linux (Ubuntu 20.04+ or Debian 11+)

### Current Resource Usage
The Docker stack consists of 5 containers with the following footprint:
- **PostgreSQL Database**: ~28 MB RAM, ~50 MB disk
- **Redis Cache**: ~10 MB RAM
- **Django Web Server** (3 Gunicorn workers): ~135 MB RAM
- **Celery Worker**: ~564 MB RAM (background tasks)
- **Celery Beat**: ~63 MB RAM (task scheduler)
- **Total**: ~800 MB RAM, ~600-800 MB disk space

**Perfect for**:
- Any modern laptop or desktop
- Minimal VPS ($5-10/month tier from DigitalOcean, Linode, Vultr, etc.)
- Cloud platforms (Railway, Render, DigitalOcean App Platform)
- Raspberry Pi 4 (4GB model)

## Quick Start with Docker (Recommended)

### Prerequisites

- Docker and Docker Compose installed

### Installation

1. **Clone or download the repository**
   ```bash
   cd cybersec-dashboard
   ```

2. **Run the setup script**
   ```bash
   ./docker-run.sh
   ```

   The script will:
   - Create a `.env` file from `.env.example`
   - Build and start Docker containers
   - Run database migrations
   - Optionally create a superuser
   - Optionally seed the database with initial data
   - Optionally fetch initial news articles

3. **Configure environment variables**

   Edit `.env` and update:
   ```env
   SECRET_KEY=your-secret-key-here-generate-a-random-one
   ```

   Generate a secure secret key:
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

4. **Access the dashboard**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Manual Setup (Without Docker)

### Prerequisites

- Python 3.11+
- PostgreSQL (or use SQLite for development)
- Redis (for Celery)

### Installation Steps

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Seed database (optional)**
   ```bash
   python scripts/seed_data.py
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Run Celery worker (in separate terminal)**
   ```bash
   celery -A config worker -l info
   ```

9. **Run Celery beat (in separate terminal)**
   ```bash
   celery -A config beat -l info
   ```

## Docker Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose stop

# Restart services
docker-compose restart

# Stop and remove containers
docker-compose down

# Rebuild containers
docker-compose up --build -d

# Execute management commands
docker-compose exec web python manage.py <command>

# Access Django shell
docker-compose exec web python manage.py shell

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Manually trigger news fetch
docker-compose exec web python manage.py shell -c "from apps.news.tasks import fetch_all_news; fetch_all_news()"
```

## Project Structure

```
cybersec-dashboard/
├── apps/
│   ├── core/           # Base templates, navigation
│   ├── news/           # News aggregator
│   ├── resources/      # Learning resources
│   ├── tools/          # Security tools directory
│   ├── cve/            # CVE tracker
│   └── learning_paths/ # Interactive learning paths/skill trees
├── config/             # Django settings
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py
├── scripts/
│   └── seed_data.py    # Database seeding script
├── static/             # Static files
├── media/              # User uploads
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── manage.py
└── README.md
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | (required) |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `DATABASE_URL` | PostgreSQL connection string | SQLite (development) |
| `CELERY_BROKER_URL` | Redis URL for Celery | `redis://redis:6379/0` |

### Adding News Sources

1. Access the admin panel at http://localhost:8000/admin
2. Navigate to **News > News sources**
3. Click "Add news source"
4. Fill in:
   - Name: Source name
   - Source type: RSS or Reddit
   - URL: Feed URL or Reddit subreddit URL
   - Is active: Checked
   - Fetch frequency: Minutes between fetches (default: 30)

### Celery Task Schedule

Background tasks are configured in `config/settings/base.py`:

- **News Fetch**: Every 30 minutes
  ```python
  'fetch-news-every-30-minutes': {
      'task': 'apps.news.tasks.fetch_all_news',
      'schedule': 1800.0,  # seconds
  }
  ```

## Docker Hub

Pre-built Docker images are available on Docker Hub:

**Image:** [adakrupp/cybersec-dashboard](https://hub.docker.com/r/adakrupp/cybersec-dashboard)

```bash
# Pull the latest image
docker pull adakrupp/cybersec-dashboard:latest

# Or pull a specific version
docker pull adakrupp/cybersec-dashboard:v1.0.0
```

To use the pre-built image, update your `docker-compose.yml` to use `image: adakrupp/cybersec-dashboard:latest` instead of building locally.

## Deployment

### Production Checklist

1. **Set environment to production**
   ```env
   DJANGO_ENV=production
   DEBUG=False
   ```

2. **Use strong SECRET_KEY**
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

3. **Configure ALLOWED_HOSTS**
   ```env
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

4. **Use PostgreSQL database**
   ```env
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```

5. **Enable HTTPS**
   - Configure `SECURE_SSL_REDIRECT=True`
   - Use reverse proxy (nginx) with SSL certificate

### Deployment Options

#### Option 1: VPS (DigitalOcean, Linode, etc.)

1. SSH into your server
2. Clone the repository
3. Set up Docker and Docker Compose
4. Configure environment variables
5. Run `./docker-run.sh`
6. Set up nginx as reverse proxy with SSL

#### Option 2: Cloud Platforms

**Railway**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

**Render**
- Connect your GitHub repository
- Set environment variables in dashboard
- Deploy as Docker container

**DigitalOcean App Platform**
- Connect repository
- Configure as Docker app
- Set environment variables
- Deploy

## Customization

### Adding New RSS Feeds

Edit `scripts/seed_data.py` and add to `seed_news_sources()`:

```python
{
    'name': 'Your Source Name',
    'source_type': 'RSS',
    'url': 'https://example.com/feed.xml',
    'is_active': True,
}
```

### Changing Theme Colors

Edit `apps/core/templates/base.html` in the Tailwind config:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'cyber-dark': '#your-color',
                'cyber-cyan': '#your-color',
                // ...
            }
        }
    }
}
```

### Adding New Tool Categories

Edit `scripts/seed_data.py` and add to `seed_tool_categories()`.

## Troubleshooting

### News Not Fetching

1. View Celery logs: `docker-compose logs celery`
2. Check that Celery beat is running: `docker-compose logs celery-beat`
3. Manually trigger fetch:
   ```bash
   docker-compose exec web python manage.py shell
   >>> from apps.news.tasks import fetch_all_news
   >>> fetch_all_news()
   ```
4. Verify news sources are active in admin panel: http://localhost:8000/admin

### Database Issues

```bash
# Reset database (WARNING: deletes all data)
docker-compose down -v
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python scripts/seed_data.py
```

### CVE Search Not Working

The NVD API has rate limits (5 requests per 30 seconds for unauthenticated requests). The app handles this automatically, but searches may take a few seconds.

## Contributing

Contributions are welcome! This is a portfolio/community project.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution

- [ ] Add more news sources
- [ ] Expand learning resources catalog
- [ ] Add more security tools
- [ ] Implement user authentication for bookmarking
- [ ] Add dark/light theme toggle
- [ ] Create mobile app
- [ ] Add threat intelligence feeds
- [ ] Implement export functionality (PDF reports)
- [ ] Add security podcast aggregator
- [ ] Create cybersecurity events calendar

## License

This project is open source and available under the MIT License.

## Acknowledgments

- **News Sources**: Krebs on Security, BleepingComputer, The Hacker News, Dark Reading, SecurityWeek, Naked Security by Sophos, Graham Cluley, Threatpost
- **APIs**: National Vulnerability Database (NVD)
- **Framework**: Django, HTMX, TailwindCSS
- **Icons**: Font Awesome

## Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review existing GitHub issues
3. Open a new issue with detailed information

## Roadmap

### Phase 1 (Completed)
- [x] News aggregator (RSS feeds)
- [x] Learning resources catalog (45 resources)
- [x] Security tools directory (84 tools)
- [x] Online security analysis tools (VirusTotal, Cisco Talos, etc.)
- [x] CVE tracker
- [x] Interactive learning paths with skill trees
- [x] Docker deployment
- [x] Background task scheduling

### Phase 2 (Future)
- [ ] User authentication and profiles
- [ ] Bookmark/save functionality
- [ ] Progress tracking for learning paths
- [ ] Email digest subscriptions
- [ ] Advanced CVE filtering
- [ ] Threat intelligence integration
- [ ] Security podcasts feed
- [ ] More learning paths (Network Security, Pentesting, Blue Team)

### Phase 3 (Future)
- [ ] Mobile-responsive PWA
- [ ] API endpoints for external access
- [ ] Custom RSS feed builder
- [ ] Community contributions (user-submitted resources)
- [ ] Job board integration
- [ ] Cybersecurity events calendar

---

**Built for the cybersecurity community**

*Perfect for portfolios, learning, and staying informed in the ever-evolving world of cybersecurity.*
