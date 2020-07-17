import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Ok(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ok(self, ctx):
        await ctx.send('👍')

def setup(client):
    client.add_cog(Ok(client))