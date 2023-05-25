import pickle
import json

from typing import List, Any, Dict

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


@router.post("/predict", response_model=Dict[str, str])
def predict(symptoms):
    """
    """
    # print(symptoms)
    model = pickle.load(open('ml_model.sav', 'rb'))
    predictions = model.predict(symptoms)
    return json.dumps(predictions)