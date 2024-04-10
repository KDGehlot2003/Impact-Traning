const axios = require('axios')
const { json } = require('body-parser')
const express = require('express')
const { join } = require('path')
const app = express()

// Make request
axios.get('https://jsonplaceholder.typicode.com/posts/1')
// Convert response to JSON



// Show response data
// .then(res => res.data)
// .catch(err => console.log(err))

 .then(res => {
    var v = res.data
    app.get('/', (req, res) => {
        res.setHeader('Content-Type', 'text/json')
        res.send(v)

    })
})
. catch(err => console.log(err))

    
app.listen(3000, () => {
    console.log('Server is running on port 3000')
})
