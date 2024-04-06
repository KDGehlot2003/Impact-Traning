var Mongoclient = require('mongodb').MongoClient;

var url = "mongodb://127.0.0.1:27017/";

Mongoclient.connect( url,{useNewUrlParser:true, useUnifiedTopology: true}, function(err, db){
    if(err) throw err;
    var dbo = db.db("college");
    var myquery = { "Designation": "Developer" };
    var newvalues = {$set: {"Designation": "Project Manager"} };
    dbo.collection("customers").updateMany(myquery, newvalues, function(err, res) {
        if(err) throw err;
        console.log("document updated created!");
        db.close();
    });
});