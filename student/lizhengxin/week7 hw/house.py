'''
本次作业是我与布乃龙同学合作完成，他在过程中给予了我很大帮助，在此表示感谢，同时，我会好好努力，争取早日实现完全独立完成作业的目标'''
import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time
mc =minecraft.Minecraft.create()
pos=mc.player.getTilePos()
bases=[]
#利用welcomehome.py获得坐标
fixed_x=829
fixed_y=93
fixed_z=274

def house(x,y,z,L,W,H,material):
#地基
    for i in range(L):
            for j in range(W):
                mc.setBlock(x+i,y,z+j,material)
#屋顶
    for i in range(L):
            for j in range(W):
                mc.setBlock(x+i,y+H,z+j,material)
#墙

    for k in range(H):
            
            for m in range(L):
                
                mc.setBlock(x+m,y+k,z,material+2)
                mc.setBlock(x+m,y+k,z+W,material+2)

            for n in range(W):
                mc.setBlock(x,y+k,z+n,material+1)
                mc.setBlock(x+L,y+k,z+n,material+1)
#窗
    for i in range(3):
        for j in range(3):
            mc.setBlock( x, y + H/2 + i, z + W/2 + j, 0)
#门

    mc.setBlock(x + L/2 , y + 1, z, 0)
    mc.setBlock(x + L/2 , y + 2, z, 0)
    mc.setBlock(x + L/2 , y , z - 1, 0)
    mc.setBlock(x + L/2 -1 , y , z - 1, 0)
    mc.setBlock(x + L/2 +1 , y , z - 1, 0)
      

    
#造27个房屋
m=0
materials = [1, 17, 18, 19, 20, 21, 22, 24, 35,
       41, 42, 43, 47, 56, 57, 22, 80, 82,
       21, 24, 35, 43, 57, 80, 17, 18, 22]
for i in range(3):
    for j in range(3):
        for k in range(3):
            bases.append([fixed_x + i*20, fixed_y + j*20, fixed_z+k*20,6+i,6+j,3+k, materials[m]])
            m=m+1
            
        
            
                
            
            
for base in bases:
    house(base[0],base[1],base[2],base[3],base[4],base[5],base[6])

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])

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
    housenum = inwhichhouse(pos.x, pos.y, pos.z)
    housenumber=str(housenum)
    if housenum < 27:
        ser.write(housenumber.encode())
        mc.postToChat('you are in the house '+(housenumber))
        time.sleep(1)
    elif housenum == 100:
        ser.write(housenumber.encode())
        mc.postToChat('please enter a house')
        time.sleep(1)


    
    
    
