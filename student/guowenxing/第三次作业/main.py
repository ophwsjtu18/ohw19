import mcpi.minecraft as minecraft
from house import create_house, in_which_house, rc_to_house
import serial
from time import sleep 
### 打开端口
port = serial.Serial(port="/dev/ttyUSB0")
sleep(1)
###创建房子
mc = minecraft.Minecraft.create()
pose = mc.player.getPos()
x, y, z = pose.x+3, pose.y+3, pose.z+3
house_pose = create_house(x, y, z, mc)
#划分房子区域
xset = set()
yset = set()
zset = set()
for i in house_pose:
    xset.add(i[0])
    yset.add(i[1])
    zset.add(i[2])
##房子的区域
domain  = [list(xset), list(yset),  list(zset)]
create_domain = lambda x : x+[i+8 for i in x]
domain = [create_domain(i) for i in domain]
for i in domain:
    i.sort()
while 1:
    pose = mc.player.getPos()
    r_c = in_which_house(pose, domain)
    port.write(str(rc_to_house(r_c)).encode())
    print(rc_to_house(r_c))
    sleep(1)