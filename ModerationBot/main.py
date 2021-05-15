from bot import Bot
from discord_slash import SlashCommand

import os
import json


bot = Bot()
slash = SlashCommand(bot, override_type=True, sync_commands=True)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


with open("configs/configBot.json") as f:
    bot.run(json.load(f)["token"])