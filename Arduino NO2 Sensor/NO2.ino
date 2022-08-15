#include <TheThingsNetwork.h>
#include <Wire.h>
#include "MutichannelGasSensor.h"

// Set your AppEUI and AppKey
const char *appEui = "0000000000000000";
const char *appKey = "C28C6C03A5D84A53010C44F9308F12F6";

#define loraSerial Serial1
#define debugSerial Serial

// Replace REPLACE_ME with TTN_FP_EU868 or TTN_FP_US915
#define freqPlan TTN_FP_EU868

TheThingsNetwork ttn(loraSerial, debugSerial, freqPlan);

void setup()
{
  loraSerial.begin(57600);
  debugSerial.begin(9600);

  // Wait a maximum of 10s for Serial Monitor
  while (!debugSerial && millis() < 10000)
    ;

  debugSerial.println("-- STATUS");
  ttn.showStatus();

  debugSerial.println("-- JOIN");
  ttn.join(appEui, appKey);
  Serial.begin(115200);  // start serial for output
  Serial.println("power on!");
  gas.begin(0x04);//the default I2C address of the slave is 0x04
  gas.powerOn();
  Serial.print("Firmware Version = ");
  Serial.println(gas.getVersion());
}

void loop()
{
  float c;
  
  c = gas.measure_NO2();
  Serial.print("The concentration of NO2 is ");
  if (c >= 0) {
      Serial.print(c);
  } else {
      Serial.print("invalid");
  }
  Serial.println(" ppm");
  
  debugSerial.println("-- LOOP");

  // Prepare payload of 1 byte to indicate LED status
  String valueString = String(c, 2);
  char value[4] = {valueString[0], valueString[1], valueString[2], valueString[3]};
  char sensor[3] = {'N', 'O', '2'};
  byte payload[7];
  payload[0] = sensor[0];
  payload[1] = sensor[1];
  payload[2] = sensor[2];
  payload[3] = value[0];
  payload[4] = value[1];
  payload[5] = value[2];
  payload[6] = value[3];

  // Send it off
  ttn.sendBytes(payload, sizeof(payload));

  delay(900000);
}
