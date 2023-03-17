import requests
import src.load_config as lc

cfg = lc.load_cfg()
fmpapi = cfg['FMPAPI']

def price_tracker(stock):
    try:
        prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock.upper().strip()}?apikey={fmpapi}').json()
        stockPrice = prices[0]['price']
    except IndexError:
        stockPrice = "NULL"
    return stockPrice
