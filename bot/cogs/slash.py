# Name: slash.py
# Kind: Slash Cog
# Version: 0.0.1

### For testing only ###

import discord
from discord.ext import commands
import data.embeds
from data.embeds import embeds
from discord.ext.commands.errors import *
from discord_slash import SlashCommand
from discord_slash import SlashContext


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slash = SlashCommand(bot, override_type=True)

        @self.slash.slash(name="ping")
        async def ping_slash(ctx):
            await ctx.send(content=f"Pong! (`{round(bot.latency*1000)}`ms)")

        @self.slash.slash(name="calculator")
        async def add_slash(ctx, mode, number1, number2):
            print("lol")


def setup(bot):
    bot.add_cog(Slash(bot))
