import serial
import serial.tools.list_ports
import time
import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

time.sleep(2)


def house(x0,y0,z0,L,W,H,M,roof):
    
    for Y in range(H):
        for X in range(L):
            mc.setBlock(x0+X,y0+Y,z0,M)
            mc.setBlock(x0+X,y0+Y,z0+W-1,M)
        for Z in range(W):
            mc.setBlock(x0+L-1,y0+Y,z0+Z,M)
            mc.setBlock(x0,y0+Y,z0+Z,M)
    for X in range(L):
        for Z in range(W):
            mc.setBlock(x0+X,y0,z0+Z,M)
            mc.setBlock(x0+X,y0+H-1,z0+Z,roof)
    for number in range(1,4):
        mc.setBlock(x0+L/2,y0+number,z0,0)
        mc.setBlock(x0+L/2-1,y0+number,z0,0)
    mc.setBlock(x0,y0+H/2,z0+W/2,0)



for y in range(3):
    m=0
    for z in range(3):
        n=0
        h=0
        for x in range(3):
            house(10+20*x,40+10*z,-250-15*y,10+n,10,6+h,17+m-y,22+n+y)
            m+=1
            n+=1
            h+=1



stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    m=0
    for y in range(3):
        for z in range(3):
            n=0
            h=0
            for x in range(3):
                if (pos.x>=10+20*x and pos.x<=(10+20*x+10+n)) and (pos.y>=40+10*z and pos.y<=40+10*z+10) and (pos.z>=-250-15*y and pos.z<=-250-15*y+10+n):
                    mc.postToChat("welcome home")
                    ser.write(str(m+1-9*y).encode())
                    print(str(m+1-9*y))
                    time.sleep(1)
                m+=1
                n+=1
                h+=1
