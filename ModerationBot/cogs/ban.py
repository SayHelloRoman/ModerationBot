import asyncio
from datetime import datetime

import discord
from discord.ext import commands, tasks
from discord_slash import cog_ext, SlashContext

from DataBase.user import User
from DataBase.AutoUnban import AutoUnban


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_unban.start()
    
    @cog_ext.cog_slash(name="ban")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx: SlashContext, user: discord.Member, days: int = 0, hours: int = 0, minutes: int = 0):
        time = (days * 86400 + hours * 3600 + minutes * 60) or None
        user = await User(user, ctx.guild)
        
        await user.ban(time)
        
        await ctx.send("User ban")
    
    @tasks.loop(seconds=120.0)
    async def auto_unban(self):
        await asyncio.sleep(30)
        await AutoUnban(self.bot)

def setup(bot):
    bot.add_cog(Slash(bot))
