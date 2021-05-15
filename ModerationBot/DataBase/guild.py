from asyncpg.connection import Connection

from .AsyncObject import Aobject

class Guild(Aobject):
    async def __init__(self, conn, guild):
        self.conn = conn

        if await conn.fetchrow(
            "SELECT * FROM guilds where guild_id = $1",
            guild.id
        ) is None:
            await conn.execute(
                "INSERT INTO guilds(guild_id) VALUES($1)",
                guild.id
            )
        
        self.guild = await conn.fetchrow(
            "SELECT * FROM guilds where guild_id = $1",
            guild.id
        )
    
    async def set_mute_role(self, role):
        await self.conn.execute(
            "UPDATE guilds SET mute_role_id = $1 WHERE id = $2",
            role.id, self.guild[0]
        )
    
    async def set_log_channel(self, channel):
        await self.conn.execute(
            "UPDATE guilds SET channel_log_id = $1 WHERE id = $2",
            channel.id, self.guild[0]
        )
    
    async def get_log_channel(self):
        guild = await self.conn.fetchrow(
            "SELECT * FROM guilds where id = $1",
            self.guild[0]
        )
        return guild[3]