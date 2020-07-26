import discord
import math
from discord.ext import commands 

class Calc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a+b)

    @commands.command()
    async def subtract(self, ctx, a: int, b: int):
        await ctx.send(a-b)

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        await ctx.send(a*b)

    @commands.command()
    async def divide(self, ctx, a: int, b: int):
        if b == 0:
            await ctx.send("Cannot divide by 0")
        else:
            await ctx.send(a/b)

    # @commands.command()
    # async def eval(self, ctx, args):
    #     resp = ""
    #     try:
    #         await resp.math.eval(args.join(' '))
    #         await ctx.send(f'The answer is `{resp}`')
    #     except:
    #         await ctx.send("Please enter a valid calculation. Valid symbols include `+,-,*,/`")
            
def setup(client):
    client.add_cog(Calc(client))