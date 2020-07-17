import discord
import random
import string
import requests
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Imgur(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def imgur(self, ctx):
            ctx.send('a')

def setup(client):
    client.add_cog(Imgur(client))