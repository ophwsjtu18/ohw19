#include "Microduino_ColorLED.h"

#define BuzzerPin6 6
int tone_list[] = {262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1046, 1175, 1318, 1397, 1568, 1760, 1967};
String SerialBuffer;
ColorLED strip = ColorLED(1, 2);
void setup()
{
  Serial.begin(9600);
  SerialBuffer = "";
  strip.begin();
}
void playTone(int note) {
  tone(BuzzerPin6, note);
  delay(300);
  noTone(BuzzerPin6);
}

char chr;
void loop()
{

  strip.setPixelColor(1 - 1, 255, 0, 51);
  strip.show();
  if (Serial.available() > 0) {
    SerialBuffer = Serial.readString();
    for (int i = (0); i <= (String(SerialBuffer).length()); i = i + (1)) {
      chr = String(SerialBuffer).charAt(i);
      if (chr < 27 && chr >= 0) {
        playTone(tone_list[7+(chr % 7)]);
        Serial.write(chr % 7+7);
      }
      break;
    }

  }

}
