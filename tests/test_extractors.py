"""
tests/test_extractors.py
Run with: pytest tests/test_extractors.py -v
"""

from utils.extractors import extract_txt, extract, extract_pdf


def test_txt_extraction_utf8():
    text = "Hello, this is a test document about machine learning."
    result = extract_txt(text.encode("utf-8"))
    assert result == text


def test_txt_extraction_via_router():
    text = "Linear algebra notes."
    result = extract(text.encode("utf-8"), "linear_algebra.txt")
    assert "linear algebra" in result.lower()


def test_unsupported_file_returns_empty():
    result = extract(b"not a text file", "image.png")
    assert result == ""


def test_empty_file_returns_empty():
    result = extract_txt(b"")
    assert result == ""


def test_router_picks_correct_extractor():
    text = "Python data analysis notes."
    # TXT
    assert extract(text.encode(), "notes.txt") != ""
    # MD
    assert extract(text.encode(), "readme.md") != ""
    # Unknown → empty
    assert extract(text.encode(), "file.xyz") == ""
