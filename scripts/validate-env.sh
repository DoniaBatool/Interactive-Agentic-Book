#!/bin/bash
# Environment variable validation script
# Checks if .env file exists and contains required variables

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$REPO_ROOT/.env"
ENV_EXAMPLE="$REPO_ROOT/.env.example"

echo "🔍 Validating environment configuration..."
echo ""

# Check if .env file exists
if [ ! -f "$ENV_FILE" ]; then
    echo "❌ ERROR: .env file not found!"
    echo ""
    echo "📋 To fix this:"
    echo "   1. Copy the example file:"
    echo "      cp .env.example .env"
    echo ""
    echo "   2. Edit .env and fill in your API keys and credentials"
    echo ""
    exit 1
fi

echo "✅ .env file exists"

# List of required variables (for production)
# In development, these are optional
OPTIONAL_VARS=(
    "OPENAI_API_KEY"
    "QDRANT_URL"
    "QDRANT_API_KEY"
    "DATABASE_URL"
    "BETTERAUTH_SECRET"
    "SMTP_HOST"
    "SMTP_PORT"
    "SMTP_USER"
    "SMTP_PASSWORD"
)

MISSING_VARS=()
CONFIGURED_VARS=()

# Check each variable
for var in "${OPTIONAL_VARS[@]}"; do
    if grep -q "^${var}=" "$ENV_FILE" && ! grep -q "^${var}=your-.*-here" "$ENV_FILE" && ! grep -q "^${var}=$" "$ENV_FILE"; then
        CONFIGURED_VARS+=("$var")
    else
        MISSING_VARS+=("$var")
    fi
done

echo ""
echo "📊 Configuration Status:"
echo ""

if [ ${#CONFIGURED_VARS[@]} -gt 0 ]; then
    echo "✅ Configured variables:"
    for var in "${CONFIGURED_VARS[@]}"; do
        echo "   - $var"
    done
fi

if [ ${#MISSING_VARS[@]} -gt 0 ]; then
    echo ""
    echo "⚠️  Missing or placeholder variables:"
    for var in "${MISSING_VARS[@]}"; do
        echo "   - $var"
    done
    echo ""
    echo "ℹ️  Note: These variables are optional in development."
    echo "   The application will start with warnings but no errors."
fi

echo ""
echo "✅ Environment validation complete!"
echo ""
echo "📝 Summary:"
echo "   - Configured: ${#CONFIGURED_VARS[@]}"
echo "   - Missing: ${#MISSING_VARS[@]}"
echo "   - Total: ${#OPTIONAL_VARS[@]}"
echo ""

if [ ${#MISSING_VARS[@]} -eq ${#OPTIONAL_VARS[@]} ]; then
    echo "⚠️  WARNING: No API keys configured!"
    echo "   The application will start but external services will not work."
    echo "   For full functionality, configure at least:"
    echo "     - OPENAI_API_KEY (for AI features)"
    echo "     - DATABASE_URL (for user data)"
    echo ""
fi

exit 0
