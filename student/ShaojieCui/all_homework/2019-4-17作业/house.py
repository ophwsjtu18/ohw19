import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import serial
import serial.tools.list_ports
import time

mc = minecraft.Minecraft.create()
ports=list(serial.tools.list_ports.comports())
for p in ports:
    print(p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
        ser=serial.Serial(port=p[0])
    else:
        print("No Arduino Device was found connected to the computer")

class house:
    def __init__(self,x,y,z,l,h,w,m=block.STONE.id,Song=random.randrange(1,12)):
        self.xo=x
        self.yo=y
        self.zo=z
        self.L=l
        self.H=h
        self.W=w
        self.M=random.randrange(1,11)
        self.song=Song


    def buildHouse(self):
        mc.setBlocks(self.xo,self.yo,self.zo,self.xo+self.L,self.yo+self.H,self.zo+self.W,self.M)
        mc.setBlocks(self.xo+1,self.yo,self.zo+1,self.xo+self.L-1,self.yo+self.H,self.zo+self.W-1,block.AIR.id)
        midx=self.xo+self.L/2
        midy=self.yo+self.H/2
        mc.setBlock(midx,self.yo,self.zo,block.AIR.id)
        mc.setBlock(midx-1,midy+1,self.zo,block.GLASS.id)
        mc.setBlock(midx+1,midy+1,self.zo,block.GLASS.id)

    def changeMaterial(self,material):
        self.M=material
        self.buildHouse()

    def changeSong(self,Song):
        self.song=Song
        self.buildHouse()

    def ifPlay(self):
        while True:
            my_pos=mc.player.getTilePos()
            mc.postToChat("x="+str(my_pos.x)+"y="+str(my_pos.y)+"z="+str(my_pos.z))
            time.sleep(1)
            if pos.x>=self.xo and pos.x<=self.xo+self.L and pos.y>=self.yo and pos.y<=self.yo+self.H and pos.z>=self.zo and pos.z<=self.zo+self.W:
                action=str(self.song)
                ser.write(action.encode())
                mc.postToChat("welcome home")
                time.sleep(5)


pos=mc.player.getTilePos()
myhouse=house(pos.x,pos.y,pos.z,3,3,3)
myhouse.buildHouse()
myhouse.changeMaterial(2)
myhouse.ifPlay()
