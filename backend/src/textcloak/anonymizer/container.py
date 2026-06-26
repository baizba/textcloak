from textcloak.anonymizer.anonymization_pipeline import AnonymizationPipeline
from textcloak.anonymizer.anonymization_service import AnonymizationService
from textcloak.anonymizer.nlp_analyzer import NlpAnalyzer

anonymization_service = AnonymizationService(
    pipeline=AnonymizationPipeline(
        analyzers=[NlpAnalyzer()]
    )
)
