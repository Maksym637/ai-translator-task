from fastapi import APIRouter, HTTPException, status
from services.ai_service import translate_text
from schemas.translator import TranslatorRequest, TranslatorResponse
from utils.constants import SUPPORTED_LANGUAGES


translator_router = APIRouter()


@translator_router.post(
    path="/translate",
    response_model=TranslatorResponse,
    description="Performs translation based on the input text and language",
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Input text should not be empty"},
        404: {"description": "Input/output language is not supported"},
    },
)
def perform_translation(payload: TranslatorRequest) -> TranslatorResponse:
    input_text, from_lang, to_lang = payload.input_text, payload.from_lang, payload.to_lang

    if not input_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Input text should not be empty")

    if from_lang not in SUPPORTED_LANGUAGES or to_lang not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=(
                "Input/output language is not supported. ",
                f"List of supported languages is: {SUPPORTED_LANGUAGES}",
            ),
        )

    text = translate_text(input_text, from_lang, to_lang)

    return TranslatorResponse(text=text)
