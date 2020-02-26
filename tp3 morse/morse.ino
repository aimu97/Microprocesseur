// digital pin 2 has a pushbutton attached to it. Give it a name:
int pushButton = 7;
int on = 0;
int led_out = 8;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
  pinMode(LED_BUILTIN,OUTPUT);
  pinMode(led_out, OUTPUT);
  }
void loop() {
  // read the input pin:
  int buttonState = digitalRead(pushButton);
  // print out the state of the button:
  Serial.println(buttonState);
  while(Serial.available()){
    int lu = Serial.read();

    if(lu== 0){
      digitalWrite(led_out,HIGH);
      delay(500);
      digitalWrite(led_out,LOW);
      
    }else if( lu == 1){
      digitalWrite(led_out,HIGH);
      delay(1000);
      digitalWrite(led_out,LOW);       
      
    }else {
      delay(1000); 
    }
    delay(500);
  }
}

  
 /* if (buttonState == 1 && on == 0){
      digitalWrite(LED_BUILTIN, HIGH); 
      digitalWrite(led_out, HIGH);
      on = 1;     
     }
  else if (buttonState == 1 && on == 1){ 
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(led_out, LOW);
      on = 0;}*/
      
       
   
