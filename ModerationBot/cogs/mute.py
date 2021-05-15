from datetime import datetime
import asyncio

import discord
from discord.ext import commands, tasks
from discord_slash import cog_ext, SlashContext

from DataBase.user import User
from DataBase.guild import Guild
from DataBase.AutoUnmute import AutoUnmute


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_unmute.start()
    
    @cog_ext.cog_slash(name="mute", guild_ids = [813735804030681199])
    async def mute(self, ctx: SlashContext, user: discord.Member, days: int = 0, hours: int = 0, minutes: int = 0):
        time = (days * 86400 + hours * 3600 + minutes * 60) or None
        user = await User(user, ctx.guild)
        text = 'User mute'
        
        try:
            await user.mute(time)
        
        except AssertionError:
            text = "Error"
        
        await ctx.send(text)
    
    @cog_ext.cog_slash(name="unmute", guild_ids = [813735804030681199])
    async def unmute(self, ctx: SlashContext, user: discord.Member):
        user = await User(user, ctx.guild)
        text = 'User unmute'

        try:
            await user.unmute()
        
        except AssertionError:
            text = "Error"
        
        await ctx.send(text)

    @cog_ext.cog_slash(name="set_mute_role", guild_ids = [813735804030681199])
    async def set_mute_role(self, ctx: SlashContext, role: discord.Role):
        guild = await Guild(ctx.guild)
        await guild.set_mute_role(role)
        await ctx.send('Unmute')
        
    @tasks.loop(seconds=120.0)
    async def auto_unmute(self):
        await asyncio.sleep(30)
        await AutoUnmute(self.bot)


def setup(bot):
    bot.add_cog(Slash(bot))
