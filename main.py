
import discord
from discord.ext import commands
from commands import ping_cmd
from events import ready

ham = commands.Bot(command_prefix='#')

@ham.command()
async def ping(ctx):
    await ping_cmd.run(ctx, ham.latency)

@ham.event
async def on_ready():
    ready.event()