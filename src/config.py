#### 他ファイルで変更されないように定数(値が変わらない変数)はconfig.py内で 
#### 定義します。値を使いたくなったらimportをして使うようにしてください。 by sunaga




#壁は定数を用意する　－＞　見やすくなるから
#通路も定数を用意したかったがよい変数名がなかったのでとりあえず保留 by sunaga
#壁
W = 1 
#弾丸
B = 2
#プレイヤー
P = 3 
#アイテム
I = 4

#### 迷路を定義->みんなでひとつずつ迷路を定義してくれ by sunaga
#### 1が壁 0が通路　
#### 10x10以上がいいなー
#### 4隅は0固定で頼む!!!! -> プレイヤーを置くから by sunaga

#野島が作る迷路
NOJIMA_MAZE = [
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,W,W,W,0,W,0,W,W,W,0],
                [0,W,0,0,0,W,0,0,0,W,0],
                [0,W,0,W,0,W,0,W,0,W,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,W,W,W,0,W,0,W,W,W,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,W,0,W,0,W,0,W,0,W,0],
                [0,W,0,0,0,W,0,0,0,W,0],
                [0,W,W,W,0,W,0,W,W,W,0],
                [0,0,0,0,0,0,0,0,0,0,0]
               ]


#ガイアが作る迷路
GAIA_MAZE = [
             [P,0,0,0,0,0,W,W,0,0],
             [0,W,0,0,W,0,0,0,0,0],
             [0,W,0,0,W,W,W,0,W,0],
             [0,W,0,0,W,0,0,0,W,0],
             [B,W,0,0,0,0,0,W,W,0],
             [0,0,W,W,W,0,0,W,0,0],
             [0,0,0,0,0,0,0,0,0,B],
             [0,W,0,W,W,W,W,W,W,0],
             [0,W,W,W,0,W,0,0,W,0],
             [0,0,0,0,0,0,0,0,W,P]
             ]


#須永が作る迷路  ->  壁をWにするとマップ見やすくない？
SUNAGA_MAZE = [
                [0,W,W,0,0,W,0,0,0,0],
                [0,0,0,0,0,0,0,W,0,0],
                [0,W,0,0,W,0,0,0,0,W],
                [0,W,0,0,0,0,W,0,0,0],
                [0,0,0,W,0,0,W,0,W,0],
                [W,W,0,0,W,0,W,0,W,0],
                [0,0,0,0,0,0,W,0,0,W],
                [0,W,W,W,0,0,0,0,0,0],
                [0,0,0,0,0,0,W,0,W,0],
                [0,0,W,0,W,0,0,0,0,0]
               ]

#みんなで作った迷路を格納します
MAZE_LIST = [NOJIMA_MAZE, GAIA_MAZE, SUNAGA_MAZE]

#座標は定数にして扱った方がミスが減るので固定しておく。
#例　posi = [2,3]
# x = posi[0], y = posi[1] より
# x = posi[X], y = posi[Y] の方が分かりやすい
X = 0
Y = 1


############################# 方向定義 ##########################
RIGHT  = (1,0)
LEFT   = (-1,0)
UP     = (0,1)
DOWN   = (0,-1)
############################# 方向定義 ##########################


#Playerの色設定
RED = 'red'
GREEN = 'green'
BLUE = 'blue'
YELLOW = 'yellow'
COLORS = [RED, GREEN, BLUE, YELLOW]



# Playerが選択するコマンド一覧

#参加コマンド
JOIN = "JOIN"

#行動コマンド
MOVE = "MOVE"
RIGHT_MOVE = "RIGHT_MOVE"
LEFT_MOVE = "LEFT_MOVE"
UP_MOVE = "UP_MOVE"
DOWN_MOVE = "DOWN_MOVE"

#攻撃コマンド
ATTACK = "ATTACK"
RIGHT_ATTACK = "RIGHT_ATTACK"
LEFT_ATTACK = "LEFT_ATTACK"
UP_ATTACK = "UP_ATTACK"
DOWN_ATTACK = "DOWN_ATTACK"
############################################



#プレイヤーからgamemanagerに送りBulletInfoオブジェクトを作成してもらう
CREATE_BULLET = "CREATE_BULLET"
##############################################


def get_direct_str(COMMAND):
    '''
        与えられたコマンドに対応する方向を文字列で返す
    '''
    if(COMMAND == (1,0)):
        return "RIGHT"
    elif(COMMAND == (-1,0)):
        return "LEFT"
    elif(COMMAND == (0,1)):
        return "UP"
    elif(COMMAND == (0,-1)):
        return "DOWN"
    else:
        return None


########################################################################迷路上のオブジェクトの定数設定######################################
OBJECT_INFO = "ObjectInfo"
PLAYER_INFO = "PlayerInfo"
BULLET_INFO = "BulletInfo"
ITEM_INFO = "ItemInfo"
########################################################################迷路上のオブジェクトの定数設定######################################



########################################################################オブジェクト管理の定数設定######################################
OBJECT_INFO_MANAGER = "ObjectInfoManager"
PLAYER_INFO_MANAGER = "PlayerInfoManager"
BULLET_INFO_MANAGER = "BulletInfoManager"
ITEM_INFO_MANAGER = "ItemInfoManager"
########################################################################オブジェクト管理の定数設定######################################


########################################################################パケットオブジェクトの定数設定######################################
PACKET = "PACKET"
SERVER_TO_CLIENT_PACKET = "SERVER_TO_CLIENT_PACKET"
CLIENT_TO_SERVER_PACKET = "CLIENT_TO_SERVER_PACKET"
########################################################################パケットオブジェクトの定数設定######################################














###################################データのやり取りで扱う辞書の定数


PACKET_TYPE = "PACKET_TYPE"
NEXT_COMMAND = "NEXT_COMMAND"
PLAYER_ID = "PLAYER_ID"
