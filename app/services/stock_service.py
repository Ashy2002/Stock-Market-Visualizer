import requests

def fetch_daily_stock_data(symbol: str, api_key: str) -> dict:
    url = (
        "https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if "Note" in data:
        raise Exception("API rate limit exceeded. Please wait and try again.")

    if "Time Series (Daily)" not in data:
        raise ValueError("Invalid API response or rate limit exceeded")

    return data["Time Series (Daily)"]
