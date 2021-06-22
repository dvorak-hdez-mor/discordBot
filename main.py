import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN =  os.getenv("DISCORD_TOKEN")
KEY_YT = os.getenv("YOUTUBE_TOKEN")

bot = commands.Bot(command_prefix="/") # Prefijo de comando

@bot.command(name="subs")
async def subs(ctx, user):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + user + "&key=" + KEY_YT).read()
    found = json.loads(data)["pageInfo"]["totalResults"]
    if(found!=0):
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        response = user + " tiene " + "{:,d}".format(int(subs)) + " suscriptores en YouTube!"
    else:
        response = "No se encontró el canal de Youtube"
    await ctx.send(response)

@bot.command(name="suma")
async def suma(ctx, a, b):
    response = int(a)+int(b)
    await ctx.send(response)

bot.run(TOKEN)

"""
.env file

DISCORD_TOKEN = ''
YOUTUBE_TOKEN = ''
"""