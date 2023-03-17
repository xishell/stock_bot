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
        embed.add_field(name=i, value=f"${st.price_tracker(i)}", inline=True)
    return embed

def add_stocks(file, stocks):
    try:
        with open(file, 'r+') as fw:
            data = fw.read()
            if data:
                tmp = json.loads(data)
                tmp.extend(stocks)
                fw.seek(0)
                fw.truncate()
                fw.write(json.dumps(tmp))
            else:
                fw.write(json.dumps(stocks))
        resp = f"tracking: {', '.join(stocks)}"
    except:
        resp = "An error occured!"
    return resp
    

def read_stocks(file):
    with open(file, "r") as fr:
        data = fr.read()
        return json.loads(data)