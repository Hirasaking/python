from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
mc.events.clearAll() #すべてのイベント削除

while True:
    pos = mc.player.getTilePos() #現在地の座標取得

    #チャットイベントの取得と処理
    for i in mc.events.pollChatPosts():

        #exitの入力で処理終了
        if i.message == "exit":
            mc.postToChat("stop")
            exit()
        #woodの入力で処理の実行
        elif i.message == "wood":
            mc.setBlock(pos.x, pos.y, pos.z, CARPET_WHITE)
            mc.setBlock(pos.x-1, pos.y, pos.z, CARPET_WHITE)
            mc.setBlock(pos.x-2, pos.y, pos.z, CARPET_WHITE)
