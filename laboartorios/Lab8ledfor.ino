void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  for(int i=5;i<13;i++){
  digitalWrite(i, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(200);
  digitalWrite(i, LOW);   // turn the LED off by making the voltage LOW
  delay(200);
  }
  for(int i=5;i<13;i++){
  int a=17-i;
  digitalWrite(a, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(200);
  digitalWrite(a, LOW);   // turn the LED off by making the voltage LOW
  delay(200);
  }

}