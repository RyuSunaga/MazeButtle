import config
import socket
import select
import threading
import info
import packet
import config
from config import JOIN
from info import PlayerInfo
#this is client file

##############################################################################################################

#命名規則について by sunaga

# file名　　　　　　　　全て小文字でなるべく短く　       myfile
# クラス名　　　　　　　最初大文字、大文字区切り　　　   ThisIsMyClass
# 関数名、メソッド名　　全小文字、アンダースコア区切り   this_is_my_func
# 変数名　　　　　　　　全小文字、アンダースコア区切り   this_is_my_val
# 定数名                全大文字、アンダースコア区切り　 THIS_IS_MY_CONST

# 自クラス内でのみ使用する内部変数と内部メソッドはアンダースコアで開始


##############################################################################################################

class Socket(object):
    '''
    サーバと通信を行うクラス
    '''
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = '127.0.0.1'
        self.PORT = 50000
        self.BUFSIZE = 4096

    #プレイヤー情報送信
    def send(self):
        ctsp = packet.ClientToServerPacket()
        ctsp.set_next_command(JOIN)
        ctsp.set_player_id(114514)
        data = ctsp.get_str_data()
        self.sock.send(data.encode())

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

class Player():
    def __init__(self):
        #self.id= PlayerInfo().get_id()
        #self.infolist = PlayerInfo()
        self.player_info_ = PlayerInfo(1,"nojima","red",[1,1])
        pass
    #def update_player(self):
    #    new_info=packet.ServerToClientPacket().get_game_info()
    #id==new_info.key:
    #            #サーバに送るパケットに同封
    #            packet.ClientToServerPacket().set_next_command(self.player_command)
    #            packet.ClientToServerPacket().set_player_id( self.id)

    #playerからのコマンド入力
    def input_command(self):
        self.player_command=config.JOIN

#Mazeオブジェクト受け取り必要情報取得
class MazeField():
    maze = packet.ServerToClientPacket().get_game_info()


soc=Socket()
soc.listen()
#soc.send()
