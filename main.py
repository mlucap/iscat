import discord
import time
import os
import sys
import json
import datetime
from discord.ext import commands
sys.dont_write_bytecode = True

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print(f'Bot has logged in at {datetime.datetime.now().time()}\nLatency is {round(client.latency * 1000)}ms')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token = os.getenv('BOT_TOKEN')
client.run(token)