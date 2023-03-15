import discord
from discord.ext import commands
import src.stock_tracker as st
import src.utils as utils
import src.load_config as lc
import os

cfg = lc.load_cfg()
fmpapi = cfg['FMPAPI']
guilds = cfg['GUILDS']
class Stocks(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(guild_ids=guilds)
    async def summary(self, ctx):
        stocks = ["AAPL", "TSLA", "SMT", "GTH"]
        await ctx.respond(embed=utils.day_sum(stocks))
        
    #@discord.slash_command(guild_ids=guilds)
    #async def price(self, ctx, stock):
    #    curr_price = st.price_tracker(fmpapi, stock)
    #    await ctx.respond(f"Current prices for stock: {stock} is ${curr_price}")
        
def setup(bot):
    bot.add_cog(Stocks(bot))