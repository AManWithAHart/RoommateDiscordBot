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
user_list = [[]]
group_list = []

@bot.event
async def on_ready():
    print("************************************")
    print()
    print("Bot is ready")
    print(f'{bot.user} has connected to Discord!')
    print()
    print("************************************")



@bot.command(name='add')
async def add_item(ctx, *, item):
    idx = -1
    #if the user is in the starting list, obtain index
    #this is slow, but eh, its my bot
    if ctx.author.name in user_list[0]:
        idx = user_list[0].index(ctx.author.name) + 1
    else:
        #if not in list, add it and add another list item to the end
        user_list[0].append(ctx.author.name)
        user_list.append([])
        idx = len(user_list[0])

    if idx == -1:
        await ctx.send("Failure to add item")
        raise ValueError("Failure to add item")

    user_list[idx].append(item)
    print(user_list)
    await ctx.send(f'Added "{item}" to {ctx.author.mention} list')


@bot.command(name='Gadd')
async def group_list_add_item(ctx, *, item):
    if item in group_list:
        await ctx.send("Brother in Christ it is already in the List")
    else:
        group_list.append(item)
        await ctx.send(f'Added "{item}" to group list')


@bot.command(name='Gremove')
async def remove_item(ctx, *, item):
    if item in group_list:
        group_list.remove(item)
        await ctx.send(f'Removed "{item}" from list.')
    else:
        await ctx.send(f'Cannot find "{item}".')

@bot.command(name='Gshow')
async def show_list(ctx):
    embed = discord.Embed(
        title="Group Grocery List",
        color=discord.Color.blue()
    )

    total_list = "\n".join(group_list)
    embed.add_field(name="", value=total_list, inline=False)
    await ctx.send(embed=embed)

@bot.command(name='Gclear')
async def clear_list(ctx):
    if group_list == []:
        await ctx.send("Silly, the list is empty!")
    else:
        my_list.clear()
        await ctx.send(f"You did it {ctx.author.mention}, you did SHOPPING")

@bot.command(name="show")
async def show_my_list(ctx):
    if ctx.author.name not in user_list[0]:
        ctx.send("You dont have a list silly")
        return
    
    embed = discord.Embed(
        title=f"{ctx.author.name} Grocery List",
        color=discord.Color.blue()
    )

    idx = user_list[0].index(ctx.author.name) + 1
    total_list = "\n".join(user_list[idx])
    embed.add_field(name="", value=total_list, inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)