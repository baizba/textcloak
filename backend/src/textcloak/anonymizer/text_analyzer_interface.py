from abc import abstractmethod, ABC

from presidio_analyzer import RecognizerResult


class TextAnalyzerInterface(ABC):

    @abstractmethod
    def analyze(self, text: str) -> list[RecognizerResult]:
        pass
