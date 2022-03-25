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
  Serial.println("Todo listo");
}

void loop() {
  pulse=digitalRead(2);
  Serial.println(pulse);
  delay(1);
}
