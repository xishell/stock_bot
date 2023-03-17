import discord
import os

import src.load_config as lc
from src.bot import Stonks

cfg = lc.load_cfg()
token = cfg['TOKEN']
intents = discord.Intents.default()
intents.message_content = True

cogs_list = [
    'stocks',
]

def main():
    client = Stonks(intents=intents)
    for cog in cogs_list:
        client.load_extension(f'src.cogs.{cog}')
    client.run(token)

if __name__ == '__main__':
    main()