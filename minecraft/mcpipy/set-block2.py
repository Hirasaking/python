from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

#5つのブロックをX座標を基準に並べる
mc.setBlock(pos.x, pos.y, pos.z, STONE)
mc.setBlock(pos.x+1, pos.y, pos.z, TNT)
mc.setBlock(pos.x+2, pos.y, pos.z, LAVA)
mc.setBlock(pos.x+3, pos.y, pos.z, LAVA)
mc.setBlock(pos.x+4, pos.y, pos.z, LAVA)
