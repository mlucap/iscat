import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Stam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stam(self, ctx):
        await ctx.send('bruh')

def setup(client):
    client.add_cog(Stam(client))