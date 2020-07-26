import discord
import pymongo
import os
from pymongo import MongoClient
import urllib.parse
from discord.ext import commands

class DB(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def register(self, ctx):
        '''
        Registers user into database
        '''
        mongo_url = "mongodb+srv://root:root1234@cluster0.fr1yq.azure.mongodb.net/test"
        cluster = MongoClient(mongo_url)
        db = cluster["UserData"]
        collection = db["UserData"]
        myquery = { "_id": ctx.author.id }
        
        if (collection.count_documents(myquery) == 0):
            post = {'_id': ctx.author.id, 'score': 1}
            collection.insert_one(post)
            await ctx.send("Accepted")
        else:
            await ctx.send('User already in Database.')

def setup(client):
    client.add_cog(DB(client))