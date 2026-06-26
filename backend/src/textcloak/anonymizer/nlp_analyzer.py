from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NerModelConfiguration, TransformersNlpEngine

from textcloak.anonymizer.text_analyzer_interface import TextAnalyzerInterface

SUPPORTED_ENTITIES: list[str] = [
    "PERSON",
    "EMAIL_ADDRESS",
    "PHONE_NUMBER",
    "URL",
    "IP_ADDRESS",
    "CREDIT_CARD",
    "IBAN_CODE",
    "LOCATION",
    "ORGANIZATION"
]

model_config = [
    {
        "lang_code": "en",
        "model_name": {
            "spacy": "en_core_web_lg",
            "transformers": "Babelscape/wikineural-multilingual-ner",
        },
    }
]

entity_mapping = {
    "PER": "PERSON",
    "PERSON": "PERSON",

    "LOC": "LOCATION",
    "LOCATION": "LOCATION",
    "GPE": "LOCATION",

    "ORG": "ORGANIZATION",
    "ORGANIZATION": "ORGANIZATION"
}

class NlpAnalyzer(TextAnalyzerInterface):

    def __init__(self):
        ner_model_configuration = NerModelConfiguration(
            model_to_presidio_entity_mapping=entity_mapping,
            labels_to_ignore=["O", "MISC"],
            aggregation_strategy="max",
            alignment_mode="expand",
        )

        nlp_engine = TransformersNlpEngine(
            models=model_config,
            ner_model_configuration=ner_model_configuration,
        )

        self.analyzer = AnalyzerEngine(
            nlp_engine=nlp_engine,
            supported_languages=["en"]
        )

    def analyze(self, text: str):
        return self.analyzer.analyze(text=text, entities=SUPPORTED_ENTITIES, language="en")