"""
ai/groq_tagger.py
Sends extracted document text to Groq API and returns validated tag schema.
"""

import json
import logging
import os
from pathlib import Path

from groq import Groq
from dotenv import load_dotenv

from ai.schemas import DocumentTagSchema

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
logger = logging.getLogger(__name__)

# Load prompt template once at module level
PROMPT_PATH = Path(__file__).parent / "prompts" / "tag_document.txt"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")

# Groq model — fast and reliable for structured JSON output
MODEL = "llama-3.3-70b-versatile"

# Max characters of document text to send (keeps cost/latency low)
MAX_CHARS = 6000


def tag_document(text: str, retries: int = 2) -> DocumentTagSchema:
    """
    Send document text to Groq and return a validated DocumentTagSchema.

    Args:
        text: Raw extracted text from the document.
        retries: Number of retry attempts on failure.

    Returns:
        DocumentTagSchema with description, difficulty, subjects, and skills.

    Raises:
        ValueError: If Groq returns invalid JSON or schema validation fails after all retries.
    """
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # Truncate to avoid token limits
    truncated = text[:MAX_CHARS]
    if len(text) > MAX_CHARS:
        logger.info(f"Document truncated from {len(text)} to {MAX_CHARS} chars for tagging.")

    last_error = None

    for attempt in range(1, retries + 2):  # retries + initial attempt
        try:
            logger.info(f"Calling Groq API (attempt {attempt})...")

            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Here is the document text:\n\n{truncated}"},
                ],
                temperature=0.1,   # low temperature = more consistent JSON
                max_tokens=1000,
            )

            raw = response.choices[0].message.content.strip()
            logger.debug(f"Groq raw response: {raw}")

            # Strip markdown fences if model wraps output despite instructions
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
                raw = raw.strip()

            data = json.loads(raw)
            schema = DocumentTagSchema(**data)
            logger.info("Tagging successful.")
            return schema

        except Exception as e:
            last_error = e
            logger.warning(f"Attempt {attempt} failed: {e}")

    raise ValueError(f"Groq tagging failed after {retries + 1} attempts. Last error: {last_error}")
