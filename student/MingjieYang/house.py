from mcpi.minecraft import  Minecraft
import mcpi.block as block
import random
import serial
import serial.tools.list_ports
import time
mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)  
def housebuild(size,initalpos_x,initalpos_y,initalpos_z,blockid):    #HouseBuild
   
    if size=="S":
        for b in range(4):
            for a in range(4):
                mc.setBlock(initalpos_x+3+b, initalpos_y, initalpos_z+a, blockid)
        for b in range(4):
            for a in range(4):
                mc.setBlock(initalpos_x+3+b, initalpos_y+3, initalpos_z+a, blockid)
        for a in range(2):
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z,blockid)
            mc.setBlock(initalpos_x+6, initalpos_y+1+a, initalpos_z,blockid)
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z+3,blockid)
            mc.setBlock(initalpos_x+6, initalpos_y+1+a, initalpos_z+3,blockid)
        for a in range(4):
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z,blockid)
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z+3,blockid)
            mc.setBlock(initalpos_x+6, initalpos_y+1, initalpos_z+a,blockid)
    elif size=="M":
        for b in range(6):
            for a in range(6):
                mc.setBlock(initalpos_x+3+b, initalpos_y, initalpos_z+a, blockid)
        for b in range(6):
            for a in range(6):
                mc.setBlock(initalpos_x+3+b, initalpos_y+5, initalpos_z+a, blockid)
        for a in range(4):
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z,blockid)
            mc.setBlock(initalpos_x+8, initalpos_y+1+a, initalpos_z,blockid)
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z+5,blockid)
            mc.setBlock(initalpos_x+8, initalpos_y+1+a, initalpos_z+5,blockid)
        for a in range(6):
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z,blockid)
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z+5,blockid)
            mc.setBlock(initalpos_x+8, initalpos_y+1, initalpos_z+a,blockid)
    else:
        size=int(size)
        for b in range(size):
            for a in range(size):
                mc.setBlock(initalpos_x+3+b, initalpos_y, initalpos_z+a, blockid)
        for b in range(size):
            for a in range(size):
                mc.setBlock(initalpos_x+3+b, initalpos_y+size, initalpos_z+a, blockid)
        for a in range(size-1):
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z,blockid)
            mc.setBlock(initalpos_x+2+size, initalpos_y+1+a, initalpos_z,blockid)
            mc.setBlock(initalpos_x+3, initalpos_y+1+a, initalpos_z+size-1,blockid)
            mc.setBlock(initalpos_x+2+size, initalpos_y+1+a, initalpos_z+size-1,blockid)
        for a in range(size):
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z,blockid)
            mc.setBlock(initalpos_x+3+a, initalpos_y+1, initalpos_z+size-1,blockid)
            mc.setBlock(initalpos_x+2+size, initalpos_y+1, initalpos_z+a,blockid)
    return int(size)

def welcome(pos_storage):
    for i in pos_storage:
        if i[0]<pos.x<i[1] and i[2]<pos.y<i[3] and i[4]<pos.z<i[5]:
            print("Welcome home!")
            action = str(random.randint(1,9)) 
            ser.write(action.encode())
            time.sleep(5)
            action = '10'
            ser.write(action.encode()) 

#InitPort      Main Part
BlockList = [1,4,5,14,15,16,17,20,35,41,42,45,87]

ports = list(serial.tools.list_ports.comports())
for p in ports:
    #print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
pos = mc.player.getTilePos()
print(pos.x,pos.y,pos.z)
x1=pos.x
y1=pos.y
z1=pos.z
pos_storage=list()
for i in range(3):
    for j in range(3):
        for k in range(3):
            Material = BlockList[random.randint(0,12)]
            tt=housebuild(random.randint(4,11),x1,y1,z1,Material)
            pos_storage.append([x1+3,x1+tt,y1,y1+tt,z1,z1+tt])  #Stire the position and size of House
            x1=x1+14
        x1= pos.x
        z1=z1+14
    z1= pos.z
    y1=y1+14
    
print("Houses_Built")

while(True):
    pos = mc.player.getTilePos()
    print("Pos[",pos.x,pos.y,pos.z,"]")
    welcome(pos_storage)
    time.sleep(5)


        
            

