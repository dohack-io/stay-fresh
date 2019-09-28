const axios = require('axios');
let gpio = require('gpio');

let ledRedState = false;

function send_data() {

  let co2 = 400 + 2600*Math.random();//400 - 3000
  let hum = 10 + 90*Math.random();
  let voc = 400 + 600*Math.random();
  let tmp = 5 + 25*Math.random();


  ledRedState = !ledRedState;
  gpio.pins[gpio.LED_RED].setValue(ledRedState);

  axios
    .post('http://192.168.0.42:5000/send-data', {
      name: 'Neo1',
      co2: co2,
      hum: hum,
      voc: voc,
      tmp: tmp
    })
    .then(res => {
      console.log(statusCode: ${res.statusCode})
      console.log(res)
    })
    .catch(error => {
      console.error(error)
    });
}

setInterval(send_data, 1000);
