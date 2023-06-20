import pytest


def test_sentiment_analysis(client):
    tests = [
        ("I love this product!", "positive", 1),
        ("I hate Mondays.", "negative", -1),
    ]

    for test in tests:
        payload = {
            "text": test[0]
        }
        response = client.post("/api/sentiment", json=payload)

        assert response.status_code == 200

        response_json = response.json()

        assert response_json["sentiment"] == test[1]
        assert response_json["value"] == test[2]
