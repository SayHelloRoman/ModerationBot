import json
import asyncio

import asyncpg


async def setting():
    with open("./configs/configDB.json") as f:
        conn = await asyncpg.connect(
            **json.load(f)
        )

    await conn.execute('''
    CREATE TABLE users ( 
    id SERIAL PRIMARY KEY,
    user_id BIGINT,
    guild_id BIGINT, 
    mute BIGINT,
    ban BIGINT);
    CREATE TABLE guilds (
    id SERIAL PRIMARY KEY,
    guild_id BIGINT,
    mute_role_id BIGINT,
    channel_log_id BIGINT);
    ''')

    return await conn.close()


asyncio.get_event_loop().run_until_complete(setting())