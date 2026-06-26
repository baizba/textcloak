from presidio_anonymizer import AnonymizerEngine, EngineResult

from textcloak.anonymizer.anonymization_pipeline import AnonymizationPipeline
from textcloak.models import AnonymizeResponse, ReplacementItem


def to_response(engine_result: EngineResult) -> AnonymizeResponse:
    replacement_items: list[ReplacementItem] = []

    if engine_result.items is not None:
        for op in engine_result.items:
            replacement_items.append(
                ReplacementItem(start=op.start, end=op.end, replacement_text=op.text or "")
            )

        replacement_items.sort(key=lambda item: item.start)

    return AnonymizeResponse(
        anonymized_text=engine_result.text or "",
        replacement_items=replacement_items,
    )


class AnonymizationService:
    def __init__(self, pipeline: AnonymizationPipeline):
        self.pipeline = pipeline
        self.anonymizer = AnonymizerEngine()

    def anonymize(self, text: str) -> AnonymizeResponse:
        analyzer_results = self.pipeline.analyze(text)
        engine_result = self.anonymizer.anonymize(text=text, analyzer_results=analyzer_results)
        return to_response(engine_result)
