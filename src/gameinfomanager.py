#ゲーム全体を管理するクラス
import packet
from config import W,B,P,I
from config import X,Y
from config import COLORS
from config import HOST,PORT
from config import MAZE_LIST
from config import JOIN
from config import RED, BLUE, GREEN, YELLOW
from config import JOIN, MOVE, ATTACK
from config import RIGHT, LEFT, UP, DOWN
from config import RIGHT_MOVE, LEFT_MOVE, UP_MOVE, DOWN_MOVE
from config import RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, DOWN_ATTACK
from config import OBJECT_INFO, PLAYER_INFO, BULLET_INFO, ITEM_INFO
from config import PACKET_TYPE, PLAYER_ID, PLAYER_NAME, PLAYER_COLOR, PLAYER_HP, PLAYER_POSI,BULLET_POSI,MAZE, PLAYER_INFO_LIST, BULLET_INFO_LIST, ITEM_INFO_LIST, TURN,TEXT,NEXT_COMMAND
from config import CLIENT_TO_SERVER_PACKET, SERVER_TO_CLIENT_PACKET
from maze import Maze
from info import PlayerInfo, BulletInfo, ItemInfo
from infomanager import PlayerInfoManager, BulletInfoManager, ItemInfoManager
from gameinfo import GameInfo
from packet import ServerToClientPacket, ClientToServerPacket
from mazesocket import MazeServerSocketManager, MazeClientSocketManager
import random
import socket
import time


