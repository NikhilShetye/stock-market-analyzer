import numpy as np

def analyze_stock(df):
    print("Highest Close:", df["CLOSE"].max())
    print("Lowest Low:", df["LOW"].min())
    print("Average Close:", df["CLOSE"].mean())

    df["Daily_Return"] = df["CLOSE"].pct_change()

    print("Volatility (Std Dev):", df["Daily_Return"].std())

    best_day = df.loc[df["Daily_Return"].idxmax()]
    worst_day = df.loc[df["Daily_Return"].idxmin()]

    print("\n📅 Best Day:\n", best_day)
    print("\n📅 Worst Day:\n", worst_day)