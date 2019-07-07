#サーバー側でゲーム上の情報をまとめて管理するために使うクラスを定義する
#今のところ管理する情報はPlayer、Bullet、Mazeの3つの情報
from config import X, Y
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import get_direct_str
from config import OBJECT_INFO,PLAYER_INFO,BULLET_INFO, ITEM_INFO
from config import OBJECT_INFO_MANAGER, PLAYER_INFO_MANAGER, BULLET_INFO_MANAGER, ITEM_INFO_MANAGER
from info import PlayerInfo
from info import BulletInfo

class ObjectInfoManager(object):
    '''
        迷路上のオブジェクトを管理するクラスの親クラス
        オブジェクトのタイプごとに管理するクラスを作る。
        基本的にサーバー側で使うことを想定している。
    '''

    def __init__(self):
        self.manager_type_ = OBJECT_INFO_MANAGER
        self.info_type_ = OBJECT_INFO
        self.object_info_list_ = []

    def set_info(self, object_info):
        '''
            対応する情報を持つクラスを格納する関数
        '''

        if(object_info.get_type() != self.info_type_):
            #格納する変数が対応する情報クラスでなければ入れさせない
            return False
        else:
            self.object_info_list_.append(object_info)
            return True


    def get_all_objectinfo(self):
        '''
            保持しているオブジェクトを全て返す。
        '''
        return self.object_info_list_

    def get_type(self):
        return self.manager_type_

    def show_all_info(self):
        '''
            格納されているすべてのObjectInfo型のObjectの情報を全て表示する。
        '''
        for object_info in self.object_info_list_:
            object_info.show_info()


class PlayerInfoManager(ObjectInfoManager):
    """
    GameManagerクラスでPlayerInfoを管理するクラス
    参加プレイヤーの人数分,PlayerInfoクラスをインスタンス変数としてもつ。
    """

    def __init__(self):
        #各参加者のPlayerInfoクラスを格納
        self.manager_type_ = PLAYER_INFO_MANAGER
        self.id_list = []
        self.is_create_player_info = False


    def init_player_info(self,id_list, name_list, posi_list):
        '''
        ゲームで最初にプレイヤーの情報を生成するときに使う
        参加プレイヤー待ちで取得しname,id情報を持つPlayerInfoクラスを生成する
        ipアドレスはプレイヤーの情報ではなくクライアントの情報なのでPlayerInfoクラスでは保持しない
        '''

        #すでに初期化している場合実行させない。
        if(self.is_create_info == True):
            print("すでにプレイヤー情報は格納されています。")
            return 

        #プレイヤーのid情報を決定
        self.id_list = id_list

        #プレイヤー情報を生成
        for id, name, posi in zip(id_list, name_list, posi_list):
            self.create_player_info(id, nama, posi)

        #フラグ変更
        self.is_create_player_info = True
        print("プレイヤー情報を生成しました。")
        return
    
    def create_player_info(id, name, posi):
        '''
            PlayerInfoオブジェクトを生成する。
        '''
        player_info = PlayerInfo(id, name, posi)
        player_info.set_id(id)
        player_info.set_name(name)
        player_info.set_posi(posi)
        self.set_info(player_info)


    def get_player_info(self,id):
        '''
            指定されたidを持つPlayerInfoを取得する
            指定したidをもつプレイヤーが存在しない場合はNoneを返す
        '''
        for player_info in self.object_info_list_:
            if(player_info.get_id() == id):
                return player_info
        
        return None
   
    def show_player_info(self,id):
        '''
            指定されたidを持つプレイヤーの情報を表示する
        '''
        for player_info in self.object_info_list_:
            if(player_info.get_id() == id):
                player_info.show_info()
                return 
       
        print("id = " + str(id) + "のプレイヤーは存在ししません。")

    
    def update_player_info(self, player_info):
        """
            プレイヤーの情報を変更する
            変更する際はidを指定する、idが一致しない場合はfalseを返す
            正常に変更が成功した場合はtrue返す
        """

        for i in range(len(self.object_info_list_)):
            if(self.player_info_list[i].get_id() == player_info.get_id()):
                self.player_info_list[i].update_player_info(player_info)
                return True
        return False

   

class BulletInfoManager(ObjectInfoManager):
    '''
        迷路上の弾丸オブジェクトを管理するクラス
    '''
    def __init__(self):
        self.manager_type_ = BULLET_INFO_MANAGER

    def get_bullet_info(self, id):
        '''
            指定したidの親を持つBulletオブジェクトを格納したリストを返す
        '''
        bullet_info_list = []
        for bullet_info in self.object_info_list_:
            if(bullet_info.get_parent_id() == id):
                bullet_info_list.append(bullet_info)
        return bullet_info_list

    def show_bullet_info(self, id):
        '''
            指定したidのBulletInfoオブジェクトの情報を全て表示する。    
        '''
        for bullet_info in self.object_info_list_:
            bullet_info.show_info()

    def create_bullet_info(self,id, player_info):
        '''
            新しいBulletオブジェクトを生成する。
        '''
        bullet = BulletInfo(player_info)
        self.set_info(bullet)

    def move_all_bullet(self):
        '''
            全てのBulletオブジェクトの座標を1ターン分進める
        '''
        for bullet in self.object_info_list_:
            bullet.update_posi()

    def delete_bullet(self,id):
        '''
            指定したidのbulletを破棄する。
        '''
        for i in range(len(self.object_info_list_)):
            if(self.object_info_list_[i].get_id() == id):
                del self.object_info_list_[i]
                return
        print("id "+str(id)+"のオブジェクトの破棄に失敗しました")
        return 


class ItemInfoManager(ObjectInfoManager):
    '''
        迷路上のアイテムオブジェクトを管理するクラス。
        これは親クラスで実際にはアイテムごとに管理するクラスを作る。

    '''

    def __init__(self):
        self.managertype_ =  ITEM_INFO_MANAGER