class GameInfoManager(object):
    """
    ゲーム全体の情報を管理するクラス
    """
    
    def __init__(self):
        #オブジェクトのidを管理する
        self.id_list_ = []
        #ipが同じ可能性があるのでリストに格納する--->いるか？
        self.ip_name_list_ = []
        self.is_init_game_ = False
        self.maze_ = None
        self.turn_ = 0
        self.player_info_manager_ = PlayerInfoManager()
        self.bullet_info_manager_ = BulletInfoManager()
        self.item_info_manager_ = ItemInfoManager()
        self.game_info_ = GameInfo()#------------------------------------------------->こいつの管理がメイン
        self.server_to_client_data_ = None
        self.client_to_server_data_ = None
        print("GameInfoManagerオブジェクトを生成しました。")

    def set_maze(self,maze):
        self.maze_ = maze

    def set_turn(self,turn):
        self.turn_ = turn

    def set_player_info_manager(self,player_info_manager):
        self.player_info_maneger_ = player_info_manager

    def set_bullet_info_manager(self,bullet_info_manager):
        self.bullet_info_maneger_ = bullet_info_manager

    def set_item_info_manager(self, item_info_manager):
        self.item_info_manager_ = item_info_manager

    def set_game_info(self,game_info):
        '''
            これを使うことはない
        '''
        pass
        
    def set_server_to_client_data(self,server_to_client_data):
        '''
            これを使うことはない
        '''
        self.server_to_client_data_ = server_to_client_data

    def set_client_to_server_data(self,client_to_server_data):
        print("GIMが新しいプレイヤーの情報を受け取りました。")
        self.client_to_server_data_  = client_to_server_data

    def get_maze(self):
        return self.maze_ 

    def get_turn(self):
        return self.turn_

    def get_player_info_manager(self):
        return self.player_info_maneger_

    def get_bullet_info_manager(self):
        return self.bullet_info_maneger_ 

    def get_item_info_manager(self):
        return self.item_info_manager_

    def get_game_info(self):
        '''
            これも使いたくない が　使い
        '''
        print("新しいGameInfoオブジェクトをMazeserverクラスに渡します。")
        return self.game_info_
        
    def get_server_to_client_data(self):
        '''
            これ使わないかも
        '''
        return self.server_to_client_data_

    def get_client_to_server_data(self):
        return self.client_to_server_data_

    def create_player_info(self):
        '''
            ゲーム開始準備中にプレイヤーから受け取ったipと名前の辞書を受け取り、idと初期座標を設定して
            プレイヤー情報を生成する。
        '''
        
        print("プレイヤー情報生成開始")
        name_list = []
        color_list = []
        maze_edge = []
        posi_list = []

        #迷路の端の座標を設定
        x_min = 0
        y_min = 0
        x_max = len(self.maze_[0]) -1
        y_max = len(self.maze_) - 1
        maze_edge = [[x_min,y_min],[x_min,y_max],[x_max,y_min],[x_max,y_max]]

        for id, player_dict in enumerate(self.client_to_server_data_):
            self.id_list_.append(id)
            name_list.append(player_dict[PLAYER_NAME])
            color_list.append(COLORS[id])
            posi_list.append(maze_edge[id])
            #print(player_dict)
        #参加プレイヤーの情報を生成
        self.player_info_manager_.init_player_info(self.id_list_, name_list,color_list, posi_list)

        print("プレイヤー情報生成完了")


    def up_date_game(self):
        '''
            セットされた情報をもとにゲームの情報を更新する
        '''
        if(self.client_to_server_data_ == None):
            print("クライアント側からの情報がセットされていません。")
            return 
        if(self.is_init_game_ == False):
            #完成まではランダムに決めない
            #self.maze_ = MAZE_LIST[random.randint(0,2)]
            self.maze_ = MAZE_LIST[1]
            print("迷路を決定しました。")
            self.create_player_info()
            print("ゲームの情報を生成しました。")
            self.is_init_game_ = True

        else:
            self.up_date_all_object_info()
            
        self.turn_ += 1
        self.game_info_ = GameInfo()
        self.game_info_.set_maze(self.maze_)
        self.game_info_.set_turn(self.turn_)
        self.game_info_.set_player_info_list(self.player_info_manager_.get_all_object_info())
        self.game_info_.set_bullet_info_list(self.bullet_info_manager_.get_all_object_info())
        self.game_info_.set_item_info_list(self.item_info_manager_.get_all_object_info())
        print("ゲームの情報を更新しました。")
        return

    def set_all_player_command(self):
        '''
            サーバーから受け取ったプレイヤーのコマンドを設定する。
        '''
        for player_info in self.client_to_server_data_:
            id = player_info[PLAYER_ID]
            next_command = player_info[NEXT_COMMAND]
            print(id,next_command)
            self.player_info_manager_.set_next_command(id,next_command)
        print("すべてのプレイヤーの次のコマンドをセットしました")
        

    def create_id(self):
        '''
            まだ生成されていないidを生成して返す
        '''
        #とりあえず1000個までオブジェクト作れるようにしておこう
        for id in range(1000):
            if(not(id in self.id_list_)):
                self.id_list_.append(id)
                print("id = ",id,"を生成しました。")
                return id
        print("これ以上idを生成できませんでした。")
        return -1

    def delete_id(self,id):
        '''
            指定したidを削除する
        '''
        self.id_list_.remove(id)
        print("id = ",id,"を削除しました。")

    def up_date_all_object_info(self):
        '''
            ゲーム上のすべての情報を更新する
        '''
        print("ゲームの情報を更新します。")
        
        ###################################################################################ここの処理まだ不安
        #弾丸を生成してから移動させるのは面倒なので最初に弾丸を移動させる
        print("全ての弾丸の座標を移動させます。")
        bullet_info_list = self.bullet_info_manager_.get_all_object_info()
        for i in range(len(bullet_info_list)):
            bullet_info = bullet_info_list[i]
            bullet_info.update_posi()
            if(bullet_info.is_posi_error()):
                id = bullet_info.get_id()
                self.bullet_info_manager_.delete_object_info(id)
                self.delete_id(id)
            else:
                self.bullet_info_manager_.update_object_info(bullet_info)
        ################################################################################################


        #########################################################################################################プレイヤーのコマンドを実行
        self.set_all_player_command()
        print("すべてのプレイヤーオブジェクトのコマンドを実行します")
        player_info_list = self.player_info_manager_.get_all_object_info()
        for i in range(len(player_info_list)):
            player_info = player_info_list[i]
            command_type = player_info.get_next_command_type()
            if(command_type == JOIN):
                #############################これ起こりえない
                print(JOIN)
                pass
            elif(command_type == MOVE):
                print(MOVE)
                #print(player_info.get_posi())
                #print(player_info.get_next_command())
                player_info.update_posi()
                player_info_manager_.update_object_info(player_info)
                #print(player_info.get_posi())
            elif(command_type == ATTACK):
                print(ATTACK)
                id = self.create_id()
                self.bullet_info_manager_.create_bullet_info(id,player_info)
                #print(len(self.bullet_info_manager_.get_all_object_info()))
                self.bullet_info_manager_.object_info_list_[-1].show_info()
                bullet_info = self.bullet_info_manager_.object_info_list_[-1]
                if(bullet_info.is_posi_error()):
                    id = bullet_info.get_id()
                    self.bullet_info_manager_.delete_object_info(id)
                    self.delete_id(id)
                else:
                    self.bullet_info_manager_.update_object_info(bullet_info)
                #print(len(self.bullet_info_manager_.get_all_object_info()))

                #self.bullet_info_manager_.object_info_list_[-1].update_posi()
                #self.bullet_info_manager_.object_info_list_[-1].show_info()
            else:
                print("何もコマンドがない")
        ############################################################################################################

        ##############################################################################################################全てのオブジェクトの変化後の座標位置をもとに処理を行う
        print("全てのオブジェクトの座標を更新しました。")
        print("衝突処理に入ります。")

        #きれいではないけど時間がないから以下の方法でやる
        maze_object_dict = [[{PLAYER_INFO:[],BULLET_INFO:[]} for y in range(10)] for x in range(10)]
        
        player_info_list = self.player_info_manager_.get_all_object_info()
        for player_info in player_info_list:
            object_type = player_info.get_object_type()
            posi = player_info.get_posi()
            x = posi[X]
            y = posi[Y]
            maze_object_dict[x][y][object_type].append(player_info)
        bullet_info_list = self.bullet_info_manager_.get_all_object_info()
        for bullet_info in bullet_info_list:
            object_type = bullet_info.get_object_type()
            posi = bullet_info.get_posi()
            x = posi[X]
            y = posi[Y]
            maze_object_dict[x][y][object_type].append(bullet_info)
        
        ####TEST
        #for x in range(10):
        #    for y in range(10):
        #        print("x,y",x,y)
        #        dic = maze_object_dict[x][y]
        #        print(dic)
        #        for player_info in dic[PLAYER_INFO]:
        #            player_info.show_info()
        #        for bullet_info in dic[BULLET_INFO]:
        #            bullet_info.show_info()
        ####TEST


        ##############################################################################################################


        return







