from gamemanager import GameManager
from packet import ClientToServerPacket, ServerToClientPacket 
from gameinfomanager import GameInfoManager
from mazesocket import MazeServerSocketManager
import socket
import ast
import threading
import time
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
from config import TEST


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
        self.HOST_ = HOST
        self.PORT_ = PORT
        self.BACKLOG_ = BACKLOG
        self.BUFSIZE_ = BUFSIZE
        self.game_info_manager_ = GameInfoManager()
        self.game_info_ = None
        self.send_data_ = None
        self.is_first_connect_ = False
        self.server_start_time_ = time.time()
        self.time_limit_ = 60
        #クライアントの接続数 -> あらかじめ最大数を決めておこう
        self.client_num_ = 3
        #クライアントを格納するリスト
        self.clients_ = []
        #ゲームの情報を通信用に整形するのに必要
        self.stcp_ = ServerToClientPacket()
        #通信に必要
        self.server_socket_manager_ = MazeServerSocketManager(HOST,PORT,BACKLOG,BUFSIZE)
        #クライアントから受け取ったプレイヤーのコマンドの情報を格納するリスト
        self.player_command_data_list_ = []

        

    def up_date_game_info(self):
        '''
            クライアントから受け取ったデータをもとにself.game_info_manager_更新する。
        '''
        self.game_info_manager_.set_client_to_server_data(self.player_command_data_list_)
        self.game_info_manager_.up_date_game()
        print("すべてのプレイヤーのコマンドを消去します。")
        self.player_command_data_list_ = []

    def create_client_game_info(self):
        '''
            クライアントに送るように更新したゲームの情報を取得する
        '''
        game_info = self.game_info_manager_.get_game_info()
        self.stcp_.set_game_info(game_info)
        send_data = self.stcp_.get_send_data()
        self.send_data_ = send_data
        #この時点でsend_dataは文字列->SocketManagerにいれて大丈夫
        #return send_data
        #print(send_data)
        #self.server_socket_manager_.set_send_data(send_data)
        #self.server_socket_manager_.transmission()


    def server_start_up(self):
        '''
            サーバーの処理を書く
            もしかしたらServerSocketManagerを使わないでsocketを使って書いた方がいいかも。
        '''
        print("サーバーを起動します")
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("ソケットを生成しました。")
        server_sock.bind((self.HOST_,self.PORT_))
        print("bindをしました。")
        #server_sock.listen(self.BUFSIZE_)
        #print("listeをしました。")
        #client_sock, client_add = server_sock.accept()

        time = 0
        while True:
            server_sock.listen(self.BUFSIZE_)
            print("listeをしました。")
            client_sock, client_add = server_sock.accept()
            ######################################################################################まずは一人だけ受け取ってみよう
            recv_data = client_sock.recv(self.BUFSIZE_)
            if(recv_data != None):
                try:
                    player_command_data = ast.literal_eval(recv_data.decode())
                    self.player_command_data_list_.append(player_command_data)
                    print("クライアントから情報を受け取りました。")
                    print(player_command_data)
                except:
                    print("クライアント側から受信したメッセージが不適切でした。")
            else:
                print("クライアントから受け取ったデータがNoneでした。")
          
            #クライアントのコマンドをもとに処理を行う
            self.up_date_game_info()
            new_game_info = self.get_client_game_info()
            client_sock.send(new_game_info.encode())
            time += 1
            print(str(time)+"回通信をしました。")
            #100回まで通信できるよ
            if(time >= 100):
                break
        client_sock.close()
        print("ソケットを閉じました")

    def server_start_up2(self):
        '''
            複数のクライアントと通信できるようにする
        '''
        print("MazeServer2を起動します")
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("ソケットを生成しました。")
        server_sock.bind((self.HOST_,self.PORT_))
        print("bindをしました。")
        server_sock.listen(10)
        
        while True:
            client_sock, client_add = server_sock.accept()
            print("[接続]{}".format(client_add))
            self.clients_.append((client_sock, client_add))

            #ここからへんまだ理解不足や
            handle_thread = threading.Thread(target=self.handler, args=(client_sock,client_add),daemon=True)
            handle_thread.start()

    def remove_connection(self,client_sock,client_add):
        '''
            クライアントとの接続を切断する。
        '''
        print("クライアントとの通信を切ります。")

    def handler(self,client_sock,client_add):
        '''
            クライアントからデータを受信する。
        '''
        print("HANDLE を起動")


        while True:
            try:
                recv_data = client_sock.recv(self.BUFSIZE_)
            except ConnectionResetError:
                self.remove_connection(client_sock, client_add)
                break
            else:
                if not recv_data:
                    self.remove_connection(client_sock,client_add)
                    break
                else:
                    print("データを受信しました。")
                    print(recv_data.decode())
                    player_command_data = ast.literal_eval(recv_data.decode())
                    self.player_command_data_list_.append(player_command_data)
                    last_client_num = len(self.player_command_data_list_)
                    print("クライアントから受け取ったプレイヤーのコマンドをサーバーにセットしました。")
                    if(self.is_first_connect_ == False):
                       #サーバーが起動してから30秒かプレイヤーの人数が4人になるまでまつ
                       while (time.time() - self.server_start_time_ <= self.time_limit_) and len(self.player_command_data_list_) < 4:
                           print("クライアントの接続を待っています。 残り時間:" +str(int(self.time_limit_ - (time.time() - self.server_start_time_)))+"秒")
                           print("現在の受付数;"+str(len(self.player_command_data_list_)))
                           time.sleep(1)
                       print("参加プレイヤーの受付を終了しました。")
                       print("参加プレイヤーは"+ str(len(self.player_command_data_list_)) + "人です。")
                       self.client_num_ = len(self.player_command_data_list_)
                       self.is_first_connect_ = True
                       print("ゲームを開始します")
                       time.sleep(5)
                       
                       #最初のゲームの情報を生成
                       if(last_client_num == len(self.player_command_data_list_)):
                           print(client_add,"あなたが最後のプレイヤーです")
                           time.sleep(5)
                           self.up_date_game_info()
                           self.create_client_game_info()
                       else:
                           print("最初のゲームの情報を生成中です、しばらくお待ちください。")
                           time.sleep(15)
                       print("クライアントにデータを送信します。")
                       new_game_info = self.send_data_
                       client_sock.send(new_game_info.encode())
                       print(client_add,"にデータを送りました")
                       print("クライアントからの情報を受け付けます。")
                       continue

                    if(len(self.player_command_data_list_) == self.client_num_):
                        print("すべてのクライアントからデータを受け取りました。")
                        time.sleep(1)
                        self.up_date_game_info()
                        self.create_client_game_info()
                    else:
                        while len(self.player_command_data_list_) < self.client_num_:
                            print("全てのクライアントからデータを受け取っていません。")
                            time.sleep(1)
                            print("送受信数:",len(self.player_command_data_list_))
                        print("すべてのクライアントからデータを受け取りました。")
                        print("ゲーム情報を更新します。10秒待機します　20秒必要かな????")
                        time.sleep(7)
                    
                    new_game_info = self.send_data_
                    client_sock.send(new_game_info.encode())
                    print(client_add,"にデータを送りました")







