import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download chart data from yf
ticker = 'AAPL'  # Apple stock
data = yf.download(ticker, start="2021-01-01", end="2024-11-01")

# Define the time frame for moving averages
short_window = 50  # 50-day moving average
long_window = 100  # 100-day moving average

# Calculate the moving averages
data['SMA50'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
data['SMA100'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

# Plot the stock price and the moving averages
plt.figure(figsize=(12, 8))  # Display chart on a screen size of 12x8
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA50'], label=f'SMA{short_window}', alpha=0.75)
plt.plot(data['SMA100'], label=f'SMA{long_window}', alpha=0.75)  # Corrected to SMA100
plt.title(f'Moving Average for {ticker}')
plt.legend(loc='best')  # Locate legend in the best position
plt.grid(True)  # Added grid for better readability
plt.show()