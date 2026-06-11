"""
ai/tagger.py
Unified tagger — routes to Groq (cloud) or Ollama (local) based on provider config.

Provider config shape (dict):
    {
        "provider": "groq" | "ollama",
        "api_key":  "<key>"          # required for groq; ignored for ollama
        "model":    "<model name>"   # optional override
        "base_url": "<url>"          # optional ollama base url (default http://localhost:11434)
    }
"""

import json
import logging
import os
from pathlib import Path

from ai.schemas import DocumentTagSchema

logger = logging.getLogger(__name__)

PROMPT_PATH = Path(__file__).parent / "prompts" / "tag_document.txt"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")

MAX_CHARS = 6000

DEFAULT_GROQ_MODEL   = "llama-3.3-70b-versatile"
DEFAULT_OLLAMA_MODEL = "llama3.2"


# ── helpers ────────────────────────────────────────────────────────────────────

def _strip_fences(raw: str) -> str:
    """Remove markdown code fences that some models add despite instructions."""
    raw = raw.strip()
    if raw.startswith("```"):
        parts = raw.split("```")
        # parts[1] is the content between first pair of fences
        raw = parts[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    return raw


def _parse_and_validate(raw: str) -> DocumentTagSchema:
    data = json.loads(_strip_fences(raw))
    return DocumentTagSchema(**data)


# ── Groq ───────────────────────────────────────────────────────────────────────

def _tag_with_groq(text: str, api_key: str, model: str, retries: int) -> DocumentTagSchema:
    from groq import Groq

    if not api_key:
        raise ValueError("Groq API key is required. Enter it in the sidebar.")

    client = Groq(api_key=api_key)
    truncated = text[:MAX_CHARS]
    last_error = None

    for attempt in range(1, retries + 2):
        try:
            logger.info(f"[Groq] Attempt {attempt} — model: {model}")
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": f"Here is the document text:\n\n{truncated}"},
                ],
                temperature=0.1,
                max_tokens=1000,
            )
            raw = response.choices[0].message.content
            return _parse_and_validate(raw)
        except Exception as e:
            last_error = e
            logger.warning(f"[Groq] Attempt {attempt} failed: {e}")

    raise ValueError(f"Groq tagging failed after {retries + 1} attempts. Last error: {last_error}")


# ── Ollama ─────────────────────────────────────────────────────────────────────

def _tag_with_ollama(text: str, model: str, base_url: str, retries: int) -> DocumentTagSchema:
    import requests

    truncated = text[:MAX_CHARS]
    url = f"{base_url.rstrip('/')}/api/chat"
    last_error = None

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": f"Here is the document text:\n\n{truncated}"},
        ],
        "stream": False,
        "options": {"temperature": 0.1},
    }

    for attempt in range(1, retries + 2):
        try:
            logger.info(f"[Ollama] Attempt {attempt} — model: {model} @ {base_url}")
            resp = requests.post(url, json=payload, timeout=120)
            resp.raise_for_status()
            raw = resp.json()["message"]["content"]
            return _parse_and_validate(raw)
        except Exception as e:
            last_error = e
            logger.warning(f"[Ollama] Attempt {attempt} failed: {e}")

    raise ValueError(f"Ollama tagging failed after {retries + 1} attempts. Last error: {last_error}")


# ── Public entry point ─────────────────────────────────────────────────────────

def tag_document(text: str, provider_cfg: dict | None = None, retries: int = 2) -> DocumentTagSchema:
    """
    Tag a document using the configured provider.

    Args:
        text:         Raw extracted document text.
        provider_cfg: Dict with provider settings (see module docstring).
                      Falls back to env vars / Groq default when None.
        retries:      Retry attempts on failure.

    Returns:
        Validated DocumentTagSchema.
    """
    if provider_cfg is None:
        # Legacy fallback: read from environment (backwards compatible)
        provider_cfg = {
            "provider": "groq",
            "api_key":  os.getenv("GROQ_API_KEY", ""),
            "model":    DEFAULT_GROQ_MODEL,
        }

    provider = provider_cfg.get("provider", "groq").lower()

    if provider == "groq":
        return _tag_with_groq(
            text=text,
            api_key=provider_cfg.get("api_key", os.getenv("GROQ_API_KEY", "")),
            model=provider_cfg.get("model", DEFAULT_GROQ_MODEL),
            retries=retries,
        )

    elif provider == "ollama":
        return _tag_with_ollama(
            text=text,
            model=provider_cfg.get("model", DEFAULT_OLLAMA_MODEL),
            base_url=provider_cfg.get("base_url", "http://localhost:11434"),
            retries=retries,
        )

    else:
        raise ValueError(f"Unknown provider: '{provider}'. Choose 'groq' or 'ollama'.")
