const express = require('express');
var cors = require('cors');
const mesql = require('mysql');
var connection = mesql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "node-practical"
});

connection.connect();
var app = express();
app.use(cors());

app.set('port', process.env.PORT || 3000);
app.get('/', function (req, res, next){
    connection.query('SELECT * FROM Employee', function (error, results, fields){
        if (error) {
            console.log("Error in Query - ${error}");
        }
        res.send(results);
    })
});

app.listen(app.get('port'), function(){ 
    console.log("Server is running on port 3000");
}
);