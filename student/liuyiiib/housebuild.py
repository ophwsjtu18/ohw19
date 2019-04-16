import mcpi.minecraft  as  minecraft
import mcpi.block    as  block
import serial
import serial.tools,list_ports
import time
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()


def  house(x0,y0,z0,l,w,h,m1):
    for  i  in  range(l):
        for  j  in  range(w):
            for   k  in  range(h):
                mc.setBlock(x0+a,y0+b,z0+c,m1)
    for   i  in  range(l-2):
        for    j   in  range(w-2):
            for   k   in  range(h-1):
                mc.setBlock(x0+a+1,y0+b+1,z0+c,0)
    for  i  in  range(l+1):
        for  j  in  range(w+1):
            mc.setBlock(x0+i,y0-1,z0+j,20)
    for  i  in  range(h):
        for   j  in  range(w):
            mc.setBlock(x0,y0+i,z0+j,m1)
    for i in range(3):
        for j in range(2):
            mc.setBlock( x0, y0 + h/2 + j, z0 + w/2 + i, 20)
            mc.setBlock( x0 + l/2 + i, y0 + h/2 + j, + z0, 20)
    for  i  in  range(l):
        for   j   in  range(w):
            mc.setBlock(x0+i,y0+h,z0+j,20)
    for  i in  range(1,3):
        x1=int((2*x0+l)/2)
        mc.setBlock(x1,y0+i,z0,0)
    
num=0
row=(10,30,60)
a=random.randint(6,10)
b=random.randint(6,10)
c=random.randint(6,10)
for  i  in  row:
    for  j   in  row:
        for  k   in   row:
            house(0+i,0+j,0+k,a,b,c,Material[num])
            num+=1

x0=0
y0=0
z0=0
def   inthehouse(x,y,z):
    if(x<=x0+l and x>=x0)and(y<=y0+h and  y>=y0)and(z<=z0+w and  z>=z0):
        return  True
    return   False
while  True:
    time.sleep(1)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    bool_pos=inthehouse(pos.x,pos.y,pos.z)
    if bool_pos :
        mc.postToChat("welcome home")
        ser.write("y".encode())
        time.sleep(2)
    else :
        mc.postToChat("you are not in a house")
