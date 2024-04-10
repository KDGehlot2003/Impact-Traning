
const request = require('request')
const express = require('express')
const app = express()
const path = require('path');
const { json } = require('body-parser');
// Request URL
var url = 'https://jsonplaceholder.typicode.com/todos/1';
request(url, (error, response, body)=>{
	// Printing the error if occurred
	if(error) console.log(error)

	// Printing status code
	console.log(response.statusCode);
	
	// Printing body
	console.log(body);
    var ans = JSON.parse(body)
    app.get('/', (req, res) => {
        res.sendFile(path.join(__dirname + '/index.html'))
        res.send(ans)
    })
});


//PORT ENVIRONMENT VARIABLE
const port = process.env.PORT || 8080;
app.listen(port, () => console.log(`Listening on port ${port}..`));
