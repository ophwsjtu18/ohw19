import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import serial
import serial.tools.list_ports
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def many_house(x,y,z,L,W,H):
    material = random.randint(0,100)
    for j in range(0,H-1):
        for i in range(0,L): #length
            mc.setBlock(x+i,y+j,z,material)
            mc.setBlock(x+i,y+j,z+W-1,material)
        for k in range(0,W):  #width
           mc.setBlock(x,y+j,z+k,material)
           mc.setBlock(x+L-1,y+j,z+k,material)
    for i in (0,1):
        mc.setBlock(x+L/2,y+i,z,block.AIR.id)
##        mc.setBlock(x+L/2-1,y+i,z,block.AIR.id)
    mc.setBlock(x+L/2,y+1,z+W-1,block.GLASS.id)
    for i in range(0,L):
        for j in range(0,W):
            mc.setBlock(x+i,y+H-1,z+j,block.GLASS.id)

def build_many_house(x,y,z,L,W,H,num):
    for i in range(0,num):
        many_house(x+L*i,y,z,L,W,H)

x=559
y=20
z=1203
L=5
W=10
H=4
num=27


build_many_house(x,y,z,L,W,H,num)

def in_house(x,y,z,L,W,H,num,pos):
    for i in range(0,num):
        if (x+i*L<=pos.x<=x+(i+1)*L)and(y<=pos.y<=y+H-1)and(z<=pos.z<=z+W):
            return i
    return 0    

def make_noise(x,y,z,L,W,H,num,pos):
    ser = serial.Serial(port = '/dev/cu.wchusbserial14430')
    while(1):
        pos=mc.player.getTilePos()
        mc.postToChat("Now: x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
        mc.postToChat("Aim: x:"+str(x)+"y:"+str(y)+"z:"+str(z))
        time.sleep(1)
        if in_house(x,y,z,L,W,H,num,pos)!=0:
            mc.postToChat("in")
            ser.write(str(in_house(x,y,z,L,W,H,num,pos)).encode())
            time.sleep(1)
        
make_noise(x,y,z,L,W,H,num,pos)
