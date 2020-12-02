# Name: calculator.py
# Kind: Cog
# Version: None

### For testing only ###

import discord
from discord import user
from discord.ext import commands
import data.embeds
from data.embeds import embeds
from discord.ext.commands.errors import *
from data.keywords import calc_words


class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calculator", aliases=["calc", "cal"])
    async def calculator_command(self, ctx, *args):
        user_message = list(args)[0]

        for word in calc_words:
            if word in user_message:
                numbers = user_message.split(word)
                x = int(numbers[0])
                y = int(numbers[1])

                if word == "+":
                    result = x + y
                    await ctx.message.delete()
                    await ctx.send(f"`{x} {word} {y} = {result}`", delete_after=120)
                elif word == "-":
                    result = x - y
                    await ctx.message.delete()
                    await ctx.send(f"`{x} {word} {y} = {result}`", delete_after=120)
                elif word == "x":
                    result = x * y
                    await ctx.message.delete()
                    await ctx.send(f"`{x} {word} {y} = {result}`", delete_after=120)
                elif word == "/":
                    result = x / y
                    await ctx.message.delete()
                    await ctx.send(f"`{x} {word} {y} = {result}`", delete_after=120)

    @calculator_command.error
    async def calculator_command_error(self, ctx, exc):
        await ctx.send("Couldn't calculate that.", delete_after=5)


def setup(bot):
    bot.add_cog(Calculator(bot))
