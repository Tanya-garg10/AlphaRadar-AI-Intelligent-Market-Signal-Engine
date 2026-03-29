import yfinance as yf

def get_stock_data(symbol):
    data = yf.download(symbol, period="3mo", interval="1d")

    if data is None or data.empty:
        raise Exception("No data found for stock")

    data = data.dropna()
    return data