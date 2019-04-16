#define BuzzerPin6 6
int item = 0;
void setup()
{
  Serial.begin(9600);
  
}

void loop()
{
  if (Serial.available() > 0) {
    item = String(Serial.readString()).toInt();
    switch (item) {
	case 0:
          noTone(BuzzerPin6);
          break;
	default:
          if(item <28){
	  tone(BuzzerPin6,262+item*100);
          }				
	}
  } 
}
