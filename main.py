import discord
import time
import os
import sys
import json
from discord.ext import commands
sys.dont_write_bytecode = True

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print('Logged in')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzMzMTE1NjE5NzgzOTk5NTg4.Xw-daQ.frUZgnMjgHf5Az2bGkWN2R0cmNI')