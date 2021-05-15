from .AsyncObject import Aobject
import asyncpg
import time
import json

class AutoUnban(Aobject):
    async def __init__(self, conn, bot):
        with open("./configs/configDB.json") as f:
            conn = await asyncpg.connect(
                **json.load(f)
            )
        
        list_user = await conn.fetch(
            "SELECT * FROM users WHERE ban < $1",
            int(time.time())
        )

        for i in list_user:
            guild = await conn.fetchrow(
                "SELECT * FROM guilds WHERE id = $1",
                i[2]
            )

            guild_ds = bot.get_guild(guild[1])
            user = await bot.fetch_user(i[1])
            print(user)

            await guild_ds.unban(user)

            await conn.execute(
                "UPDATE users SET ban = null WHERE id = $1",
                i[0]
            )
        
        await conn.close()