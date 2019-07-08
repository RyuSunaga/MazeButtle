
import config
from config import X, Y
from config import MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACKN
from config import CREATE_BULLET
from config import get_direct_str
from config import OBJECT_INFO,PLAYER_INFO,BULLET_INFO, ITEM_INFO
from config import OBJECT_INFO_MANAGER, PLAYER_INFO_MANAGER, BULLET_INFO_MANAGER, ITEM_INFO_MANAGER
from info import PlayerInfo
from info import BulletInf


class GameInfo(self):
    '''
       ゲームの情報を保持するクラス
       このオブジェクトをパケットに格納してサーバー側からクライアント側に送
       つまりこのオブジェクトはGUIを描画できるだけの情報を保持することになる。
    '''

    def __init__(self):
        self.player_object_info_list_ = []
        self.bullet_object_info_list_ = []
        self.item_object_info_list_ = []
        self.turn_ = None
        self.maze_ = None
        


   