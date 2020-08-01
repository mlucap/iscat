import discord
from discord.ext import commands 

class Duck(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def duck(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/733759365089198220/738959992186470510/video0.mp4')

def setup(client):
    client.add_cog(Duck(client))