# Name: weather.py
# Kind: Cog
# Version: 0.0.1

import datetime as dt
import json

import data.embeds
import discord
import requests
from data.embeds import embeds
from discord.ext import commands
from discord.ext.commands.errors import *

api_key = "2c065577f96a20c5300d6dd9944c16b5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def miles_to_km(Value):
    return int(Value) * 1.609


def kelvin_to_celsius(Value):
    return int(Value) - 273.15


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="weather")
    async def test_command(self, ctx, city):
        if city is None:
            await ctx.send("Please provide a city.")
        else:
            embed = discord.Embed(
                titel=f"Weather information about {city}",
                color=ctx.author.color,
                timestamp=dt.datetime.utcnow()
            )

            complete_url = f"{base_url}appid={api_key}&q={city}"
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":

                main = x["main"]
                wind = x["wind"]
                weather = x["weather"]

                weather_condition = weather[0]["main"]

                temp = round(kelvin_to_celsius(main["temp"]), 1)
                wind_speed = round(miles_to_km(wind["speed"]), 1)

                embed.add_field(name="Weather Condition:",
                                value=f"{weather_condition}")
                embed.add_field(name="Temperature:", value=f"{temp} °C")
                embed.add_field(name="Wind Speed:", value=f"{wind_speed} km/h")

                await ctx.send(embed=embed)
            else:
                await ctx.send("Couldn't find that city.")


def setup(bot):
    bot.add_cog(Weather(bot))
