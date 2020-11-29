# Name: test.py
# Kind: Cog
# Version: None

### For testing only ###

import discord
from discord.ext import commands
import data.embeds
from data.embeds import embeds
from discord.ext.commands.errors import *


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test_command(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Test(bot))
