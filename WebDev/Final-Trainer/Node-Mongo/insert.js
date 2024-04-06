var Mongoclient = require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/";

Mongoclient.connect( url,{useNewUrlParser:true, useUnifiedTopology:true}, function(err, db){
    if(err) throw err;
    var dbo = db.db("college");
    // var myobj = { Empcode: "E001", Name: "Rohit", "Email": "rohit@gmail.com", "Designation": "Developer", "Country": "India" };
    var myobj = { Empcode: "E002", Name: "Rajesh", "Email": "rajesh@gmail.com", "Designation": "Manager", "Country": "India" };
    dbo.collection("customers").insertOne(myobj, function(err, res){
        if(err) throw err;
        
        console.log("data inserted !");
        db.close();
    });
});