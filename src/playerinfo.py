from config import X,Y

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
        

    ##########################################プレイヤー情報を設定するための関数##############################################
    def set_id(self, id):
        self.id_ = id

    def set_name(self, name):
        self.name_ = name
        

    def set_hp(self,hp):
        self.hp = hp
        

    def set_posi(self,posi):
        self.posi_[X] = posi[X]
        self.posi_[Y] = posi[Y]
        

    def set_power(self, power):
        self.power = power
        

    def set_speed(self, speed):
        self.speed = speed
        

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

    ##########################################ここまでプレイヤー情報を設定するための関数##############################################
        
    def show_info(self):
        '''
            playerの情報をすべて表示する関数
        '''
        print("--------------------------------------------------------------")
        print("ID:",self.get_id())
        print("Name:",self.get_name())
        print("HP:",self.get_hp())
        print("(X, Y):",self.get_posi())
        print("Power:",self.get_power())
        print("Speed:",self.get_speed())
        print("--------------------------------------------------------------")

        return