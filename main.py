import discord, json
import random, string, os
import time, datetime
from discord.ext import commands
from discord import Embed, File

def gen(number):
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0'
    ]
    return "".join(random.choices(chars, k=16))

def NitroBox(number):
    code1 = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    return f'https://discord.com/billing/promotions/xbox-game-pass/redeem/{code1}'

with open('config.json') as f:
	config = json.load(f)

token = config.get('token')
prefix = config.get("prefix")


bot = commands.Bot(command_prefix=prefix)
link = "discord.gift/"

@bot.event
async def on_ready():
    print("Im alive :D")
    print(f"Prefix: {prefix}")

@bot.command()
async def massnitro(ctx, number: int):
    x=0
    while x < number:
        await ctx.author.send(link + gen(number))
        x=x+1
    else:
        print(f"Generated {number} codes of Nitro for the user {ctx.author} in time {datetime.datetime.now()}")
        await ctx.send(f"I generated {number} of Nitro Unchecked codes for {ctx.author.mention}")
        return

@bot.command()
async def massnitrobox(ctx, number: int):
    x=0
    while x < number:
        await ctx.author.send(NitroBox(number))
        x=x+1
    else:
        print(f"Generated {number} codes of Nitro Xbox for the user {ctx.author} in time {datetime.datetime.now()}")
        await ctx.send(f"I generated {number} of Nitro Xbox Unchecked codes for {ctx.author.mention}")
        return

bot.run(token)
