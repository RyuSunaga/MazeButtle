#this file is server file
from config import MAZE_LIST
from config import W
from config import X,Y
from config import RIGHT,LEFT,UP,DOWN,ATTACK
from config import HOST, PORT, BACKLOG, BUFSIZE
from playerinfo import PlayerInfo 
import random
import socket
import time


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
#print(RIGHT)

#座標変換はこんな感じにすればミスが減ると思う 右へ移動の場合 by sunaga
#posi = [3,6]
#print("現在の座標",posi)

#posi[X] += RIGHT[X]
#posi[Y] += RIGHT[Y]
#print("右へ移動後の座標",posi)

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
        self.id_list = []
        self.ip_name_list = []
        self.player_info_maneger = PlayerInfoManager()
        print("ゲーム開始準備　開始")
        

    def maze_decision(self):
        """
            ゲームで使用する迷路を決定する関数、現在はランダムで選択しているが
            時間に余裕があればプレイヤーの選択で決定してもいいかも。 by sunaga
        """

        #self.maze_ = MAZE_LIST[random.randint(0,2)]
        self.maze_ = MAZE_LIST[0]

        print("迷路決定完了")
        for l in self.maze_:
            print(l)

        return self


    def preparation_game(self):
        """
            ゲーム参加者待ちのサーバー処理参加プレイヤーの名前とipアドレスを受け取り
            それらを使い参加プレイヤーの情報を生成する
            そして参加プレイヤーにゲームで使用する迷路を決定して決定した迷路と各プレイヤーの情報を
            送信する。
            
        """
        #参加申請を受け取り self.ip_nameを設定する
        self.get_participation_command()

        #迷路を決定
        self.maze_decision()
        
        #プレイヤー情報を生成
        self.create_player_info()

        return self

    def get_participation_command(self):
        '''
            プレイヤーのゲーム参加コマンドを受け取り
            各プレイヤーのipと名格をマッピングした辞書を返す。
        '''
        print("通信開始(しない)")

        print("サーバー処理中(してない)")
         ###############################################################未完成####################################################
        #サーバー処理
        #try:
        #    sock.bind((HOST,PORT))
        #    sock.listen(BACKLOG)
    
        #ループは時間と参加人数で制限を書ける
        #start_time_sec = time.time()
        #member_num = 0
        #id = 1

        #while(passed_time_sec < 180 or member_num < 3):

            #conn, address = sock.accept()
            #try:
                #application  = conn.recv(BUFSIZE)
                #msg = b_msg.decode('utf-8')
                #print(msg)
                
                #受け取ったメッセージの内容をみて処理を行う、この時点ではPlayerInfoを返さない
                
                
            #finally:
                #conn.close()

            
            #end_time_sec = time.time()
            
            #paseed_time_sec = end_time_sec - start_time_sec
        
        ###############################################################未完成####################################################
        print("通信終了(してない)")

        #通信を行わないテスト用の値を用意 通信
        self.ip_name_list = [['127.0.0.1',"sawada"],['127.0.0.1',"sunaga"],['127.0.0.1',"nojima"]]
        print("参加プレイヤー")
        for ip_name in self.ip_name_list:
            print(ip_name[1])

        return 

    
    def create_player_info(self):
        '''
            ゲーム開始準備中にプレイヤーから受け取ったipと名前の辞書を受け取り、idと初期座標を設定して
            プレイヤー情報を生成する。
        '''
        
        print("プレイヤー情報生成開始")

        #参加プレイヤーのidのリストを生成
        self.id_list = [id+1 for id in range(len(self.ip_name_list))]

        #参加プレイヤーの名前のリストを生成
        name_list = [ip_name[1] for ip_name in self.ip_name_list]
        print(name_list)
        #迷路の端の座標を設定
        x_min = 0 
        y_min = 0
        x_max = len(self.maze_[0]) -1
        y_max = len(self.maze_) - 1
        maze_edge = [[x_min,y_min],[x_min,y_max],[x_max,y_min],[x_max,y_max]]
        print(maze_edge)
       
        #参加人数分のプレイヤーの位置座標を生成
        player_posi = [maze_edge[i] for i in range(len(self.ip_name_list))]
        print(player_posi)
        
        #参加プレイヤーの情報を生成
        self.player_info_maneger.init_player_info(self.id_list, name_list, player_posi)

        print("プレイヤー情報生成完了")


        return 


    def get_command(self):
        pass



    def pass_info(self):
        pass

    def main(self):
        pass
        
    

class PlayerInfoManager(object):
    """
    GameManagerクラスでPlayerInfoを管理するクラス
    参加プレイヤーの人数分,PlayerInfoクラスをインスタンス変数としてもつ。
    """

    def __init__(self):
        #各参加者のPlayerInfoクラスを格納
        self.player_info_list = []
        self.id_list = []
        

    def init_player_info(self,id_list, name_list, posi_list):
        '''
        ゲームで最初にプレイヤーの情報を生成するときに使う
        参加プレイヤー待ちで取得しname,id情報を持つPlayerInfoクラスを生成する
        ipアドレスはプレイヤーの情報ではなくクライアントの情報なのでPlayerInfoクラスでは保持しない
        '''

        self.id_list = id_list

        for id, name, posi in zip(id_list, name_list, posi_list):
            player_info = PlayerInfo()
            player_info.set_id(id)
            player_info.set_name(name)
            player_info.set_posi(posi)
            self.player_info_list.append(player_info)

        return self

    def get_all_player_info(self):
        '''
            登録されたPlayerInfoクラスを全てリストの形式で取得する
            何も登録されてない場合はNoneを返す。
        '''
        return player_info_list

    def get_player_info(self,id):
        '''
            指定されたidを持つPlayerInfoを取得する
            指定したidをもつプレイヤーが存在しない場合はNoneを返す
        '''
        for player_info in self.player_info_list:
            if(id == player_info.get_id()):
                return player_info
        
        return None

    def show_all_player_info(self):
        '''
           登録されているすべてのプレイヤーの情報を表示する
        '''
        for player_info in self.player_info_list:
            player_info.show_info()

    def show_player_info(self,id):
        '''
            指定されたidを持つプレイヤーの情報を表示する
        '''
        for player_info in self.player_info_list:
            if(id == player_info.get_id()):
                player_info.show_info()
                return 
        
        print("id = " + str(id) + "のプレイヤーは存在ししません。")

    
    def up_data_player_info(self):
        """
            プレイヤーの情報を変更する
            変更する際はidを指定する、idが一致しない場合はfalseを返す
            正常に変更が成功した場合はtrue返す
        """
        pass
   

