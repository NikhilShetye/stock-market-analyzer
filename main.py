import pandas as pd
from src.analysis import analyze_stock
from src.signals import generate_signals
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("data/stock.csv")
    print("📊 Running Analysis...\n")
    analyze_stock(df)

    print("\n📈 Generating Signals...\n")
    df = generate_signals(df)

    print(df.tail())
    df["CLOSE"].plot()
    plt.show()

if __name__ == "__main__":
    main()