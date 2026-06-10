"""
utils/secrets.py
Reads secrets from Streamlit Cloud secrets OR local .env file.
Works in both local development and production deployment.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env for local development (no-op in production)
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")


def get_secret(key: str) -> str:
    """
    Get a secret by key. Checks in this order:
    1. Streamlit secrets (production)
    2. Environment variables / .env (local dev)
    """
    # Try Streamlit secrets first (only available when running on Streamlit Cloud)
    try:
        import streamlit as st
        val = st.secrets.get(key)
        if val:
            return val
    except Exception:
        pass

    # Fall back to environment variable
    val = os.getenv(key)
    if not val:
        raise EnvironmentError(f"Secret '{key}' not found in Streamlit secrets or .env")
    return val
