from .AsyncObject import Aobject

import asyncpg

import time

import json

class AutoUnmute(Aobject):
    async def __init__(self, conn, bot):
        with open("./configs/configDB.json") as f:
            conn = await asyncpg.connect(
                **json.load(f)
            )
        
        list_user = await conn.fetch(
            "SELECT * FROM users WHERE mute < $1",
            int(time.time())
        )

        for i in list_user:
            guild = await conn.fetchrow(
                "SELECT * FROM guilds WHERE id = $1",
                i[2]
            )

            guild_ds = bot.get_guild(guild[1])
            user = guild_ds.get_member(i[1])
            role = guild_ds.get_role(guild[2])

            await user.remove_roles(role)

            await conn.execute(
                "UPDATE users SET mute = null WHERE id = $1",
                i[0]
            )
        
        await conn.close()
