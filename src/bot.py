import discord

class Stonks(discord.Bot):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

