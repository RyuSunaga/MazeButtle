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
import tkinter as tk

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
        self.game_info_data_ = {PACKET_TYPE: CLIENT_TO_SERVER_PACKET,
                                TEXT: "のこり一週間頑張ろう!!!!!",
                                MAZE: MAZE_LIST[1],
                                TURN: 5,
                                PLAYER_HP: 5,  # これはidを見てこのクラスを保持しているクラスのplayer_idと一致するplayerのhpを入れる
                                PLAYER_INFO_LIST: [{PLAYER_ID: 1, PLAYER_NAME: "Gaia", PLAYER_COLOR: RED, POSI: [0, 0]},
                                                   {PLAYER_ID: 2, PLAYER_NAME: "Nojima",
                                                       PLAYER_COLOR: BLUE, POSI: [9, 9]},
                                                   {PLAYER_ID: 3, PLAYER_NAME: "Sunaga", PLAYER_COLOR: YELLOW, POSI: [0, 9]}],
                                BULLET_INFO_LIST: [{POSI: [0, 2]}, {POSI: [4, 9]}, {POSI: [8, 1]}, {POSI: [9, 6]}],
                                ITEM_INFO_LIST: []
                                }
        #このクライアントが扱うプレイヤーのidを持つ
        self.player_id_ = None
        self.next_command_ = None
        self.player_hp_=None

    #サーバからのソケット取得、及びデコードによりgame_info_data_更新
    def listen(self):
        mcsm=MazeClientSocketManager(self.HOST_,self.PORT_,self.BACKLOG_,self.BUFSIZE_)
        try:
            mcsm.connect()
            mcsm.recv()
        except Exception as e:
            print(e)
        finally:
            mcsm.socket_.close()
            print("サーバとの通信終了")

    #迷路呼び出し
    def call_maze(self):
        self.maze_field_ = mazefield.MazeField("text", self.game_info_data_)
        root = tk.Tk()
        self.maze_field_.move_player()
        self.maze_field_.attack_player()
        self.maze_field_.create_maze(self.game_info_data_[MAZE])
        root.mainloop()

    def set_player_id(self):
        '''
        プレイヤーのidをセット
        '''
        self.player_id_=self.game_info_data_[PLAYER_ID]

    def set_next_command(self,next_command_):
        '''
        次のコマンドをセット
        '''
        self.next_command_=next_command_

    def set_player_hp(self):
        '''
        プレイヤーのhpをセット
        '''
        self.player_hp_=self.game_info_data_[PLAYER_HP]

    def set_ctsp(self):
        self.ctsp_=packet.ClientToServerPacket()
        self.ctsp_.set_player_id(self.get_playe_id)
        self.ctsp_.set_next_command(self.get_next_command)


    def get_next_command(self):
        '''
        次のコマンドを返す
        '''
        return self.next_command_

    def get_playe_id(self):
        '''
        プレイヤーのidを返す
        '''
        return self.player_id_

    def send(self):
        self.maze_client_socket_manager_.set_send_data(
            self.ctsp_)
        self.maze_client_socket_manager_.transmission()

    #tkinterで推したボタンに対応する定数をnext_command_にセットする
    def convert_command(self):
        if self.maze_field_.move_player().up_move()==UP_MOVE:
            self.set_next_command(UP_MOVE)
        if self.maze_field_.move_player() == DOWN_MOVE:
            self.set_next_command(DOWN_MOVE)
        if self.maze_field_.move_player()==RIGHT_MOVE:
            self.set_next_command(RIGHT_MOVE)
        if self.maze_field_.move_player()==LEFT_MOVE:
            self.set_next_command(LEFT_MOVE)
        if self.maze_field_.attack_player() == UP_ATTACK:
            self.set_next_command(UP_ATTACK)
        if self.maze_field_.attack_player() == DOWN_ATTACK:
            self.set_next_command(DOWN_ATTACK)
        if self.maze_field_.attack_player() == RIGHT_ATTACK:
            self.set_next_command(RIGHT_ATTACK)
        if self.maze_field_.attack_player() == LEFT_ATTACK:
            self.set_next_command(LEFT_ATTACK)

    def convert_up_move(self):
        if self.maze_field_.move_player().up_move() == UP_MOVE:
            self.set_next_command(UP_MOVE)


mazeclient = MazeClient(HOST,PORT,BACKLOG,BUFSIZE)

thrd=threading.Thread(target=mazeclient.convert_command)
thrd.start()

mazeclient.call_maze()

