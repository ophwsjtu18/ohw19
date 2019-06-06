    
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import serial
import serial.tools.list_ports
import time


def house(xo,yo,zo,L,H,W,M=block.STONE.id):
    mc.setBlocks(xo,yo,zo,xo+L,yo+H,zo+W,M)
    mc.setBlocks(xo+1,yo,zo+1,xo+L-1,yo+H,zo+W-1,block.AIR.id)
    midx=xo+L/2
    midy=yo+H/2
    mc.setBlock(midx,yo,zo,block.AIR.id)
    mc.setBlock(midx-1,midy+1,zo,block.GLASS.id)
    mc.setBlock(midx+1,midy+1,zo,block.GLASS.id)
    
mc = minecraft.Minecraft.create()

ports=list(serial.tools.list_ports.comports())
for p in ports:
    print(p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
        ser=serial.Serial(port=p[0])
    else:
        print("No Arduino Device was found connected to the computer")
materials=[1,2,3,4,12,13,14,15,16,17,21,24]
bases=[]
i=1    
for a in range(3):
    for b in range(3):
        for c in range(3):
            house(180+7*a,20+7*b,20+7*c,a+4,b+4,c+4,materials[random.randrange(0,12)])
            bases.append([180+7*a,184+8*a,20+7*b,24+8*b,20+7*c,24+8*c,i])
            i=i+1


while True:
    pos=mc.player.getTilePos()
    mc.postToChat("x="+str(pos.x)+"y="+str(pos.y)+"z="+str(pos.z))
    time.sleep(1)
    for base in bases:
        if pos.x>=base[0] and pos.x<=base[1] and pos.y>=base[2] and pos.y<=base[3] and pos.z>=base[4] and pos.z<=base[5]:
            action=str(base[6]/3+1)
            ser.write(action.encode())
            mc.postToChat("welcome home"+str(base[6]))
            time.sleep(5)
