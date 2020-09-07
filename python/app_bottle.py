import bottle

from psycopg2 import pool
import ujson

app = bottle.Bottle()

pools = None


def get_pool():
    global pools
    if pools is None:
        pools = pool.SimpleConnectionPool(
            1, 5, database="test", user="postgres", password="1234", port=5432,
        )
    return pools


response = {"test": "1", "test2": 2, "test3": True}


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@app.route("/json")
def json():
    return ujson.dumps(response)


@app.route("/fact")
def fact():
    fac(15)
    return "OK"


@app.route("/fib")
def fib():
    fibonacci(15)
    return "OK"


@app.route("/db_bytes")
def db_bytes():
    conn = get_pool().getconn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM _bytes")
    cursor.fetchall()
    cursor.close()
    get_pool().putconn(conn)
    return "OK"


@app.route("/db_test")
def db_test():
    pool = get_pool()
    conn = pool.getconn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM _test")
    cursor.fetchall()
    cursor.close()
    pool.putconn(conn)
    return "OK"
