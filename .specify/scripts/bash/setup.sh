#!/usr/bin/env bash
# setup.sh — Bootstrap the Knowledge Vault development environment

set -e

echo "🔧 Setting up Knowledge Vault..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Check for .env
if [ ! -f .env ]; then
  cp .env.example .env
  echo "⚠️  Created .env from .env.example — fill in your API keys before running."
fi

echo "✅ Setup complete. Run: source .venv/bin/activate && streamlit run app.py"
