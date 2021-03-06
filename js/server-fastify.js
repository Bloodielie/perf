const fastify = require('fastify')()
const { Pool } = require('pg')
const pool = new Pool({
    host: 'localhost',
    user: 'postgres',
    max: 5,
    password: '1234',
    database: "test"
})

let response = {"test": "1", "test2": 2, "test3": true}


function fac(n){
    if (n == 0) {
        return 1
    }
    return fac(n - 1) * n
}


function fibonacci(n){
    if (n == 1 || n == 2){
        return 1
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}


fastify.get('/json', (request, reply) => {
  reply.send(response)
})


fastify.get('/fact', (request, reply) => {
    fac(15)
    reply.send("OK")
})


fastify.get('/fib', (req, reply) => {
    fibonacci(15)
    reply.send("OK")
})

fastify.get("/db_bytes", async function(req, reply) {
    const {rows} = await pool.query("SELECT * FROM _bytes")
    reply.send("OK")
})

fastify.get("/db_test", async function(req, reply) {
    const {rows} = await pool.query("SELECT * FROM _test")
    reply.send("OK")
})


fastify.listen(8000)
