/*const express = require('express')
const app = express();

app.get('/', (req, res) => {
  res.sendFile('public/index.html',{root: __dirname})
});

app.listen(8000, () => {
  console.log('Example app listening on port 8000!')
});*/

const express = require('express');
const app = express();
const path = require('path');

app.use(express.static(__dirname+'/public'));

app.listen(8000,()=>{
  console.log('Servidor corriendo en el puerto 8000 <3');
});
