import discord
from discord.ext import commands
import time 

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """shows the latency"""
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        
        await ctx.send(f':ping_pong:\nGateway: `{round(self.client.latency * 1000)}ms`\nHTTP API: `{ping}ms`')

def setup(client):
    client.add_cog(Ping(client))