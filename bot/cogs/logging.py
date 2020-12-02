# Name: logging.py
# Kind: Cog
# Version: 0.0.1

### For testing only ###

import discord
from discord.ext import commands
import data.embeds
from data.embeds import embeds
from discord.ext.commands.errors import *


class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_member_update(before, after):
    #     if len(before.roles) < len(after.roles):
    #         # The user has gained a new role, so lets find out which one
    #         newRole = next(
    #             role for role in after.roles if role not in before.roles)

    #         print(f"User gained {newRole.name}")


def setup(bot):
    bot.add_cog(Logging(bot))
