import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time
import random


#初始化mc
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

#连接外设
ports = list(serial.tools.list_ports.comports())
for p in ports:
    #print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#清除空间
def clear(x0,y0,z0,length,height,width):
    for i in range(0,length):
        for j in range(0,height):
            for k in range(0,width):
                mc.setBlock(x0+i, y0+j, z0+k, block.AIR.id)

#房子类
class House:
    def __init__(self, x0,y0,z0,length,height,width,material,action):
        self.x, self.y, self.z = x0, y0, z0
        self.length, self.height, self.width = length, height, width
        self.material = material
        self.base = [x0,x0+length,y0,y0+height,z0,z0+width]
        self.action = str(action)

        #先生成立方体
        for i in range(0,length):
            for j in range(0,height):
                for k in range(0,width):
                    mc.setBlock(x0+i, y0+j, z0+k, material)

        #再挖空
        clear(x0+1,y0+1,z0+1,length-2,height-2,width-2)

        #造门
        for i in range(int(length/2)-2,int(length/2)+2):
            for j in range(0,4):
                mc.setBlock(x0+i, y0+1+j, z0, block.AIR.id)

        #造窗
        for i in range(int(height/2)-1,int(height/2)+2):
            for j in range(int(width/2)-1,int(width/2)+1):
                mc.setBlock(x0, y0+i, z0+j, block.AIR.id)

    def rebuild(self):
        #先生成立方体
        for i in range(0,length):
            for j in range(0,height):
                for k in range(0,width):
                    mc.setBlock(x0+i, y0+j, z0+k, material)

        #再挖空
        clear(x0+1,y0+1,z0+1,length-2,height-2,width-2)

        #造门
        for i in range(int(length/2)-2,int(length/2)+2):
            for j in range(0,4):
                mc.setBlock(x0+i, y0+1+j, z0, block.AIR.id)

        #造窗
        for i in range(int(height/2)-1,int(height/2)+2):
            for j in range(int(width/2)-1,int(width/2)+1):
                mc.setBlock(x0, y0+i, z0+j, block.AIR.id)

    def isInside(self, mc_pos):
        if self.base[0]<mc_pos.x<self.base[1] and self.base[2]<mc_pos.y<self.base[3] and self.base[4]<mc_pos.z<self.base[5]:
            print("Welcome home!")
            ser.write(self.action.encode())
            time.sleep(5)
            action = '10'
            ser.write(self.action.encode()) #关闭


x,y,z=150,20,150 #找了比较开阔的位置

#clear(x-20,y,z-20,100,100,100) #将周围部分的东西清除（耗时久，仅第一次使用）

#for i in range(0,100):
#    for j in range(0,100):
#        mc.setBlock(x-20+i,y-1,z-20+j,87) #铺地，确保脚底下有东西（耗时久，仅第一次使用）

mc.player.setTilePos(x,y,z)

idList = [1,4,5,14,15,16,17,20,35,41,42,45,87] #选取了一些比较适合建房的材料

houses=[]

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            houses.append(House(x0=x+i*15,y0=y+j*15,z0=z+3+k*15,length=10+k,height=10+j,
                    width=10+i,material=idList[random.randint(0,len(idList)-1)],
                                action = str(random.randint(1,9))))

print('Initilization Finished!')
while(True):
    pos = mc.player.getTilePos()
    print("The position now is [",pos.x,pos.y,pos.z,"]")
    for house in houses:
        house.isInside(pos)
    time.sleep(10)
        
        
        
        
