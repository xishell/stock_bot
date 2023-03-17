import discord
from discord.ext import commands
import src.stock_tracker as st
import src.utils as utils
import src.load_config as lc
import os

cfg = lc.load_cfg()
guilds = cfg['GUILDS']
stock_db = cfg['STOCK_DB']
class Stocks(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(guild_ids=guilds)
    async def summary(self, ctx):
        stocks = ["AAPL", "TSLA", "SMT", "GTH"]
        await ctx.respond(embed=utils.day_sum(stocks))
        
    @discord.slash_command(guild_ids=guilds)
    async def price(self, ctx, stocks):
        st = stocks.strip().split(',')
        print(st)
        await ctx.respond(embed=utils.embed_price(st, "Current price"))
        
    @discord.slash_command(guild_ids=guilds)
    async def track(self, ctx, stocks):
        st = stocks.strip().split(',')
        await ctx.respond(utils.add_stocks(stock_db, st))
    
    @discord.slash_command(guild_ids=guilds)
    async def liststocks(self, ctx, stocks):
        if stocks.lower() == "all":
            all = utils.read_stocks(stock_db)
            embed = utils.embed_price(all, "Current price", "All")
        else:
            st = stocks.strip().split(',')
            embed = utils.embed_price(st, "Current price")
        await ctx.respond(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Stocks(bot))