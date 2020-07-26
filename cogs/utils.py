import discord
import logging
from discord.ext import commands
from discord.ext.commands import Cog, Context, errors
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice

class Utils(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def confirm(self, ctx):
        confirmation = BotConfirmation(ctx, 0x012345)
        await confirmation.confirm("Are you sure?")

        if confirmation.confirmed:
            await confirmation.update("Confirmed", color=0x55ff55)
        else:
            await confirmation.update("Not confirmed", hide_author=True, color=0xff5555)

    @commands.command()
    async def choice(self, ctx):
        multiple_choice = BotMultipleChoice(ctx, ['one', 'two', 'three', 'four', 'five', 'six'], "Testing stuff")
        await multiple_choice.run()

        await multiple_choice.quit(multiple_choice.choice)

def setup(client):
    client.add_cog(Utils(client))