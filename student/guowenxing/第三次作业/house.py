import mcpi.block as block
import bisect

def _house(x,y,z,mc):
    """房子空间内可有对角俩个点确定，(x+1,y+1,z+1), (x+9, y+9, z+9)"""
    for i in range(10):
        for j in range(10):
            for k in range(10):
                mc.setBlock(x+i, y+j, z+k, block.STONE.id)

    for i in range(8):
        for j in range(8):
            for k in range(8):
                mc.setBlock(x+1+i, y+1+j, z+1+k , block.AIR.id)
    #door
    for i in range(4):
        mc.setBlock(x+4, y+i, z, block.AIR.id)
        mc.setBlock(x+5, y+i, z, block.AIR.id)

    #windows
    mc.setBlock(x+10, y+5, z+5, block.AIR.id)
    return (x, y, z)

def create_house(x, y, z, mc):
    """
    创建房子阵列
    (x,y,z)为房子阵列的最左下角坐标
    """
    every_house_pose = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                every_house_pose.append(_house(x+i*15, y+j*15,z+k*15,mc))

    return every_house_pose


def in_which_house(pose, domain):
    """
    判断位置是否在房子内
    先对位置分类，然后返回位置
    """
    place = [bisect.bisect(domain[0],pose.x), bisect.bisect(domain[1], pose.y), bisect.bisect(domain[2], pose.z)]
    if not (all([i%2 for i in place])):
        return [0,0,0]
    return place

def rc_to_house(place):
    """
    将房子的点映射到1~27个房子中
    """
    if not any(place):
        return 0
    place_ = [(i+1)/2 for i in place]
    return int((place_[0]-1)*9+(place_[1]-1)*3+place_[2])