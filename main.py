
import discord
from discord.ext import commands
ham = commands.Bot(command_prefix='#')

@ham.command()
async def ping(ctx):
    await ctx.send('pong')
