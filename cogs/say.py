import discord
from discord.ext import commands
import asyncio

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def say(self, ctx, *args):
        """says what you said"""
        msg = ' '.join(args)
        await ctx.message.delete()
        return await ctx.send(msg)

def setup(client):
    client.add_cog(Say(client))