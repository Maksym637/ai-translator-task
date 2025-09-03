import pytest
from unittest.mock import patch, MagicMock
from services.ai_service import translate_text


@patch("ai_translator_api.services.ai_service.translator")
def test_translate_text_success(mock_translator):
    mock_translation_item = MagicMock()
    mock_translation_item.text = "Ciao"

    mock_translator.translate.return_value = [{"translations": [mock_translation_item]}]
    actual_text = translate_text("Hello", "en", "it")

    assert actual_text == "Ciao"


def test_translate_text_failure():
    with pytest.raises(RuntimeError) as exception_info:
        translate_text("Hello", "...", "...")

    assert "Translation failed: 400035 - The source language is not valid." == str(exception_info.value)
