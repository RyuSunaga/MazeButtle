from gamemanager import GameManager
from packet import ClientToServerPacket, ServerToClientPacket 
from gameinfomanager import GameInfoManager
from mazesocket import MazeServerSocketManager
import socket
import ast
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
        self.HOST_ = HOST
        self.PORT_ = PORT
        self.BACKLOG_ = BACKLOG
        self.BUFSIZE_ = BUFSIZE
        self.game_info_manager_ = GameInfoManager()
        self.game_info_ = None
        #ゲームの情報を通信用に整形するのに必要
        self.stcp_ = ServerToClientPacket()
        #通信に必要
        self.server_socket_manager_ = MazeServerSocketManager(HOST,PORT,BACKLOG,BUFSIZE)
        
        self.player_command_data_list_ = []
        
        #まだ実行していないプレイヤーのIDとコマンドを保持
        #クライアントが完成するまではとりあえず以下のデータを使う。
        #参加コマンド用のテスト
        #self.player_command_data_list_ = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Nojima",NEXT_COMMAND:JOIN,TEXT:""},
        #                                  {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Gaia",NEXT_COMMAND:JOIN,TEXT:""},
        #                                  {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:None,PLAYER_NAME:"Sunaga",NEXT_COMMAND:JOIN,TEXT:""}]
        #移動コマンド用のテスト
        #self.player_command_data_list_ = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:0,PLAYER_NAME:"Nojima",NEXT_COMMAND:RIGHT_MOVE,TEXT:""},
        #                                  {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:1,PLAYER_NAME:"Gaia",NEXT_COMMAND:DOWN_MOVE,TEXT:""},
        #                                  {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:2,PLAYER_NAME:"Sunaga",NEXT_COMMAND:UP_MOVE,TEXT:""}]

        #弾丸生成用のテスト
        #self.player_command_data_list_ = [{PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:0,PLAYER_NAME:"Nojima",NEXT_COMMAND:RIGHT_ATTACK,TEXT:""},
        #                                  {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:1,PLAYER_NAME:"Gaia",NEXT_COMMAND:DOWN_ATTACK,TEXT:""},
        #                                  {PACKET_TYPE:CLIENT_TO_SERVER_PACKET,HOST:'127.0.0.1',PORT:50000,PLAYER_ID:2,PLAYER_NAME:"Sunaga",NEXT_COMMAND:UP_ATTACK,TEXT:""}]


    def up_date_game_info(self):
        '''
            クライアントから受け取ったデータをもとにself.game_info_manager_更新する。
        '''
        self.game_info_manager_.set_client_to_server_data(self.player_command_data_list_)
        self.game_info_manager_.up_date_game()
        print("すべてのプレイヤーのコマンドを消去します。")
        self.player_command_data_list_ = []

    def get_client_game_info(self):
        '''
            クライアントに送るように更新したゲームの情報を取得する
        '''
        game_info = self.game_info_manager_.get_game_info()
        self.stcp_.set_game_info(game_info)
        send_data = self.stcp_.get_send_data()
        #この時点でsend_dataは文字列->SocketManagerにいれて大丈夫
        return send_data
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

def MAIN():
    '''
        はやくこれを書きたい
    '''
    pass
##########################################TEST##############################################################


test6()







