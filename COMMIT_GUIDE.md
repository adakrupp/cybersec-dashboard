# Safe Commit Guide - Your Secrets Are Protected!

## 🔒 Automatic Security Protection

Your repository has an **automatic pre-commit hook** that runs BEFORE every commit.

### What It Does:
- ✅ Checks if `.env` is gitignored
- ✅ Scans staged files for actual credential values
- ✅ Verifies `.env.example` has only placeholders
- ❌ **BLOCKS the commit** if real secrets are detected

### You're Protected From:
- Accidentally committing `.env` file
- Committing actual SECRET_KEY values
- Committing real Reddit API credentials
- Committing database passwords

## 📝 How to Commit Safely (Every Time)

### Regular Commits (After Changes):

```bash
# 1. Stage your changes
git add .

# 2. Commit (security check runs AUTOMATICALLY)
git commit -m "Your commit message"

# 3. Push to GitHub
git push
```

**That's it!** The pre-commit hook runs automatically and will stop you if anything is wrong.

## ⚠️ If Pre-Commit Hook Blocks Your Commit

If you see:
```
❌ COMMIT BLOCKED - Security issues detected!
```

**DO NOT bypass it!** It found real secrets in your staged files.

### How to Fix:

1. **Check what was flagged:**
   ```bash
   git diff --cached | grep -i "secret\|password"
   ```

2. **Unstage the problematic file:**
   ```bash
   git reset HEAD <filename>
   ```

3. **Remove the secret from the file** or revert changes

4. **Try committing again**

## 🚀 Push to GitHub (First Time)

```bash
# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/cybersec-dashboard.git
git branch -M main
git push -u origin main
```

## 🔄 Future Updates (Add Features/Fix Bugs)

```bash
# Make your changes to code
# ...

# Add and commit (security check runs automatically!)
git add .
git commit -m "Add new feature: XYZ"

# Push
git push
```

**The pre-commit hook runs on EVERY commit** - you're always protected!

## 🧪 Manual Security Check (Optional)

You can manually run the security check anytime:

```bash
./check-secrets.sh
```

## ✅ What's Safe to Commit

These files are 100% safe and have NO secrets:
- ✅ All Python code (`.py` files)
- ✅ Templates (`.html` files)
- ✅ Docker files (`Dockerfile`, `docker-compose.yml`)
- ✅ Documentation (`.md` files)
- ✅ `.env.example` (only placeholders)
- ✅ Configuration files
- ✅ Database migrations

## ❌ What's NEVER Committed (Gitignored)

These are automatically excluded by `.gitignore`:
- ❌ `.env` (your actual secrets)
- ❌ `db.sqlite3` (local database)
- ❌ `__pycache__/` (Python cache)
- ❌ `venv/` (virtual environment)
- ❌ `.vscode/`, `.idea/` (IDE files)

## 🎯 Quick Commands

```bash
# Check what will be committed
git status

# See changes to be committed
git diff --cached

# Run security check manually
./check-secrets.sh

# Undo last commit (if you made a mistake)
git reset --soft HEAD~1

# Remove file from staging
git reset HEAD <filename>
```

## 📚 Related Docs

- `SECURITY.md` - Comprehensive security guidelines
- `NEXT_STEPS.md` - Publishing to GitHub & Docker Hub
- `REDDIT_API_SETUP.md` - Reddit API setup

---

## 💡 Pro Tips

1. **The pre-commit hook is your friend** - Don't try to bypass it!
2. **Test locally first** - Make sure code works before committing
3. **Commit often** - Small commits are better than large ones
4. **Write clear commit messages** - Future you will thank you

## 🆘 Need Help?

If the pre-commit hook is blocking you and you think it's a false positive:
1. Check what's flagged: `git diff --cached`
2. If it's detecting placeholder text (like "your-secret-key"), that's okay - commit anyway
3. If it's detecting ACTUAL credentials, DO NOT commit!

---

**Remember: Your `.env` file with real secrets stays LOCAL and is NEVER committed!** ✅🔒
