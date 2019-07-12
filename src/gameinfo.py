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
    def __init__(self):
        self.maze_ = None
        self.turn_ = None
        self.player_info_list_ = None
        self.bullet_info_list_ = None
        self.item_info_list_ = None


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

    def set_maze(self, maze):
        self.maze_ = maze

    def set_turn(self, turn):
        self.turn_ = turn

    def set_player_info_list(self, player_info_list):
        self.player_info_list_ = player_info_list

    def set_bullet_info_list(self, bullet_info_list):
        self.bullet_info_list_ = bullet_info_list

    def set_item_info_list(self, item_info_list):
        self.item_info_list_ = item_info_list

    def get_maze(self):
        return self.maze_

    def get_turn(self):
        return self.turn_

    def get_player_info_list(self):
        return self.player_info_list_

    def get_bullet_info_list(self):
        return self.bullet_info_list_

    def get_item_info_list(self):
        return self.item_info_list_


