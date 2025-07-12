import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
import time

def track_stock(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    
    try:
        info = stock.info
        price = info.get('currentPrice') or info.get('regularMarketPrice')
        currency = info.get('currency', 'INR')
        name = info.get('shortName', ticker_symbol)
    except Exception as e:
        print("Error fetching live data:", e)
        return

    print(f"\n📈 {name} ({ticker_symbol})")
    print(f"🕒 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💰 Live Price: {currency} {price}")

def plot_stock_chart(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period="7d", interval="1m")

    if data.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label="Close Price", color="blue")
    plt.title(f"{ticker_symbol} Price Chart (Last 7 Days)")
    plt.xlabel("Date/Time")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter stock symbol (e.g., RELIANCE.NS): ").strip()
    # while True:
    #     track_stock(ticker)
    #     time.sleep(5)
    track_stock(ticker)
    plot_stock_chart(ticker)
