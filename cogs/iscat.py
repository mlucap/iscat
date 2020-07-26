import discord
import random
import string
import logging
from discord.ext import commands

class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def iscat(self, ctx):
        """iscat?"""
        if 'https://imgur.com' in ctx.message.content:
            try:
                await ctx.send(f'There is a `nan%` chance there is a cat in that image')
            except:
                await ctx.send('There was an error reading the image. Logging.')
                logging.error(f' -- User: {ctx.message.author} Error: Error reading image: {ctx.message.content.id}')
        else:
            await ctx.send('No link provided. Please be sure to use imgur links `>iscat [link]`.')

def setup(client):
    client.add_cog(Cat(client))