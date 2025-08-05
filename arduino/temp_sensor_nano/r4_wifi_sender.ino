#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Skoden";
const char* password = "Ashlyn23";

const int tempPin = A1;

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    int raw = analogRead(tempPin);
    float voltage = raw * 3.3 / 1023.0;
    float temperatureC = (voltage - 0.5) * 100.0;
    float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
    Serial.print("Raw ADC: ");
    Serial.println(raw);
    Serial.print("Voltage: ");
    Serial.println(voltage, 3);


    Serial.print("Temperature (F): ");
    Serial.println(temperatureF);

    HTTPClient http;
    http.begin("http://192.168.12.132:5001/sensor-data");  // Use correct port here!
    http.addHeader("Content-Type", "application/json");

    String postData = "{\"temperature\": " + String(temperatureF, 1) + "}";
    int httpResponseCode = http.POST(postData);

    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);

    http.end();
  } else {
    Serial.println("WiFi not connected");
  }

  delay(2000);  // Send data every 2 seconds
}
