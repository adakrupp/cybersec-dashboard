# Security Guidelines

## Files That Contain Secrets (NEVER COMMIT)

These files contain sensitive information and are automatically excluded by `.gitignore`:

- ✅ `.env` - Your actual credentials (gitignored)
- ✅ `db.sqlite3` - Local database (gitignored)
- ✅ `celerybeat-schedule` - Celery schedule file (gitignored)

## Files Safe to Commit

These files have NO secrets and are safe for public repos:

- ✅ `.env.example` - Template with placeholder values only
- ✅ `docker-compose.yml` - Uses environment variables, no hardcoded secrets
- ✅ All Python code - No secrets in source code
- ✅ `README.md` - Public documentation
- ✅ All configuration files

## Pre-Commit Security Checklist

**Before pushing to GitHub:**

1. **Verify .env is gitignored**
   ```bash
   git status
   # Should NOT see .env in the list
   ```

2. **Check for accidentally staged secrets**
   ```bash
   git diff --cached | grep -i "secret\|password\|api_key"
   # Should return nothing or only .env.example placeholders
   ```

3. **Verify .env.example has no real values**
   ```bash
   cat .env.example
   # Should only see: "your-secret-key-here", "your-reddit-client-id", etc.
   ```

4. **Double-check with git grep** (after first commit)
   ```bash
   git grep -i "REDDIT_CLIENT_ID" | grep -v ".env.example"
   # Should return nothing
   ```

## Environment Variables Management

### Development (Local)
- Copy `.env.example` to `.env`
- Add your real credentials to `.env`
- Never commit `.env`

### Production Deployment

**Docker Hub:**
- Image contains NO secrets
- Users must provide their own `.env` file
- Document this in README

**Cloud Platforms (Railway, Render, etc.):**
- Set environment variables in platform dashboard
- Never hardcode in docker-compose.yml or code

**VPS/Self-Hosted:**
- Copy `.env.example` to `.env` on server
- Add production credentials
- Set proper file permissions: `chmod 600 .env`

## What to Do If Secrets Are Accidentally Committed

If you accidentally commit secrets to Git:

1. **Immediately revoke/regenerate the credentials**
   - Reddit: Delete the app and create a new one
   - Django: Generate a new SECRET_KEY

2. **Remove from Git history** (if not pushed yet)
   ```bash
   git reset HEAD~1  # Undo last commit
   # Fix the issue, then commit again
   ```

3. **If already pushed to GitHub:**
   - Revoke credentials immediately
   - Consider the repository compromised
   - Use `git filter-branch` or BFG Repo-Cleaner to remove from history
   - Force push (if repo is private/yours)
   - Better: Create new repository with clean history

## Reporting Security Issues

If you find a security vulnerability in this project:
- **DO NOT** open a public GitHub issue
- Email: [your-email] (or create security policy on GitHub)

## Additional Security Measures

### Recommended for Production:

1. **Use strong SECRET_KEY**
   ```python
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. **Enable HTTPS**
   - Set `SECURE_SSL_REDIRECT=True`
   - Configure reverse proxy (nginx) with SSL

3. **Restrict ALLOWED_HOSTS**
   ```env
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

4. **Use read-only database user for app** (if needed)

5. **Regular updates**
   ```bash
   pip list --outdated
   ```

## Questions?

See README.md for more deployment and configuration guidance.
