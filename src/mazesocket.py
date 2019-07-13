#this file is server file
import socket
import config
from config import X, Y
from config import W,B,P,I
from config import JOIN, MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import CREATE_BULLET
from config import get_direct_str
from config import OBJECT_INFO,PLAYER_INFO,BULLET_INFO, ITEM_INFO
from config import OBJECT_INFO_MANAGER, PLAYER_INFO_MANAGER, BULLET_INFO_MANAGER, ITEM_INFO_MANAGER
from config import PACKET, SERVER_TO_CLIENT_PACKET, CLIENT_TO_SERVER_PACKET
from info import PlayerInfo, BulletInfo
from packet import  ServerToClientPacket, ClientToServerPacket





class MazeSocketManager(object):
    '''
        クライアントとの通信処理で必要な情報と変数を扱うクラス。
        Serverとしてではなく、通信
    '''

    def __init__(self,HOST,PORT,BACKLOG,BUFSIZE):
        self.socket_ = None
        self.HOST_ = HOST
        self.PORT_ = PORT
        self.BACKLOG_ = BACKLOG
        self.BUFSIZE_ = BUFSIZE
        self.game_info_data_ = None
        self.player_command_data_ = None

    def is_possible_communication(self):
        '''
            通信に必要な情報が設定されているかを判断する
        '''
        if(self.HOST_ == None or self.PORT_ == None or self.BACKLOG_ == None or self.BUFSIZE_ == None):
            print("ソケット通信の準備が完了していません。")
            return False
        else:
            print("ソケット通信の準備が完了しています。")
            return True

    def set_HOST(self, HOST):
        self.HOST_ = HOST

    def set_PORT(self, PORT):
        self.PORT_ = PORT

    def set_BACKLOG(self, BACKLOG):
        self.BACKLOG_

    def set_BUFSIZE(self,BUFSIZE):
        self.BUFSIZE_ = BUFSIZE

    def get_HOST(self):
        return self.HOST_

    def get_PORT(self):
        return self.PORT_

    def get_BACKLOG(self):
        return self.BACKLOG_

    def get_BUFSIZE(self):
        return self.BUFSIZE_

    def create_socket(self):
        '''
            socktを生成
            閉じるのを忘れるなよ
        '''
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("ソケットを生成しました。")


    def close_socket(self):
        '''
            socketを閉じる
        '''
        self.socket_.close()
        self.socket_ = None
        print("ソケットを閉じました。")

    #def send(self,send_data):
    #    '''
    #        送信したいデータを入れる
    #        Packetクラスでget_send_data()から受け取ったデータを引数に入れる
    #    '''
    #    self.socket_.send(send_data.encode())
    #    print("送信完了")


class MazeServerSocketManager(MazeSocketManager):


    def __init__(self,HOST,PORT,BACKLOG,BUFSIZE):
        super().__init__(HOST,PORT,BACKLOG,BUFSIZE)
        #################################注意　サーバー側は複数のクライアントのデータを受け取る
        #この二つ辞書にした方がいいのかもね
        self.conn_ = None
        self.addr_ = None

    def bind(self):
        '''
            接続待ちをするIPアドレスとポート番号を指定
        '''
        self.socket_.bind((self.HOST_, self.PORT_))
        print("bindをしました。")


    def listen(self, connect_num):
        '''
            接続を待つ。connect_numは接続数
        '''
        print("listenを開始します")
        self.socket_.listen(self.BACKLOG_)
        print("listenをしました。")

    def accept(self):
        '''
            接続を待ち受ける
        '''
        self.conn_, self.addr_ = self.socket_.accept()


    def recv(self):
        '''
            データを受け取る
        '''
        if(self.conn_ == None):
            print("connがないためデータの受信ができません。")
        else:
            self.player_command_data_ = self.conn_.recv(self.BUFSIZE_).decode()
            print(self.addr_,"からデータを受け取りました。")
            #self.conn_ = None
            #self.addr_ = None
            #print("connを消しました。")
            #print("addrを消しました。")

    def send(self,send_data):
        '''
            送信したいデータを入れる
            Packetクラスでget_send_data()から受け取ったデータを引数に入れる
        '''
        self.conn_.send(send_data.encode())
        print("送信完了")


    def transmission(self):
        '''
            通信処理をまとめたい
            ここらへんは勉強不足のため変なコード書くかもだけど許してくれ...
        '''
        self.create_socket()
        self.bind()
        self.listen(1)
        self.accept()
        self.recv()
        print(self.player_command_data_)
        self.send("send_data")
        self.close_socket()

class MazeClientSocketManager(MazeSocketManager):
    '''
        のじま、まかせた
    '''
    def __init__(self,HOST,PORT,BACKLOG,BUFSIZE):
        super().__init__(HOST,PORT,BACKLOG,BUFSIZE)
        self.send_data = None

    def connect(self):
        '''
            IPアドレスとポートを指定
            して接続を要求
        '''
        if(self.socket_ == None):
            print("ソケットが生成されていません。")
        else:
            self.socket_.connect((self.HOST_, self.PORT_))
            print("connect完了")

    def recv(self):
        '''
            データを受け取る
        '''
        if(self.socket_ == None):
            print("ソケットが生成されていません。")
        else:
            self.game_info_data_ = self.socket_.recv(self.BUFSIZE_).decode()
            print("サーバー側からデータを受け取りました。")


    def send(self):
        '''
            送信したいデータを入れる
            Packetクラスでget_send_data()から受け取ったデータを引数に入れる
        '''
        self.socket_.send(self.send_data.encode())
        print("送信完了")

    def set_send_data(self,send_data):
        '''
            サーバー側に送りたい情報をセットする
        '''
        self.send_data = send_data
        print("情報セット完了")

    def transmission(self):
        '''
            通信処理をまとめたい
            ここらへんは勉強不足のため変なコード書くかもだけど許してくれ...
        '''
        self.create_socket()
        self.connect()
        self.send()
        self.recv()
        self.close_socket()







