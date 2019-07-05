from playerinfo import PlayerInfo
from iteminfo import Bullet

#クライアントとサーバー間で扱うデータ群をまとめるクラス
#info関連のクラスをインスタンス変数として持つ
class Packet(object):

    def __init__(self):
        '''
            オブジェクト毎にリストを作る
        '''
        self.player_info_list_ = []
        self.bullet_info_list_ = []
        #maze_info_はサーバー側からプレイヤー側に渡されるときのみ更新される
        self.maze_info_ = None
        self.now_turn_ = None

    def __del__(self):
        print("パケットクラスが破棄されます")

    #下の関数はこのクラスの目的として不適切かもしれない->情報管理クラスをつくる?

    #def update_player_info_list(self, id, player_info):
    #   '''
    #        指定したidのplayer_infoを更新する
    #        更新できたならばTrue
    #        そうでないならばFalseを返す
    #    '''
    #    for i in range(len(self.player_info_list_)):
    #        if(self.player_info_list_[i].get_id == id):
    #            self.player_info_list_[i] = player_info
    #            return True

    #    return False

    #def update_bullet_info_list(self):