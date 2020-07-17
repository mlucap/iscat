import discord
from discord.ext import commands
import requests
import aiohttp
import asyncio
import logging
from discord.ext.commands import Cog, Context, errors


class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    logging.getLogger('asyncio').setLevel(logging.CRITICAL)
    # def cog_unload(self) -> None:
    #     if self.__session:
    #         asyncio.get_event_loop().create_task(self.__session.close())

    @commands.command(aliases=['cf', 'cat'])
    async def catfact(self, ctx: commands.Context) -> None:
        """Gets a random cat fact."""

        await ctx.trigger_typing()

        try:
            async with aiohttp.ClientSession().get("https://catfact.ninja/fact") as response:
                fact = (await response.json())["fact"]
                length = (await response.json())["length"]
                await ctx.send(f'Random cat fact number {length}:\n{fact}')
            await aiohttp.ClientSession().close()
                
        except aiohttp.ClientError:
            logging.error('Api call error')
            await ctx.send("`API call error. Unable to fetch catfact. Details in console.`")


def setup(client):
    client.add_cog(Cat(client))