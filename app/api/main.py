"""FastAPI service wrapping predict(). Run: make api  → http://localhost:8000/docs

A website or mobile app calls POST /predict with JSON rows.
"""
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from src.models.predict_model import predict

app = FastAPI(title="Project API")


class Row(BaseModel):
    id: int
    feature_1: float
    feature_2: float
    category: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict_endpoint(rows: list[Row]):
    df = pd.DataFrame([r.model_dump() for r in rows])
    out = predict(df)
    return out.to_dict(orient="records")
