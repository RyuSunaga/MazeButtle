

from gamemanager import GameManager
from packet import ClientToServerPacket, ServerToClientPacket 
from mazesocket import MazeServerSocketManager
from gameinfomanager import GameInfoManeger


##############################################################################################################

#命名規則について by sunaga

# file名　　　　　　　　全て小文字でなるべく短く　       myfile
# クラス名　　　　　　　最初大文字、大文字区切り　　　   ThisIsMyClass
# 関数名、メソッド名　　全小文字、アンダースコア区切り   this_is_my_func
# 変数名　　　　　　　　全小文字、アンダースコア区切り   this_is_my_val
# 定数名                全大文字、アンダースコア区切り　 THIS_IS_MY_CONST

# 自クラス内でのみ使用する内部変数と内部メソッドはアンダースコアで開始


##############################################################################################################


#test
#print(RIGHT)

#座標変換はこんな感じにすればミスが減ると思う 右へ移動の場合 by sunaga
#posi = [3,6]
#print("現在の座標",posi)

#posi[X] += RIGHT[X]
#posi[Y] += RIGHT[Y]
#print("右へ移動後の座標",posi)

##############################################################################################################









######################################デモ用のサーバーの情報
HOST = '127.0.0.1'
PORT = 50000
BACKLOG = 10
BUFSIZE = 4096
######################################

class MazeServer(sobject):
    '''
        ゲームのサーバー
        須永の集大成
        この中はきれいにまとめたい
    '''
    
    def __init__(self,HOST,PORT,BACKLOG,BUFSIZE):
        #ゲームの情報を管理するのに必要
        self.game_info_manager_ = GameInfoManeger()
        #ゲームの情報を通信用に整形するのに必要
        self.stcp_ = ServerToClientPacket()
        #通信に必要
        self.server_socket_manager = MazeServerSocketManager(HOST,PORT,BACKLOG,BUFSIZE)
        #まだ表示していないプレイヤーのIDとコマンドを保持
        self.player_command_data = []

    def start_up(self):
        '''
            ゲームサーバー起動
        '''
        pass






















