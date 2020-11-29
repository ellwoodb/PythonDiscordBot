# Name: embeds.py
# Kind: data
# Version: 0.1.0

# Color codes: https://gist.github.com/thomasbnt/b6f455e2c7d743b796917fa3c205f812

import discord  # Import the discord API
import datetime as dt  # Import the datetime module as dt


class embeds():  # Embeds class
    def __inti__(self):
        pass

    # Create a kick embed
    def kick(ctx, member, member_avatar, reason="Not provided by user"):
        embed = discord.Embed(
            color=15105570,  # Set the color (15105570 = orange)
            timestamp=dt.datetime.utcnow()  # Set the timestamp as the time now
        )
        embed.add_field(
            name=f"Info:", value=f"{member} kicked by {ctx.author}", inline=False)  # Add a field with informations about the kick
        # Add a field with the reason of the kick
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        # Set the author to the one that used the command
        embed.set_author(name=ctx.author, icon_url=member_avatar)

        return embed  # Return the embed object

    # Create a ban embed
    def ban(ctx, member, member_avatar, reason="Not provided by user"):
        embed = discord.Embed(
            color=15105570,  # Set the color (15105570 = orange)
            timestamp=dt.datetime.utcnow()  # Set the timestamp as the time now
        )
        embed.add_field(
            name=f"Info:", value=f"{member} banned by {ctx.author}", inline=False)  # Add a field with informations about the ban
        # Add a field with the reason of the kick
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        # Set the author to the one that used the command
        embed.set_author(name=ctx.author, icon_url=member_avatar)

        return embed  # Return the embed object

    # Create a message deletion embed
    def msg_delete(msg, author, channel, member_avatar):
        embed = discord.Embed(
            color=15158332,  # Set the color (15158332 = red)
            timestamp=dt.datetime.utcnow()  # Set the timestamp as the time now
        )
        embed.add_field(
            name=f"Info:", value=f"Message of {author} deleted in <#{channel}>", inline=False)  # Add a field with informations about the message deletion
        # Set the author to the one that used the command
        embed.set_author(name=author, icon_url=member_avatar)

        return embed  # Return the embed object
