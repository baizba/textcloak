from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )


class AnonymizeRequest(CamelModel):
    text: str


class ReplacementItem(CamelModel):
    start: int
    end: int
    replacement_text: str


class AnonymizeResponse(CamelModel):
    anonymized_text: str
    replacement_items: list[ReplacementItem]
