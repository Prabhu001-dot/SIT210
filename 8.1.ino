// Include the Wire library for I2C
#include <Wire.h>

// LED on pin 13
const int yellow = 13;
const int green = 12;
const int red = 5;

void setup() {
  // Join I2C bus as slave with address 9
  Wire.begin(0x9);
  
  // Call onRecieving when data received                
  Wire.onReceive(onRecieving);
  
  // Setup pin 13 as output and turn LED off
  pinMode(yellow, OUTPUT);
  digitalWrite(yellow, LOW);
  pinMode(green, OUTPUT);
  digitalWrite(green, LOW);
  pinMode(red, OUTPUT);
  digitalWrite(red, LOW);
}

// Function that executes whenever data is received from master
void onRecieving(int input) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    if(c == 0)
    {
      digitalWrite(yellow, 0);
      digitalWrite(green, 0);
      digitalWrite(red, 0);
    }
    else if(c == 1)
    {
      digitalWrite(yellow, 1);
      digitalWrite(green, 0);
      digitalWrite(red, 0);
    }
    else if(c == 2)
    {
      digitalWrite(yellow, 0);
      digitalWrite(green, 1);
      digitalWrite(red, 0);
    }

    else if(c == 3)
    {
      digitalWrite(yellow, 0);
      digitalWrite(green, 0);
      digitalWrite(red, 1);
    }
  }
}
void loop() {
  delay(100);
}
