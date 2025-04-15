# Stock Price and Moving Averages Visualization

This project downloads historical stock price data using the `yfinance` library and visualizes the moving averages along with the closing price of a selected stock. It is particularly useful for financial analysis and gaining insights into stock trends.

---

## Features
- Download historical stock price data for any ticker symbol.
- Calculate **Simple Moving Averages (SMA)** for custom time frames (e.g., 50-day and 100-day SMAs).
- Plot the closing price and moving averages using Matplotlib for visual insights.

---

## Prerequisites

Ensure you have the following installed:
- **Python 3.7 or later**
- Required Python libraries:
  - `yfinance`
  - `pandas`
  - `matplotlib`

To install the libraries, you can use:
```bash
pip install yfinance pandas matplotlib

ticker = 'AAPL'  # Replace 'AAPL' with your desired stock ticker.
