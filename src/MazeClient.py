import config
import socket
import select
import threading
import info
import packet
import config

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
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 50000
    BUFSIZE = 4096

    #プレイヤー情報送信
    def send(self):

        packed = packet.ClientToServerPacket()
        sock.send(packed.get().encode())

    #プレイヤー情報受信
    def listen(self, sock, HOST, PORT, BUFSIZE):
        try:
            sock.connect((HOST, PORT))
            while True:
                r_ready_sockets, w_ready_sockets, e_ready_sockets = select.select([sock], [], [])
                try:
                    #サーバから受け取ったパケットをデコード
                    packet.ServerToClientPacket() = sock.recv(BUFSIZE).decode()
                    #packet.ClientToServerPacket().get_game_info を用いて他のプレイヤー描画更新処理
                except:
                    break
        except Exception as e:
            print(e)
        finally:
            sock.close()
            print("サーバとの接続が切断されました")

class Playerinfo():
    def __init__(self):
        self.id=info.PlayerInfo().set_id()
        self.infolist = info.PlayerInfo()

    def update_player(self):
        new_info=packet.ServerToClientPacket().get_game_info()
        for _ in new_info:
            if self.id==new_info.key:
                #サーバに送るパケットに同封
                packet.ClientToServerPacket().set_next_command(self.player_command)
                packet.ClientToServerPacket().set_player_id( self.id)

    #playerからのコマンド入力
    def input_command(self):
        self.player_command=config.JOIN

#Mazeオブジェクト受け取り必要情報取得
class MazeField():
    pass

