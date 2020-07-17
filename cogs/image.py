import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def image(self, ctx):
        await ctx.send('https://imgur.com/a/vKsHmi3')

def setup(client):
    client.add_cog(Image(client))