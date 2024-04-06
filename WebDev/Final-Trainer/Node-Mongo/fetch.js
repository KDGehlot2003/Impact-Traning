var Mongoclient = require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/";

Mongoclient.connect( url,{useNewUrlParser:true, useUnifiedTopology:true}, function(err, db){
    if(err) throw err;
    var dbo = db.db("college");
    dbo.collection("customers").find({}).toArray(function(err, res){
        if(err) throw err;
        console.log(res);
        db.close();
    });
});