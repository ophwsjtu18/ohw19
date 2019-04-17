

import mcpi.minecraft as minecraft
import mcpi.block as block


mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
def house(x0,y0,z0,L,W,H,M):
    pos.x=x0
    pos.y=y0
    pos.z=z0
    House_W=range(1,W+1)
    House_H=range(H)
    House_L=range(L)
    for i in House_W:
        for j in House_H:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,45)
            mc.setBlock(pos.x+L-1,pos.y+j,pos.z+i,45)
            if i==1 or i==10:
                for m in House_L:
                    mc.setBlock(pos.x+m,pos.y+j,pos.z+i,45)
    mc.setBlock(pos.x,pos.y,pos.z+round(W/2),0)
    mc.setBlock(pos.x,pos.y+1,pos.z+round(W/2),0)

    wind1=range(2,H-1)
    wind2=range(2,L-1)
    for i in wind2:
        for j in wind1:
            mc.setBlock(pos.x+i,pos.y+j,pos.z+1,20)
            mc.setBlock(pos.x+i,pos.y+j,pos.z+W,20)
    for i in House_H:
        for j in House_W:
            mc.setBlock(pos.x+i,pos.y+H+1,pos.z+j,80)
            mc.setBlock(pos.x+i,pos.y+H,pos.z+j,80)
            mc.setBlock(pos.x+i,pos.y-1,pos.z+j,5)

a=range(0,60,20)
for i in a:
    for j in a:
        for m in a:
            house(-60+i,85+j,-60+m,10,10,10,45)


