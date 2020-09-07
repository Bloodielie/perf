import asyncpg
from fastapi import FastAPI
from fastapi.responses import JSONResponse, UJSONResponse, ORJSONResponse

app = FastAPI()

response = {"test": "1", "test2": 2, "test3": True}
pool = None


@app.on_event("startup")
async def startup_event():
    global pool
    pool = await asyncpg.create_pool("postgres://postgres:1234@127.0.0.1:5432/test", min_size=1, max_size=5)


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@app.get("/json")
async def json():
    return JSONResponse(response)


@app.get("/ujson")
async def ujson():
    return UJSONResponse(response)


@app.get("/orjson")
async def orjson():
    return ORJSONResponse(response)


@app.get("/sync_json")
def sync_json():
    return JSONResponse(response)


@app.get("/sunc_ujson")
def sunc_ujson():
    return UJSONResponse(response)


@app.get("/sunc_orjson")
def sunc_orjson():
    return ORJSONResponse(response)


@app.get("/fact")
async def fact_find():
    fac(15)
    return "OK"


@app.get("/sync_fact")
async def fact_find_sunc():
    fac(15)
    return "OK"


@app.get("/fib")
async def fib_find():
    fibonacci(15)
    return "OK"


@app.get("/sync_fib")
async def fib_find_sunc():
    fibonacci(15)
    return "OK"


@app.get("/db_bytes")
async def db_bytes():
    async with pool.acquire() as con:
        await con.fetch("SELECT * FROM _bytes")
    return "OK"


@app.get("/db_test")
async def db_test():
    async with pool.acquire() as con:
        await con.fetch("SELECT * FROM _test")
    return "OK"


@app.get("/db_type")
async def db_type():
    async with pool.acquire() as con:
        await con.fetch("select typname, typnamespace, typowner, typlen, typbyval, typcategory, typispreferred, typisdefined, typdelim, typrelid, typelem, typarray from pg_type where typtypmod = -1 and typisdefined = True")
    return "OK"


@app.get("/db_full")
async def db_full():
    async with pool.acquire() as con:
        await con.fetch("SELECT * FROM _bytes")
        await con.fetch("SELECT * FROM _test")
        await con.fetch("select typname, typnamespace, typowner, typlen, typbyval, typcategory, typispreferred, typisdefined, typdelim, typrelid, typelem, typarray from pg_type where typtypmod = -1 and typisdefined = True")
    return "OK"
