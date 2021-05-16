import logging

from discord import channel
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import discord

from DataBase.guild import Guild


class Slash(commands.Cog):
    def __init__(self, bot):
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        guild = await Guild(ctx.guild)
        channel = ctx.guild.get_channel(await guild.get_log_channel())

        if not channel is None:
            author = ctx.author.name
            func = ctx.name
            embed = discord.Embed(title=f"\nuser: {author}\ncommand: {func}")
            
            logging.info(f"\nuser: {author}\ncommand: {func}")
            await channel.send(embed=embed)
    
    @cog_ext.cog_slash(name="set_log_channel", guild_ids = [813735804030681199])
    @commands.has_permissions(administrator=True)
    async def set_log_channel(self, ctx: SlashContext, channel: discord.channel.TextChannel):
        guild = await Guild(ctx.guild)
        await guild.set_log_channel(channel)
        await ctx.send('Success!')
    
    

def setup(bot):
    bot.add_cog(Slash(bot))