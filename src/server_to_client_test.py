import config
import socket
import select
import threading
import info
import packet
import config
from config import MAZE_LIST
from config import JOIN
from config import RED, BLUE, GREEN, YELLOW
from config import JOIN, MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import TEST
from info import PlayerInfo,BulletInfo,ItemInfo
from gameinfo import GameInfo
from packet import ClientToServerPacket, ServerToClientPacket

class Socket(object):
    '''
    サーバと通信を行うクラス
    '''
    def __init__(self,game_info):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = '127.0.0.1'
        self.PORT = 50000
        self.BUFSIZE = 4096
        self.gema_info_ = game_info

    #プレイヤー情報送信
    def send(self):
        stcp = ServerToClientPacket()
        stcp.set_game_info(self.gema_info_)
        stcp.set_text("うまくいってくれぇぇぇぇぇぇぇぇぇぇぇ")
        send_data = stcp.get_send_data()
        self.sock.send(send_data.encode())
        print("送信完了")

    #プレイヤー情報受信
    def listen(self):
        try:
            self.sock.connect((self.HOST, self.PORT))
            for _ in range(2):
                #r_ready_sock
                # ets, w_ready_sockets, e_ready_sockets = select.select([sock], [], [])
                try:
                    self.send()
                    #サーバから受け取ったパケットをデコード
                    msg  = self.sock.recv(self.BUFSIZE).decode()
                    print(type(msg),msg)
                    #packet.ClientToServerPacket().get_game_info を用いて他のプレイヤー描画更新処理
                except:
                    break
        except Exception as e:
            print(e)
        finally:
            self.sock.close()
            print("サーバとの接続が切断されました")






########################Socket test用オブジェクト生成#########################
maze = MAZE_LIST[1]

turn = 1

player_info1 = PlayerInfo(1,"Gaia",RED,[0,0])
#player_info1.prepare_next_command(RIGHT_ATTACK)
player_info1.prepare_next_command(LEFT_MOVE)
player_info1.update_posi()

player_info2 = PlayerInfo(2,"Nojima",BLUE,[9,9])
#player_info2.prepare_next_command(UP_ATTACK)
player_info2.prepare_next_command(UP_MOVE)
player_info2.update_posi()

player_info3 = PlayerInfo(3,"Sunaga",YELLOW,[0,9])
#player_info3.prepare_next_command(DOWN_ATTACK)
player_info3.prepare_next_command(DOWN_MOVE)
player_info3.update_posi()

player_info_list = [player_info1, player_info2, player_info3]

bullet_info1 = BulletInfo(10,player_info1)
bullet_info2 = BulletInfo(11,player_info2)
bullet_info3 = BulletInfo(12,player_info3)
bullet_info_list = [bullet_info1, bullet_info2, bullet_info3]

item_info_list = []

game_info = GameInfo()
game_info.set_maze(maze)
game_info.set_turn(turn)
game_info.set_player_info_list(player_info_list)
game_info.set_bullet_info_list(bullet_info_list)
game_info.set_item_info_list(item_info_list)

########################Socket test用オブジェクト生成#########################

sc = Socket(game_info)
sc.listen()











