import serial
import serial.tools.list_ports
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import requests
import re

mc = minecraft.Minecraft.create()


def fire(pos):
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            mc.setBlock(pos.x+i,pos.y,pos.z+j,block.FIRE.id)
            # print(pos.x+i,pos.y+j,pos.z)


def movement(lu,rd,length,width): #input:left_up and right_down
    # x and y
    x=length
    y=width
    shift = 50
    center_dot = [(lu[0]+rd[0])/2,(lu[1]+rd[1])/2]
    if center_dot[0]>x/2+shift:
        return 'b'
    elif center_dot[0]<x/2-shift:
        return 'a'
    else:
        return 'c'

def crawler(url):
    content=requests.get(url)
    print(content.text)
    return content.text

def last_pos(pos,content):
    while(0<=ord(content[pos])-ord('0')<10):
        pos+=1
    return pos
def next_pos(pos,content):
    while (True):
        if 0<=ord(content[pos])-ord('0')<10:
            break
        else:
            pos+=1
    return pos
def change(content):
    list=[]
    fnp=10 #first_num_pos
    f_pos =l_pos= fnp
    for i in range(7):
        f_pos = next_pos(l_pos, content)
        l_pos = last_pos(f_pos, content)
        num = eval(content[f_pos:l_pos])
        list.append(num)
        # print(num)
    lu=[list[0],list[2]]
    rd=[list[1],list[3]]
    length=list[5]
    width=list[4]
    return [lu,rd,length,width]

def run():
    action = "empty"
    url = "http://192.168.43.84/test.html"
    while True:
        pos = mc.player.getTilePos()
        content = crawler(url)
        dot_list = change(content)
        action = movement(dot_list[0],dot_list[1],dot_list[2],dot_list[3])
        print(action)
        ser.write(action.encode()) #output to arduino
        if(action=='c'):
            time.sleep(2)
            fire(pos)
        time.sleep(1)


print ('Program begin!')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
        ser=serial.Serial(port=p[0])
    else :
        print ("No Arduino Device was found connected to the computer")

# ser=serial.Serial(port='COM4')
ser=serial.Serial(port='/dev/tty.usbmodem14441')
# wait 2 seconds for arduino board restart
time.sleep(2)
# fire(pos)
run()