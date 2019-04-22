import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

mc = minecraft.Minecraft.create()
ports = list(serial.tools.list_ports.comports())
pos=mc.player.getTilePos()
for p in ports:
    print(p[1])
    if "SERIAL" in p[1]:
        ser=serial.Serial(port=p[0])
    else:
        print("No Arduino Device was found connected to the computer")

class house:
    def __init__(self,x,y,z,L,W,H,M1,M2,M3):
        self.x0=x
        self.y0=y
        self.z0=z
        self.L=L
        self.W=W
        self.H=H
        self.M1=M1
        self.M2=M2
        self.M3=M3
        self.songNumber=1
        for i in range(self.L):
            for j in range(self.W):
                mc.setBlock(self.x0 + i, self.y0, self.z0 +j, M1)
        #ceiling
        for i in range(self.L):
            for j in range(self.W):
                mc.setBlock(self.x0 + i, self.y0 + self.H, self.z0 + j, self.M2)     
        #wall
        for i in range(self.H):
            for j in range(self.L):
                mc.setBlock( self.x0 + j, self.y0 + i, z0,self.M3)
                mc.setBlock( self.x0 + j, self.y0 + i, self.z0 + self.W-1,self.M3)
            for k in range(self.W):
                mc.setBlock( self.x0 , self.y0 + i, self.z0 + k,self.M3)
                mc.setBlock( self.x0 + self.L-1, self.y0 + i, self.z0 + k,self.M3)
        #window
        for i in range(3):
            for j in range(2):
                mc.setBlock( self.x0,self.y0 + self.H/2 + j, self.z0 + self.W/2 + i,glass)
                mc.setBlock( self.x0 + self.L/2 + i, self.y0 + self.H/2 + j,  self.z0,glass)
        #door
        for i in range(self.L):
            for j in range(self.H):
                if i > self.L/2 - 2 and i < self.L/2 + 2:
                    if j < self.H/2:
                        mc.setBlock(self.x0+i, self.y0+j, self.z0+self.W-1, 0)
                    else:
                        mc.setBlock(self.x0+i, self.y0+j, self.z0+self.W-1, self.M3)
                else:
                    mc.setBlock(self.x0+i, self.y0+j, self.z0+self.W, self.M3)
    
    def ifPlayerIn(self, x, y, z):
        self.inHouse = (x >= self.x0 and x <= self.x0 + self.L) and (y >= self.y0 and y <= self.y0 + self.H) and (z >= self.z0 and z <= self.z0 + self.W)
        if self.inHouse:
            ser.write(self.songNumber.encode())  #插入com口后启用
            mc.postToChat('Playing song '+str(self.songNumber))
            time.sleep(1)
        else:
            mc.postToChat('Please enter a house')  
            time.sleep(1)  

    def changeMaterial(self, mat1,mat2,mat3):
        self.__init__(self.x0,self.y0,self.z0,self.L,self.W,self.H,mat1,mat2,mat3)
    
    def changeSong(self, song):
        self.songNumber = song


def main():
    pos=mc.player.getTilePos()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                House=house(-72+15*i, 32 + 15*k , 144+15*j,10,10,10, i+1, j+2, k+3)
    house.changeMaterial(17)
    house.changeSong(3)
    while True:
        time.sleep(0.5)
        mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
        house.ifPlayerIn(pos.x,pos.y,pos.z)
        
if __name__ =='__main__':
    main()