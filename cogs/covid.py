import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors
import aiohttp
import requests
import json
import time
from datetime import datetime

class Covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def covid(self, ctx):
        """Retrieves covid19 data"""

        url = 'https://covid2019-api.herokuapp.com/v2/total'
        r = requests.get(url)
        data = json.loads(r.text)
        d = data['data']
        confirmed = d['confirmed']
        recovered = d['recovered']
        deaths = d['deaths']
        active = d['active']

        embedConfirmed = discord.Embed(title='Confirmed Cases', description='{:,}'.format(confirmed), colour=discord.Color.blue())
        embedActive = discord.Embed(title='Active Cases', description='{:,}'.format(active), colour=discord.Color.orange())
        embedRecovered = discord.Embed(title='Recovered Cases', description='{:,}'.format(recovered), colour=discord.Color.green())
        embedDeaths = discord.Embed(title='Deaths', description='{:,}'.format(deaths), colour=discord.Color.red())

        await ctx.send(embed=embedConfirmed)
        await ctx.send(embed=embedRecovered)
        await ctx.send(embed=embedActive)
        await ctx.send(embed=embedDeaths)
        await ctx.send(f'`Last updated {datetime.date(datetime.now())}`')

def setup(client):
    client.add_cog(Covid(client))