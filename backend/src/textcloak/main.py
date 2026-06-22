from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from textcloak.models import AnonymizeRequest

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
async def anonymize(payload: AnonymizeRequest):
    # TODO: replace with real anonymization logic.
    return {"text": payload.text}
