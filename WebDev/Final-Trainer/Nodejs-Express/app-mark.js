
//Now, import body-parser and get the POST request data as shown below.
var express = require('express');
var app = express();
const path = require('path');
var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));
app.get('/', function (req, res)
{
res.sendFile(path.join(__dirname+'/mark.html'));
});
app.post('/submit-form', function (req, res) {
    var marks = Number(req.body.maths) + Number(req.body.science) + Number(req.body.english);
    var max = Math.max(Number(req.body.maths), Number(req.body.science), Number(req.body.english));

    res.send("Total Marks: \n"+marks+"<br>Max Marks: \n"+max);
    // res.send("Max Marks: \n"+max);
});
var server = app.listen(5000, function () {
    console.log('Node server is running..');
});


