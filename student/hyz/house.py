import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

a=pos.x
b=pos.y
c=pos.z

material=[1,2,3,4,133,5/1,5/2,5/3,7,14,15,16,121,17/1,133,17/3,21,22,41,42,45,48,49,56,57,73,88]

tmp=0

def house(a, b ,c , L, W, H, M):
	for j in range(H):
		for i in range(W):
			if j>=1 and j<=3:
				if i>=int(W/2)-1 and i<=int(W/2):
					pass
				else:
					mc.setBlock(a+1+i, b+j, c+1, M)
			else:
				mc.setBlock(a+1+i, b+j, c+1, M)
			mc.setBlock(a+1+i, b+j, c+L, M)
			
		for k in range(L-2):
			if (k==int(L/2)-1 or k==int(L/2)-2) and (j==int(H/2) or j==int(H/2)-1):           
				pass
			else:				
				mc.setBlock(a+1, b+j, c+k+2, M)
				mc.setBlock(a+W, b+j, c+k+2, M)
	
	for i in range(W-2):                       			#底
		for k in range(L-2):
			mc.setBlock(a+2+i, b, c+2+k, M)
			
	for i in range(W-2):						#顶
		for k in range(L-2):
			mc.setBlock(a+2+i, b+H-1, c+2+k, M)
    
print([a,b,c])

for j in range(3):
	for i in range(3):
		for k in range(3):
			house(a+14*i, b+14*j, c+14*k, 10, 10, 10, material[tmp])
			tmp=tmp+1   
			
#origin : (189, 53, -160)
