const express = require('express')
const app = express()

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
  

app.listen(3000)
