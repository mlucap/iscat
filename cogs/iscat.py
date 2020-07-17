import discord
from discord.ext import commands

class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def iscat(self, ctx):
        """iscat?"""
        await ctx.send('idk yet!')

def setup(client):
    client.add_cog(Cat(client))