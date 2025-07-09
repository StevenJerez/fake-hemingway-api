# test_api.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

SAMPLE_TEXT = (
    "I believe the project was completed quickly by the team in order to achieve faster results. "
    "However, we consider that additional improvements are possible."
)

def test_analyze_endpoint():
    """
    Test that /analyze returns correct metrics including qualifiers count.
    """
    response = client.post("/analyze", json={"text": SAMPLE_TEXT})
    assert response.status_code == 200
    data = response.json()

    # Basic structure
    assert "paragraphs" in data
    assert "sentences" in data
    assert "words" in data
    assert "letters" in data
    assert "adverbs" in data
    assert "passive" in data
    assert "complex" in data
    assert "qualifiers" in data
    assert "readability_score" in data

    # Specific checks
    assert data["paragraphs"] == 1
    assert data["adverbs"] >= 1          # 'quickly'
    assert data["passive"] >= 1          # passive voice detected
    assert data["complex"] >= 1          # 'in order to', 'additional'
    assert data["qualifiers"] >= 2       # 'i believe', 'we consider'

def test_suggest_endpoint():
    """
    Test that /suggest returns suggestions for adverbs, passive, complex, and qualifiers.
    """
    response = client.post("/suggest", json={"text": SAMPLE_TEXT})
    assert response.status_code == 200
    suggestions = response.json().get("suggestions", [])

    types = {s["type"] for s in suggestions}
    # Expect at least one suggestion of each type
    assert "adverb" in types
    assert "passive" in types
    assert "complex" in types
    assert "qualifier" in types

    # Each suggestion should have required fields
    for s in suggestions:
        assert "length" in s
        assert "type" in s
        assert "suggestion" in s

def test_rewrite_endpoint():
    """
    Test that /rewrite applies at least one simplification.
    """
    response = client.post("/rewrite", json={"text": SAMPLE_TEXT})
    assert response.status_code == 200
    rewritten = response.json().get("rewritten_text", "")

    # Original adverb 'quickly' should be removed or replaced
    assert "quickly" not in rewritten.lower()

    # Qualifier phrases should be removed
    assert "i believe" not in rewritten.lower()
    assert "we consider" not in rewritten.lower()