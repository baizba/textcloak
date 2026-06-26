from pydantic import BaseModel


class AnonymizeRequest(BaseModel):
    text: str


class ReplacementItem(BaseModel):
    start: int
    end: int
    replacement_text: str


class AnonymizeResponse(BaseModel):
    anonymized_text: str
    replacement_items: list[ReplacementItem]
