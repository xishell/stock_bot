import discord

def day_sum(stocks: list):
    embed = discord.Embed(
        title="Summary",
        description="Test Embed",
        color=discord.Colour.blurple(),
    )
    for i in stocks:
        embed.add_field(name=i, value=i, inline=True)
    
    return embed