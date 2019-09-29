const axios = require('axios');
let gpio = require('gpio');
let lowsys = require('lowsys');

let ledRedState = false;

let n_id = "O1";
let n_name = "Office 1";

function send_data() {

    let n_co2 = 400 + 2600 * Math.random();//400 - 3000
    let n_hum = 10 + 90 * Math.random();
    let n_voc = 400 + 600 * Math.random();
    let n_tmp = 5 + 25 * Math.random();


    ledRedState = !ledRedState;
    gpio.pins[gpio.LED_RED].setValue(ledRedState);

    axios
        .post('http://192.168.0.42:5000/send-data', {
            id: n_id,
            name: n_name,
            co2: n_co2,
            hum: n_hum,
            voc: n_voc,
            tmp: n_tmp
        })
        .then(res => {
            console.log("statusCode: ${res.statusCode}")
            console.log(res)
        })
        .catch(error => {
            console.error(error)
        });
    lowsys.kickWatchdog();
}

setInterval(send_data, 5000);