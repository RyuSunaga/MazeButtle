from gamemanager import GameManager
from packet import ClientToServerPacket, ServerToClientPacket 
from gameinfomanager import GameInfoManager
from mazesocket import MazeServerSocketManager
from config import HOST,PORT
from config import MAZE_LIST
from config import JOIN
from config import RED, BLUE, GREEN, YELLOW
from config import JOIN, MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import PACKET_TYPE, PLAYER_ID, PLAYER_NAME, PLAYER_COLOR, PLAYER_HP, PLAYER_POSI,BULLET_POSI,MAZE, PLAYER_INFO_LIST, BULLET_INFO_LIST, ITEM_INFO_LIST, TURN,TEXT,NEXT_COMMAND
from config import CLIENT_TO_SERVER_PACKET, SERVER_TO_CLIENT_PACKET


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

class MazeServer(object):
    '''
        ゲームのサーバー
        須永の集大成
        この中はきれいにまとめたい
    '''
    
    def __init__(self,HOST,PORT,BACKLOG,BUFSIZE):
        #ゲームの情報を管理するのに必要
        self.game_info_manager_ = GameInfoManager()
        self.game_info_ = None
        #ゲームの情報を通信用に整形するのに必要
        self.stcp_ = ServerToClientPacket()
        #通信に必要
        self.server_socket_manager = MazeServerSocketManager(HOST,PORT,BACKLOG,BUFSIZE)
        
        
        #まだ実行していないプレイヤーのIDとコマンドを保持
        #クライアントが完成するまではとりあえず以下のデータを使う。
        #参加コマンド用のテスト
        self.player_command_data = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Nojima",NEXT_COMMAND:JOIN,TEXT:""},
                                    {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Gaia",NEXT_COMMAND:JOIN,TEXT:""},
                                    {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Sunaga",NEXT_COMMAND:JOIN,TEXT:""}]
        #移動コマンド用のテスト
        #self.player_command_data = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:1,PLAYER_NAME:"Nojima",NEXT_COMMAND:RIGHT_MOVE,TEXT:""},
        #                            {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:2,PLAYER_NAME:"Gaia",NEXT_COMMAND:DOWN_MOVE,TEXT:""},
        #                            {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:3,PLAYER_NAME:"Sunaga",NEXT_COMMAND:UP_MOVE,TEXT:""}]

        #弾丸生成用のテスト
        #self.player_command_data = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:1,PLAYER_NAME:"Nojima",NEXT_COMMAND:RIGHT_ATTACK,TEXT:""},
        #                            {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:2,PLAYER_NAME:"Gaia",NEXT_COMMAND:DOWN_ATTACK,TEXT:""},
        #                            {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:3,PLAYER_NAME:"Sunaga",NEXT_COMMAND:UP_ATTACK,TEXT:""}]


    def up_date_game_info_manager(self):
        '''
            クライアントから受け取ったデータをもとにself.game_info_manager_更新する。
        '''
        self.game_info_manager_.set_client_to_server_data(self.player_command_data)



##########################################TEST##############################################################
def test1():
    '''
        クライアントからの情報が無事にGameInfoManager()に渡されるのかのテスト
    '''
    print("TEST1")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.up_date_game_info_manager()
    print(MS.game_info_manager_.get_client_to_server_data())

def test2():
    '''
        JOINコマンドを無事に実行できたかをテスト
        正常に実行されるとクライアントに渡される情報をが生成される。
    '''
    print("TEST2")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.up_date_game_info_manager()
    MS.game_info_manager_.up_date_game()
    game_info = MS.game_info_manager_.get_game_info()
    print(game_info.get_maze())
    MS.stcp_.set_game_info(game_info)
    send_data = MS.stcp_.get_send_data()
    print(send_data)
##########################################TEST##############################################################


test2()







