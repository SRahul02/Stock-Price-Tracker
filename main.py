import yfinance as yf

def track_stock(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period="1d")

    if data.empty:
        print("Invalid ticker or no data available.")
        return

    latest = data.iloc[-1]
    print(f"\n📈 Stock: {ticker_symbol}")
    print(f"📅 Date: {latest.name.date()}")
    print(f"🔓 Open: ₹{latest['Open']:.2f}")
    print(f"📈 High: ₹{latest['High']:.2f}")
    print(f"📉 Low: ₹{latest['Low']:.2f}")
    print(f"✅ Close: ₹{latest['Close']:.2f}")
    print(f"📊 Volume: {int(latest['Volume'])}")

if __name__ == "__main__":
    ticker = input("Enter stock symbol (e.g., RELIANCE.NS): ").strip()
    track_stock(ticker)
