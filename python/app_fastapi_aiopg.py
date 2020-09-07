import aiopg
from fastapi import FastAPI

app = FastAPI()

response = {"test": "1", "test2": 2, "test3": True}
pool = None


@app.on_event("startup")
async def startup_event():
    global pool
    pool = await aiopg.create_pool(
        "dbname=test user=postgres password=1234 port=5432 host=127.0.0.1", minsize=1, maxsize=5
    )


@app.get("/db_bytes")
async def db_bytes():
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM _bytes")
            await cursor.fetchall()
    return "OK"


@app.get("/db_test")
async def db_test():
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM _test")
            await cursor.fetchall()
    return "OK"


@app.get("/db_series")
async def db_type():
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("select typname, typnamespace, typowner, typlen, typbyval, typcategory, typispreferred, typisdefined, typdelim, typrelid, typelem, typarray from pg_type where typtypmod = -1 and typisdefined = True")
            await cursor.fetchall()
    return "OK"


@app.get("/db_full")
async def db_full():
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM _bytes")
            await cursor.fetchall()
            await cursor.execute("SELECT * FROM _test")
            await cursor.fetchall()
            await cursor.execute("select typname, typnamespace, typowner, typlen, typbyval, typcategory, typispreferred, typisdefined, typdelim, typrelid, typelem, typarray from pg_type where typtypmod = -1 and typisdefined = True")
            await cursor.fetchall()
    return "OK"
