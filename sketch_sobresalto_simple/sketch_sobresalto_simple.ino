#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;

int x;
int y;
//int z;
//int v;
int pulse;

unsigned long tIni;
unsigned long tCurrent;
String currTime;
bool record;
String p="";
//char p='0';
String input = "";
String dataString;


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
   * This pins are used to conect to the microphone
   * 2 ----- OUT
   * 3 ----- VCC
   */
  pinMode(2,INPUT);
  pinMode(3,OUTPUT);
  digitalWrite(3, HIGH);
  
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
  while(p!=""){
    p=Serial.readString();
  }
  input = Serial.readString();
  if(input == "r"){
    Serial.println("Entre input != "" y grabar ");
    grabar(4000);
    Serial.println("Termina grabar ");
    delay(1000);
    input="";
  }
}

/**
 * Records for the time given by parameters
 * @param tRecord Time to record, in milliseconds
 */
 void grabar(int tRecord){
  Serial.println("Inicia grabar");
  record=true;
  tIni = millis();
  while (record) {
    tCurrent=millis() - tIni;
    record= tCurrent < tRecord;
    // Tome los valores de X y Y y póngalos en un String:
    x = accelero.getXVolt();
    y = accelero.getYVolt();
    //z = abs(accelero.getZVolt());
    //v = x + y + z;
    pulse=digitalRead(2);
    currTime=String(tCurrent);
    
    dataString = currTime + "," + String(x) + "," + String(y)+","+String(pulse);

    // Print to the serial port
    
    Serial.println(dataString);
    }
  Serial.println("Datos tomados.");
}
