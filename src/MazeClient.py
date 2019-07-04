import playerinfo as pi
import config
import socket
import select
import threading

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

    def listen(self, sock, HOST, PORT, BUFSIZE):
        try:
            sock.connect((HOST, PORT))
            while True:
                r_ready_sockets, w_ready_sockets, e_ready_sockets = select.select([sock], [], [])
                try:
                    recev_msg = sock.recv(BUFSIZE).decode()
                except:
                    break
        except Exception as e:
            print(e)
        finally:
            sock.close()
            print("サーバとの接続が切断されました")


'''
情報の受け渡しについて
辞書型にid,commandを格納    {id,command}

'''

"""
プレイヤー自身の初期情報
------------------------------------------------------------
1.プレイヤーID              id   int
2.体力、初期値5             hp   int
3.位置情報、初期値[X,Y]     posi    int
4.攻撃力、初期値2           power   int
5.速度、初期値1             speed    int
------------------------------------------------------------
"""

class Player():
    def __init__(self):
        self.id=pi.PlayerInfo().set_id()
        self.infolist = pi.PlayerInfo()

    def UpdatePlayer(self,new_info):
        #infolistからidを取得
        if self.id==new_info.key:
            self.myinfo = new_info

