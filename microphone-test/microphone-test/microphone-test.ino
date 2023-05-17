#include <AcceleroMMA7361.h>
// https://github.com/jeroendoggen/Arduino-MMA7361-library

AcceleroMMA7361 accelero;
int pulse;

unsigned long tIni;
unsigned long tCurrent;
String currTime;
bool record;
String p="";
//char p='0';
String input = "";
String dataString;
int x;
int y;
int z;

void setup() {

  Serial.begin(57600);
  Serial.println("Hey, listen");

  /**
   * This pins are used to conect to the microphone
   * 2 ----- OUT
   * 3 ----- VCC
   */
  // pinMode(2,INPUT);
  pinMode(3,OUTPUT);
  digitalWrite(3, HIGH);

  accelero.begin(12, 11, 10, 9, A0, A1, A2);    
  accelero.setARefVoltage(3.3);                   //sets the AREF voltage to 3.3V
  accelero.setSensitivity(HIGH);                   //sets the sensitivity to +/-6G
  accelero.calibrate();

  
  Serial.println("Todo listo");
}

void loop() {
  tCurrent=millis() - tIni;
    // Tome los valores de X y Y y póngalos en un String:
    x = accelero.getXVolt();
    y = accelero.getYVolt();
    
    z = accelero.getZVolt();
    //v = x + y + z;
    currTime=String(tCurrent);
    
    dataString = currTime + "," + String(x) + "," + String(y)+","+String(pulse);
  
  
  //pulse=digitalRead(2);
  pulse = analogRead(A15);
  Serial.println(pulse);
  delay(1);
}
