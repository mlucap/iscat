import discord
from discord.ext import commands
import requests
import aiohttp
import asyncio
import logging
import random
from discord.ext.commands import Cog, Context, errors


class Fact(commands.Cog):
    def __init__(self, client):
        self.client = client

    logging.getLogger('asyncio').setLevel(logging.CRITICAL)
    # def cog_unload(self) -> None:
    #     if self.__session:
    #         asyncio.get_event_loop().create_task(self.__session.close())

    @commands.command(aliases=['f', 'uf'])
    async def fact(self, ctx: commands.Context) -> None:
        """Gets a useless fact."""

        await ctx.trigger_typing()

        try:
            async with aiohttp.ClientSession().get("https://uselessfacts.jsph.pl/random.json?language=en") as response:
                fact = (await response.json())["text"]
                num = random.randint(1, 200)
                await ctx.send(f'Useless fact number {num}:\n{fact}')
            await aiohttp.ClientSession().close()
                
        except aiohttp.ClientError:
            logging.error('Api call error')
            await ctx.send("`API call error. Unable to fetch catfact. Details in console.`")


def setup(client):
    client.add_cog(Fact(client))