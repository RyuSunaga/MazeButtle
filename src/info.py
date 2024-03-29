#迷路上のオブジェクトを定義する＋クラス
import time
import config
import config
from config import X, Y
from config import W,B,P,I
from config import RIGHT, LEFT, UP, DOWN
from config import JOIN, MOVE, ATTACK
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import CREATE_BULLET
from config import OBJECT_INFO, PLAYER_INFO, BULLET_INFO, ITEM_INFO
from config import get_direct_str
from config import PLAYER_INFO, BULLET_INFO, ITEM_INFO
from config import PACKET_TYPE, PLAYER_ID, PLAYER_NAME, PLAYER_COLOR, PLAYER_HP, PLAYER_POSI,BULLET_POSI,MAZE, PLAYER_INFO_LIST, BULLET_INFO_LIST, ITEM_INFO_LIST, TURN,TEXT,NEXT_COMMAND
from config import TEST


#################################     メモ     #######################################################

#迷路上のオブジェクトって弾丸とプレイヤー以外になんかあるかな????
#例えばスピードアップするアイテムとか?

####何か案があったらここにコメントアウトして書いてほしい


#################################     メモ     #######################################################



class ObjectInfo(object):
    '''
        迷路上のオブジェクトの情報クラスの親クラス。
        今のところ用意するオブジェクトはPlayerとItemとBullet
    '''
    def __init__(self, id, posi):
        #オブジェクト毎に一意のidを設定する。
        self.id_ = id
        self.posi_ = [posi[X],posi[Y]]
        self.object_type_ = OBJECT_INFO

    def __del__(self):
        '''
            子クラスからデストラクタって実行されるのかな？
            実行されてほしい
            だめだったら子クラスで再定義
        '''
        print("id" + str(self.id_) + "の" + self.object_type_ + "を破棄しました。")

    def set_id(self, id):
        self.id_ = id

    def set_posi(self,posi):
        self.posi_[X] = posi[X]
        self.posi_[Y] = posi[Y]

    def get_id(self):
        return self.id_

    def get_posi(self):
        return self.posi_

    def get_object_type(self):
        return self.object_type_

    def show_info(self):
        print("--------------------------------------------------------------")
        print("ObjectType",self.object_type_)
        print("--------------------------------------------------------------")

        

