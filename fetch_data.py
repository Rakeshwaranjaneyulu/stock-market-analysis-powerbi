import yfinance as yf
import pandas as pd
from datetime import datetime

# Tickers to download
tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN']

# Today's date
today = datetime.today().strftime('%Y-%m-%d')

# Download stock data from 2023 to today
data = yf.download(tickers, start="2023-01-01", end=today, group_by='ticker')

# Save each ticker's data to a separate CSV
for ticker in tickers:
    df = data[ticker].copy()
    df.reset_index(inplace=True)
    df['Ticker'] = ticker
    df.to_csv(f'output/{ticker}_stock_data.csv', index=False)

print(" All stock data saved to /output folder!")
