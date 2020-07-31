import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title = "cat",
            colour = disord.Color.blue()
        )

        embed.set_image('/images/cat.png')
        embed.add_field(name='isCat', value='Value')

        # await ctx.say(embed=embed)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Info(client))