class PlayerInfo(ObjectInfo):
    """
        ObjectInfoの子クラス
        プレイヤーの情報を扱うためのクラス
    """
    def __init__(self,id, name,color, posi):
        super().__init__(id, posi)

        self.object_type_ = PLAYER_INFO
        self.name_ = name
        self.color_ = color
        self.hp_ = 5
        #self.posi_ = [None,None]
        self.power_ = 1
        self.speed_ = 1
        #次に行うコマンドを保持する、処理を行ったらNoneに戻す
        self.next_command_ = None
        
        #次のコマンドのタイプ（移動か攻撃）と座標を設定
        self.next_command_type_ = None
        self.next_command_direct_ = [None,None]

        #移動前の座標を保持しておく
        self.last_posi_ = posi

        #最新の情報
        self.state_text_ = None

    ##########################################プレイヤー情報を設定するための関数##############################################
 

    def set_name(self, name):
        self.name_ = name

    def set_color(self,color):
        self.color_ = color
       
    def set_hp(self,hp):
        self.hp_ = hp
        
    def set_power(self, power):
        self.power_ = power
        
    def set_speed(self, speed):
        self.speed_ = speed

    def set_next_command(self,command):
        self.next_command_ = command
       

    def set_next_command_type(self, command):
        '''
            コマンド毎にコマンドのタイプを決定する
        '''
        print("aaaaa")
        if(command == JOIN):
            self.next_command_type_ = JOIN
        elif(command == RIGHT_MOVE or command  == LEFT_MOVE or command == UP_MOVE or command == DOWN_MOVE):
            self.next_command_type_ = MOVE
        elif(command == RIGHT_ATTACK or command  == LEFT_ATTACK or command == UP_ATTACK or command == DOWN_ATTACK):
            self.next_command_type_ = ATTACK
        else:
            self.next_command_type_ = None

    def set_next_command_direct(self, command):
        '''
            コマンド毎にコマンドを実行する方向を決定する
        '''
        if(command == RIGHT_ATTACK or command == RIGHT_MOVE):
            self.next_command_direct_ = RIGHT
        elif(command == LEFT_ATTACK or command == LEFT_MOVE):
            self.next_command_direct_ = LEFT 
        elif(command == UP_ATTACK or command == UP_MOVE):
            self.next_command_direct_ = UP
        elif(command == DOWN_ATTACK or command == DOWN_MOVE):
            self.next_command_direct_ = DOWN
        else:
            #方向無し
            self.next_command_direct_ = [0,0]
        print(self.next_command_direct_)

    def set_state_text(self,text):
        self.state_text_ = text

    ##########################################ここまでプレイヤー情報を設定するための関数##############################################

    
    ##########################################プレイヤー情報を取得するための関数##############################################


    def get_name(self):
        return self.name_

    def get_color(self):
        return self.color_

    def get_hp(self):
        return self.hp_

    def get_power(self):
        return self.power_

    def get_speed(self):
        return self.speed_

    def get_next_command(self):
        return self.next_command_
    
    def get_next_command_type(self):
        return self.next_command_type_

    def get_next_command_direct(self):
        return self.next_command_direct_

    def get_dict_send_data(self):
        '''
            PlayerInfoを通信で使える形に変更する(辞書型) -> 文字列じゃない!!!!
        '''
        send_player_data = {}
        send_player_data[PLAYER_ID] = self.id_
        send_player_data[PLAYER_NAME] = self.name_
        send_player_data[PLAYER_HP] = self.hp_
        send_player_data[PLAYER_COLOR] = self.color_
        send_player_data[PLAYER_POSI] = self.posi_
        print("PlayerInfoの通信用データを生成しました。")
        return send_player_data

    def get_state_text_(self):
        return self.state_text_

    ##########################################ここまでプレイヤー情報を設定するための関数##############################################
        
    def show_info(self):
        '''
            playerの情報をすべて表示する関数
        '''
        print("--------------------------------------------------------------")
        print("ObjectType",self.object_type_)
        print("ID:",self.id_)
        print("Name:",self.name_)
        print("Color:",self.color_)
        print("HP:",self.hp_)
        print("(X, Y):",self.posi_)
        print("Power:",self.power_)
        print("Speed:",self.speed_)
        print("NextCommand:",self.next_command_)
        print("NextCommandType:",self.next_command_type_)
        print("NextCommandDict:",self.next_command_direct_)
        print("--------------------------------------------------------------")

    def prepare_next_command(self, command):
        '''
            受け取ったコマンドを実行するための準備をする。
        '''

        #次のコマンドを設置する
        self.set_next_command(command)
       
        #コマンドのタイプを設定する
        self.set_next_command_type(command)

        #コマンドの方向を設定する
        self.set_next_command_direct(command)

    def execute_next_command(self, command):
         '''
            コマンドを実行するためのコマンドを返す
            移動ならMOVE
            攻撃ならATTACK
            を返す。
            実際の行動はマネージャークラスが行う
         '''
         self.prepare_next_command(command)
         return self.next_command_type_

    def update_posi(self):
         '''
            この関数はmanagerクラスから実行される
            設定されているnext_commandの情報をもとにプレイヤーの位置を更新する。
         '''
         next_posi = [self.posi_[X] + self.next_command_direct_[X], self.posi_[Y] + self.next_command_direct_[Y]]
         if(not(0 <= next_posi[X] and next_posi[X] <= 9)):
             print("そこには移動できません")
             self.last_posi_ = self.posi_
             return
         if(not(0 <= next_posi[Y] and next_posi[Y] <= 9)):
             print("そこには移動できません")
             self.last_posi_ = self.posi_
             return
         self.last_posi_ = self.posi_
         self.posi_ = next_posi
         print("Name " + self.name_ + "の位置情報を更新しました。")

    def get_last_posi(self):
        return self.last_posi_

    def back_last_posi(self):
        '''
            衝突処理などで元の座標に戻りたいとき使う
        '''
        print(self.name_,"を最後にいた座標に戻します。")
        self.posi_ = self.last_posi_
        print("Name " + self.name_ + "の位置情報を更新しました。")

    def decrease_hp(self,damage):
        '''
            ダメージ分HPを減らす
        '''
        print(self.name_,"のHPを",damage,"減らします。")
        #time.sleep(5)
        self.hp_ -= damage
        
    def clear_next_command(self):
        '''
            設定されているコマンドが実行されたら使う
            設定してあるコマンドを全て消去
        '''
        self.next_command_ = None
        self.next_command_type_ = None
        self.next_command_direct_[X] = None
        self.next_command_direct_[Y] = None
        
    ########################################################################なんかこの関数使いたくない################
    def update_player_info(self,player_info):
        '''
            受け取ったPlayerInfoクラスのインスタンス変数でこの
            クラスのインスタンス変数を変更する。
        '''
      
        self.id_ = player_info.get_id()
        self.name_ = player_info.get_name()
        self.color_ = player_info.get_color()
        self.hp_ = player_info.get_hp()
        self.posi_ = player_info.get_posi() 
        self.speed_ = player_info.get_speed()
        self.power_ = player_info.get_power()
        print(self.name_ + "の情報を変更しました")

    ########################################################################なんかこの関数使いたくない################



