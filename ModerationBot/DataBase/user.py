import time

from .AsyncObject import Aobject


class User(Aobject):
    async def __init__(self, conn, user, guild):
        self.conn = conn
        self.user = user
        self.guild_ds = guild

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

        if await conn.fetchrow(
            "SELECT * FROM users where user_id = $1 and guild_id = $2",
            user.id, self.guild[0]
        ) is None:
            await conn.execute(
                "INSERT INTO users(user_id, guild_id) VALUES($1, $2)",
                user.id, self.guild[0]
            )
    
    async def mute(self, time_mute):
        assert not self.guild[2] is None

        if not time_mute is None:
            await self.conn.execute(
                "UPDATE users SET mute = $1 WHERE user_id = $2 and guild_id = $3",
                int(time.time()) + time_mute, self.user.id, self.guild[0]
            )
        
        role = self.guild_ds.get_role(self.guild[2])
        await self.user.add_roles(role)
    
    async def unmute(self):
        assert not self.guild[2] is None

        await self.conn.execute(
            "UPDATE users SET mute = $1 WHERE user_id = $2 and guild_id = $3",
            None, self.user.id, self.guild[0]
        )
        
        role = self.guild_ds.get_role(self.guild[2])
        await self.user.remove_roles(role)
    
    async def ban(self, time_mute):
        if not time_mute is None:
            await self.conn.execute(
                "UPDATE users SET ban = $1 WHERE user_id = $2 and guild_id = $3",
                int(time.time()) + time_mute, self.user.id, self.guild[0]
            )
        
        await self.user.ban(reason='Чел фейспам ты в бане')