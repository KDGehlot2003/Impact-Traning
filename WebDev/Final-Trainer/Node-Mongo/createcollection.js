var Mongoclient = require('mongodb').MongoClient;

var url = "mongodb://127.0.0.1:27017/";

Mongoclient.connect( url,{useNewUrlParser:true, useUnifiedTopology: true}, function(err, db){
    if(err) throw err;
    var dbo = db.db("college");
    dbo.createCollection("customers", function(err, result){
        if(err) throw err;
        console.log("Collection created!");
        db.close();
    });
});