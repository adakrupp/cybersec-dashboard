"""
News feed fetchers for RSS sources (including Reddit RSS feeds)
"""

import feedparser
from datetime import datetime, timezone
from django.utils import timezone as django_timezone
from .models import NewsSource, NewsArticle
import logging

logger = logging.getLogger(__name__)


class RSSFeedFetcher:
    """Fetch news from RSS feeds"""

    @staticmethod
    def fetch_feed(source):
        """Fetch articles from an RSS feed source"""
        try:
            feed = feedparser.parse(source.url)
            articles_created = 0

            for entry in feed.entries[:20]:  # Limit to 20 most recent
                # Parse published date
                published_date = None
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    published_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    published_date = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
                else:
                    published_date = django_timezone.now()

                # Get summary
                summary = ''
                if hasattr(entry, 'summary'):
                    summary = entry.summary[:500]  # Limit length
                elif hasattr(entry, 'description'):
                    summary = entry.description[:500]

                # Get author
                author = entry.get('author', '')

                # Create or update article
                article, created = NewsArticle.objects.get_or_create(
                    url=entry.link,
                    defaults={
                        'title': entry.title,
                        'source': source,
                        'published_date': published_date,
                        'summary': summary,
                        'author': author,
                    }
                )

                if created:
                    articles_created += 1

            logger.info(f"Fetched {articles_created} new articles from {source.name}")
            return articles_created

        except Exception as e:
            logger.error(f"Error fetching RSS feed from {source.name}: {str(e)}")
            return 0


def fetch_all_sources():
    """Fetch news from all active RSS sources (including Reddit RSS feeds)"""
    total_articles = 0

    # Fetch from all RSS sources (includes Reddit RSS feeds)
    rss_sources = NewsSource.objects.filter(is_active=True, source_type='RSS')
    for source in rss_sources:
        total_articles += RSSFeedFetcher.fetch_feed(source)

    logger.info(f"Total new articles fetched: {total_articles}")
    return total_articles
