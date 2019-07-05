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
        #次に行うコマンドを保持する、処理を行ったらNoneに戻す
        self.next_command = None

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
