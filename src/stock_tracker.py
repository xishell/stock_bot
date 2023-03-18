import requests
import src.load_config as lc

cfg = lc.load_cfg()
fmpapi = cfg['FMPAPI']

def get_info(stock):
    try:
        info = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock.upper().strip()}?apikey={fmpapi}').json()
        ret_info = info[0]
    except IndexError:
        ret_info = "NULL"
    return ret_info