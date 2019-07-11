#this file is server file
import socket
import config
from config import X, Y
from config import W,B,P,I
from config import JOIN, MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACKN
from config import CREATE_BULLET
from config import get_direct_str
from config import OBJECT_INFO,PLAYER_INFO,BULLET_INFO, ITEM_INFO
from config import OBJECT_INFO_MANAGER, PLAYER_INFO_MANAGER, BULLET_INFO_MANAGER, ITEM_INFO_MANAGER
from config import PACKET, SERVER_TO_CLIENT_PACKET, CLIENT_TO_SERVER_PACKET
from info import PlayerInfo, BulletInfo
from packet import  ServerToClientPacket, ClientToServerPacket





class MazeSocket(object):
    '''
        クライアントとの通信処理で必要な情報と変数を扱うクラス。
        Serverとしてではなく、通信
    '''

    def __init__(self):
        self.HOST_ = None#HOST
        self.PORT_ = None#PORT
        self.BACKLOG_ = None#BACKLOG
        self.BUFSIZE_ = None#BUFSIZE

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
       
class MazeServerSocket(MazeSocket):
    

    def __init__(self):
        super().__init__()
        self.ip_name_list_ = []
        self.server_to_client_packet_ = None#None
        self.client_to_server_packet_ = None#[]
    
    def set_server_to_clietn_packet(server_to_client_packet):
        '''
            サーバー側からクライアント側に渡すパケットをセットする。
        '''
        self.server_to_client_packet_ = server_to_client_packet

    def delete_all_client_to_sever_packet(self):
        '''
            クライアント側から受け取ったパケットをすべて消す。
        '''
        for i in range(len(self.client_to_server_packet_)):
            del self.client_to_server_packet_[i]
        print("クライアント側から受け取ったパケットをすべて消去しました。")


    def get_client_to_server_packet(server_to_client_packet):
        '''
            クライアント側から受け取ったパケットを取得する。
        '''
        return self.client_to_server_packet_
        
    def get_ip_name_list(self):
        '''
            プレイヤーのゲーム参加コマンドを受け取り
            各プレイヤーのipと名前をマッピングした辞書を返す。
        '''
        return self.ip_name_list_
       
    def show_ip_name_list(self):
        for ip_name in self.ip_name_list_:
            #定数を使ってもいいけど何回も使わないだろうから取り合えず数値を使う。
            print("ip : " +  str(ip_name[0]) + "  name : " + ip_name[1])


    def wait_participation_command(self):
        '''
            クライアントと通信して参加コマンドを受け取る
            ClientToServerPacketに参加コマンドをセットしてもらったものを受け取る
            それ以外は受け取らないよ
            参加プレイヤーのipとnameを含むリストを格納したリストをインスタンス変数として保持する
        '''

        print("参加プレイヤー受付開始")
        #################
        #通信処理
        #################

        #################
        #self.ip_name_listの生成
        #################
        print("参加プレイヤー受付終了")
        


        ip_name_list = [['127.0.0.1',"sawada"],['127.0.0.1',"sunaga"],['127.0.0.1',"nojima"]]
        #テスト用のコード、上の処理が完成するまではベタ打ちで対応
        self.ip_name_list_ = ip_name_list
        print("参加プレイヤーを表示します。")
        
        #参加プレイヤ―のipと名前を表示
        self.show_ip_name_list()

class MazeClientSocket(object):
    '''
        のじま、まかせた
    '''
    def __init__(self):
        super().__init__()

    pass

