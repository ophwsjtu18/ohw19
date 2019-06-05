from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import math

mc=Minecraft.create()
pos=mc.player.getTilePos()

origin_x=-11 #（-11，-457，-1）是初始绝对坐标，用来选取建模的原点
origin_y=-1
origin_z=-457

time.sleep(2)


class HUMAN():
    def __init__(self,initdata):
        self.data = initdata
        self.num=self.data[0]
        self.buildhuman()
        self.xx=self.data[2]+origin_x 
        self.angel=self.data[1]
        self.zz=self.data[2]*math.tan(self.data[1]/180*3.14)+origin_z
        self.exist=True

    def buildhuman(self):
        x=self.data[2]+origin_x 
        z=self.data[2]*math.tan(self.data[1]/180*3.14)+origin_z
        y=origin_y
        block=self.data[3]
        
        mc.setBlock(x,y,z,block)  #the two legs
        mc.setBlock(x,y+1,z,block)
        mc.setBlock(x,y+2,z,block)
        mc.setBlock(x+2,y,z,block)
        mc.setBlock(x+2,y+1,z,block)
        mc.setBlock(x+2,y+2,z,block)

        mc.setBlock(x,y+3,z,block)  #the body
        mc.setBlock(x,y+4,z,block)
        mc.setBlock(x,y+5,z,block)
        mc.setBlock(x+1,y+3,z,block)
        mc.setBlock(x+1,y+4,z,block)
        mc.setBlock(x+1,y+5,z,block)
        mc.setBlock(x+2,y+3,z,block)
        mc.setBlock(x+2,y+4,z,block)
        mc.setBlock(x+2,y+5,z,block)

        mc.setBlock(x+1,y+6,z,block) #the head
        mc.setBlock(x+1,y+7,z,block)
        mc.setBlock(x+1,y+8,z,block)
        mc.setBlock(x+2,y+8,z,block)
        mc.setBlock(x,y+8,z,block)
        
        mc.setBlock(x-1,y+5,z,block)  #two arms
        mc.setBlock(x-2,y+5,z,block)
        mc.setBlock(x-2,y+4,z,block)
        mc.setBlock(x-2,y+3,z,block)
        mc.setBlock(x+3,y+5,z,block)
        mc.setBlock(x+4,y+5,z,block)
        mc.setBlock(x+4,y+4,z,block)
        mc.setBlock(x+4,y+3,z,block)

    def getnum(self):
        return self.num

    def getangel(self):
        return self.angel

    def getx(self):
        return float(self.xx)

    def getz(self):
        return float(self.zz)

    def destroy(self):
        self.data[3]=0
        self.buildhuman()
        self.exist=False

    def if_exist(self):
        return self.exist

#定义array=[NUM序号,angel夹角,distance_in_x_axis=6模型原点距离（不需要改）, block=1模型材质]
        


def build_and_destroy():
    file=open("test.txt") #txt的相对路径
    line=file.readline()
    result=[]

    while line:
        line=line.strip()
        tem=line.split()
        array=[float(tem[0]),float(tem[1]),10,1]       
        result.append(HUMAN(array))
        line=file.readline()

    file.close()
    while True:  #每隔一段时间调用一次函数的话，这里改成延时
        pos=mc.player.getTilePos()
        for elem in result:
            if abs(pos.x-elem.getx())<2 and abs(pos.z-elem.getz())<2 and elem.if_exist()==True: #这里的2是小人走到模型多近时摧毁，如果人较多，模型就会离的很近，2需要改小
                elem.destroy()
                print( elem.getangel())

                       
build_and_destroy() #调用该函数就会返回摧毁对象的所在的角度



        
