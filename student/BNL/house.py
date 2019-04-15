import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

mc = minecraft.Minecraft.create()
#pos = mc.player.getTilePos()
#mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

#原点
zerox = 98
zeroy = 34
zeroz = 43

bases = []
mat = [1, 17, 18, 19, 20, 21, 22, 24, 35,
       41, 42, 43, 47, 56, 57, 22, 80, 82,
       21, 24, 35, 43, 57, 80, 17, 18, 22]
number = 0

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

def build_house(x0, y0, z0, L = 10, W = 10, H = 10, M = 0):
    mat0 = 5
    mat1 = M
    mat2 = 0
    mat3 = 20
    #bottom
    for i in range(L):
        for j in range(W):
            mc.setBlock(x0 + i, y0, z0 +j, mat0)
            #mc.setBlock(x0 + i, y0 + 1, z0 +j, 50)
    #top
    for i in range(L):
        for j in range(W):
            mc.setBlock(x0 + i, y0 + H, z0 + j, 89)     
    #wall
    for i in range(H):
        for j in range(L):
            mc.setBlock( x0 + j, y0 + i, z0, mat1)
            mc.setBlock( x0 + j, y0 + i, z0 + W-1, mat1)
        for k in range(W):
            mc.setBlock( x0 , y0 + i, z0 + k, mat1)
            mc.setBlock( x0 + L-1, y0 + i, z0 + k, mat1)
    #window
    for i in range(3):
        for j in range(2):
            mc.setBlock( x0, y0 + H/2 + j, z0 + W/2 + i, mat3)
            mc.setBlock( x0 + L/2 + i, y0 + H/2 + j, + z0, mat3)
    #door
    mc.setBlock(x0 + L/2 , y0 + 1, z0, mat2)
    mc.setBlock(x0 + L/2 , y0 + 2, z0, mat2)
    mc.setBlock(x0 + L/2 , y0 , z0 - 1, mat1)
    mc.setBlock(x0 + L/2 -1 , y0 , z0 - 1, mat1)
    mc.setBlock(x0 + L/2 +1 , y0 , z0 - 1, mat1)

for row in range(3):
    for line in range(3):
        for high in range(3):
            bases.append([zerox + row*20, zeroy + line*20, zeroz + high*20,7 + row, 7 + line,4 + high, mat[number]])
            number = number + 1
for base in bases:
    build_house(base[0],base[1],base[2],base[3],base[4],base[5],base[6])

#清除房子
'''
for x in range(80):
    for y in range(80):
        for z in range(80):
            mc.setBlock(zerox + x , zeroy + y, zeroz + z, 0)

'''
def inwhichhouse(x, y, z):
    inhouse = []
    for base in bases:
        inhouse.append((x >= base[0] and x <= base[0] + base[3]) and (y >= base[1] and y <= base[1] + base[5]) and (z >= base[2] and z <= base[2] + base[4]))
    for number in range(27):
        if inhouse[number] :
            return number
        elif inhouse[number] == False and number == 26:
            return 100
while True:
    time.sleep(0.5)
    pos = mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    housenumber = inwhichhouse(pos.x, pos.y, pos.z)
    strnum = str(housenumber)
    
    if housenumber < 27:
        #ser.write(strnum.encode())  #插入com4后启用
        mc.postToChat('you are in the house '+str(housenumber))
        time.sleep(1)
    elif housenumber == 100:
        #ser.write(strnum.encode())  #插入com4后启用
        mc.postToChat('please enter a house')
        time.sleep(1)
    
    
