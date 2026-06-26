from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import TransformersNlpEngine, NerModelConfiguration
from presidio_anonymizer import AnonymizerEngine

from experiment.test_data import clean_data, expected_anonymized_data

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

# test data and control data must have same size
assert len(clean_data) == len(expected_anonymized_data)

error_count: int = 0
total_count: int = len(clean_data)

for clean_text, expected_anonymized_text in zip(clean_data, expected_anonymized_data):
    results = analyzer.analyze(
        text=clean_text,
        entities=SUPPORTED_ENTITIES,
        language="en",
    )

    anonymized_text_result = anonymizer.anonymize(
        text=clean_text,
        analyzer_results=results,
    )

    if anonymized_text_result.text != expected_anonymized_text:
        error_count += 1

        print(f"Clean: {clean_text}")
        print("Analyzer results:")
        for result in results:
            print(
                result.entity_type,
                repr(clean_text[result.start:result.end]),
                result.score,
                result.start,
                result.end,
            )
        print()
        print(f"Expected: {expected_anonymized_text}")
        print(f"Actual: {anonymized_text_result.text}")
        print(f"Actual items:")
        for item in anonymized_text_result.items:
            print(item)
        print("=" * 100)

failure_rate = round(error_count / total_count, 2) * 100
print(f"Total: {total_count}, Errors: {error_count}, Failure-Rate: {failure_rate:.0f}%")