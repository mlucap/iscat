import discord
import urllib.parse
from discord.ext import commands

class Google(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx, *, searchquery: str):
        '''
        Returns a url that will search google with the provided text.
        '''
        searchquerylower = searchquery.lower()
        if searchquerylower.startswith('images '):
            await ctx.send('<https://www.google.com/search?tbm=isch&q={}>'
                        .format(urllib.parse.quote_plus(searchquery[7:])))
        else:
            await ctx.send('<https://www.google.com/search?q={}>'
                        .format(urllib.parse.quote_plus(searchquery)))

def setup(client):
    client.add_cog(Google(client))