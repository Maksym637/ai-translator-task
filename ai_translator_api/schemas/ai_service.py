from typing import List
from pydantic import BaseModel


class TranslationItem(BaseModel):
    text: str
    to: str


class TranslatorResponse(BaseModel):
    translations: List[TranslationItem]
