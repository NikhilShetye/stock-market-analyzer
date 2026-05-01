import numpy as np
from sklearn.linear_model import LinearRegression

def train_model(df):
    df = df.dropna()

    df["Day"] = np.arange(len(df))

    X = df[["Day"]]
    y = df["CLOSE"]

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_price(model, df):
    next_day = [[len(df)]]
    return model.predict(next_day)[0]