import discord
import requests
import time
import random
from datetime import datetime

URL = 'https://api.hypixel.net/skyblock/auctions?key=c4dcb81a-e2df-465e-8f8d-a128c8362e3c&page=1'

async def run(ctx):
    r = requests.get(url=URL)
    data = r.json()
    auction_info = data['auctions']
    random_auction_number = random.randint(0,300)
    auction_random = auction_info[random_auction_number]
    start_of_auc_timestamp = int(auction_random['start']) / 1000
    end_of_auc_timestamp = int(auction_random['end']) / 1000
    Start_of_auc_datetime = datetime.fromtimestamp(start_of_auc_timestamp)
    End_of_auc_datetime = datetime.fromtimestamp(end_of_auc_timestamp)
    
    embed=discord.Embed()
    embed.add_field(name='Item name', value=auction_random['item_name'])
    embed.add_field(name='Tier',value=auction_random['tier'])
    embed.add_field(name='Start of Auc/BIN',value=Start_of_auc_datetime)
    embed.add_field(name='End of Auc/BIN',value=End_of_auc_datetime)
    embed.add_field(name='Starting bid',value=auction_random['starting_bid'])
    embed.add_field(name='Item Category',value=auction_random['category'])
    embed.add_field(name='Auctioneer',value=auction_random['auctioneer'])
    embed.add_field(name='Profile ID',value=auction_random['profile_id'])
    embed.add_field(name='UUID',value=auction_random['uuid'])
    # if auction_random['bin'] is True:
    #     embed.add_field(name='Type',value='BIN')
    # else:
    #     embed.add_field(name='Type',value='Auction')
    await ctx.send(embed=embed)
