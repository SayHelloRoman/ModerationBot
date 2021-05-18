import logging

from discord import channel
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import discord

from DataBase.guild import Guild
from log import get_logger


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.info_log = get_logger("Я всё вижу блять", "INFO")
        self.error_log = get_logger("Ярик нам пизда", "ERROR")
    
    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        guild = await Guild(ctx.guild)
        channel = ctx.guild.get_channel(await guild.get_log_channel())

        if not channel is None:
            author = ctx.author.name
            func = ctx.name
            embed = discord.Embed(title=f"nuser: {author}, command: {func}")
            
            self.info_log.info(f"user: {author}, command: {func}")
            await channel.send(embed=embed)
    
    @cog_ext.cog_slash(name="set_log_channel")
    @commands.has_permissions(administrator=True)
    async def set_log_channel(self, ctx: SlashContext, channel: discord.channel.TextChannel):
        guild = await Guild(ctx.guild)
        await guild.set_log_channel(channel)
        await ctx.send('Success!')
    
    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, ex):
        self.error_log.error(f"Тебя давно не ебали {ex}?")
    

def setup(bot):
    bot.add_cog(Slash(bot))