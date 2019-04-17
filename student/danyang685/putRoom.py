import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3
mc = minecraft.Minecraft.create()
#pos = mc.player.getTilePos()#player location
pos=Vec3.Vec3(-6,0,49)
def setBlock(vec,blockType,blockData):
    mc.setBlock(vec.x,vec.y,vec.z,blockType, blockData)


vecForward=pos+Vec3.Vec3(2,0,3)
blockType = mc.getBlock(pos)
print(pos)
mc.events.pollChatPosts
houseX=8
houseZ=6
houseY=6
for i in range(-houseX-90,houseX+90):
    for j in range(8):
        for k in range(-houseZ-90,houseZ+90):
            pass
            #setBlock(pos+Vec3.Vec3(i,j,k),block.AIR.id, 1)


for i in range(-houseX-90,houseX+90):
    for j in range(-1,0):
        for k in range(-houseZ-90,houseZ+90):
            pass
            #setBlock(pos+Vec3.Vec3(i,j,k),block.DIRT.id, 3)

def BuildHouse(houseCenter,houseSize,mainMaterial):
    xSize=houseSize.x
    ySize=houseSize.y
    zSize=houseSize.z
    for i in range(-xSize,xSize+1):
        for j in range(ySize):
            setBlock(houseCenter+Vec3.Vec3(i,j,zSize),mainMaterial.id, 1)
            setBlock(houseCenter+Vec3.Vec3(i,j,-zSize),mainMaterial.id, 1)
    for i in range(-zSize,zSize+1):
        for j in range(ySize):
            setBlock(houseCenter+Vec3.Vec3(xSize,j,i),mainMaterial.id, 1)
            setBlock(houseCenter+Vec3.Vec3(-xSize,j,i),mainMaterial.id, 1)
    for i in range(-xSize,xSize+1):
        for j in range(-zSize,zSize+1):
            setBlock(houseCenter+Vec3.Vec3(i,ySize,j),block.AIR.id, 1)#top
            setBlock(houseCenter+Vec3.Vec3(i,0,j),mainMaterial.id, 1)#bottom
    halfX=int(xSize/2)
    halfY=int(ySize/2)
    halfZ=int(zSize/2)
    sizeWindow=int(ySize/3)
    for i in range(halfY-sizeWindow,halfY+1):
        for j in range(-1,2):
            setBlock(houseCenter+Vec3.Vec3(j,i,zSize),block.GLASS.id, 1)

material=[block.CLAY,block.STONE_BRICK,block.SANDSTONE,block.BEDROCK,block.COAL_ORE,block.IRON_BLOCK,block.IRON_ORE,block.GOLD_BLOCK,block.GOLD_ORE,block.DIAMOND_ORE,block.DIAMOND_BLOCK,block.LAPIS_LAZULI_BLOCK]

houseSize=Vec3.Vec3(9,9,8)
print(len(material))
index=0
for i in [-40,0,40]:
    for j in [-50,0,50]:
        for k in [0,20,40]:
            houseLoc=pos+Vec3.Vec3(i,k,j)
            BuildHouse(houseLoc,houseSize,material[index%12])
            index+=1


