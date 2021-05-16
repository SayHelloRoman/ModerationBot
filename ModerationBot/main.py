import os
import json

from discord_slash import SlashCommand
from discord.ext import commands
from discord import Intents


bot = commands.Bot(command_prefix="!", intents=Intents.all())
slash = SlashCommand(bot, override_type=True, sync_commands=True)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


with open("configs/configBot.json") as f:
    bot.run(json.load(f)["token"])
