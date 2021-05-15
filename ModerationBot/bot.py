from discord.ext import commands
import discord

from DataBase.user import User
from DataBase.guild import Guild
from DataBase.AutoUnmute import AutoUnmute
from DataBase.AutoUnban import AutoUnban

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

        self.User = User
        self.Guild = Guild
        self.AutoUnmute = AutoUnmute
        self.AutoUnban = AutoUnban