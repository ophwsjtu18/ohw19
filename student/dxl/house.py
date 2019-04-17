import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

def buildhouse(x,y,z):
	SIZE=random.randint(10,15)
	M=random.randint(78,92)
	midx = x+SIZE/2
	midy = y+SIZE/2
	mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,M)
	mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
	mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
	mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
	mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
	mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
	mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
	
			
for a in range(0,3):
	for b in range(0,3):
		for c in range(0,3):
				buildhouse(pos.x+20*a+2,pos.y+20*b,pos.z+20*c)
