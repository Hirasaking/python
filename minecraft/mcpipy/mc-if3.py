from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos() #現在地の座標取得

for posX in range(100):
    for posZ in range(100):
        for posY in range(100):
        #プレイヤーと同じ高さにあるブロック取得
            blockType = mc.getBlock(pos.x+posX, pos.y+posY, pos.z+posZ)
            #置き換えたいブロックの判定 木→ブロック
            if blockType == 17:
                mc.setBlock(pos.x+posX, pos.y+posY, pos.z+posZ, WOOD_PLANKS)
            #置き換えたいブロックの判定　葉→雪
            elif blockType == 18:
                mc.setBlock(pos.x+posX, pos.y+posY, pos.z+posZ, SNOW_BLOCK)
