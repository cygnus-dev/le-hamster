import discord
import requests
import time

URL = 'https://api.hypixel.net/skyblock/auctions?key=c4dcb81a-e2df-465e-8f8d-a128c8362e3c&page=1'

async def run(ctx):
    await ctx.send("m")
    r = requests.get(url=URL)
    data = r.json()
    await ctx.send(r.json)