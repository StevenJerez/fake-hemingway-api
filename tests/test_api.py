import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_empty_text():
    response = client.post("/analyze", json={"text": ""})
    assert response.status_code == 200
    data = response.json()
    assert data["readability_score"] == 0
    assert data["adverb_count"] == 0
    assert data["passive_voice_count"] == 0
    assert data["complex_count"] == 0
    assert data["hard_sentences"] == 0
    assert data["very_hard_sentences"] == 0

@pytest.mark.parametrize("text,expected_score", [
    ("Short sentence.", 0),
    ("This is a long and complex sentence that might score higher.", pytest.approx(10, abs=5)),
])
def test_analyze_readability(text, expected_score):
    response = client.post("/analyze", json={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["readability_score"], float)

# Add tests for /suggest and /rewrite when implemented