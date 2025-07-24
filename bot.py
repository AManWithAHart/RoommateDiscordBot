# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True # Enable the message content intent


load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

#client = discord.Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
my_list = []

@bot.event
async def on_ready():
    print("Bot is ready")
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='add')
async def add_item(ctx, *, item):
    my_list.append(item)
    await ctx.send(f'Added "{item}" to the list')


@bot.command(name='remove')
async def remove_item(ctx, *, item):
    if item in my_list:
        my_item.remove(item)
        await ctx.send(f'Removed "{item}" from list.')
    else:
        await ctx.send(f'Cannot find "{item}".')

@bot.command(name='show')
async def show_list(ctx):
    embed = discord.Embed(
        title="Grocery List",
        color=discord.Color.blue()
    )

    total_list = "\n".join(my_list)
    embed.add_field(name="", value=total_list, inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)