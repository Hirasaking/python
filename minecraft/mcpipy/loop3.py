from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()

pos = mc.player.getTilePos() #現在地の座標取得

for i in range(5):
    #5*5のブロック設置
    #mc.setBlocks(pos.x, pos.y+i, pos.z, pos.x+4, pos.y+i, pos.z+4, STONE)

    #5*5の階段状ブロック設置
    mc.setBlocks(pos.x+i, pos.y+i, pos.z, pos.x+4, pos.y+i, pos.z+4, STONE)
