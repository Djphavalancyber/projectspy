import requests
from pydantic import BaseModel
from typing import List

class Ticker(BaseModel):
    symbol: str
    price: float
    volume: float
    timestamp: str

class TickerResponse(BaseModel):
    tickers: List[Ticker]

def fetch_tickers() -> TickerResponse:
    headers = {
        "api_key": "",
        "api_secret": "",
        "content_type": "application/json",
    }
    response = requests.get(
        "https://api.india.delta.exchange/v2/tickers?symbols=BTC-USD,ETH-USD",
        headers=headers,
    )
    response.raise_for_status()
    raw_data = response.json()
    tickers = [Ticker(**item) for item in raw_data]
    return TickerResponse(tickers=tickers)

if __name__ == "__main__":
    data = fetch_tickers()
    print(data.json(indent=2))
