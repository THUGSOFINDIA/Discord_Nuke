import discord
import asyncio
import time
import sys
from discord.ext import commands
from random import randint

intents = getattr(getattr(discord, "Intents"), "default")()
setattr(intents, "members", True)

bot = commands.Bot(command_prefix="!", intents=intents)

    
@bot.event
async def on_ready():
    print("Very nice bot, very good use :)")

@bot.command()
async def nuke(ctx):                            
    await getattr(ctx, "send")(f"This guy tried to nuke your server, get a load of this guy {ctx.author} | {ctx.author.id}")

@bot.command()
async def spam(ctx):
    await getattr(ctx, "send")("Great ham substitute.")

@bot.command()
async def ban(ctx):
    await getattr(ctx, "send")("MISSING PARAMATER: You must provide a member to ban.")    

@bot.command()
async def kick(ctx):
    await getattr(ctx, "send")("M"+"I"+"S"+"S"+"I"+"N"+"G"+" "+"P"+"A"+"R"+"A"+"M"+"A"+"T"+"E"+"R"+":"+" "+"Y"+"o"+"u"+" "+"m"+"u"+"s"+"t"+" "+"p"+"r"+"o"+"v"+"i"+"d"+"e"+" "+"a"+" "+"m"+"e"+"m"+"b"+"e"+"r"+" "+"t"+"o"+" "+"k"+"i"+"c"+"k"+".")  
        

@bot.command()
async def droles(ctx):
    await getattr(ctx, "send")(f"Current list of this Discord server's roles. \N{SLIGHTLY SMILING FACE} {', '.join(r.name for r in ctx.guild.roles)}")

@bot.command()
async def sroles(ctx):
    await getattr(ctx, "send")("E"+"r"+"r"+"o"+"r"+" "+"s"+"p"+"a"+"m"+"m"+"i"+"n"+"g"+" "+"r"+"o"+"l"+"e"+"s"+"!")
        
@bot.command()
async def alert(ctx):
    await getattr(ctx, "send")("I deleted this command as I believed it was just really dumb.")

with open("bot_token.txt", "r") as token_file:
    bot_token = token_file.read()

if not bot_token:
    print("Done borked the token")

bot.run(bot_token)