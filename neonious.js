var net = require('net');
let http = require('http');
let fs = require('fs');
let gpio = require('gpio');
const request = require('request')

var HOST = '192.168.0.100';


function sendData() {
const request = require('request')

request.post(HOST, {
  json: {
    id: '1',
    name: 'Neo_1',
    messwert: '12345'
  }


  }
}, (error, res, body) => {
  if (error) {
    console.error(error)
    return
  }
  console.log(`statusCode: ${res.statusCode}`)
  console.log(body)
})
}

setInterval(sendData, 1000);
