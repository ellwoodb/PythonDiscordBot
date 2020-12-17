# Name: embeds.py
# Kind: data
# Version: 0.1.0

# Color codes: https://gist.github.com/thomasbnt/b6f455e2c7d743b796917fa3c205f812

import datetime as dt  # Import the datetime module as dt

import discord
from discord.embeds import Embed  # Import the discord API
from discord.ext import commands  # Import more of the discord API


class embeds():  # Embeds class
    def __inti__(self):
        pass

    # Create a kick embed
    def kick(ctx, member, reason="Not provided by user"):
        embed = discord.Embed(
            color=15105570,  # Set the color (15105570 = orange)
            timestamp=dt.datetime.utcnow()  # Set the timestamp as the time now
        )
        embed.add_field(
            name=f"Info:", value=f"{member} kicked by {ctx.author}", inline=False)  # Add a field with informations about the kick
        # Add a field with the reason of the kick
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        # Set the author to the one that used the command
        embed.set_author(name=ctx.author)

        return embed  # Return the embed object

    # Create a ban embed
    def ban(ctx, member, reason="Not provided by user"):
        embed = discord.Embed(
            color=15105570,  # Set the color (15105570 = orange)
            timestamp=dt.datetime.utcnow()  # Set the timestamp as the time now
        )
        embed.add_field(
            name=f"Info:", value=f"{member} banned by {ctx.author}", inline=False)  # Add a field with informations about the ban
        # Add a field with the reason of the kick
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        # Set the author to the one that used the command
        embed.set_author(name=ctx.author)

        return embed  # Return the embed object

    # # Create a message deletion embed
    # def msg_delete(msg):
    #     author = msg.author
    #     channel = msg.channel.id

    #     embed = discord.Embed(
    #         color=15158332,  # Set the color (15158332 = red)
    #         timestamp=dt.datetime.utcnow()  # Set the timestamp as the time now
    #     )
    #     embed.add_field(
    #         name=f"Info:", value=f"Message of {author} deleted in <#{channel}>", inline=False)  # Add a field with informations about the message deletion
    #     # Set the author to the one that used the command
    #     embed.set_author(name=author)

    #     return embed  # Return the embed object

    # Create a infringement embed
    def infringement(msg, word, author, channel):
        embed = discord.Embed(
            color=15158332,  # Set the color (15158332 = red)
            timestamp=dt.datetime.utcnow()  # Set the timestamp as the time now
        )
        embed.add_field(
            name=f"Info:", value=f"Message of {author} in <#{channel}> contained blacklisted word {word}", inline=False)  # Add a field with informations about the message deletion
        embed.add_field(name=f"Consequence:", value=f"Message deleted.")
        # Set the author to the one that used the command
        embed.set_author(name=author)

        return embed  # Return the embed object
