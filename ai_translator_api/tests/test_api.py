from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from utils.constants import SUPPORTED_LANGUAGES
from main import app


client = TestClient(app)


@patch("ai_translator_api.routes.translator.translate_text")
def test_perform_translation_200(mock_translate_text):
    mock_translate_text = MagicMock()
    mock_translate_text.return_value = "Ciao"

    response = client.post(
        "/translate",
        json={"input_text": "Hello", "from_lang": "en", "to_lang": "it"},
    )

    assert response.status_code == 200
    assert response.json() == {"text": "Ciao"}


def test_perform_translation_400():
    response = client.post(
        "/translate",
        json={"input_text": "", "from_lang": "en", "to_lang": "it"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Input text should not be empty"}


def test_perform_translation_404():
    response = client.post(
        "/translate",
        json={"input_text": "Hello", "from_lang": "...", "to_lang": "..."},
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": [
            "Input/output language is not supported. ",
            f"List of supported languages is: {SUPPORTED_LANGUAGES}",
        ]
    }
