import asyncpg
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import UJSONResponse, PlainTextResponse

response = {"test": "1", "test2": 2, "test3": True}
pool = None


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


async def json(req):
    return UJSONResponse(response)


async def fact(req):
    fac(15)
    return PlainTextResponse("OK")


async def fib(req):
    fibonacci(15)
    return PlainTextResponse("OK")


async def db_bytes(req):
    async with pool.acquire() as con:
        await con.fetch("SELECT * FROM _bytes")
    return PlainTextResponse("OK")


async def db_test(req):
    async with pool.acquire() as con:
        await con.fetch("SELECT * FROM _test")
    return PlainTextResponse("OK")


routes = [
    Route('/json', json),
    Route('/fact', fact),
    Route('/fib', fib),
    Route('/db_bytes', db_bytes),
    Route('/db_test', db_test),
]

app = Starlette(routes=routes, on_startup=[startup_event],)
