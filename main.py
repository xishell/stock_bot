import discord
import os
from dotenv import load_dotenv
import src.stock_tracker as stock_tracker
import src.utils as utils
load_dotenv()
token = os.getenv('TOKEN')
fmpapi = os.getenv('FMPAPI')



class Stonks(discord.Bot):
    async def on_ready(self):
        print(f"Logged in as {self.user}")



@Stonks.slash_command(guild_ids=['445474022113804288'])
async def price(ctx, stock):
    curr_price = stock_tracker.price_tracker(fmpapi, stock)
    await ctx.respond(f"Current prices for stock: {stock} is ${curr_price}")
        
@Stonks.slash_command(guild_ids=['445474022113804288'])
async def summary(ctx):
    stocks = ["AAPL", "TSLA", "SMT", "GTH"]
    await ctx.respond(embed=utils.day_sum(stocks))

intents = discord.Intents.default()
intents.message_content = True

def main():
    client = Stonks(intents=intents)
    client.run(token)
        
        
