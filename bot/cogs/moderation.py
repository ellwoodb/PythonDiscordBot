# Name: moderation.py
# Kind: Cog
# Version: 0.1.1

import discord  # Import the discord API
from data.embeds import embeds  # Import the embeds
from data.keywords import bad_words  # Import the bad word list
from discord.ext import commands  # Import more of the discord API
# Import errors of the discord API
from discord.ext.commands.errors import MissingPermissions, MissingRole


# Create the "NoUserProvided" error to raise later
class NoUserProvided(commands.CommandError):
    pass


class Moderation(commands.Cog):  # Create the moderation cog
    def __init__(self, bot):
        self.bot = bot  # Define bot

    # Message filter
    @commands.Cog.listener()
    async def on_message(self, msg):  # Trigger on a new message
        for keyword in bad_words:
            # If there is a bad word in the message
            if keyword in str(msg.content).lower():
                channel = msg.channel  # Define channel the message was sent in

                # Inform the user not to use nad words
                await channel.send(f"<@{msg.author.id}>, please do not use these words.",
                                   delete_after=5)
                await msg.delete()  # Delete the message

                # TODO: User infringements

    # # Log message deletes
    # @commands.Cog.listener()
    # async def on_message_delete(self, msg):  # Trigger on a message deletion

    #     if msg.author.bot:  # If the message author is a bot do nothing
    #         return
    #     else:  # If the message author is a human
    #         msg_delete_embed = embeds.msg_delete(
    #             msg)  # Create the deletion embed
    #         log_channel = self.bot.get_channel(
    #             777895572660682753)  # Get the log channel from id

    #         # Send the deletion embed to the log channel
    #         await log_channel.send(embed=msg_delete_embed)

    # Kick command
    @commands.command(name="kick")
    # Trigger on a kick command
    async def kick_command(self, ctx, member: discord.Member, *, reason=None):
        log_channel = self.bot.get_channel(
            777895572660682753)  # Get the log channel by id

        if not member:  # If there is no member mentioned raise "NoUserProvided"
            raise NoUserProvided

        await member.kick(reason=reason)  # Kick the mentioned user
        await ctx.message.delete()  # Delete the kick message
        # Send kick confirmation
        await ctx.send(f"User {member} has been kicked", delete_after=3)

        if not reason:  # If there is no reason given
            # Create the kick embed without a reason
            kick_embed = embeds.kick(ctx, member, ctx.author.icon_url)
            # Send the kick embed to the log channel
            await log_channel.send(embed=kick_embed)
        else:  # If there is a reason
            # Create the kick embed with a reason
            kick_embed = embeds.kick(ctx, member, ctx.author.icon_url, reason)
            # Send the kick embed to the log channel
            await log_channel.send(embed=kick_embed)

    # On kick command error
    @kick_command.error
    # Trigger on an error of the kick command
    async def kick_command_error(self, ctx, exc):
        if isinstance(exc, NoUserProvided):  # If the error is "NoUserProvided"
            # Tell the user to provide a user to kick
            await ctx.send("Please provide a valid user.", delete_after=5)
        if isinstance(exc, MissingRole):  # If the error is "MissingRole"
            # Tell the user that he doesn't have permissons to kick a user
            await ctx.send("You do not have the permission to do that.", delete_after=5)
        if isinstance(exc, MissingPermissions):  # If the error is "MissingPermissions"
            # Tell the user that the bot has not enough permissions to kick the user
            await ctx.send("I can't kick this user.", delete_after=5)

    # Ban command
    @commands.command(name="ban")
    # Trigger on a kick command
    async def ban_command(self, ctx, member: discord.Member, *, reason=None):
        log_channel = self.bot.get_channel(
            777895572660682753)  # Get the log channel by id

        if not member:  # If there is no member mentioned raise "NoUserProvided"
            raise NoUserProvided

        await member.kick(reason=reason)  # Ban the mentioned user
        await ctx.message.delete()  # Delete the ban message
        # Send ban confirmation
        await ctx.send(f"User {member} has been banned", delete_after=3)

        if not reason:  # If there is no reason given
            # Create the ban embed without a reason
            ban_embed = embeds.ban(ctx, member, ctx.author.icon_url)
            # Send the ban embed to the log channel
            await log_channel.send(embed=ban_embed)
        else:  # If there is a reason
            # Create the ban embed with a reason
            ban_embed = embeds.ban(ctx, member, ctx.author.icon_url, reason)
            # Send the ban embed to the log channel
            await log_channel.send(embed=ban_embed)

    # On ban command error
    @ban_command.error
    # Trigger on an error of the ban command
    async def ban_command_error(self, ctx, exc):
        if isinstance(exc, NoUserProvided):  # If the error is "NoUserProvided"
            # Tell the user to provide a user to ban
            await ctx.send("Please provide a valid user.", delete_after=5)
        if isinstance(exc, MissingRole):  # If the error is "MissingRole"
            # Tell the user that he doesn't have permissons to ban a user
            await ctx.send("You do not have the permission to do that.", delete_after=5)
        if isinstance(exc, MissingPermissions):  # If the error is "MissingPermissions"
            # Tell the user that the bot has not enough permissions to ban the user
            await ctx.send("I can't ban this user.", delete_after=5)


def setup(bot):
    bot.add_cog(Moderation(bot))  # load the cog to the bot
