int analogPinVit = A0;
int analogPinFor = A1;
int vit = 0;
int force = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  vit = analogRead(analogPinVit);
  force = analogRead(analogPinFor);
  Serial.print(vit);
  Serial.print(";");       
  Serial.println(force);
  delay(100);
}
