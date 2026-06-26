from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from textcloak.anonymizer.anonymization_pipeline import AnonymizationPipeline
from textcloak.anonymizer.anonymization_service import AnonymizationService
from textcloak.anonymizer.nlp_analyzer import NlpAnalyzer
from textcloak.models import AnonymizeRequest, AnonymizeResponse

# Origins allowed to call the API. localhost:4200 is the Angular dev server,
# textcloak.ai is the production frontend.
ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "https://textcloak.ai",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/anonymize")
async def anonymize(payload: AnonymizeRequest) -> AnonymizeResponse:
    service = AnonymizationService(
        pipeline=AnonymizationPipeline(
            analyzers=[NlpAnalyzer()]
        )
    )
    return service.anonymize(payload.text)
