from fastapi import APIRouter, HTTPException

from app.models.ml_sentiment_analysis import SentimentClassifier
from app.schemas import sentiment_schema
from app.schemas.schemas import HTTPError

api = APIRouter()
model = SentimentClassifier()


@api.post("/analyze", responses={200: {"model": sentiment_schema.SentimentGET}, 400: {"model": HTTPError}})
def getSentiment(payload: sentiment_schema.SentimentPOST | None = None):
    try:
        text = payload.text
        sent = sentiment_schema.SentimentGET(**model.predict(text))
        return sent
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
