#!/usr/bin/env bash
# run_tests.sh — Run all unit tests with coverage report

set -e

source .venv/bin/activate

echo "🧪 Running tests..."
pytest tests/ -v --tb=short

echo "✅ All tests passed."
