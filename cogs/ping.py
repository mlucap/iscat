import discord
from discord.ext import commands
import time 

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """shows the latency"""
        await ctx.send(f'`Latency {round(self.client.latency * 1000)} ms`')

def setup(client):
    client.add_cog(Ping(client))