from src.analysis import analyze_stock
from app.model import train_model, predict_price

def get_analysis(df):
    return analyze_stock(df)

def get_prediction(df):
    model = train_model(df)
    prediction = predict_price(model, df)
    return {"predicted_price": float(prediction)}