#!/bin/bash

# Security Check Script - Run before committing to GitHub
# This script checks for accidentally committed secrets

echo "🔒 Security Check - Scanning for secrets..."
echo "========================================="
echo ""

ERRORS=0

# Check 1: Verify .env is not tracked
echo "✓ Checking if .env is properly ignored..."
if git ls-files | grep -q "^\.env$"; then
    echo "❌ ERROR: .env file is tracked by git!"
    echo "   Run: git rm --cached .env"
    ERRORS=$((ERRORS + 1))
else
    echo "  ✅ .env is not tracked (good!)"
fi
echo ""

# Check 2: Verify .env exists locally (should not be committed)
if [ -f .env ]; then
    echo "✓ Checking .env file..."
    echo "  ✅ .env exists locally (your secrets are safe)"
else
    echo "  ⚠️  No .env file found (you may need to create one)"
fi
echo ""

# Check 3: Scan staged files for ACTUAL secret values (not just the words)
echo "✓ Scanning staged files for actual secret values..."
# Look for actual credentials patterns, exclude placeholders, documentation, and code
# Only flag if it looks like a real credential (no "your", "placeholder", "example", etc.)
if git diff --cached | grep -E "^[+].*SECRET_KEY=['\"]?[a-zA-Z0-9!@#\$%^&*()_+=\-]{30,}" | grep -v "your\|placeholder\|example\|CHANGE\|generate\|django-insecure" > /dev/null; then
    echo "❌ ERROR: Actual SECRET_KEY value found in staged files!"
    git diff --cached | grep "SECRET_KEY=" --color=always | head -3
    ERRORS=$((ERRORS + 1))
elif git diff --cached | grep -E "^[+].*REDDIT_CLIENT_(ID|SECRET)=['\"]?[a-zA-Z0-9_-]{15,}" | grep -v "your\|placeholder\|example\|actual\|client_id_here\|client_secret_here" > /dev/null; then
    echo "❌ ERROR: Actual Reddit credentials found in staged files!"
    git diff --cached | grep -E "^[+].*REDDIT_CLIENT" --color=always | head -3
    ERRORS=$((ERRORS + 1))
else
    echo "  ✅ No actual secret values detected in staged files"
fi
echo ""

# Check 4: Verify .env.example has only placeholders
echo "✓ Checking .env.example..."
if grep -E "(SECRET_KEY|REDDIT_CLIENT)" .env.example | grep -v "your-\|generate-a" > /dev/null; then
    echo "❌ WARNING: .env.example might contain real values!"
    echo "   Contents:"
    grep -E "(SECRET_KEY|REDDIT_CLIENT)" .env.example
    ERRORS=$((ERRORS + 1))
else
    echo "  ✅ .env.example contains only placeholders"
fi
echo ""

# Check 5: List files that will be committed
echo "✓ Files staged for commit:"
if git diff --cached --name-only | head -20; then
    echo ""
else
    echo "  (no files staged yet)"
    echo ""
fi

# Check 6: Verify migrations are created
echo "✓ Checking migrations..."
MIGRATION_DIRS=$(find apps/*/migrations -type d 2>/dev/null | wc -l)
if [ "$MIGRATION_DIRS" -eq 0 ]; then
    echo "  ⚠️  No migration directories found"
else
    echo "  ✅ Migration directories exist"
fi
echo ""

# Summary
echo "========================================="
if [ $ERRORS -eq 0 ]; then
    echo "✅ All security checks passed!"
    echo ""
    echo "Safe to commit. Run:"
    echo "  git add ."
    echo "  git commit -m 'Initial commit: CyberSec Dashboard'"
    echo "  git push"
else
    echo "❌ Found $ERRORS security issue(s)!"
    echo "   Fix the errors above before committing."
    exit 1
fi
