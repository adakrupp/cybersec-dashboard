# Next Steps - Adding Reddit & Publishing

## ✅ Current Status

Your dashboard is **SECURE** and ready to publish:

- ✅ `.env` is gitignored (your secrets are safe)
- ✅ `.env.example` has only placeholders
- ✅ Docker image will NOT contain secrets
- ✅ All security checks pass

## 📝 Step 1: Add Reddit API Credentials (5 minutes)

1. **Get Reddit API credentials** (follow `REDDIT_API_SETUP.md`)
   - Go to https://www.reddit.com/prefs/apps
   - Create app (type: "script")
   - Get `client_id` and `client_secret`

2. **Add to your .env file**
   ```bash
   nano .env
   ```

   Update these lines:
   ```env
   REDDIT_CLIENT_ID=your_actual_client_id_here
   REDDIT_CLIENT_SECRET=your_actual_secret_here
   ```

3. **Restart Docker**
   ```bash
   docker-compose restart
   ```

4. **Activate Reddit sources in admin**
   - Go to http://localhost:8000/admin
   - Navigate to News > News sources
   - Check "Is active" for:
     - r/netsec
     - r/cybersecurity
   - Save

5. **Test it works**
   ```bash
   docker-compose exec web python manage.py shell -c "from apps.news.tasks import fetch_all_news; fetch_all_news()"
   ```

   You should see logs showing Reddit posts being fetched!

## 📦 Step 2: Publish to GitHub (Safe!)

1. **Run security check**
   ```bash
   ./check-secrets.sh
   ```

   Should show: "✅ All security checks passed!"

2. **Create GitHub repository**
   - Go to https://github.com/new
   - Name: `cybersec-dashboard` (or your choice)
   - Description: "Self-hosted cybersecurity dashboard with news aggregation, learning resources, tools directory, and CVE tracker"
   - Make it **Public**
   - DON'T initialize with README (we have one)

3. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit: CyberSec Dashboard"
   git remote add origin https://github.com/YOUR_USERNAME/cybersec-dashboard.git
   git push -u origin main
   ```

4. **Verify .env is NOT on GitHub**
   - Check your repo on GitHub
   - Should see `.env.example` but NOT `.env`
   - ✅ Your secrets are safe!

## 🐳 Step 3: Publish to Docker Hub (Optional)

1. **Create Docker Hub account** (if needed)
   - https://hub.docker.com/signup

2. **Login**
   ```bash
   docker login
   ```

3. **Build and push**
   ```bash
   # Build the image
   docker build -t YOUR_DOCKERHUB_USERNAME/cybersec-dashboard:latest .

   # Push to Docker Hub
   docker push YOUR_DOCKERHUB_USERNAME/cybersec-dashboard:latest

   # Tag a version
   docker tag YOUR_DOCKERHUB_USERNAME/cybersec-dashboard:latest YOUR_DOCKERHUB_USERNAME/cybersec-dashboard:v1.0.0
   docker push YOUR_DOCKERHUB_USERNAME/cybersec-dashboard:v1.0.0
   ```

4. **Make it public**
   - Go to Docker Hub repository settings
   - Set to Public

5. **Update README with your Docker Hub link**
   ```bash
   nano README.md
   ```

   Add at the top:
   ```markdown
   ![Docker Pulls](https://img.shields.io/docker/pulls/YOUR_USERNAME/cybersec-dashboard)
   ```

## 🎯 Step 4: Create GitHub Releases (Optional but Professional)

1. **Create a release on GitHub**
   - Go to your repo → Releases → Create new release
   - Tag: `v1.0.0`
   - Title: "Initial Release - CyberSec Dashboard v1.0.0"
   - Description:
     ```markdown
     ## Features
     - 📰 News aggregator (RSS + Reddit)
     - 📚 Learning resources catalog
     - 🛠️ Security tools directory
     - 🐛 CVE tracker with NVD API
     - 🐳 Fully Dockerized

     ## Installation
     See [README.md](./README.md) for setup instructions
     ```

## 📋 Security Reminders

**NEVER commit:**
- ❌ `.env` file
- ❌ Database files (db.sqlite3)
- ❌ Real credentials anywhere in code

**Always check before pushing:**
```bash
./check-secrets.sh
git status  # Should NOT see .env
```

## 🚀 Share Your Project!

Once published, share it on:
- LinkedIn (great for job hunting!)
- Reddit: r/opensource, r/cybersecurity
- Dev.to or Medium blog post
- Your portfolio website

## 💼 Portfolio Tips

Add to your project showcase:
- ✨ "Full-stack Django application with Celery background tasks"
- ✨ "Docker/Docker Compose deployment"
- ✨ "API integrations (Reddit, NVD)"
- ✨ "Modern HTMX frontend with TailwindCSS"
- ✨ "Automated news aggregation with scheduled tasks"

## 📧 Questions?

See:
- `SECURITY.md` - Security guidelines
- `REDDIT_API_SETUP.md` - Reddit API setup
- `README.md` - Full documentation

---

**You're ready to go! 🎉**
