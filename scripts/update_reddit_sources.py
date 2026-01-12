"""
Update Reddit news sources to use RSS feeds instead of API
Run this with: docker-compose exec web python scripts/update_reddit_sources.py
"""

import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.news.models import NewsSource


def update_reddit_sources():
    """Update Reddit sources to use RSS feeds"""
    print("\n" + "="*60)
    print("UPDATING REDDIT SOURCES TO USE RSS FEEDS")
    print("="*60 + "\n")

    # Update r/netsec
    try:
        netsec = NewsSource.objects.get(name='r/netsec')
        netsec.source_type = 'RSS'
        netsec.url = 'https://www.reddit.com/r/netsec/.rss'
        netsec.is_active = True
        netsec.save()
        print("✓ Updated r/netsec to use RSS feed")
    except NewsSource.DoesNotExist:
        print("⚠ r/netsec source not found - run seed_data.py first")

    # Update r/cybersecurity
    try:
        cybersec = NewsSource.objects.get(name='r/cybersecurity')
        cybersec.source_type = 'RSS'
        cybersec.url = 'https://www.reddit.com/r/cybersecurity/.rss'
        cybersec.is_active = True
        cybersec.save()
        print("✓ Updated r/cybersecurity to use RSS feed")
    except NewsSource.DoesNotExist:
        print("⚠ r/cybersecurity source not found - run seed_data.py first")

    print("\n" + "="*60)
    print("✓ REDDIT SOURCES UPDATED SUCCESSFULLY!")
    print("="*60)
    print("\nReddit feeds are now using public RSS (no API key needed)")
    print("Active sources:")
    for source in NewsSource.objects.filter(is_active=True):
        print(f"  • {source.name} ({source.source_type})")
    print("")


if __name__ == '__main__':
    update_reddit_sources()
