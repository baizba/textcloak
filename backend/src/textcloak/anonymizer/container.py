from textcloak.anonymizer.anonymization_pipeline import AnonymizationPipeline
from textcloak.anonymizer.anonymization_service import AnonymizationService
from textcloak.anonymizer.nlp_analyzer import NlpAnalyzer

nlp_analyzer_ = NlpAnalyzer()

anonymization_service = AnonymizationService(
    pipeline=AnonymizationPipeline(
        analyzers=[nlp_analyzer_]
    )
)
