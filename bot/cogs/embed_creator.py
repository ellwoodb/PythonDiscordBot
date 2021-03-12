# Name: embed_creator.py
# Kind: Cog
# Version: 0.0.1

from typing import Optional

import data.embeds
import discord
from data.embeds import embeds
from discord.ext import commands
from discord.ext.commands.errors import *
import datetime as dt

colors = ["green", "blue", "purple", "orange", "red", "grey", "dark green",
          "dark blue", "dark purple", "dark orange", "dark red", "dark grey"]
color_codes = ["3066993", "3447003", "10181046", "15105570", "15158332",
               "9807270", "2067276", "2123412", "7419530", "11027200", "10038562", "9936031"]


class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed", aliases=["create", "embeds"])
    async def create_embed_command(self, ctx, msg, color, embed_content):
        if color in colors:
            color_index = colors.index(color)
            global color_code
            color_code = color_codes[int(color_index)]
        embed = discord.Embed(
            color=int(color_code),
            timestamp=dt.datetime.utcnow(),
            description=embed_content
        )
        ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Embeds(bot))
