from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot()
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def aooni(ctx):
    await ctx.send('なんですか')

@bot.command()
async def おはよう(ctx):
    # メッセージを書きます
    m = "おはようございます" + ctx.author.name + "さん！"
    await ctx.channel.send(m)

bot.run(token)
