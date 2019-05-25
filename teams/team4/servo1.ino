#include<Servo.h>
Servo base; //控制底座转向
Servo source; //控制子弹的补充
Servo safety; //控制安全装置的开关
Servo launcher; //控制发射
#define PIN_BASE 0
#define PIN_SOURCE 1
#define PIN_SAFETY 2
#define PIN_LAUNCHER 3
int pos=0;
static last_pos=0;
void rotate(int);
void launch();
void setup() {
 base.attach(PIN_BASE);
 source.attach(PIN_SOURCE);
 safety.attach(PIN_SAFETY);
 launcher.attach(PIN_LAUNCHER);
// Serial.begin(9600);

// Serial.println("hello world");
}

void loop() {
//pos=Serial.read();//得到投石机转动角度存到pos
  /*******转动********/
  rotate(pos);
  /*********经过一些判断条件后发射*******/
  //发射总过程
  launch();
}

void rotate(int pos)
{  
  if(pos>last_pos)
   for(int i = last_pos;i<=pos;++i)
        {
          base.write(i);
          delay(1);
        }
  else
   for(int i = last_pos;i>=pos;--i)
        {
          base.write(i);
          delay(1);
        }
  last_pos=pos;
}

void launch()
{
  //撤掉安装装置
  for(;;;)
  {
    safety.write(i);
    delay(1);
  }
  //发射
    for(;;;)
  {
    launcher.write(i);
    delay(1);
  }
  //发射装置复原
  for(;;;)
  {
    launcher.write(i);
    delay(1);
  }
  //加上安全装置
  for(;;;)
  {
    safety.write(i);
    delay(1);
  }
  //补充弹药
  for(;;;)
  {
    source.write(i);
    delay(1);
  }
  for(;;;)
  {
    source.write(i);
    delay(1);
  }
}

