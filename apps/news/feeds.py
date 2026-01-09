"""
News feed fetchers for RSS and Reddit sources
"""

import feedparser
import praw
from datetime import datetime, timezone
from django.conf import settings
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


class RedditFetcher:
    """Fetch news from Reddit subreddits"""

    @staticmethod
    def fetch_subreddit(source):
        """Fetch top posts from a subreddit"""
        try:
            # Check if Reddit credentials are configured
            if not settings.REDDIT_CLIENT_ID or not settings.REDDIT_CLIENT_SECRET:
                logger.warning(f"Reddit API credentials not configured. Skipping {source.name}")
                return 0

            # Initialize Reddit client
            reddit = praw.Reddit(
                client_id=settings.REDDIT_CLIENT_ID,
                client_secret=settings.REDDIT_CLIENT_SECRET,
                user_agent=settings.REDDIT_USER_AGENT,
            )

            # Extract subreddit name from URL (e.g., r/netsec from https://reddit.com/r/netsec)
            subreddit_name = source.url.split('/r/')[-1].rstrip('/')

            subreddit = reddit.subreddit(subreddit_name)
            articles_created = 0

            # Fetch hot posts
            for submission in subreddit.hot(limit=20):
                # Skip stickied posts
                if submission.stickied:
                    continue

                # Get the actual URL (might be reddit post or external link)
                url = submission.url if not submission.is_self else f"https://reddit.com{submission.permalink}"

                # Parse published date
                published_date = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)

                # Create or update article
                article, created = NewsArticle.objects.get_or_create(
                    url=url,
                    defaults={
                        'title': submission.title,
                        'source': source,
                        'published_date': published_date,
                        'summary': submission.selftext[:500] if submission.is_self else '',
                        'author': str(submission.author) if submission.author else '',
                        'score': submission.score,
                    }
                )

                # Update score if article exists
                if not created:
                    article.score = submission.score
                    article.save()
                else:
                    articles_created += 1

            logger.info(f"Fetched {articles_created} new posts from {source.name}")
            return articles_created

        except Exception as e:
            logger.error(f"Error fetching Reddit posts from {source.name}: {str(e)}")
            return 0


def fetch_all_sources():
    """Fetch news from all active sources"""
    total_articles = 0

    # Fetch from RSS sources
    rss_sources = NewsSource.objects.filter(is_active=True, source_type='RSS')
    for source in rss_sources:
        total_articles += RSSFeedFetcher.fetch_feed(source)

    # Fetch from Reddit sources
    reddit_sources = NewsSource.objects.filter(is_active=True, source_type='REDDIT')
    for source in reddit_sources:
        total_articles += RedditFetcher.fetch_subreddit(source)

    logger.info(f"Total new articles fetched: {total_articles}")
    return total_articles
