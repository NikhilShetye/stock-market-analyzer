def analyze_stock(df):
    df["Daily_Return"] = df["CLOSE"].pct_change()

    return {
        "max_close": float(df["CLOSE"].max()),
        "min_close": float(df["CLOSE"].min()),
        "avg_close": float(df["CLOSE"].mean()),
        "volatility": float(df["Daily_Return"].std())
    }