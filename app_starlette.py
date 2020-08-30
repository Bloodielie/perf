from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import UJSONResponse, PlainTextResponse

response = {"test": "1", "test2": 2, "test3": True}


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


routes = [
    Route('/json', json),
    Route('/fact', fact),
    Route('/fib', fib),
]

app = Starlette(routes=routes)
