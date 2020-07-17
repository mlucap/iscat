import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors

class Error(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(error)

def setup(client):
    client.add_cog(Error(client))