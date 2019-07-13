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
from config import MAZE_LIST
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import CLIENT_TO_SERVER_PACKET
from config import RED, BLUE, GREEN, YELLOW
from config import PACKET_TYPE, PLAYER_ID, PLAYER_NAME, PLAYER_COLOR, PLAYER_HP, POSI, MAZE, PLAYER_INFO_LIST, BULLET_INFO_LIST, ITEM_INFO_LIST, TURN, TEXT
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
HOST = '127.0.0.1'
PORT = 50000
BACKLOG = 10
BUFSIZE = 4096
#ctss = MazeClientSocketManager(HOST,PORT,BACKLOG,BUFSIZE)
#ctss.set_send_data("送りたい情報")
#ctss.transmission()
############################################

class MazeClient(object):

    def __init__(self,HOST,PORT,BACKLOG,BUFSIZE):
        self.HOST_ = HOST
        self.PORT_ = PORT
        self.BACKLOG_ = BACKLOG
        self.BUFSIZE_ = BUFSIZE
        self.maze_field_ = None
        self.ctsp_ = None
        self.maze_client_socket_manager_ = MazeClientSocketManager(
                                self.HOST_,
                                self.PORT_,
                                self.BACKLOG_,
                                self.BUFSIZE_
                                )
        #これはサーバーから受け取ったデータが格納される
        #self.game_info_data = None

        self.game_info_data = {PACKET_TYPE: CLIENT_TO_SERVER_PACKET,
                                TEXT: "のこり一週間頑張ろう!!!!!",
                                MAZE: MAZE_LIST[1],
                                TURN: 5,
                                PLAYER_HP: 5,  # これはidを見てこのクラスを保持しているクラスのplayer_idと一致するplayerのhpを入れる
                                PLAYER_INFO_LIST: [{PLAYER_ID: 1, PLAYER_NAME: "Gaia", PLAYER_COLOR: RED, POSI: [0, 0]},
                                                   {PLAYER_ID: 2, PLAYER_NAME: "Nojima",PLAYER_COLOR: BLUE, POSI: [9, 9]},
                                                   {PLAYER_ID: 3, PLAYER_NAME: "Sunaga", PLAYER_COLOR: YELLOW, POSI: [0, 9]}],
                                BULLET_INFO_LIST: [{POSI: [0, 2]}, {POSI: [4, 9]}, {POSI: [8, 1]}, {POSI: [9, 6]}],
                                ITEM_INFO_LIST: []
                                }

        #このクライアントが扱うプレイヤーのidを持つ
        self.player_id_ = None
        self.next_command_ = None
        self.player_hp_=None
        self.player_info_list_=None
        self.bullet_info_list_=None
        self.socket_=None
        self.text_=None

    #サーバからのソケット取得、及びデコードによりgame_info_data_更新
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

    #ここの処理がわからない
    def set_player_id(self):
        #self.player_id_= self.game_info_data[PLAYER_INFO_LIST]
        self.player_id_=1

    def set_player_hp(self):
        self.player_hp_= self.game_info_data[PLAYER_HP]

    def set_player_info_list(self):
        self.player_info_list_= self.game_info_data[PLAYER_INFO_LIST]

    def set_bullet_info_list_(self):
        self.bullet_info_list_= self.game_info_data[BULLET_INFO_LIST]

    def set_maze_field(self):
        self.maze_field_=self.game_info_data[MAZE]

    def set_text(self):
        self.text_=self.game_info_data[TEXT]

    def get_game_info_data(self):
        return self.game_info_data

    def get_player_id(self):
        packet.ClientToServerPacket().set_player_id(self.player_id_)

    def get_maze_field(self):
        return self.maze_field_

    def send(self):
        self.maze_client_socket_manager_.set_send_data(
            self.ctsp_)
        self.maze_client_socket_manager_.transmission()


#以下本処理

mazeclient = MazeClient(HOST,PORT,BACKLOG,BUFSIZE)
#mazeclient.listen()

mazeclient.set_player_id()
mazeclient.set_player_hp()
mazeclient.set_maze_field()
mazeclient.set_player_info_list()
mazeclient.set_bullet_info_list_()

maze_object=mazefield.MazeField(mazeclient.set_text(),mazeclient.get_game_info_data())

maze_object.move_player()
maze_object.attack_player()
maze_object.create_maze(mazeclient.get_maze_field())
