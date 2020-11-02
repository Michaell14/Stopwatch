import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Ready!!!!")

@client.event
async def on_member_join(member):
    print("f'{member}' has joined the monkey cage. prepare for battle'")

@client.event
async def on_member_remove(member):
    print("lol you left")
client.run("NzY5MzEzNDQ2MTUxNTg1Nzkz.X5NM-g.iMRt1w_lDZpjTEYiW5fRLvoA548")
