import discord
from discord.ext import commands

intents =  discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Привет!Я бот {bot.user}!")

@bot.command()
async def lox(ctx, count_lox = 1):
    await ctx.send('Сам лох' * count_lox)


bot.run("MTE1OTg3ODgxMTAwNjAwOTM0NA.GDG7pS.RJVJE_F8ew1utyamSq-cvv4eHJFQGc2UWhc78I")