from presidio_analyzer import RecognizerResult

from textcloak.anonymizer.text_analyzer_interface import TextAnalyzerInterface


class AnonymizationPipeline:
    def __init__(self, analyzers: list[TextAnalyzerInterface]):
        self.analyzers = analyzers

    def analyze(self, text: str) -> list[RecognizerResult]:
        result: list[RecognizerResult] = []

        for analyzer in self.analyzers:
            result.extend(analyzer.analyze(text=text))

        return result