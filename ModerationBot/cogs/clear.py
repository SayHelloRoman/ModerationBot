import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cog_ext.cog_slash(name="clear")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx: SlashContext, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send("Success!")

def setup(bot):
    bot.add_cog(Slash(bot))
