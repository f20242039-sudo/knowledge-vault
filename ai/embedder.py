"""
ai/embedder.py
Converts text into a 384-dimensional vector using sentence-transformers.
Runs fully locally — no API calls, no cost.
The model is downloaded once and cached automatically by sentence-transformers.
"""

import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

MODEL_NAME = "all-MiniLM-L6-v2"
MAX_TOKENS = 512  # model's effective input limit


@lru_cache(maxsize=1)
def _load_model():
    """Load the embedding model once and cache it for the session."""
    from sentence_transformers import SentenceTransformer
    logger.info(f"Loading embedding model: {MODEL_NAME}")
    return SentenceTransformer(MODEL_NAME)


def embed(text: str) -> list[float]:
    """
    Convert text into a 384-dimensional embedding vector.

    Args:
        text: Any string — document content or a search query.

    Returns:
        List of 384 floats representing the semantic meaning of the text.
    """
    if not text or not text.strip():
        raise ValueError("Cannot embed empty text.")

    model = _load_model()
    vector = model.encode(text, normalize_embeddings=True)
    return vector.tolist()
