import serial
import serial.tools.list_ports
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "CH340" in p[1]:
        ser = serial.Serial(port=p[0])
        print('Connectect to', p[0])
        break
    else:
        print("No Device found")
time.sleep(2)
mc = minecraft.Minecraft.create()
def checkRoom():
    pos = mc.player.getTilePos()#player location
    x=pos.x#-54 - -38   #-14 - 8  #26-42  

    y=pos.y#21 - 27  #41 -47   # 61-67

    z=pos.z#106 -92  #56 - 42   #6 -  -8
    
    xRange=[-54,-38,-14,2,26,42]
    yRange=[21,27,41,47,61,67]
    zRange=[106,92,56,42,6,-8]
    zRange.reverse()

    xLoc=9
    yLoc=9
    zLoc=9
    for i in range(3):
        if x>=xRange[i*2] and x<=xRange[i*2+1]:
            xLoc=i
            break
    for i in range(3):
        if y>=yRange[i*2] and y<=yRange[i*2+1]:
            yLoc=i
            break
    for i in range(3):
        if z>=zRange[i*2] and z<=zRange[i*2+1]:
            zLoc=i
            break
    print([x,y,z])
    print([xLoc,yLoc,zLoc])

    if xLoc!=9 and yLoc!=9 and zLoc!=9:
        message=zLoc*9+yLoc*3+xLoc
        byteData=bytes([message])
        ser.write(byteData)
        ser.flush()
        print(message)
    time.sleep(1)
while 1:
    checkRoom()
