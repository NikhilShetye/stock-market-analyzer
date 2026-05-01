from fastapi import APIRouter
import pandas as pd
from app.service import get_analysis, get_prediction

router = APIRouter()

df = pd.read_csv("data/stock.csv")

@router.get("/")
def home():
    return {"message": "Stock Analyzer API running"}

@router.get("/analysis")
def analysis():
    return get_analysis(df)

@router.get("/predict")
def predict():
    return get_prediction(df)