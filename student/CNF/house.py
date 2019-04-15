import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time


mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

def house(x0, y0, z0, L, W, H, M1, M2, M3):
    #wall_1
    for i in range(L):
        for j in range(H):
            mc.setBlock(x0 + i, y0+j, z0, M1)

    #floor
    for i in range(L+1):
        for j in range(W+1):
            mc.setBlock(x0+i, y0-1, z0+j, M2)

    #wall_2
    for i in range(H):
        for j in range(W):
            mc.setBlock(x0, y0+i, z0+j, M1)

    #wall_window
    for i in range(H):
        for j in range(W+1):
             if i >2 and i <6:
                if j > W/2 - 2 and j < W/2 + 2:
                    mc.setBlock(x0+L, y0+i, z0+j, 20)
                else:
                     mc.setBlock(x0+L, y0+i, z0+j, M1)
             else:
                 mc.setBlock(x0+L, y0+i, z0+j, M1)
           
                

    #wall_door
    for i in range(L):
        for j in range(H):
            if i > L/2 - 2 and i < L/2 + 2:
                if j < H/2:
                    mc.setBlock(x0+i, y0+j, z0+W, 0)
                else:
                    mc.setBlock(x0+i, y0+j, z0+W, M1)
            else:
                mc.setBlock(x0+i, y0+j, z0+W, M1)

    #ceiling
    for i in range(H+1):
        for j in range(W+1):
                mc.setBlock(x0+i, y0+H, z0+j, M3)


k=0

for i in range(3):
    for j in range(3):
        for k in range(3):
            house(-100+15*i, 16 + 15*k , 250+15*j, 6+i, 7+i,8+i, i+21, j+21, k+22)
            

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

time.sleep(2)

stayed_time = 0
while True:
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if pos.x < -100+15*i + 6 + i and pos.x > -100 + 15*i and pos.z < 250+15*j + 8 + i and pos.z > 250 + 15*j and pos.y < 15 + 15*k + 7 + i and pos.y > 15 + 15*k:
                    print(stayed_time)
                    stayed_time=stayed_time+2
                    time.sleep(1)
                   
                    if stayed_time > 15:
                        m = i*10 + j
                        ser.write(str(m).encode())
                       
                        print(m,"send")
                        stayed_time = 0
                        time.sleep(1)
            
                   
               
              
            




