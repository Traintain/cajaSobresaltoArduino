#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;

int x;
int y;
//int v;
unsigned long tIni;
unsigned long t;
unsigned long tCurrent;

//String dataString = "";

void setup() {

  Serial.begin(57600);
  Serial.println("Hey, listen");
  Serial.println("initialization done.");
  
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
   */
  accelero.begin(10, 9, 7, 8, A0, A1, A2);    
  accelero.setARefVoltage(3.3);                   //sets the AREF voltage to 3.3V
  accelero.setSensitivity(HIGH);                   //sets the sensitivity to +/-6G
  accelero.calibrate();
  Serial.println("Todo listo");
}

void loop() {
  delay(200);
    t=350000;
    grabar(t);
    while(1){     
    }
}

/**
 * Records for the time given by parameters
 * @param tRecord Time to record, in milliseconds
 */
 void grabar(unsigned long tRecord){
  Serial.println("Se grabara por " + String(tRecord/60000)+" minutos");

  tIni = millis();
  while (tCurrent<tRecord) {
    // Tome los valores de X y Y y póngalos en un String:
    x = accelero.getXVolt();
    y = accelero.getYVolt();
//    v = x + y;
    //dataString = ;
    // Print to the serial port too:
    Serial.println(String(millis() - tIni) + "," + String(x) + "," + String(y));
    tCurrent=millis() - tIni;
  }
  Serial.println("Datos tomados.");
 }
