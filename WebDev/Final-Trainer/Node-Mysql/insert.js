
// import
var mesql = require('mysql');

var con = mesql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "node-practical"
});

// Connection to database
con.connect(function(err) {
    if (err){
        console.log("Error in connection");
        console.log(err);
    };
    console.log("Database Connected!");
    var sql = "INSERT INTO Employee (EmpCode, Name, Email, Designation) VALUES ('E002', 'Krunal', 'krunal123@gmail.com', 'Manager')";
    con.query(sql, function(err, result) {
        if (err)
            console.log("Error in Query - ${err}")
        else
            console.log(result);
    });
});