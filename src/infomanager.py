#サーバー側でゲーム上の情報をまとめて管理するために使うクラスを定義する
from config import X, Y
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import get_direct_str
from info import PlayerInfo
from info import BulletInfo

class PlayerInfoManager(object):
    """
    GameManagerクラスでPlayerInfoを管理するクラス
    参加プレイヤーの人数分,PlayerInfoクラスをインスタンス変数としてもつ。
    """

    def __init__(self):
        #各参加者のPlayerInfoクラスを格納
        self.player_info_list = []
        self.id_list = []
        

    def init_player_info(self,id_list, name_list, posi_list):
        '''
        ゲームで最初にプレイヤーの情報を生成するときに使う
        参加プレイヤー待ちで取得しname,id情報を持つPlayerInfoクラスを生成する
        ipアドレスはプレイヤーの情報ではなくクライアントの情報なのでPlayerInfoクラスでは保持しない
        '''

        self.id_list = id_list

        for id, name, posi in zip(id_list, name_list, posi_list):
            player_info = PlayerInfo()
            player_info.set_id(id)
            player_info.set_name(name)
            player_info.set_posi(posi)
            self.player_info_list.append(player_info)


    def get_all_player_info(self):
        '''
            登録されたPlayerInfoクラスを全てリストの形式で取得する
            何も登録されてない場合はNoneを返す。
            #######################################################################################Packetに格納するときに使う。
        '''
        return player_info_list

    def get_player_info(self,id):
        '''
            指定されたidを持つPlayerInfoを取得する
            指定したidをもつプレイヤーが存在しない場合はNoneを返す
        '''
        for player_info in self.player_info_list:
            if(id == player_info.get_id()):
                return player_info
        
        return None

    def show_all_player_info(self):
        '''
           登録されているすべてのプレイヤーの情報を表示する
        '''
        for player_info in self.player_info_list:
            player_info.show_info()

    def show_player_info(self,id):
        '''
            指定されたidを持つプレイヤーの情報を表示する
        '''
        for player_info in self.player_info_list:
            if(id == player_info.get_id()):
                player_info.show_info()
                return 
        
        print("id = " + str(id) + "のプレイヤーは存在ししません。")

    
    def update_player_info(self, id, player_info):
        """
            プレイヤーの情報を変更する
            変更する際はidを指定する、idが一致しない場合はfalseを返す
            正常に変更が成功した場合はtrue返す
        """

        for i in range(len(self.player_info_list)):
            if(id == self.player_info_list[i].get_id()):
                self.player_info_list[i].update_player_info(player_info)
                return True
        return False


class ItemInfoManager(object):
    '''
        迷路上のオブジェクトを管理するクラス。
    '''

    pass

