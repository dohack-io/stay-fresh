let net = require('net');
let http = require('http');
let fs = require('fs');
let gpio = require('gpio');

let HOST = '192.168.0.42';

const request = require('request')

function sendData() {


  let jstring = "";
  let co2 = 400 + 2600*Math.random();//400 - 3000
  let hum = 10 + 90*Math.random();
  let voc = 400 + 600*Math.random();
  let tmp = 5 + 25*Math.random();

  //jstring = "{" + "\"name\":\"Besprechungsraum 1\"," +
  //"\"co2\":\"" + co2.toString() +"\",\"hum\":\"" +
  //hum.toString()"\",\"voc\":\"" + voc.toString() + "\",\"tmp\":\"" +
  //tmp.toString() + "\" }";




request.post(HOST,
  {
    name: 'Neo1',
    co2: co2,
    hum: hum,
    voc: voc,
    tmp: tmp
  }
, (error, res, body) => {
  if (error) {
    console.error(error)
    return
  }
  console.log(`statusCode: ${res.statusCode}`)
  console.log(body)
})
setTimeout(sendData, 1000);
}
