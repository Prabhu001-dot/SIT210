int Sensor = A1;
int analogValue;
void setup() {
    pinMode(Sensor, INPUT);
}

void loop() {
    analogValue = analogRead(Sensor);
    String lightintensity = String (analogValue);
    if (analogValue > 10)
    {
            Particle.publish("Sunlight" , "Low" , PRIVATE);
    }
    else 
    {
            Particle.publish("Sulight" , "High" ,PRIVATE);
    }
    Particle.publish("Lightintensity", lightintensity, PRIVATE);

    delay(2000);
}