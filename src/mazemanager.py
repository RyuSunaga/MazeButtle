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
from info import BulletInfo


class MazeManager(object):
    '''
        迷路の情報を扱うクラス
    '''
    
    def __init__(self):
        self.maze_ = None

    def show_maze(self):
        for l in self.maze_:
            print(l)


    def maze_decision(self):
        """
            ゲームで使用する迷路を決定する関数、現在はランダムで選択しているが
            時間に余裕があればプレイヤーの選択で決定してもいいかも。 by sunaga
        """

        #self.maze_ = MAZE_LIST[random.randint(0,2)]
        #テスト中は迷路固定
        self.maze_ = MAZE_LIST[0]
        print("迷路を決定しました。")






