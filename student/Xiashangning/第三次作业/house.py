import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print(ports)
ser = None

for p in ports:
    print(p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
        ser = serial.Serial(port=p[0])
    else:
        print("No Arduino Device was found connected to the computer")
        exit()

mc = minecraft.Minecraft.create()
locs = []


def build_house(px, py, pz):
    for y in range(-1, 6):
        for x in range(-6, 6):
            for z in range(-6, 6):
                mc.setBlock(px + x, py + y, pz + z, block.AIR.id)
    for y in range(-1, 5):
        for x in range(-5, 5):
            for z in range(-5, 5):
                if y == -1:
                    mc.setBlock(px + x, py + y, pz + z, block.WOOD_PLANKS.id)
                elif y == 4:
                    mc.setBlock(px + x, py + y, pz + z, block.STONE.id)
                else:
                    if z == -5 or z == 4 or x == -5 or x == 4:
                        mc.setBlock(px + x, py + y, pz + z, block.BRICK_BLOCK.id)
    mc.setBlock(px - 5, py + 1, pz, block.AIR.id)
    mc.setBlock(px - 5, py, pz, block.AIR.id)
    mc.setBlock(px + 4, py + 1, pz, block.GLASS.id)
    mc.setBlock(px + 4, py + 1, pz - 1, block.GLASS.id)
    mc.setBlock(px, py + 1, pz - 5, block.GLASS.id)
    mc.setBlock(px, py + 1, pz + 4, block.GLASS.id)
    locs.append([px, py, pz])


def build_houses(pos):
    for y in range(3):
        for x in range(3):
            for z in range(3):
                build_house(pos.x + 13 * x, 4 * y, pos.z + 13 * z)


def in_room(pos):
    cnt = 0
    x = pos.x
    y = pos.y
    z = pos.z
    for l in locs:
        if (l[0] - 5) <= x <= (l[0] + 4) and l[1] <= y <= (l[1] + 4) and (l[2] - 5) <= z <= (l[2] + 4):
            return cnt
        cnt += 1
    return -1


pos = mc.player.getTilePos()
build_houses(pos)
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    num = in_room(pos)
    print(pos)
    if num is not -1:
        print("在第" + str(num) + "间")
        ser.write(str(num).encode())
        print("send ok")
