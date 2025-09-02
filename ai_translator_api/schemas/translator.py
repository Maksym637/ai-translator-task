from pydantic import BaseModel


class TranslatorRequest(BaseModel):
    input_text: str
    from_lang: str
    to_lang: str


class TranslatorResponse(BaseModel):
    text: str
