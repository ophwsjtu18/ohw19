#include<Servo.h>

Servo base; //控制底座转向
Servo source; //控制子弹的补充
Servo safety; //控制安全装置的开关
Servo launcher; //控制发射

#define PIN_BASE 4
#define PIN_SAFETY 7
#define PIN_SOURCE 8
#define PIN_LAUNCHER 11

int pos=90;
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
    Serial.println(data);
    delay(2);
    switch(data){
      case 'a':
      unclockwise();break;  //逆时针转
      case 'b':
      clockwise();break;   //顺时针转
      case 'c':
      launch();break;
    }
  }
  delay(100);
}

void initEvery()
{
  base.write(pos);
  safety.write(17);
  launcher.write(100);
  source.write(130);
}

void unclockwise(){
  if(pos>=170)
    Serial.println("Unable to turn unclockwisely!");
  else{
    int shift=5;
    for(int i=0; i<shift; i++){
      base.write(pos+i);
      delay(10);
      }
    pos=pos+shift;
    Serial.println("clockwise!");
  }
}


void clockwise(){
  if(pos<=10)
    Serial.println("Unable to turn clockwisely!");
  else{
    int shift=5;
    for(int i=0; i<shift; i++){
      base.write(pos-i);
      delay(10);
      }
    pos-=shift;Serial.println("unclockwise!");
  }
  
}

void launch()
{
  
  
  
  //发射
//    for(int i=150;i>=0;--i)
//  {
//    launcher.write(i);
  launcher.write(20);
    delay(1000);
//  }
  delay(100);

  //撤掉安装装置
  for(int i=17;i<=90;++i)
  {
    safety.write(i);
    delay(10);
  }
  delay(100);
  
  //发射装置复原
  for(int i=20;i<=150;++i)
  {
    launcher.write(i);
    delay(1);
  }
  delay(3000);
  
  //加上安全装置
  for(int i=90;i>=17;--i)
  {
    safety.write(i);
    delay(10);
  }
  launcher.write(100);
  
  //补充弹药
  for(int i=130;i>=70;--i)
  {
    source.write(i);
    delay(10);
  }
  delay(100);
  for(int i=70;i<=130;++i)
  {
    source.write(i);
    delay(10);
  }
  delay(100);
  Serial.println("throw finished!");
}
