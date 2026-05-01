def generate_signals(df):
    df["MA_10"] = df["CLOSE"].rolling(window=10).mean()

    def signal(row):
        if row["CLOSE"] > row["MA_10"]:
            return "BUY"
        else:
            return "SELL"

    df["Signal"] = df.apply(signal, axis=1)
    return df