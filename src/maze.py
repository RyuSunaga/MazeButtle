import config
from config import X, Y
from config import W,B,P,I
from config import MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import CREATE_BULLET
from config import get_direct_str
from config import OBJECT_INFO,PLAYER_INFO,BULLET_INFO, ITEM_INFO
from config import OBJECT_INFO_MANAGER, PLAYER_INFO_MANAGER, BULLET_INFO_MANAGER, ITEM_INFO_MANAGER
from info import PlayerInfo
from info import BulletInfo

#########################################################################################################


#使わない


#########################################################################################################



class Maze(object):
    '''
        迷路クラス
        本当はしたくなかったけど簡単のためにInfo関連のオブジェクトも入れよう
        目的は
            ガイアの作った迷路を描画するクラスで描画しやすい情報を渡すこと
    '''

    def __init__(self):
        self.is_decision = False
        self.player_info_list_ = []
        self,bullet_info_list_ = []
        self.item_info_list_ = []
        #maze_は0,W,P,Iのどれか
        self.maze_ = None

    def is_decision_maze(self):
        '''
            迷路が決定されたかを返す関数
            決定されているならtrue,そうでないならばfalseを返す
        '''
        if(self.is_decision):
            print("迷路は決定されています。")
            return True
        else:
            print("迷路が決定されていません。")
            return False

    def get_maze(self):
        '''
            迷路を取得するための関数
            迷路描画クラスで使う
        '''
        if(self.is_decision_maze()):
            return self.maze_
        else:
            return None

    def get_edge_posi(self):
        '''
            迷路の端の座標を格納したリストを返す
        '''
        if(self.is_decision_maze):
                #迷路の端の座標を設定
                x_min = 0
                y_min = 0
                x_max = len(self.maze_[0]) -1
                y_max = len(self.maze_) - 1
                maze_edge = [[x_min,y_min],[x_min,y_max],[x_max,y_min],[x_max,y_max]]
                return maze_edge
        else:
            return None

    def show_maze(self):
        if(self.is_decision_maze()):
            for l in self.maze_:
                print(l)
        else:
            return

    def maze_decision(self):
        """
            ゲームで使用する迷路を決定する関数、現在はランダムで選択しているが
            時間に余裕があればプレイヤーの選択で決定してもいいかも。 by sunaga
        """

        #self.maze_ = MAZE_LIST[random.randint(0,2)]
        #テスト中は迷路固定
        self.maze_ = MAZE_LIST[0]
        print("迷路を決定しました。")

        self.is_decision = True

    def get_player_color(self, posi):
        '''
            選択した座標のプレイヤーの色を取得する
            迷路を描画するときに使ってくれ
        '''
        pass

    ############################################################################################設計ミスかな...................これってマネージャーの仕事だよね  今回は許して by sunaga
    def get_player_info(self,player_posi):
        '''
          迷路上のプレイヤーの座標から一致するPlayerInfoオブジェクトを返す
        '''
        for player_info in self.player_info_list_:
            if(player_info.get_posi() == player_posi):
                return player_info
        return None


    def get_bullet_info(self,bullet_posi):
        '''
           迷路上の弾丸の座標から一致するBulletInfoオブジェクトを返す
        '''
        for bullet_info in self.bullet_info_list_:
            if(bullet_info.get_posi() == bullet_posi):
                return bullet_info
        return None

    def get_item_info(self,item_posi):
        '''
           迷路上のアイテムの座標から一致するItemInfoオブジェクトを返す
        '''
        for item_info in self.item_info_list_:
            if(item_info.get_posi() == item_posi):
                return item_info
        return None
    ############################################################################################設計ミスかな...................これってマネージャーの仕事だよね  今回は許して by sunaga






