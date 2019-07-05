from info import PlayerInfo
from info import BulletInfo

#クライアントとサーバー間で扱うデータ群をまとめるクラス
#info関連のクラスをインスタンス変数として持つ
#余裕があったら色々新しい迷路上のオブジェクトを追加しよう。 by sunaga


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

    def set_player_info(self, id, player_info):
        '''
            player_infoオブジェクトをインスタンス変数に格納する。

        '''

    def get_player_info(self,id):
        '''
            idと一致するPlayerInfoオブジェクトを取得する
            一致するidのオブジェクトが存在しなかった場合Noneを返す
        '''
        for player_info in self.player_info_list_:
            if(id == player_info.get_id()):
                return player_info

        return None

   