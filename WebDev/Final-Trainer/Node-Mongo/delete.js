
var Mongoclient = require('mongodb').MongoClient;

var url = "mongodb://127.0.0.1:27017/";

Mongoclient.connect( url,{useNewUrlParser:true, useUnifiedTopology: true}, function(err, db){
    if(err) throw err;
    var dbo = db.db("college");
    var myquery = { "Designation": "Manager" };
    dbo.collection("customers").deleteOne(myquery, function(err, obj) {
        if(err) throw err;
        console.log("document deleted created!");
        db.close();
    });
});