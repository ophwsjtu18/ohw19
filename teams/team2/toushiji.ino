#include <Servo.h>
Servo baseServo;
Servo trayServo;
Servo armServo;
Servo traylockServo;

#define baseBegin 47      //底板初始位置
#define trayClosed 80
#define trayOpened 140
#define armBegin 170    //投石臂初始位置
#define armRelease 40
#define lockClosed 180
#define lockOpened 140    //挡板打开或关闭

void setup(){
  Serial.begin(9600);
  baseServo.attach(9);      //MG995
  trayServo.attach(6);      //SG90 9G
  armServo.attach(5);       //MG995
  traylockServo.attach(3);  //SG90 9G
  sweep(baseServo,baseServo.read(),baseBegin,5);
  delay(1000);
  reset();
  trayClose();
  delay(2000);
}

void sweep(Servo servo,int from,int to,int speed)      //舵机复位
{
  int pos=0;
  if (from<to)
  {
    for(pos=from;pos<=to;pos+=1)
    {
      servo.write(pos);
      delay(speed);
    }
  }
    else
    {
      for (pos=from;pos>=to;pos-=1)
      {
        servo.write(pos);
        delay(speed);
      }
    }
}

void reset()           //复位
{
  sweep(traylockServo,traylockServo.read(),lockClosed,5);
  sweep(armServo,armServo.read(),armBegin,10);
  delay(1000);
}

void trayClose()
{
  sweep(trayServo,trayServo.read(),trayClosed,2);
}

void trayOpen()
{
  sweep(trayServo,trayServo.read(),trayOpened,2);
}

void stoneRelease()       //石头滚入凹槽
{
  sweep(traylockServo,traylockServo.read(),lockOpened,5);
}

void stoneClose()
{
  traylockServo.write(180);
}

void prepareToShoot(int armArm)
{
  int armshoot;
  armshoot=(180-armArm)/3;
  sweep(armServo,armBegin,armshoot,5);
}

void baseRevolveRight()
{
 sweep(baseServo,baseServo.read(),baseServo.read()-25,1);
}

void baseRevolveLeft()
{
  sweep(baseServo,baseServo.read(),baseServo.read()+25,1);
}
void loop()
{
  if (Serial.available()>0){
    int data=Serial.readString().toInt();
    Serial.println(data);
    delay(500);
    if(data==2)      //串口收到2，底板向左旋转
    {
      baseRevolveLeft();
    }
    if(data==3)     //串口收到3，底板向右旋转
    {
      baseRevolveRight();
    }
    if (data==1)    //串口收到1，进入发射程序
    {
    stoneRelease();
    stoneClose();
    delay(1000);
    prepareToShoot(100);
    trayServo.write(140);
    reset();
  
    trayClose();
    }
  }
}
