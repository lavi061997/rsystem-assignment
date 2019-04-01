
var noble = require('noble');

// check bluetooth on or off and start scan
noble.on('stateChange', scan);

function scan(state){
  if (state === 'poweredOn') {
    noble.startScanning();
  } else {
    noble.stopScanning();
  }
}

// for every peripheral device run this function
noble.on('discover', foundPeripheral);

function foundPeripheral(peripheral) {
  //here we output the uuid and address of bluetooth.
  console.log('\n Discovered new peripheral with UUID ' + peripheral.uuid+ ':');
  console.log('\t Peripheral Bluetooth address:' + peripheral.address);

};
