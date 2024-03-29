//#include <SD.h> //SCK pin 13, MISO pin 12, MOSI pin 11
//#include <SPI.h>

#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;

int x;
int y;
//int z;
//int v;
unsigned long tIni;
bool record;
String p="0";
//char p='0';
unsigned long t;
unsigned long tCurrent;
String dataString;
String currTime;
int pulse;

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
   */
  accelero.begin(10, 9, 7, 8, A0, A1, A2);    
  accelero.setARefVoltage(3.3);                   //sets the AREF voltage to 3.3V
  accelero.setSensitivity(HIGH);                   //sets the sensitivity to +/-6G
  accelero.calibrate();
  Serial.println("Todo listo");
}

void loop() {
  delay(200);
  p=Serial.readString();
  //p=Serial.read();
  if (p=="p"){
    t=900000;
    Serial.println(String(t));
    grabar(t);
    t=0;
  }else if(p=="s"){
 //   Serial.println(String(t));
    t=1800000;
    grabar(t);
    t=0;
    while(true){
      Serial.println("Datos tomados."); 
    }
  }else if (p=="t"){
    Serial.println(String(t));
    t=60000;
    grabar(t);
    t=0;
  }else{
    Serial.println(p);
  }
}

/**
 * Records for the time given by parameters
 * @param tRecord Time to record, in milliseconds
 */
 void grabar(unsigned long tRecord){
//  Serial.println("Creating file...");
//  data = SD.open("SA.csv", FILE_WRITE);
//  data.println("//////////////////////////////////////////");
//  data.println("");
//  data.println("//////////////////////////////////////////");
//  data.println("Time, Value, x, y, z");
//  Serial.println("Se grabara por " + String(tRecord/60000)+" minutos");
  record=true;

  Serial.println("L");
  tIni = millis();  
  while (record) {
    tCurrent=millis() - tIni;
    record= tCurrent < tRecord;
    //Serial.println(record);
    //String dataString = "";
    // Tome los valores de X y Y y póngalos en un String:
    x = accelero.getXVolt();
    y = accelero.getYVolt();
    //z = abs(accelero.getZVolt());
    //v = x + y + z;
    pulse=digitalRead(2);
    currTime=String(tCurrent);
    
    dataString = currTime + "," + String(x) + "," + String(y)+","+String(pulse);

    // Print to the serial port too:
    
    Serial.println(dataString);
    
    //In case there's a problem and the record must be stoped suddenly and saved
    //p=Serial.read();
    //if(p=='x'){
    //  record=false;
    //  break;
    }
    Serial.flush();
    Serial.println("Datos tomados.");
  }
