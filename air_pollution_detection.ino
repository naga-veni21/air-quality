#define BLYNK_TEMPLATE_ID "TMPL3KoSmSViv"
#define BLYNK_TEMPLATE_NAME "gas"
#define BLYNK_AUTH_TOKEN "Ce3pYsArR4OFOL2t7wWc5IlhPKSt-r2N"
#define BLYNK_PRINT Serial
#include<WiFi.h>
#include<BlynkSimpleEsp32.h>
const char* ssid = "Password Ledhu";
const char* password = "12345678"; //2.4hz

// Define the gas sensor pin
const int gasSensorPin = 34; // Adjust according to your setup
String gasResult;

void setup() {
  Serial.begin(115200);
    Blynk.begin(BLYNK_AUTH_TOKEN,ssid,password);
  pinMode(gasSensorPin, INPUT); // Set gas sensor pin as input
}

void loop() {
  Blynk.run();
  int gasLevel = analogRead(gasSensorPin); // Read the gas sensor value
    Blynk.virtualWrite(V0,gasLevel);

  // Add gas sensor conditions
  if (gasLevel < 200) { // Example threshold for low gas level
    gasResult = "safe";
  } else if (gasLevel >= 200 && gasLevel < 400) { // Medium gas level
    gasResult = "caution";
  } else { // High gas level
    gasResult = "danger";
    Blynk.logEvent("harmful_gas","harmful gas is detected");
  }

  Serial.print("#"); // SOF
  Serial.print(","); // separator
  Serial.print(gasLevel);
  Serial.print(",");
  Serial.print(gasResult); // Add gas result
  Serial.println("~"); // EOF, \r\n
  delay(4000);
}
