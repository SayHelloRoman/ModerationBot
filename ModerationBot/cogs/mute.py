import discord
from discord.ext import commands, tasks

from datetime import datetime

from discord_slash import cog_ext, SlashContext

import asyncio

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_unmute.start()
    
    @cog_ext.cog_slash(name="mute", guild_ids = [813735804030681199])
    async def mute(self, ctx: SlashContext, user: discord.Member, days: int = 0, hours: int = 0, minutes: int = 0):
        time = days * 86400 + hours * 3600 + minutes * 60
        user = await self.bot.User(user, ctx.guild)
        text = 'User mute'

        if not time:
            time = None
        
        try:
            await user.mute(time)
        
        except AssertionError:
            text = "Error"
        
        await ctx.send(text)
    
    @cog_ext.cog_slash(name="unmute", guild_ids = [813735804030681199])
    async def unmute(self, ctx: SlashContext, user: discord.Member):
        user = await self.bot.User(user, ctx.guild)
        text = 'User unmute'

        try:
            await user.unmute()
        
        except AssertionError:
            text = "Error"
        
        await ctx.send(text)

    @cog_ext.cog_slash(name="set_mute_role", guild_ids = [813735804030681199])
    async def set_mute_role(self, ctx: SlashContext, role: discord.Role):
        guild = await self.bot.Guild(ctx.guild)
        await guild.set_mute_role(role)
        await ctx.send('ok')
        
    @tasks.loop(seconds=120.0)
    async def auto_unmute(self):
        await asyncio.sleep(30)
        print('30 second')
        await self.bot.AutoUnmute(self.bot)


def setup(bot):
    bot.add_cog(Slash(bot))