#迷路上のオブジェクトを定義するクラス
from config import X, Y
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import get_direct_str

#################################     メモ     #######################################################

#迷路上のオブジェクトって弾丸とプレイヤー以外になんかあるかな????
#例えばスピードアップするアイテムとか?

####何か案があったらここにコメントアウトして書いてほしい


#################################     メモ     #######################################################



class PlayerInfo(object):
    """
        プレイヤーの情報を扱うためのクラス
    """
    def __init__(self):
        self.id_ = None
        self.name_ = None
        self.hp_ = 10
        self.posi_ = [None,None]
        self.power_ = 1
        self.speed_ = 1
        #次に行うコマンドを保持する、処理を行ったらNoneに戻す
        self.next_command = None

    ##########################################プレイヤー情報を設定するための関数##############################################
    def set_id(self, id):
        self.id_ = id

    def set_name(self, name):
        self.name_ = name
       
    def set_hp(self,hp):
        self.hp_ = hp
        
    def set_posi(self,posi):
        self.posi_[X] = posi[X]
        self.posi_[Y] = posi[Y]
        
    def set_power(self, power):
        self.power_ = power
        
    def set_speed(self, speed):
        self.speed_ = speed
        
    def set_command(self,command):
        #configファイルにあるコマンドの形で受け取る
        self.last_command_ = command

    ##########################################ここまでプレイヤー情報を設定するための関数##############################################

    
    ##########################################プレイヤー情報を取得するための関数##############################################

    def get_id(self):
        return self.id_

    def get_name(self):
        return self.name_

    def get_hp(self):
        return self.hp_

    def get_posi(self):
        return self.posi_

    def get_power(self):
        return self.power_

    def get_speed(self):
        return self.speed_

    def get_coomand(self):
        return self.last_command_
    ##########################################ここまでプレイヤー情報を設定するための関数##############################################
        
    def show_info(self):
        '''
            playerの情報をすべて表示する関数
        '''
        print("--------------------------------------------------------------")
        print("Player Infomation")
        print("ID:",self.id_)
        print("Name:",self.name_)
        print("HP:",self.hp_)
        print("(X, Y):",self.posi_)
        print("Power:",self.power_)
        print("Speed:",self.speed_)
        print("--------------------------------------------------------------")


    def update_player_info(self,player_info):
        '''
            受け取ったPlayerInfoクラスのインスタンス変数でこの
            クラスのインスタンス変数を変更する。
        '''
      
        self.id_ = player_info.get_id()
        self.name_ = player_info.get_name()
        self.hp_ = player_info.get_hp()
        self.posi_ = player_info.get_posi() 
        self.speed_ = player_info.get_speed()
        self.power_ = player_info.get_power()
        print(self.name_ + "の情報を変更しました")


class BulletInfo(object):
    """
        弾丸オブジェクト
        打ったプレイヤーのid,座標、飛んでいく方向,攻撃力,速さの情報を保持する
        今のところ弾丸はプレイヤーのspeedと同じ
    """

    def __init__(self,player_info, extra_info = None):
        """
            extre_infoは弾丸に情報をつけ足すとき使う。
            いまは実装の予定なし。
        """
        #プレイヤーの位置情報を取得
        player_posi = player_info().get_posi()
        #コマンドが飛んでいく方向をベクトルで表している
        self.direct_ = player_info().get_command()
        
        self.parent_id_ = player_info.get_id()
        self.posi_ = [player_posi[X]+direct[X], player_posi[Y]+direct[Y]]
        self.power_ = player_info.get_power()
        self.speed_ = player_info.get_speed()

    def __del__(self):
        print("Parent ID " + str(self.parent_id_) + "のBulletオブジェクトを破棄します")

    def set_parent_id(self, parent_id):
        self.parent_id_ = parent_id

    def set_posi(self, posi):
        self.posi_ = posi

    def set_direct(self, direct):
        self.direct_ = direct

    def set_power(self, power):
        self.power_ = power

    def set_speed(self, speed):
        self.speed_ = speed

    def get_parent_id(self):
        return self.parent_id_

    def get_posi(self):
        return self.posi_ 

    def get_direct(self):
        return self.direct_

    def get_power(self):
        return self.power_

    def get_speed(self):
        return self.speed_

    def show_info(self):
        '''
            playerの情報をすべて表示する関数
        '''

        print("--------------------------------------------------------------")
        print("Bullet Infomation")
        print("Parent ID:",self.parent_id_)
        print("Posi:(X, Y):",self.get_posi())
        print("Direct:",get_direct_str(self.set_direct))
        print("Power:",self.power_)
        print("Speed:",self.speed_)
        print("--------------------------------------------------------------")

    def update_posi(self):
        """
            インスタンス変数の情報から、弾丸を次のターンの座標へ移動する。
        """
        
        self.posi_ = [self.posi_[X] + self.get_direct_[X], self.posi_[Y] + self.direct_[Y]]
        print("Parent ID " + str(self.parent_id_) + "の弾丸の座標の更新に成功しました。")