import json

import asyncpg


class Aobject:
    pool = None
    
    async def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if Aobject.pool is None:

            with open("./configs/configDB.json") as f:

                Aobject.pool = await asyncpg.connect(
                    **json.load(f)
                )
        
        await instance.__init__(Aobject.pool, *args, **kwargs)

        return instance