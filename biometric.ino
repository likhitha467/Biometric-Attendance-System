



const int validButton = 2;
const int invalidButton = 3;

const int greenLED = 8;
const int redLED = 9;

void setup() {
  pinMode(validButton, INPUT_PULLUP);
  pinMode(invalidButton, INPUT_PULLUP);

  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);

  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW);
}

void loop() {

  // Valid fingerprint simulation
  if (digitalRead(validButton) == LOW) {
    digitalWrite(greenLED, HIGH);
    digitalWrite(redLED, LOW);

    delay(300);
  }

  // Invalid fingerprint simulation
  if (digitalRead(invalidButton) == LOW) {
    digitalWrite(greenLED, LOW);
    digitalWrite(redLED, HIGH);

    delay(300);
  }
}
