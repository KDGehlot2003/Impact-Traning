var http = require('http'); // Import Node.js core module
var fs = require('fs');
var server = http.createServer(function (req, res) {
      //create web server
    
    if (req.url == '/') { //check the URL of the current request
        
        // set response header
        fs.readFile('index.html', function(err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            return res.end();
        }); 
    
    }

    else if (req.url == "/courses") {
        fs.readFile('courses.html', function(err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            return res.end();
        }); 
    }
    else if (req.url == "/contact") {
        fs.readFile('contact.html', function(err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            return res.end();
        });
    }
    else
        res.end('Invalid Request!');
});
server.listen(5000); //6 - listen for any incoming requests
console.log('Node.js web server at port 5000 is running..')




