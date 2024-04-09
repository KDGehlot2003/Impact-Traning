const express = require("express");
var cors = require("cors"); //npm i cors
const mysql = require("mysql");
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "node-practical"
});
connection.connect();
var app = express();
app.use(cors());

app.set("port", process.env.PORT || 5000);
app.get("/", function (req, res, next) {
  connection.query("SELECT * FROM Employee", function (err, result) {
    if (err) {
      console.log(err);
      res.status(400).send(err);
    }
    res.status(200).send(result);
  });
});
app.listen(5000, function () {
  console.log("Server is running.. on Port 5000");
});