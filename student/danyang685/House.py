import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3

from time import sleep

import serial
import serial.tools.list_ports

'''
设计名叫House的类，类里面有changeMaterial ChangeSong ifPlayerIn 函数 其中 ifPlayerIn 函数会判断玩家是否进屋，如果进屋则唱自己的歌。
'''

mc = minecraft.Minecraft.create()

ser=None
for p in list(serial.tools.list_ports.comports()):
    if "CH340" in p[1]:
        ser = serial.Serial(port=p[0])
        break
    else:
        pass

def setBlock(vec,blockType,blockData):
    mc.setBlock(vec.x,vec.y,vec.z,blockType, blockData)

materialList=[block.CLAY,block.STONE_BRICK,block.SANDSTONE,block.BEDROCK,block.COAL_ORE,block.IRON_BLOCK,block.IRON_ORE,block.GOLD_BLOCK,block.GOLD_ORE,block.DIAMOND_ORE,block.DIAMOND_BLOCK,block.LAPIS_LAZULI_BLOCK]

class RoomException(Exception):
    pass
class House:
    vecZero=Vec3.Vec3(0,0,0)
    houseCenter=None
    houseSize=None
    mainMaterial=None
    built=False
    
    def __init__(self,houseCenter=None,houseSize=None,buildNow=False,material=materialList[0],song=1,useSerialport=True):
        print(houseCenter,houseSize)
        if houseCenter:
            self.houseCenter=houseCenter
        if houseSize:
            self.houseSize=houseSize
        if material:
            self.mainMaterial=material
        self.useSerialport=useSerialport
        if buildNow:
            self.build()
        self.song=song

    def _setBlock(self,vec,blockType,blockData):
        mc.setBlock(vec.x,vec.y,vec.z,blockType, blockData)
    def _getVec3(self,x,y,z):
        return Vec3.Vec3(x,y,z)
    def _build(self,mainMaterial,material2):
        xSize=houseSize.x
        ySize=houseSize.y
        zSize=houseSize.z
        for i in range(-xSize,xSize+1):
            for j in range(ySize):
                self._setBlock(self.houseCenter+self._getVec3(i,j,zSize),mainMaterial.id, 1)
                self._setBlock(self.houseCenter+self._getVec3(i,j,-zSize),mainMaterial.id, 1)
        for i in range(-zSize,zSize+1):
            for j in range(ySize):
                self._setBlock(self.houseCenter+self._getVec3(xSize,j,i),mainMaterial.id, 1)
                self._setBlock(self.houseCenter+self._getVec3(-xSize,j,i),mainMaterial.id, 1)
        for i in range(-xSize,xSize+1):
            for j in range(-zSize,zSize+1):
                self._setBlock(self.houseCenter+self._getVec3(i,ySize,j),block.AIR.id, 1)#top
                self._setBlock(self.houseCenter+self._getVec3(i,0,j),mainMaterial.id, 1)#bottom
        halfY=int(ySize/2)
        sizeWindow=int(ySize/3)
        for i in range(halfY-sizeWindow,halfY+1):
            for j in range(-1,2):
                self._setBlock(self.houseCenter+self._getVec3(j,i,zSize),material2.id, 1)
    def changeMaterial(self,material):
        self.mainMaterial=material
        if self.built:
            self.build()
    def build(self):
        if not (self.houseCenter and self.houseSize and self.mainMaterial):
            raise RoomException
        self._build(self.mainMaterial,block.GLASS)
        self.built=True
    def destroy(self):
        if self.built:
            self._build(block.AIR,block.AIR)
            self.built=False
        else:#not built yet
            pass
    def _getPlayerPos(self):
        return mc.player.getTilePos()
    def ifPlayerIn(self):
        if not self.built:
            return False
        playerPos=self._getPlayerPos()

        # print(playerPos)
        # print(self.houseSize)
        if not(playerPos.y>(self.houseCenter.y) and playerPos.y<(self.houseCenter.y+self.houseSize.y-2)):
            return False
        elif not(playerPos.x>self.houseCenter.x-self.houseSize.x and playerPos.x<self.houseCenter.x+self.houseSize.x):
            # print("not X")
            return False
        elif not(playerPos.z>self.houseCenter.z-self.houseSize.z and playerPos.z<self.houseCenter.z+self.houseSize.z):
            # print("not Z")
            return False
        else:
            if self.useSerialport:
                byteData=bytes([self.song])
                ser.write(byteData)
                ser.flush()
            return True
    
    def ChangeSong(self,newSong):
        self.song=newSong
