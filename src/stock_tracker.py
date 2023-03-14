import requests

def price_tracker(api_key, stock):
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock.upper()}?apikey={api_key}').json()
    stockPrice = prices[0]['price']
    return stockPrice
