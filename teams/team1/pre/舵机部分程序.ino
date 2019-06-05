#include <Servo.h>
#define pinSer0 5
#define pinSer1 6
#define pinSer2 9

Servo servo0;
Servo servo1;
Servo servo2;

void setup() {
  // put your setup code here, to run once:
  servo0.attach(pinSer0);
  servo1.attach(pinSer1);
  servo2.attach(pinSer2);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.read() == '1')
  {
    onelaunch(70,15);
    delay(1000);
  }
  else
  set();  
}

void set()
{
  servo0.write(70);
  servo1.write(180);
  servo2.write(90);
}
void onelaunch(int angle1, int angle2) //angle1蓄力前角度 angle2蓄力后角度
{ servo2.write(90);
  servo2.write(0);
  delay(500);
  servo2.write(90);
  servo1.write(180);//下舵机归位
  servo0.write(angle1);//上舵机初始归位
  
  servo1.write(70); //挡住投射器
  delay(500);
  
  for(int i = angle1; i >= angle2; i--){
  servo0.write(i);//蓄力 
  delay(40);//蓄力速度
  }

  servo1.write(180); //放开投射器
  delay(500);
  
  for(int i = angle2; i <= angle1; i++){
  servo0.write(i);
  //归位
  delay(40);// 归位速度 
  }
  set(); 
}

