int led_out = 12;
int led_out2 = 13;
int res;
int sensorVal; 
int cmd;
void setup() {
  Serial.begin(9600);
  pinMode(led_out,OUTPUT);
}

void loop() {
  sensorVal = analogRead(A0);
  cmd = sensorToLed(sensorVal);
  digitalWrite(led_out,HIGH);
  digitalWrite(led_out2,LOW);
  delay(sensorVal);
  digitalWrite(led_out2,HIGH);
  digitalWrite(led_out,LOW);
  delay(sensorVal);

  Serial.print("Sensor: ");
  Serial.println(sensorVal);
  Serial.print("Command : ");
  Serial.println(cmd);
}

float sensorToLed(int raw){
 int val = map(sensorVal, 0, 1023, 0, 200);
 val=max(val,0);
 val=min(val,200);
 return val;
}
