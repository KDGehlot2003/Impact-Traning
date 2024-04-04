var fs = require('fs');

fs.appendFile('test.txt', ' India', function (err) { 
                        if (err)
        console.log(err);
                        else
        console.log('Append operation complete.');
});