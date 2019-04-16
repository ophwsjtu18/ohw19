import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

def main():
    mc=minecraft.Minecraft.create()
    pos=mc.player.getTilePos()
    k=0
    def buildding(x0, y0, z0, L , W , H, M1,M2,M3):
        glass = 20
        #bottom
        for i in range(L):
            for j in range(W):
                mc.setBlock(x0 + i, y0, z0 +j, M1)
        #ceiling
        for i in range(L):
            for j in range(W):
                mc.setBlock(x0 + i, y0 + H, z0 + j, M2)     
        #wall
        for i in range(H):
            for j in range(L):
                mc.setBlock( x0 + j, y0 + i, z0,M3)
                mc.setBlock( x0 + j, y0 + i, z0 + W-1,M3)
            for k in range(W):
                mc.setBlock( x0 , y0 + i, z0 + k,M3)
                mc.setBlock( x0 + L-1, y0 + i, z0 + k,M3)
        #window
        for i in range(3):
            for j in range(2):
                mc.setBlock( x0, y0 + H/2 + j, z0 + W/2 + i,glass)
                mc.setBlock( x0 + L/2 + i, y0 + H/2 + j, + z0,glass)
        #door
        for i in range(L):
            for j in range(H):
                if i > L/2 - 2 and i < L/2 + 2:
                    if j < H/2:
                        mc.setBlock(x0+i, y0+j, z0+W-1, 0)
                    else:
                        mc.setBlock(x0+i, y0+j, z0+W-1, M3)
                else:
                    mc.setBlock(x0+i, y0+j, z0+W, M3)


    for i in range(3):
        for j in range(3):
            for k in range(3):
                buildding(-72+15*i, 32 + 15*k , 144+15*j,10,10,10, i+1, j+2, k+3)
                


    ports = list(serial.tools.list_ports.comports())


    for p in ports:
        print (p[1])
        if "SERIAL" in p[1]:
            ser=serial.Serial(port=p[0])
        else :
            print ("Not found")

    time.sleep(2)
    stayed_time = 0
    while True:
        pos=mc.player.getTilePos()
        mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if pos.x < -72+15*i + 10 and pos.x > -72 + 15*i and pos.z < 250+15*j + 8 + i and pos.z > 250 + 15*j and pos.y < 15 + 15*k + 7 + i and pos.y > 15 + 15*k:
                        print(stayed_time)
                        stayed_time=stayed_time+2
                        time.sleep(1)
                   
                        if stayed_time > 15:
                            m = i*10 + j+k
                            ser.write(str(m).encode())
                            mc.postToChat("you have entered the house!")
                            print(m,"send")
                            stayed_time = 0
                            time.sleep(1)






if __name__ == '__main__':
  main()