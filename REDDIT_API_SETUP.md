# Reddit API Setup Guide

Reddit API is **100% FREE** with no rate limits for read-only access.

## Steps to Get Credentials

1. **Go to Reddit Apps Page**
   - Visit: https://www.reddit.com/prefs/apps
   - Log in to your Reddit account (create one if needed)

2. **Create a New App**
   - Scroll to the bottom
   - Click "create another app..." button

3. **Fill in the Form**
   - **Name**: `CyberSecHub` (or any name)
   - **App type**: Select **"script"** (important!)
   - **Description**: (optional) `Personal cybersecurity news dashboard`
   - **About URL**: (optional) Leave blank
   - **Redirect URI**: `http://localhost:8000` (required but not used)

4. **Get Your Credentials**
   - Click "create app"
   - You'll see your new app with:
     - **client_id**: The random string under the app name (looks like: `abc123XYZ789`)
     - **client_secret**: Labeled as "secret" (looks like: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`)

5. **Add to Your .env File**
   - Copy the values into your `.env` file:
   ```env
   REDDIT_CLIENT_ID=your_client_id_here
   REDDIT_CLIENT_SECRET=your_client_secret_here
   ```

## Important Notes

- ✅ **Free forever** - No credit card required
- ✅ **Read-only access** - We only read public posts
- ✅ **No rate limits** for reasonable use
- ✅ **No user authentication** needed (we don't post anything)
- 🔒 **Keep credentials private** - Never commit to GitHub

## Verify It Works

After adding credentials, restart Docker and activate Reddit sources:

```bash
# Restart containers
docker-compose restart

# Or in admin panel:
# Go to News > News sources
# Check "Is active" for r/netsec and r/cybersecurity
# Save
```

Then manually fetch to test:
```bash
docker-compose exec web python manage.py shell -c "from apps.news.tasks import fetch_all_news; fetch_all_news()"
```

You should see logs showing Reddit posts being fetched!
