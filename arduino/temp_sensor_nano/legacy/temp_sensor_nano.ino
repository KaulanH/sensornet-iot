const int tempPin = A1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int raw = analogRead(tempPin);
  float voltage = raw * 5.0 / 1023.0;
  float temperatureC = (voltage - 0.5) * 100.0;
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

  Serial.println(temperatureF);  // Send ONLY Fahrenheit
  delay(2000);
}


