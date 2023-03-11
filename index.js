const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
app.get('/', (req, res) => {
 
 var dataToSend;
 let command = req.query.command

 const python = spawn('python3', ['light-control.py', '--target', '192.168.1.209', '-c', command]);

 // collect data from script
 python.stdout.on('data', function (data) {
  dataToSend = data.toString();
 });
 python.stderr.on('data', function (data) {
  dataToSend = data.toString();
 });

 python.on('close', (code) => {
 // send data to browser
 res.send(dataToSend)
 });
 
})
app.listen(port, () => console.log(`Listening on port ${port}!`))