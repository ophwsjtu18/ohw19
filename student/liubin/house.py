import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

def house(x,y,z,l,w,h,block):
    for x0 in range(l):
        for y0 in range(h):
            mc.setBlock(x+x0,y+y0,z,block)
            mc.setBlock(x+x0,y+y0,z+w,block)

    for x0 in range(l):
        for z0 in range(w):
            mc.setBlock(x+x0,y,z+z0,block)
            mc.setBlock(x+x0,y+h,z+z0,block)

    for y0 in range(h):
        for z0 in range(w):
            mc.setBlock(x,y+y0,z+z0,block)
            mc.setBlock(x+l,y+y0,z+z0,block)

    for y0 in range(1,5):  
        for z0 in range(3,5):
            mc.setBlock(x+l,y+y0,z+z0,0)

    for y0 in range(6,9):
        for z0 in range(6,9):
            mc.setBlock(x,y+y0,z+z0,0)

blockset=[1,2,3,4,5,7,14,15,16,17,19,21,22,23,24,25,29,33,35]
index=0

for x1 in range(0,40,15):
    for z1 in range(0,40,15):
        house(-114+x1,9,-436+z1,10,10,10,blockset[index])
        index+=1
        if index>18:
            index=0

for x1 in range(0,40,15):
    for z1 in range(0,40,15):
        house(-114+x1,24,-436+z1,11,11,11,blockset[index])
        index+=1
        if index>18:
            index=0

for x1 in range(0,40,15):
    for z1 in range(0,40,15):
        house(-114+x1,39,-436+z1,12,12,12,blockset[index])
        index+=1
        if index>18:
            index=0

floor1=[[-114,-104,-436,-426,"1"],[-114,-104,-421,-411,"2"],[-114,-104,-406,-396,"3"],
        [-100,-90,-436,-426,"4"],[-100,-90,-421,-411,"5"],[-100,-90,-406,-396,"6"],
        [-85,-75,-436,-426,"7"],[-85,-75,-421,-411,"8"],[-85,-75,-406,-396,"9"]
       ]
floor2=[[-114,-103,-436,-425,"10"],[-114,-103,-421,-410,"11"],[-114,-103,-406,-395,"12"],
        [-100,-90,-436,-426,"13"],[-100,-90,-421,-411,"14"],[-100,-90,-406,-396,"15"],
        [-85,-75,-436,-426,"16"],[-85,-75,-421,-411,"17"],[-85,-75,-406,-396,"18"]
       ]
floor3=[[-114,-104,-436,-426,"19"],[-114,-104,-421,-411,"20"],[-114,-104,-406,-396,"21"],
        [-100,-90,-436,-426,"22"],[-100,-90,-421,-411,"23"],[-100,-90,-406,-396,"24"],
        [-85,-75,-436,-426,"25"],[-85,-75,-421,-411,"26"],[-85,-75,-406,-396,"927"]
       ]

ports=list(serial.tools.list_ports.comports())

for p in ports:
    if "SERIAL" in p[1]:
        ser=serial.Serial(port=p[0])

time.sleep(2)

while True:
    time.sleep(2)
    pos=mc.player.getTilePos()
    if pos.y>9 and pos.y<19:
        for floor in floor1:
            if pos.x>floor[0] and pos.x<floor[1] and pos.z>floor[2] and pos.z<floor[3]:
                ser.write(floor[4].encode())
                
    elif pos.y>24 and pos.y<35:
        for floor in floor2:
            if pos.x>floor[0] and pos.x<floor[1] and pos.z>floor[2] and pos.z<floor[3]:
                ser.write(floor[4].encode())

    elif pos.y>39 and pos.y<51:
        for floor in floor3:
            if pos.x>floor[0] and pos.x<floor[1] and pos.z>floor[2] and pos.z<floor[3]:
                ser.write(floor[4].encode())
        

            

	
