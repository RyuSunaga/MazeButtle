#this file is server file
from config import NOJIMA_MAZE,GAIA_MAZE,SUNAGA_MAZE
from config import W
from config import X,Y
from config import RIGHT,LEFT,UP,DOWN,ATTACK

##############################################################################################################

#命名規則について by sunaga

# file名　　　　　　　　全て小文字でなるべく短く　       myfile
# クラス名　　　　　　　最初大文字、大文字区切り　　　   ThisIsMyClass
# 関数名、メソッド名　　全小文字、アンダースコア区切り   this_is_my_func
# 変数名　　　　　　　　全小文字、アンダースコア区切り   this_is_my_val
# 定数名                全大文字、アンダースコア区切り　 THIS_IS_MY_CONST

# 自クラス内でのみ使用する内部変数と内部メソッドはアンダースコアで開始


##############################################################################################################


#test
print(RIGHT)

#座標変換はこんな感じにすればミスが減ると思う 右へ移動の場合 by sunaga
posi = [3,6]
print("現在の座標",posi)

posi[X] += RIGHT[X]
posi[Y] += RIGHT[Y]
print("右へ移動後の座標",posi)

##############################################################################################################




class GameManager(object):
    """
    ゲーム全体を管理するクラス
    主な処理は
        1.ゲーム開始前のプレイヤーの参加コマンドの受け取り
        2.参加者情報の設定
        3.迷路の決定及び参加者の配置
        4.参加者のコマンドを受け取る
        5.受け取ったコマンドを使い参加者の情報を更新する -> PlayerInfoManager()クラスを使う 
        6.更新した情報を参加者に返す -> 勝敗が決まらなければ4に戻る
        7.勝敗が決まったら結果を参加者に返す
    """
    
    def __init__(self):
        pass

    def preparation_game(self):
        pass

    def get_participation_command(self):
        pass

    def get_command(self):
        pass

    def up_data_player_info(self):
        pass

    def pass_player_info(self):
        pass

    def main(self):
        pass
        


class PlayerInfoManager(object):
    """
    GameManagerクラスでプレイヤーの情報を管理するクラス
    参加プレイヤーの人数分,PlayerInfoクラスをインスタンス変数としてもつ。
    """

    def __init__(self,id_list, name_list ,posi_list):
        self.player_info_list = []

        #参加プレイヤー分のPlayerInfoクラスを生成
        for id in range(len(id_list)):
            player_info_list.append(PlayerInfo(id_list[id],name_list[id],posi_list[id]))


    def up_data_player_info(self):
        """
            プレイヤーの情報を変更する
            変更する際はidを指定する、idが一致しない場合はfalseを返す
            正常に変更が成功した場合はtrue返す
        """
        pass
   

class PlayerInfo(object):
    """
        プレイヤーの情報を保持するためのクラス
    """
    def __init__(self,id,name,posi):
        self.id_ = id
        self.name_ = name
        self.hp = 100
        self.posi = posi
        self.power = 1
        self.spee = 1
