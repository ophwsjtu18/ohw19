import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

mc = minecraft.Minecraft.create()

#原点
zerox = 98
zeroy = 34
zeroz = 43

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")


#清除房子
'''
for x in range(80):
    for y in range(80):
        for z in range(80):
            mc.setBlock(zerox + x , zeroy + y, zeroz + z, 0)

'''
    
class House(object):
    def __init__(self,x0, y0, z0, L = 10, W = 10, H = 10, M = 1 ):
        self.base = [0,0,0,0,0,0]
        self.base[0] = x0
        self.base[1] = y0
        self.base[2] = z0
        self.base[3] = L
        self.base[4] = W
        self.base[5] = H
        self.songNumber = 1
        mat0 = 5
        self.mat1 = M
        mat2 = 0
        mat3 = 20
        #bottom
        for i in range(self.base[3]):
            for j in range(self.base[4]):
                mc.setBlock(self.base[0] + i, self.base[1], self.base[2] +j, mat0)
                #mc.setBlock(self.base[0] + i, self.base[1] + 1, self.base[2] +j, 50)
        #top
        for i in range(self.base[3]):
            for j in range(self.base[4]):
                mc.setBlock(self.base[0] + i, self.base[1] + H, self.base[2] + j, 89)     
        #wall
        for i in range(self.base[5]):
            for j in range(self.base[3]):
                mc.setBlock( self.base[0] + j, self.base[1] + i, self.base[2], self.mat1)
                mc.setBlock( self.base[0] + j, self.base[1] + i, self.base[2] + W-1, self.mat1)
            for k in range(self.base[4]):
                mc.setBlock( self.base[0] , self.base[1] + i, self.base[2] + k, self.mat1)
                mc.setBlock( self.base[0] + L-1, self.base[1] + i, self.base[2] + k, self.mat1)
        #window
        for i in range(3):
            for j in range(2):
                mc.setBlock( self.base[0], self.base[1] + H/2 + j, self.base[2] + W/2 + i, mat3)
                mc.setBlock( self.base[0] + L/2 + i, self.base[1] + H/2 + j, + self.base[2], mat3)
        #door
        mc.setBlock(self.base[0] + L/2 , self.base[1] + 1, self.base[2], mat2)
        mc.setBlock(self.base[0] + L/2 , self.base[1] + 2, self.base[2], mat2)
        mc.setBlock(self.base[0] + L/2 , self.base[1] , self.base[2] - 1,self.mat1)
        mc.setBlock(self.base[0] + L/2 -1 , self.base[1] , self.base[2] - 1, self.mat1)
        mc.setBlock(self.base[0] + L/2 +1 , self.base[1] , self.base[2] - 1, self.mat1)
    def ifPlayerIn(self, x, y, z):
        self.inHouse = (x >= self.base[0] and x <= self.base[0] + self.base[3]) and (y >= self.base[1] and y <= self.base[1] + self.base[5]) and (z >= self.base[2] and z <= self.base[2] + self.base[4])
        if self.inHouse:
            #ser.write(self.songNumber.encode())  #插入com口后启用
            mc.postToChat('Playing song '+str(self.songNumber))
            time.sleep(1)
        else:
            mc.postToChat('Please enter a house')  
            time.sleep(1)  
    def changeMaterial(self, mat):
        self.__init__(self.base[0],self.base[1],self.base[2],self.base[3],self.base[4],self.base[5],mat)
    def changeSong(self, song):
        self.songNumber = song

house = House(zerox,zeroy,zeroz, 8, 8, 6)
house.changeMaterial(17)
house.changeSong(3)
while True:
    time.sleep(0.5)
    pos = mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    house.ifPlayerIn(pos.x,pos.y,pos.z)
