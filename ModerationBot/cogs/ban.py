import asyncio
from datetime import datetime

import discord
from discord.ext import commands, tasks
from discord_slash import cog_ext, SlashContext


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_unban.start()
    
    @cog_ext.cog_slash(name="ban", guild_ids = [813735804030681199])
    async def ban(self, ctx: SlashContext, user: discord.Member, days: int = 0, hours: int = 0, minutes: int = 0):
        time = days * 86400 + hours * 3600 + minutes * 60
        user = await self.bot.User(user, ctx.guild)

        if not time:
            time = None
        
        await user.ban(time)
        
        await ctx.send("User ban")
    
    @tasks.loop(seconds=120.0)
    async def auto_unban(self):
        await asyncio.sleep(30)
        await self.bot.AutoUnban(self.bot)

def setup(bot):
    bot.add_cog(Slash(bot))