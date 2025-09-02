from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.translation.text import TextTranslationClient
from schemas.ai_service import TranslatorResponse
from config import settings


credential = AzureKeyCredential(settings.AZURE_AI_KEY)
translator = TextTranslationClient(credential=credential, region=settings.AZURE_AI_REGION)


def translate_text(input_text: str, from_lang: str, to_lang: str) -> str:
    try:

        response_list = translator.translate(body=[input_text], from_language=from_lang, to_language=[to_lang])
        response_item = response_list[0]

        translation_response = TranslatorResponse(**response_item)
        translation_list = translation_response.translations

        translation_item = translation_list[0]

    except HttpResponseError as error:
        raise RuntimeError(f"Translation failed: {error.error.code} - {error.error.message}")

    return translation_item.text
