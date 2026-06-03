import yfinance as yf
import pandas as pd

tickers = {
    "Lloyds":"LLOY.L",
    "Barclays":"BARC.L",
    "Goldman Sachs":"GS"
}

all_data = []

for bank, ticker in tickers.items():
    df = yf.download(
        ticker,
        start="2015-01-01",
        end="2026-01-01"
    )

    df["Bank"] = bank
    df.reset_index(inplace=True)

    all_data.append(df)

combined_df = pd.concat(all_data)

combined_df.to_csv("bank_stock_data.csv", index=False)

print(combined_df.head())