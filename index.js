let net = require('net');
let http = require('http');
let fs = require('fs');
let gpio = require('gpio');

let HOST = '192.168.0.100';

const request = require('request')

function sendData() {

request.post(HOST,
  {
    id: '1',
    name: 'Neo_1',
    messwert: '12345'
  }
}, (error, res, body) => {
  if (error) {
    console.error(error)
    return
  }
  console.log(`statusCode: ${res.statusCode}`)
  console.log(body)
})
setTimeout(sendData, 1000);
}
