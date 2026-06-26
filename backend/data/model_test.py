from presidio_anonymizer import AnonymizerEngine

from data.test.en.general import clean_data, expected_anonymized_data
from textcloak.anonymizer import container

anonymizer = AnonymizerEngine()
analyzer = container.nlp_analyzer_

# test data and control data must have same size
assert len(clean_data) == len(expected_anonymized_data)

error_count: int = 0
total_count: int = len(clean_data)

for clean_text, expected_anonymized_text in zip(clean_data, expected_anonymized_data):
    results = analyzer.analyze(clean_text)

    anonymized_result = anonymizer.anonymize(text=clean_text, analyzer_results=results)

    if anonymized_result.text != expected_anonymized_text:
        error_count += 1

        print(f"Clean: {clean_text}")
        print("Analyzer results:")
        for result in results:
            print(
                result.entity_type,
                repr(clean_text[result.start:result.end]),
                result.score,
                result.start,
                result.end
            )
        print()
        print(f"Expected: {expected_anonymized_text}")
        print(f"Actual: {anonymized_result.text}")
        print(f"Actual items:")
        for item in anonymized_result.items or []:
            print(item)
        print("=" * 100)

failure_rate = round(error_count / total_count, 2) * 100
print(f"Total: {total_count}, Errors: {error_count}, Failure-Rate: {failure_rate:.0f}%")
