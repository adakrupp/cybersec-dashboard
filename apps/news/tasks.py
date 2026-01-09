"""
Celery tasks for news aggregation
"""

from celery import shared_task
from .feeds import fetch_all_sources
import logging

logger = logging.getLogger(__name__)


@shared_task
def fetch_all_news():
    """
    Periodic task to fetch news from all sources
    This task is scheduled in settings.py to run every 30 minutes
    """
    logger.info("Starting news fetch task...")
    try:
        total_articles = fetch_all_sources()
        logger.info(f"News fetch completed. {total_articles} new articles added.")
        return f"Success: {total_articles} articles fetched"
    except Exception as e:
        logger.error(f"Error in fetch_all_news task: {str(e)}")
        return f"Error: {str(e)}"


@shared_task
def fetch_single_source(source_id):
    """
    Fetch news from a single source (for manual triggers)
    """
    from .models import NewsSource
    from .feeds import RSSFeedFetcher, RedditFetcher

    try:
        source = NewsSource.objects.get(id=source_id)

        if source.source_type == 'RSS':
            articles_count = RSSFeedFetcher.fetch_feed(source)
        elif source.source_type == 'REDDIT':
            articles_count = RedditFetcher.fetch_subreddit(source)
        else:
            return f"Unknown source type: {source.source_type}"

        logger.info(f"Fetched {articles_count} articles from {source.name}")
        return f"Success: {articles_count} articles fetched from {source.name}"

    except NewsSource.DoesNotExist:
        logger.error(f"Source with id {source_id} does not exist")
        return f"Error: Source not found"
    except Exception as e:
        logger.error(f"Error fetching from source {source_id}: {str(e)}")
        return f"Error: {str(e)}"
