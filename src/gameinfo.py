import config
from config import X, Y
from config import W,B,P
from config import MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACKN
from config import CREATE_BULLET
from config import get_direct_str
from config import OBJECT_INFO,PLAYER_INFO,BULLET_INFO, ITEM_INFO
from config import OBJECT_INFO_MANAGER, PLAYER_INFO_MANAGER, BULLET_INFO_MANAGER, ITEM_INFO_MANAGER
from info import PlayerInfo, BulletInfo, ItemInfo
from infomanager import PlayerInfoManager, BulletInfoManager, ItemInfoManager
from info import PACKET, SERVER_TO_CLIENT_PACKET, CLIENT_TO_SERVER_PACKET

class GameInfo(self):
    '''
       ゲームの情報を保持するクラス
       このオブジェクトをパケットに格納してサーバー側からクライアント側に送
       つまりこのオブジェクトはGUIを描画できるだけの情報を保持することになる。
    '''
    def __init__(self):
        self.player_info_list_ = []
        self.bullet_info_list_ = []
        self.item_info_list_ = []

        #ゲームのターン数を保持する
        self.turn_ = None
        #self.maze_は0,W,B,Pの4つのうちのどれかが渡される。
        self.maze_ = None

    def get_turn(self):
        return self.turn_

    def get_maze(self):
        '''
            迷路の座標情報を取得する
        '''
        return self.maze_
        
    ############################################################################################設計ミスかな...................これってマネージャーの仕事だよね  
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
    ############################################################################################設計ミスかな...................
    






