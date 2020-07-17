import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class G(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def g(self, ctx):
        await ctx.send('0 bruh go .battleall')

def setup(client):
    client.add_cog(G(client))