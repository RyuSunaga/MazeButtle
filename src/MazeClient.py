import config
import socket
import select
import threading
import info
import packet
from info import PlayerInfo
from packet import ClientToServerPacket, ServerToClientPacket
from mazesocket import MazeClientSocketManager
import mazefield

########################################################
#テストのため
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
########################################################

##############################################################################################################

#命名規則について by sunaga

# file名　　　　　　　　全て小文字でなるべく短く　   myfile
# クラス名　　　　　　　最初大文字、大文字区切り　　　   ThisIsMyClass
# 関数名、メソッド名　　全小文字、アンダースコア区切り   this_is_my_func
# 変数名　　　　　　　　全小文字、アンダースコア区切り   this_is_my_val
# 定数名                全大文字、アンダースコア区切り　 THIS_IS_MY_CONST

# 自クラス内でのみ使用する内部変数と内部メソッドはアンダースコアで開始


##############################################################################################################


####################################Socketの使い方参考にして
C_HOST = '127.0.0.1'
C_PORT = 50000
C_BACKLOG = 10
C_BUFSIZE = 4096
#ctss = MazeClientSocketManager(HOST,PORT,BACKLOG,BUFSIZE)
#ctss.set_send_data("送りたい情報")
#ctss.transmission()
############################################

class MazeClient(object):

    def __init__(self,player_name,HOST,PORT,BACKLOG,BUFSIZE):
        self.HOST_ = HOST
        self.PORT_ = PORT
        self.BACKLOG_ = BACKLOG
        self.BUFSIZE_ = BUFSIZE
        self.maze_field_ = None
        self.ctsp_ = None
        self.player_id_ = None
        self.player_next_command_ = None
        self.player_name_ = player_name
        self.server_to_client_message_ = None 
        #最初のコマンドをサーバーに送信したかどうか
        self.is_send_first_command_ = False
        self.maze_client_socket_manager_ = MazeClientSocketManager(HOST,PORT,BACKLOG,BUFSIZE)
        self.ctsp_ = ClientToServerPacket()
        #クライアントがサーバー側に渡すデータを格納する
        self.str_player_command_data_ = None
        #これはサーバーから受け取ったデータが格納される
        self.game_info_data = None

        print(self.player_name_,"クライアントの情報を生成しました。")

    def first_connect(self):
        '''
            サーバーとの最初の通信を行う
        '''
        if(self.is_send_first_command_ == True):
            print("もう最初の通信は終わりましたよ")
        else:
            print("最初の通信を行います。")
            self.player_next_command_ = JOIN
            self.create_send_data()
            self.maze_client_socket_manager_.set_send_data(self.str_player_command_data_)
            print("クライアント側からサーバー側に送信する情報をセットしました。")
            self.maze_client_socket_manager_.transmission()
            print("最初の通信を終了します。")

    def create_send_data(self):
        '''
            サーバー側に送るデータを取得する
        '''
        self.ctsp_.set_host(self.HOST_)
        self.ctsp_.set_port(self.PORT_)
        self.ctsp_.set_player_id(self.player_id_)
        self.ctsp_.set_player_name(self.player_name_)
        self.ctsp_.set_next_command(self.player_next_command_)
        self.ctsp_.set_text(self.server_to_client_message_)
        self.str_player_command_data_ = self.ctsp_.info_to_dict()
        print("クライアントからサーバーに渡すデータを生成しました。")
    
    #ここの処理がわからない -> 悪い野島これは須永のミス
    def set_player_id(self,id):
        #self.player_id_= self.game_info_data[PLAYER_INFO_LIST]
        self.player_id_ = id 

    def get_game_info_data(self):
        return self.game_info_data

    def get_player_id(self):
        return self.player_id_

    
    #サーバからのソケット取得、及びデコードによりgame_info_data_更新
    #まだ使うか謎
    def listen(self):
        self.socket_=MazeClientSocketManager(self.HOST_, self.PORT_,
                                self.BACKLOG_, self.BUFSIZE_).create_socket_2()
        try:
            self.socket_.connect((self.HOST_,self.PORT_))
            self.game_info_data = self.socket_.recv()
        except Exception as e:
            print(e)
        finally:
            self.socket_.close()
            print("サーバとの通信終了")




#以下本処理
print("HOSTとかPORTとかが変な動きするかも")
player_command_data = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Nojima",NEXT_COMMAND:JOIN,TEXT:""},
                       {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Gaia",NEXT_COMMAND:JOIN,TEXT:""},
                       {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Sunaga",NEXT_COMMAND:JOIN,TEXT:""}]
     



#########################TEST#####################
test_name = 'Ryu'
MC = MazeClient(test_name,C_HOST,C_PORT,C_BACKLOG,C_BUFSIZE)
MC.first_connect()

#########################TEST#####################

















