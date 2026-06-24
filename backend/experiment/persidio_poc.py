from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import TransformersNlpEngine, NerModelConfiguration
from presidio_anonymizer import AnonymizerEngine

from experiment.test_data import test_data

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

analyzer = AnalyzerEngine(
    nlp_engine=nlp_engine,
    supported_languages=["en"]
)

anonymizer = AnonymizerEngine()

for text in test_data:
    results = analyzer.analyze(
        text=text,
        entities=SUPPORTED_ENTITIES,
        language="en",
    )

    print("TEXT:")
    print(text)
    print()

    print("RESULTS:")
    for result in results:
        print(
            result.entity_type,
            text[result.start:result.end],
            result.score,
            result.start,
            result.end,
        )

    anonymized_text = anonymizer.anonymize(
        text=text,
        analyzer_results=results,
    )

    print()
    print("ANONYMIZED:")
    print(anonymized_text.text)
    print("--------------------")