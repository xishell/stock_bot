import discord
import src.stock_tracker as st
import random as rd
import json


def day_sum(stocks: list):
    embed = discord.Embed(
        title="Summary",
        description="Test Embed",
        color=discord.Colour.blurple(),
    )
    for i in stocks:
        embed.add_field(name=i, value=i, inline=True)
    
    return embed

def embed_price(stocks: list, title: str, desc=None):
    rand_color = discord.Colour.from_rgb(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
    embed = discord.Embed(
        title=title,
        description=desc,
        color=rand_color
    )
    for i in stocks:
        embed.add_field(name=i, value=f"${st.get_info(i)['price']}", inline=True)
    return embed