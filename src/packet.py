
import info
from config import PACKET_TYPE, PLAYER_ID, PLAYER_NAME, PLAYER_COLOR, PLAYER_HP, POSI,MAZE, PLAYER_INFO_LIST, BULLET_INFO_LIST, ITEM_INFO_LIST, TURN,TEXT,NEXT_COMMAND
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
        return self.text_

    def __del__(self):
        print(self.packet_type_ + "が破棄されます")


class ServerToClientPacket(Packet):
    '''
        サーバー側からクライアント側に渡すパケット
        つまり、クライアント側はこのパケットを受け取る。
    '''
    def __init__(self):
        self.packet_type_ = SERVER_TO_CLIENT_PACKET
        self.game_info_ = None
        self.maze_ = None
        self.turn_ = None
        self.text_ = None
        #これはこのクラス内では常にNone　わかりやすさのために定義しているだけよ by sunaga
        self.player_hp_ = None
        self.dict_player_info_list_ = []
        self.dict_bullet_info_list_ = []
        self.dict_item_info_list_ = []

        self.dict_client_to_server_data =  {PACKET_TYPE:None,
                                            TEXT:None,
                                            MAZE:None,
                                            TURN:None,
                                            PLAYER_HP:None,#これはidを見てこのクラスを保持しているクラスのplayer_idと一致するplayerのhpを入れる------->これはクライアントの仕事やな
                                            PLAYER_INFO_LIST:[],
                                            #PLAYER_INFO_LIST:[{PLAYER_ID:1,PLAYER_NAME:"Gaia",PLAYER_COLOR:RED,POSI:[0,0]},
                                            #                  {PLAYER_ID:2,PLAYER_NAME:"Nojima",PLAYER_COLOR:BLUE,POSI:[9,9]},
                                            #                  {PLAYER_ID:3,PLAYER_NAME:"Sunaga",PLAYER_COLOR:YELLOW,POSI:[0,9]}],
                                            #BULLET_INFO_LIST:[{POSI:[0,2]},{POSI:[4,9]},{POSI:[8,1]},{POSI:[9,6]}],
                                            BULLET_INFO_LIST:[],
                                            ITEM_INFO_LIST:[]
                                            }

        self.str_client_to_server_data = None

        print(self.packet_type_,"生成完了")

    def __del__(self):
        print(self.packet_type_ + "が破棄されます")


    def set_game_info(self,game_info):
        '''
            game_info
            ->>>>>>>>>>>>>>>>>>>>>>>>>.こいつを使うと自動的にgame_info内のすべてのデータを通信用に準備できるようにする。
        '''
        self.game_info_ = game_info
        self.set_maze()
        self.set_turn()
        self.set_player_hp()
        self.set_dict_player_info_list()
        self.set_dict_bullet_info_list()
        self.set_dict_item_info_list()

    def set_maze(self):
        if(self.game_info_ == None):
            print("GameInfoが設定されていません")
            print("PacketにMazeの設定に失敗しました。")
        else:
            self.maze_ = self.game_info_.get_maze()
            print("PacketにMazeが設定されました。")


    def set_turn(self):
        if(self.game_info_ == None):
            print("GameInfoが設定されていません")
            print("PacketにTurnの設定に失敗しました。")
        else:
            self.turn_ = self.game_info_.get_turn()
            print("PacketにTurnが設定されました。")


    def set_player_hp(self):
        self.player_hp_ = None
        print("PacketにPlayer HPが設定されました。")

        
    def set_dict_player_info_list(self):
        if(self.game_info_ == None):
            print("GameInfoが設定されていません")
            print("PacketにPlayerInfoListの設定に失敗しました。")
        else:
            player_info_list = self.game_info_.get_player_info_list()
            for player_info in player_info_list:
                self.dict_player_info_list_.append(player_info.get_dict_send_data())
            print("PacketにPlayerInfoListが設定されました。")

    def set_dict_bullet_info_list(self):
        if(self.game_info_ == None):
            print("GameInfoが設定されていません")
            print("PacketにBulletInfoListの設定に失敗しました。")
        else:
            bullet_info_list = self.game_info_.get_bullet_info_list()
            for bullet_info in bullet_info_list:
                self.dict_bullet_info_list_.append(bullet_info.get_dict_send_data())
            print("PacketにBulletInfoListが設定されました。")

    def set_dict_item_info_list(self):
        if(self.game_info_ == None):
            print("GameInfoが設定されていません")
            print("PacketにItemInfoListの設定に失敗しました。")
        else:
            self.dict_item_info_list_ = []
            print("PacketにItemInfoListが設定されました。")

            
    def set_text(self,text):
        self.text_ = text
        print("Packetにtextが設定されました。")



    def info_to_dict(self):
        '''
            設定してあるインスタンス変数からソケット通信で送受信用の形式に変更する。(辞書型)
        '''
        print("クライアント側に送る情報を生成します。")
        self.dict_client_to_server_data[PACKET_TYPE] = self.packet_type_
        self.dict_client_to_server_data[MAZE] = self.maze_
        self.dict_client_to_server_data[TURN] = self.turn_
        self.dict_client_to_server_data[TEXT] = self.text_
        self.dict_client_to_server_data[PLAYER_HP] = self.player_hp_
        self.dict_client_to_server_data[PLAYER_INFO_LIST] = self.dict_player_info_list_
        self.dict_client_to_server_data[BULLET_INFO_LIST] = self.dict_bullet_info_list_
        self.dict_client_to_server_data[ITEM_INFO_LIST] = self.dict_item_info_list_
        self.str_client_to_server_data = str(self.dict_client_to_server_data)
        print("クライアント側に送る情報を生成しました。")

    def get_send_data(self):
        '''
            インスタンス変数を通信できる形式に変更して返す
        '''
        self.info_to_dict()
        return self.str_client_to_server_data


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
        self.dict_client_to_server_data = {PACKET_TYPE:None,
                                           TEXT:None,
                                           NEXT_COMMAND:None,
                                           PLAYER_ID:None}
        self.str_client_to_server_data = None

        print(self.packet_type_,"生成完了")

    def __del__(self):
        print(self.packet_type_ + "が破棄されます")

    def set_next_command(self,command):
        self.next_command_ = command

    def set_player_id(self,player_id):
        self.player_id_ = player_id

    def get_next_command(self):
        return self.get_next_command

    def get_player_id(self):
        return self.player_id_
    

    def info_to_dict(self):
        '''
            この関数自体は他のクラスでは使われません by sunaga
            設定してあるインスタンス変数からソケット通信で送受信用の形式に変更する。(辞書型)
        '''
        print("サーバー側に送る情報を生成します。")
        self.dict_client_to_server_data[PACKET_TYPE] = self.packet_type_
        self.dict_client_to_server_data[NEXT_COMMAND] = self.next_command_
        self.dict_client_to_server_data[PLAYER_ID] = self.player_id_
        self.dict_client_to_server_data[TEXT] = self.text_
        self.str_client_to_server_data = str(self.dict_client_to_server_data)
        print("サーバー側に送る情報を生成しました。")

    def get_send_data(self):
        '''
            インスタンス変数を通信できる形式に変更して返す
        '''
        self.info_to_dict()
        return self.str_client_to_server_data



