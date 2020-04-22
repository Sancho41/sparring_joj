import discord
from get_git_content import get_git_content

from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
  await ctx.send('pong')

@bot.command()
async def git_get(ctx, arg):
  code, extension = get_git_content(arg)
  message = f"```{extension}\n{code}```"
  try:
    await ctx.send(message)
  except:
    await ctx.send("Código excede limite do discord 😢")

bot.run('NTY2NjM3NjEyNzU3MTU1ODQw.XqCf-Q.ubi67iNJkn4yYtEJvu3rS95Hd9I')
