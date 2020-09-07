const express = require('express')
const app = express()
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


app.get('/json', function (req, res) {
  res.send(JSON.stringify(response))
})


app.get('/fact', function (req, res) {
    fac(15)
    res.send("OK")
})

app.get('/fib', function (req, res) {
    fibonacci(15)
    res.send("OK")
})

app.get("/db_bytes", async function(req, res) {
    const {rows} = await pool.query("SELECT * FROM _bytes")
    res.send("OK")
})

app.get("/db_test", async function(req, res) {
    const {rows} = await pool.query("SELECT * FROM _test")
    res.send("OK")
})

app.listen(8000)
