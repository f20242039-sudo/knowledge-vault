"""
tests/test_embedder.py
Run with: pytest tests/test_embedder.py -v
Note: first run downloads the model (~80MB), may take a minute.
"""

import pytest
from ai.embedder import embed


def test_embed_returns_list():
    result = embed("Introduction to machine learning.")
    assert isinstance(result, list)


def test_embed_is_384_dimensions():
    result = embed("Linear algebra and matrix operations.")
    assert len(result) == 384


def test_embed_returns_floats():
    result = embed("Python data analysis with NumPy.")
    assert all(isinstance(x, float) for x in result)


def test_similar_texts_are_close():
    """Two documents about the same topic should have similar embeddings."""
    import math

    vec1 = embed("Introduction to neural networks and deep learning.")
    vec2 = embed("Basics of deep learning and neural network architecture.")

    # Cosine similarity (vectors are already normalized)
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    assert dot_product > 0.65, f"Expected similarity > 0.65, got {dot_product:.3f}"


def test_different_texts_are_far():
    """Two completely unrelated documents should have low similarity."""
    vec1 = embed("Quantum mechanics and wave-particle duality.")
    vec2 = embed("Italian pasta recipes and cooking techniques.")

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    assert dot_product < 0.6, f"Expected similarity < 0.6, got {dot_product:.3f}"


def test_empty_text_raises():
    with pytest.raises(ValueError):
        embed("")


def test_whitespace_only_raises():
    with pytest.raises(ValueError):
        embed("   ")
