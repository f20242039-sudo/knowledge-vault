"""
ai/groq_tagger.py
Sends extracted document text to Groq API and returns validated tag schema.
"""

import json
import logging
from pathlib import Path

from groq import Groq

from ai.schemas import DocumentTagSchema
from utils.secrets import get_secret

logger = logging.getLogger(__name__)

PROMPT_PATH = Path(__file__).parent / "prompts" / "tag_document.txt"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")

MODEL = "llama-3.3-70b-versatile"
MAX_CHARS = 6000


def tag_document(text: str, retries: int = 2) -> DocumentTagSchema:
    client = Groq(api_key=get_secret("GROQ_API_KEY"))
    truncated = text[:MAX_CHARS]

    last_error = None
    for attempt in range(1, retries + 2):
        try:
            logger.info(f"Calling Groq API (attempt {attempt})...")
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Here is the document text:\n\n{truncated}"},
                ],
                temperature=0.1,
                max_tokens=1000,
            )
            raw = response.choices[0].message.content.strip()
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
