from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='fd/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def command(ctx):
    await ctx.send('このコマンドは私が作られて一番最初にできた物です')


bot.run(token)
