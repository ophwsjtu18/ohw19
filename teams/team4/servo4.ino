#include<Servo.h>

Servo base; //控制底座转向
Servo source; //控制子弹的补充
Servo safety; //控制安全装置的开关
Servo launcher; //控制发射

#define PIN_BASE 4
#define PIN_SAFETY 7
#define PIN_SOURCE 8
#define PIN_LAUNCHER 11

int pos=0;
char data;
void initEvery();

void setup() {
  
 base.attach(PIN_BASE);
 source.attach(PIN_SOURCE);
 safety.attach(PIN_SAFETY);
 launcher.attach(PIN_LAUNCHER);
 
 Serial.begin(9600);
 
 initEvery();
 
}

void loop() {
  
  if(Serial.available())    //串口接收到数据
  {
    data = Serial.read();     //获取串口接收到的数据
    delay(2);
    switch(data){
      case 'a':
      base.write(++pos);break;  //逆时针转
      case 'b':
      base.write(--pos);break;   //顺时针转
      case 'c':
      launch();break;
    }
  }
}

void initEvery()
{
  base.write(0);
  safety.write(0);
  launcher.write(150);
  source.write(110);
}

void launch()
{
  
  //撤掉安装装置
  for(int i=0;i<=90;++i)
  {
    safety.write(i);
    delay(15);
  }
  delay(100);
  
  //发射
    for(int i=150;i>=0;--i)
  {
    launcher.write(i);
    delay(1);
  }
  delay(1000);
  
  //发射装置复原
  for(int i=0;i<=150;++i)
  {
    launcher.write(i);
    delay(15);
  }
  delay(100);
  
  //加上安全装置
  for(int i=90;i>=0;--i)
  {
    safety.write(i);
    delay(15);
  }
  
  //补充弹药
  for(int i=110;i>=60;--i)
  {
    source.write(i);
    delay(15);
  }
  delay(1000);
  for(int i=60;i<=110;++i)
  {
    source.write(i);
    delay(15);
  }
  delay(100);
}
