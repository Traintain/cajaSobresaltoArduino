#include <SD.h> //SCK pin 13, MISO pin 12, MOSI pin 11
#include <SPI.h>

#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;

int x;
int y;
int z;
int v;
unsigned long tIni;

const int chipSelect = 4; //puerto donde está conectdo el CS del shield de SD
File data;

int play=6;
int fwd;
int bck;

void setup() {

  Serial.begin(9600);
Serial.println("Hey, listen");
  pinMode(play, INPUT);
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);

  Serial.print("Initializing SD card...");
  //Comprueba quw hay una tarjeta SD 
  if (!SD.begin(chipSelect)) {
    Serial.println("initialization failed!");
    while (1);
  }
  Serial.println("initialization done.");

  accelero.begin(10, 9, 7, 8, A0, A1, A2);    //sleepPin, selfTestPin, zeroGPin, gSelectPin, xPin, yPin, zPin
  accelero.setARefVoltage(5);                   //sets the AREF voltage to 3.3V
  accelero.setSensitivity(HIGH);                   //sets the sensitivity to +/-6G
  accelero.calibrate();
  Serial.println("Todo listo");

  
}

 //Este método graba por 5 segundos

void loop() {

  delay(200);
  Serial.println(play);
  if(digitalRead(play)==LOW){
      Serial.println("Creating file...");
      data = SD.open("AATEST.csv", FILE_WRITE);
      data.println("//////////////////////////////////////////");
      data.println("");
      data.println("//////////////////////////////////////////");
      //Si el momento en que se presiona no hay diferencia de voltaje entre las patas del interruptor, entonces se debe leer LOW como el evento de presionar
      tIni=millis();

      while((millis()-tIni)<20000){

        String dataString = "";
  // Tome los valores de X y Y y póngalos en un String:
     x=abs(accelero.getXAccel());
     y=abs(accelero.getYAccel());
//     z=abs(accelero.getZAccel());
     v=x+y;
       dataString = String(millis()-tIni) + "," + String(v) + ",";
    
       data.println(dataString);
    // print to the serial port too:
       Serial.println(v);
    }
     Serial.println("Datos tomados.");
     data.close();
   }
} 
