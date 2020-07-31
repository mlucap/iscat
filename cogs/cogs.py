import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors
import time

class Cogs(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f'`cogs.{extension} loaded`')

    @commands.command()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'`cogs.{extension} unloaded`')

    @commands.command()
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f'`cogs.{extension} reloaded`')
    
def setup(client):
    client.add_cog(Cogs(client))