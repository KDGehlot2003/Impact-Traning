const axios = require('axios');
const express = require('express');
var app = express();   

axios.get('http://localhost:3000')
    .then(response => {
        var v = response.data;
        console.log(response.data);
        
        app.get('/', function (req, res, next){
            res.send(v);
        });

    })
    .catch(error => {
        console.log(error);
    });

app.listen(5000, function(){
    console.log("Server is running on port 5000");
}
);