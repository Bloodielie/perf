# Python/Js web perf

## Preparation postgres
```bash
CREATE TABLE _bytes(b bytea); INSERT INTO _bytes(b) (SELECT repeat('a', 1000)::bytea FROM generate_series(1, 100));
CREATE TABLE _test(a int[]); INSERT INTO _test(a) (SELECT (SELECT array_agg(i) FROM generate_series(1, 100) as s(i)) FROM generate_series(1, 100));
```

## Apache-benchmark testing
```bash
ab -n 100000 -c 1000 http://127.0.0.1:{8000/3000}/{json/fib/fact/db_bytes/db_test}
```

## Js run
```bash
pm2-runtime ecosystem.config.js  
```

## Python run
```bash
bash {gunicorn-uvicorn-fast-fastapi.sh/gunicorn-uvicorn-fast-starlette.sh}
```


## Result in my computer
![perf](https://i.imgur.com/zSaWTkF.png)


## Database drivers
+ python
  + ![asyncpg](https://github.com/MagicStack/asyncpg)
+ node.js
  + ![node-postgres](https://github.com/brianc/node-postgres)