##########################################TEST##############################################################
def test1():
    '''
        クライアントからの情報が無事にGameInfoManager()に渡されるのかのテスト
    '''
    print("TEST1")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.up_date_game()
    print(MS.game_info_manager_.get_client_to_server_data())

def test2():
    '''
        JOINコマンドを無事に実行できたかをテスト
        正常に実行されるとクライアントに渡される情報をが生成される。
    '''
    print("TEST2")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.up_date_game_info()
    MS.game_info_manager_.up_date_game()
    game_info = MS.game_info_manager_.get_game_info()
    print(game_info.get_maze())
    MS.stcp_.set_game_info(game_info)
    send_data = MS.stcp_.get_send_data()
    print(send_data)


def test3():
    '''
        受け取ってあるデータをつかいクライアントに最新の情報を送信するところまでをやってみる
    '''
    print("TEST3")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.up_date_game_info()
    MS.send_client_game_info()

def test4():
    '''
        プレイヤーオブジェクトにコマンドをセットする。
    '''
    print("TEST4")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    #############################実験中は下二つを行う必要がある。
    MS.up_date_game_info()
    MS.game_info_manager_.up_date_all_object_info()

def test5():
    '''
        1回目の更新と二回目の更新の違いをチェック
    '''
    print("TEST5")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.up_date_game_info()
    game_info = MS.game_info_manager_.get_game_info()
    MS.stcp_.set_game_info(game_info)
    send_data = MS.stcp_.get_send_data()
    print("-----------------------------------------------------------------------------------------------------------")
    print("1回目のゲームの情報")
    print(send_data)
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(2,10):
        MS.up_date_game_info()
        game_info = MS.game_info_manager_.get_game_info()
        MS.stcp_.set_game_info(game_info)
        send_data = MS.stcp_.get_send_data()
        print("-----------------------------------------------------------------------------------------------------------")
        print(str(i)+"回目のゲームの情報")
        print(send_data)
        print("-----------------------------------------------------------------------------------------------------------")

def test6():
    '''
        複数回情報を更新して正常に動くかをチェック
    ''' 
    #クライアントが完成するまではとりあえず以下のデータを使う。
    #参加コマンド用のテスト
    player_command_data = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Nojima",NEXT_COMMAND:JOIN,TEXT:""},
                           {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Gaia",NEXT_COMMAND:JOIN,TEXT:""},
                           {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Sunaga",NEXT_COMMAND:JOIN,TEXT:""}]
    #移動コマンド用のテスト
    player_command_data = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:0,PLAYER_NAME:"Nojima",NEXT_COMMAND:RIGHT_MOVE,TEXT:""},
                           {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:1,PLAYER_NAME:"Gaia",NEXT_COMMAND:DOWN_MOVE,TEXT:""},
                           {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:2,PLAYER_NAME:"Sunaga",NEXT_COMMAND:UP_MOVE,TEXT:""}]

    #弾丸生成用のテスト
    player_command_data = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:0,PLAYER_NAME:"Nojima",NEXT_COMMAND:RIGHT_ATTACK,TEXT:""},
                           {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:1,PLAYER_NAME:"Gaia",NEXT_COMMAND:DOWN_ATTACK,TEXT:""},
                           {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:2,PLAYER_NAME:"Sunaga",NEXT_COMMAND:UP_ATTACK,TEXT:""}]



def test6():
    '''
        MazeClientとの通信を試みる
    '''
    print("TEST6")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.server_start_up()

def test7():
    '''
        複数のクライアントと通信する
    '''
    print("TEST7")
    MS = MazeServer(HOST,PORT,BACKLOG,BUFSIZE)
    MS.server_start_up2()



def MAIN():
    '''
        はやくこれを書きたい
    '''
    pass
##########################################TEST##############################################################


test7()







