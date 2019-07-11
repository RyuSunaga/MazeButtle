import info
from info import ObjectInfo, PlayerInfo, BulletInfo, ItemInfo
from gameinfo import GameInfo
from config import PACKET, SERVER_TO_CLIENT_PACKET, CLIENT_TO_SERVER_PACKET

#クライアントとサーバー間で扱うデータ群をまとめるクラス
#info関連のクラスをインスタンス変数として持つ
#余裕があったら色々新しい迷路上のオブジェクトを追加しよう。 by sunaga

#1サーバー側からクライアント側に渡す際に必要な情報
    #1.1各プレイヤーの新しい情報
    #1.2迷路を表示するのに必要な情報

#2クライアント側からサーバー側に渡す際に必要な情報
    #2.1クライアントが操作しているプレイヤーが選択したコマンド



class Packet(object):
    '''
        Packetの親クラス
    '''

    def __init__(self):
        self.packet_type_ = PACKET
        self.text_ = None

    def set_text(self, text):
        '''
            相手に伝えたいメッセージがあればこれを使おう。
        '''
        self.text_ = text

    def get_packet_type(self):
        return self.packet_type_

    def get_text(self):
        return text

    def __del__(self):
        print(self.packet_type_ + "が破棄されます")


class ServerToClientPacket(Packet):
    '''
        サーバー側からクライアント側に渡すパケット
        つまり、クライアント側はこのパケットを受け取る。
    '''
    def __init__(self):
        self.packet_type_ = SERVER_TO_CLIENT_PACKET

        #maze_infoにGUIに必要な情報をすべて保持させるのがシンプルでいいかも
        self.game_info_ = None

    def set_game_info(self,game_info):
        self.game_info_ = game_info

    def get_game_info(self):
        return self.game_info_

    def __del__(self):
        print(self.packet_type_ + "が破棄されます")

    def info_to_dict(self):
        '''
            設定してあるインスタンス変数からソケット通信で送受信可能な形式に変更する。
            形式はjsonをイメージ(辞書みたいな形)
            dictを文字列に変えて返す
        '''
        pass 



class ClientToServerPacket(Packet):
    '''
        クライアント側からサーバー側に渡すパケット
        つまり、サーバー側はこのパケットを受け取る。
    '''

    def __init__(self):
        self.packet_type_ = CLIENT_TO_SERVER_PACKET

        #プレイヤーが次に行うコマンドを保持するインスタンス変数　－＞　超重要
        self.next_command_ = None

        #クライアントが担当しているプレイヤーのidを保持するインスタンス変数 -> これがないと設定されたコマンドが誰の行動かわからなくなる。
        self.player_id_ = None

        self.data = {}

    def set_next_command(self,command):
        self.next_command_ = command

    def set_player_id(self,player_id):
        self.player_id_ = player_id

    def get_next_command(self):
        return get_next_command

    def get_player_id(self):
        return self.player_id_

    def __del__(self):
        print(self.packet_type_ + "が破棄されます")
 