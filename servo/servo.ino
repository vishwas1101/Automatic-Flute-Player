#include <Servo.h>

#define pin1 8
#define pin2 9

#define pinServo1 2
#define pinServo2 3
#define pinServo3 4
#define pinServo4 5
#define pinServo5 6
#define pinServo6 7

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

int iniServo1 = 0, iniServo2 = 0, iniServo3 = 0, iniServo4 = 0, iniServo5 = 0, iniServo6 = 0;

int angle = 90;
int speed1;   //this takes the speed of the blower 

//All notes are here
//0 indicates the hole being closed 
//1 indicates the hole being open
//2 indicates the hole being half open
/*int c_sharp[] = {1,1,1,0,0,0};
int d[] = {1,1,0.5,0,0,0};
int d_sharp[] = {1,1,0,0,0,0};
int e[] = {1,0.5,0,0,0,0};
int f[] = {1,0,0,0,0,0};
int f_sharp[] = {0.5,0,0,0,0,0};
int g[] = {0,0,0,0,0,0};
int g_sharp[] = {1,1,1,1,1,1};
int a[] = {1,1,1,1,1,0.5};
int a_sharp[] = {1,1,1,1,1,0};
int b[] = {{1,1,1,1,0,0}*/

void b(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(angle);
  servo6.write(angle);
}

void c_sharp(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(angle);
  servo5.write(angle);
  servo6.write(angle);
}

void d(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(angle);
  servo4.write(angle);
  servo5.write(angle);
  servo6.write(angle); 
}


void d_sharp(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(angle);
  servo4.write(angle);
  servo5.write(angle);
  servo6.write(angle);

}

void e(){
  servo1.write(0);
  servo2.write(angle);
  servo3.write(angle);
  servo4.write(angle);
  servo5.write(angle);
  servo6.write(angle);

}

void f(){
  servo1.write(0);
  servo2.write(angle);
  servo3.write(angle);
  servo4.write(angle);
  servo5.write(angle);
  servo6.write(angle);

}

void g(){
  servo1.write(angle);
  servo2.write(angle);
  servo3.write(angle);
  servo4.write(angle);
  servo5.write(angle);
  servo6.write(angle);  
}

void g_sharp(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
  servo6.write(0);

}

void a(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
  servo6.write(angle);

}

void a_sharp(){
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
  servo6.write(angle);

}

void setup() {
  // put your setup code here, to run once:

    servo1.attach(pinServo1);
    servo2.attach(pinServo2);
    servo3.attach(pinServo3);
    servo4.attach(pinServo4);
    servo5.attach(pinServo5);
    servo6.attach(pinServo6);

    servo1.write(iniServo1);
    servo2.write(iniServo2);
    servo3.write(iniServo3);
    servo4.write(iniServo4);
    servo5.write(iniServo5);
    servo6.write(iniServo6);
    
    pinMode(pin1,OUTPUT);
    pinMode(pin2,OUTPUT);
}



void loop() {
  // put your main code here, to run repeatedly:

//you may write your song here

speed1 = 160;
a_sharp();
analogWrite(pin2 , speed1);
delay(2000);

speed1 = 150;
b();
analogWrite(pin2 , speed1);
delay(2000);

speed1 = 180;
c_sharp;
analogWrite(pin2 , speed1);
delay(2000);

speed1 = 230;
d_sharp();
analogWrite(pin2 , speed1);
delay(2000);

speed1 = 230;
f();
analogWrite(pin2 , speed1);
delay(2000);

speed1 = 180;
c_sharp();
analogWrite(pin2 , speed1);
delay(2000);

speed1 = 150;
b();
analogWrite(pin2 , speed1);
delay(2000);

speed1 = 230;
f();
analogWrite(pin2 , speed1);
delay(2000);

}
