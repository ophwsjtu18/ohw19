import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
ports=list(serial.tools.list_ports.comports())
Material=[1,7,5,17,22,35,42,41,45,
          48,86,57,91,89,88,173,153,2,
          3,73,98,133,79,35,80,19,121]     #pick several materials
for p in ports:
    print(p[1])
    if "SERIAL" in p[1] or "URAT" in p[1]:
        ser=serial.Serial(port=p[0])
    else:
        print("No Arduino Device was found connected to the computer")

def house(x0,y0,z0,L,W,H,M):
    for a in range(0,L):
        for c in range(0,W):
            for b in range(0,H):
                mc.setBlock(x0+a,y0+b,z0+c,M)
    for a in range(0,L-2):
        for c in range(0,W-2):
            for b in range(0,H-1):
                mc.setBlock(x0+1+a,y0+1+b,z0+1+c,0)    #replace blocks to air in the center
    for a in range(0,L):
        for b in range(0,W):
            mc.setBlock(x0+a,y0+H,z0+b,20)   #use the glass as the ceiling
    for a in range(1,3):
        x1=int((2*x0+L)/2)
        mc.setBlock(x1,y0+a,z0,0)   # build a door
    x1=int(x0+L/4)
    y1=int(y0+H/2)
    mc.setBlock(x1,y1,z0,0)   # build a window

num=0
row=(20,40,60)
for a in row:
    for b in row:
        for c in row:
            house(-105+a,40+c,179+b,8,8,8,Material[num])
            num+=1                                       #build 27 houses
x0=-105
y0=40
z0=179
def in_house(x,y,z):
    if (x <= x0+L and x >= x0)and(y <= y0+H and y >= y0)and(z <= z0+W and z >= z0):
        return True
    return False

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    bool_pos=in_house(pos.x,pos.y,pos.z)
    if bool_pos :
        mc.postToChat("welcome home")
        ser.write("y".encode())
        time.sleep(1)
    else :
        mc.postToChat("you are not in a house")



