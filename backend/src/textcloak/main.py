from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from textcloak.anonymizer import container
from textcloak.models import AnonymizeRequest, AnonymizeResponse

# Origins allowed to call the API. localhost:4200 is the Angular dev server,
# textcloak.ai is the production frontend.
ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "https://textcloak.ai",
    "https://www.textcloak.ai"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["POST"],
    allow_headers=["*"],
)

anonymization_service = container.anonymization_service


@app.post("/anonymize")
async def anonymize(payload: AnonymizeRequest) -> AnonymizeResponse:
    return anonymization_service.anonymize(payload.text)
