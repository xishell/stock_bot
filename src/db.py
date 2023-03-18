import aiosqlite as sq
import asyncio as aio
import src.load_config as lc
cfg = lc.load_cfg()
file = cfg['STOCK_DB']

async def create_db():
    async with sq.connect(file) as db:
        print(sq.sqlite_version)
        c = await db.cursor()
        await c.execute("""CREATE TABLE stocks (
            ticker text,
            name text,
            curr_price float,
            buy_price float
            )""")
        await db.commit()
        
async def add_stocks_db(stocks: list):
    async with sq.connect(file) as db:
        c = await db.cursor()
        for i in stocks:
            await c.execute("INSERT INTO stocks VALUES (:ticker, :name, :curr_price, :buy_price)", i)
        await db.commit()
    return "Stocks added"

async def query_stock_db(stock: list):
    async with sq.connect(file) as db:
        tmp = []
        async with db.execute(f"SELECT * FROM stocks WHERE ticker in ({', '.join(['?']*len(stock))})", stock) as cursor:
            async for i in cursor:
                tmp.append(await dict_factory(cursor, i))
        return tmp
                
async def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def main():
    test_stock = [{'ticker': 'AAPL', 'name': 'Apple Inc.', 'curr_price': 50.3, 'buy_price': 20.72}, {'ticker': 'TSLA', 'name': 'Tesla motors', 'curr_price': 127.23, 'buy_price': 70.67}]
    #aio.run(add_stocks(test_stock))
    #aio.run(create_db())
    #print(aio.run(query_stock(["AAPL"])))
    #aio.run(add_db())

if __name__ == '__main__':
    main()

