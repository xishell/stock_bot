import asyncio as aio
import src.stock_tracker as st
import src.db as db
import random as rd

def get_stocks(stocks: list):
    stock_info = aio.run(db.query_stock_db(stocks))
    return stock_info

def add_stocks(stocks: list):
    stock_list = []
    for i in stocks:
        stock_info = st.get_info(i)
        stock = {
            'ticker': i,
            'name': stock_info['name'],
            'curr_price': stock_info['price'],
            'buy_price': rd.random(1, 999.99)
        }
        stock_list.append(stock)
    return aio.run(db.add_stocks_db(stock_list))