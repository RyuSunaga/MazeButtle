import config
import info
from config import X, Y
from config import W,B,P,I
from config import JOIN, MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import CREATE_BULLET
from config import OBJECT_INFO,PLAYER_INFO,BULLET_INFO, ITEM_INFO
from config import OBJECT_INFO_MANAGER, PLAYER_INFO_MANAGER, BULLET_INFO_MANAGER, ITEM_INFO_MANAGER
from config import PACKET, SERVER_TO_CLIENT_PACKET, CLIENT_TO_SERVER_PACKET
from config import get_direct_str
from maze import Maze
from info import PlayerInfo, BulletInfo, ItemInfo
from infomanager import PlayerInfoManager, BulletInfoManager, ItemInfoManager


########################################################################################　GameInfoはゲーム中一回しか生成しない。　更新し続けるイメージ
class GameInfo(object):
    '''
       ゲームの情報を保持するクラス
       このオブジェクトをパケットに格納してサーバー側からクライアント側に送
       つまりこのオブジェクトはGUIを描画できるだけの情報を保持することになる。
    '''
    #################################
    #Info系オブジェクトはmanagerオブジェクトを使って設定する
    #################################
    def __init__(self, player_info_list, bullet_info_list, item_info_list,turn):
        self.player_info_list_ = player_info_list
        self.bullet_info_list_ = bullet_info_list
        self.item_info_list_ = item_info_list
        self.maze_object_ = Maze()
        self.turn_ = turn

    def inspect_list(self,info_list1, info_list2):
        '''
            二つのリストが上書き可能か調べる-->>>>>>>>>>>>>>>>>>>>>>>>>>>>>とりあえず後で
            調べるのは
            1.配列の長さ ------> PlayerInfo()のリストの場合
            2.オブジェクトのタイプ
        '''
        #if(info_list1[0] == PLAYER_INFO):
        #    if(len(info_list1) != len(info_list2)):
        #        print("プレイヤーオブジェクトの数がそろっていません")
        #        return False
        pass

    def set_player_info_list(self, player_info_list):
        pass

    def set_turn(self, turn):
        self.turn_ = turn

    def get_turn(self):
        return self.turn_

    def get_maze_object(self):
        '''
            迷路オブジェクトを取得
        '''
        return self.maze_object_

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








