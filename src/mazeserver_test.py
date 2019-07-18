#mazeserverファイルに含まれるコードのテスト用ファイル
from config import TEST

from MazeServer import GameManager
from MazeServer import PlayerInfoManager



def test1():
    '''
    コンストラクタ
    迷路決定
    PlayerInfoの表示ができるかテストする
    '''
    gm = GameManager()

    gm.preparation_game()

    gm.player_info_maneger.show_all_player_info()

    gm.player_info_maneger.show_player_info(1)


test1()