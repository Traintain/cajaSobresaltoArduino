//#include <SD.h> //SCK pin 13, MISO pin 12, MOSI pin 11
//#include <SPI.h>

#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;

int x;
int y;
//int z;
//int v;
int in_time=0;
unsigned long tIni;
bool record;
String p="0";
//char p='0';
unsigned long t;
unsigned long tCurrent;
String dataString;

//const int chipSelect = 4; //puerto donde está conectdo el CS del shield de SD
//File data;

void setup() {

  Serial.begin(57600);
  Serial.println("Hey, listen");

  //Serial.print("Initializing SD card...");
  //Comprueba quw hay una tarjeta SD
//  if (!SD.begin(chipSelect)) {
//    Serial.println("initialization failed!");
 //   while (1);
//  }
//  Serial.println("initialization done.");
  
  /**
   * This are the pins used to conect the accelerometer to the Arduino.
   * Feel free to change them if you please.
   * 10 ----- sleepPin
   * 9  ----- selfTestPin
   * 7  ----- zeroGPin
   * 8  ----- gSelectPin
   * A0 ----- xPin
   * A1 ----- yPin
   * A2 ----- zPin
   * 3V3 ---- AREF
   */
  accelero.begin(10, 9, 7, 8, A0, A1, A2);    
  accelero.setARefVoltage(3.3);                   //sets the AREF voltage to 3.3V
  accelero.setSensitivity(HIGH);                   //sets the sensitivity to +/-6G
  accelero.calibrate();
  Serial.println("Todo listo");
}

void loop() {
  in_time=Serial.parseInt();
  //p=Serial.read();
  if(in_time != 0){
    grabar(in_time);
  }
}

/**
 * Records for the time given by parameters
 * @param tRecord Time to record, in milliseconds
 */
 void grabar(int tRecord){
  record=true;
  Serial.println("L");
  tIni = millis();  
  while (record) {
    tCurrent=millis() - tIni;
    record= tCurrent < tRecord;
    // Tome los valores de X y Y y póngalos en un String:
    x = accelero.getXVolt();
    y = accelero.getYVolt();
    //z = abs(accelero.getZVolt());
    //v = x + y + z;
    dataString = String(millis() - tIni) + "," + String(x) + "," + String(y);

    // Print to the serial port
    
    Serial.println(dataString);
    }
    for(int i=0;i<10;i++){
      Serial.println("Datos tomados.");
    }
  }