class BulletInfo(ObjectInfo):
    """
        弾丸オブジェクト
        打ったプレイヤーのid,座標、飛んでいく方向,攻撃力,速さの情報を保持する
        今のところ弾丸はプレイヤーのspeedと同じ
    """

    def __init__(self,id, player_info, extra_info = None):
        """
            extre_infoは弾丸に情報をつけ足すとき使う。
            いまは実装の予定なし。
        """
        super().__init__(id,[0,0])

        self.object_type_ = BULLET_INFO
        #プレイヤーの位置情報を取得
        player_posi = player_info.get_posi()
        #コマンドが飛んでいく方向をベクトルで表している
        self.direct_ = player_info.get_next_command_direct()
        self.parent_id_ = player_info.get_id()
        self.posi_ = [player_posi[X]+self.direct_[X], player_posi[Y]+self.direct_[Y]]
        self.power_ = player_info.get_power()
        self.speed_ = player_info.get_speed()

    def __del__(self):
        print("Parent ID " + str(self.parent_id_) + "のBulletオブジェクトを破棄します")

    def set_parent_id(self, parent_id):
        self.parent_id_ = parent_id

    def set_direct(self, direct):
        self.direct_ = direct

    def set_power(self, power):
        self.power_ = power

    def set_speed(self, speed):
        self.speed_ = speed

    def get_parent_id(self):
        return self.parent_id_

    def get_direct(self):
        return self.direct_

    def get_power(self):
        return self.power_

    def get_speed(self):
        return self.speed_

    def get_dict_send_data(self):
        '''
            PlayerInfoを通信で使える形に変更する(辞書型) -> 文字列じゃない!!!!
        '''
        send_bullet_data = {}
        send_bullet_data[BULLET_POSI] = self.posi_
        print("BulletInfoの通信用データを生成しました。")
        return send_bullet_data


    def show_info(self):
        '''
            playerの情報をすべて表示する関数
        '''

        print("--------------------------------------------------------------")
        print("ObjectType",self.object_type_)
        print("ObjectID",self.id_)
        print("Parent ID:",self.parent_id_)
        print("Posi:(X, Y):",self.posi_)
        print("Direct:",self.direct_)
        print("Power:",self.power_)
        print("Speed:",self.speed_)
        print("--------------------------------------------------------------")

    def update_posi(self):
        """
            インスタンス変数の情報から、弾丸を次のターンの座標へ移動する。
        """
        
        self.posi_ = [self.posi_[X] + self.direct_[X], self.posi_[Y] + self.direct_[Y]]
        print("Parent ID " + str(self.parent_id_) + "の弾丸の座標の更新に成功しました。")

    def is_posi_error(self):
        '''
            座標が迷路外ならばTrue
            そうでないならばFalseを返す
        '''
        if(not(0 <= self.posi_[X] and self.posi_[X] <= 9)):
             print("弾丸座標エラー")
             return True
        if(not(0 <= self.posi_[Y] and self.posi_[Y] <= 9)):
             print("弾丸座標エラー")
             return True
        print("弾丸の座標は正常です。")
        return False 
         

class ItemInfo(ObjectInfo):
    '''
        迷路上のアイテムの親クラス
    '''
    def __init__(self):
        self.object_type_ = ITEM_INFO
        self.item_type_ = None

    def get_item_type(self):
        return self.item_type_




