const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const app = express();
const port = 4000;
const url = 'mongodb://localhost:27017';
const dbName = 'college';
const client = new MongoClient(url, { useUnifiedTopology: true });
app.get('/customers', async (req, res) => {
  try {
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection('restaurants');

// Find all documents in the collection
    const employees = await collection.find({}).toArray();
    // Respond with the list of employee documents in JSON format
    res.json(employees);
  } catch (e) {
    res.status(500).send('Error connecting to the database');
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
});
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});