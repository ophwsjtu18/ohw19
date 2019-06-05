#include <AFMotor.h>
AF_DCMotor motor0(2,MOTOR12_64KHZ);
AF_DCMotor motor1(1,MOTOR12_64KHZ);
int speed0 = 255;//移动速度 0-255
char state = '2';
int counter = 0;
bool flag1 = true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  motor0.setSpeed(speed0);
  motor1.setSpeed(speed0);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() > 0)
  { state = Serial.read();
    //Serial.println(state);
    delay(2);
  }
  //if(state == 0)
  //motor0.run(FORWARD);
  switch(state){
    case '0':{runround(50);delay(50);break;}//串口读到0 进入来回走状态 每次长度3秒
    case '1':{motor0.run(FORWARD);motor1.run(FORWARD);delay(50);break;}// 串口读到1 进入向前走状态
    case '2':{motor0.run(RELEASE);motor1.run(RELEASE);delay(50); break;}//串口读到2 进入停止状态
  }
}

void runround(int dist)
{
  if (flag1)
  {
    motor0.run(FORWARD);motor1.run(FORWARD);
    delay(50);
    counter++;
  }
  if (!flag1)
  {
    motor0.run(BACKWARD);motor1.run(BACKWARD);
    delay(50);
    counter--;
  }
  if (counter == dist || counter == 0) 
  flag1 = !flag1;
}
