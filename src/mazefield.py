
#this is GUI file
import tkinter as tk
from config import MAZE_LIST
from config import RIGHT_MOVE,LEFT_MOVE,UP_MOVE,DOWN_MOVE
from config import RIGHT_ATTACK,LEFT_ATTACK,UP_ATTACK,DOWN_ATTACK
from config import SERVER_TO_CLIENT_PACKET
from config import RED, BLUE, GREEN, YELLOW
from config import PACKET_TYPE, PLAYER_ID, PLAYER_NAME, PLAYER_COLOR, PLAYER_HP,PLAYER_POSI,BULLET_POSI ,MAZE, PLAYER_INFO_LIST, BULLET_INFO_LIST, ITEM_INFO_LIST, TURN,TEXT
#from maze import Maze


#############################################################################

#ガイア　こっから本番だべ頼んだ by sunaga

#############################################################################



class MazeField(object):
    '''
        MazeClientオブジェクトが保持するクラス。
        主な目的は現在のゲームの情報の描画とタッチしたUIからコマンドを生成すること。
        一言でいうとUIと中身のつなぎこみを行うクラス。
    '''

    def __init__(self,text, game_info_data):
        '''

        '''
        self.text_ = text
        #ガイアへ
        #通信処理が正常に実行されると以下のような変数が格納されるから
        #しばらくはこれが入力されたことにして正常に描画できるように実装してくれ
        #変わるのは中身だけだから一回つくれれば使いまわせるよ

        ####################################################################配列は文字列から変換させて作るか,,,
        self.game_info_data_ = {PACKET_TYPE:SERVER_TO_CLIENT_PACKET,
                                TEXT:"のこり一週間頑張ろう!!!!!",
                                MAZE:MAZE_LIST[1],
                                TURN:5,
                                PLAYER_HP:3,#これはidを見てこのクラスを保持しているクラスのplayer_idと一致するplayerのhpを入れる
                                PLAYER_INFO_LIST:[{PLAYER_ID:1,PLAYER_NAME:"Gaia",PLAYER_COLOR:RED,PLAYER_POSI:[2,3]},
                                                  {PLAYER_ID:2,PLAYER_NAME:"Nojima",PLAYER_COLOR:BLUE,PLAYER_POSI:[9,9]},
                                        
                                        {PLAYER_ID:3,PLAYER_NAME:"Sunaga",PLAYER_COLOR:YELLOW,PLAYER_POSI:[0,9]}],
                                BULLET_INFO_LIST:[{BULLET_POSI:[0,2]},{BULLET_POSI:[4,9]},{BULLET_POSI:[8,1]},{BULLET_POSI:[9,6]}],
                                ITEM_INFO_LIST:[]
                                }

    #########################################################################################ここから下、ガイアが作った関数コピペしたからうまく動かないかも。
    def up_move(self):
        print("up")
        return UP_MOVE

    def left_move(self):
        print("left")
        return LEFT_MOVE

    def right_move(self):
        print("right")
        return RIGHT_MOVE

    def down_move(self):
        print("down")
        return DOWN_MOVE

    def up_attack(self):
        print("up")
        return UP_ATTACK

    def left_attack(self):
        print("left")
        return LEFT_ATTACK

    def right_attack(self):
        print("right")
        return RIGHT_ATTACK

    def down_attack(self):
        print("down")
        return DOWN_ATTACK
    
    #bulletの位置をMAZE配列に書き込む関数
    def locate_bullet(self):
        
        maze=self.game_info_data_["MAZE"]
        
        #既存のbulletを消去
        count_row=0
        for i in maze:
            count_col=0
            for j in i:
                if j==2:
                    maze[count_row][count_col]=0
                count_col+=1
            count_row+=1
    
        bullet_list=self.game_info_data_["BULLET_INFO_LIST"]
        
        #新しいbulletを追加
        for i in self.game_info_data_["BULLET_INFO_LIST"]:
            b_posi=i["BULLET_POSI"]
            count_row=0
            for j in maze:
                if count_row==b_posi[0]:
                    count_col=0
                    for k in j:
                        if count_col==b_posi[1]:
                            maze[count_col][count_row]=2
                        count_col+=1
                count_row+=1
                
        self.game_info_data_["MAZE"]=maze
    
    #playerの位置をMAZE配列に書き込む関数
    def locate_player(self):
        maze=self.game_info_data_["MAZE"]
        
        #既存のplayerを消去
        count_row=0
        for i in maze:
            count_col=0
            for j in i:
                if j==3:
                    maze[count_row][count_col]=0
                count_col+=1
            count_row+=1
    
        player_list=self.game_info_data_["PLAYER_INFO_LIST"]
        
        #新しいplayerを追加
        for i in self.game_info_data_["PLAYER_INFO_LIST"]:
            p_posi=i["PLAYER_POSI"]
            print(p_posi)
            count_row=0
            for j in maze:
                if count_row==p_posi[1]:
                    print(count_row)
                    count_col=0
                    for k in j:
                        if count_col==p_posi[0]:
                            print(count_col)
                            maze[count_row][count_col]=3
                        count_col+=1
                count_row+=1
                
        self.game_info_data_["MAZE"]=maze
        print(maze)
            
        
                    
    def create_maze(self,maze):
        root=tk.Tk()
        root.title("迷路")
        
        canvas=tk.Canvas(master=root,bg="white",height=60*len(maze),width=60*len(maze[0]))
        canvas1=tk.Canvas(master=root,bg="white",height=80,width=250)


        label1=tk.Label(master=root,text="Turn"+str(self.game_info_data_["TURN"]),font=("メイリオ","44"),bg="#cccccc")
        label1.place(relx=0.45,rely=0.89,relwidth=0.28,relheight=0.1)
        text1=tk.Text(master=root,state=tk.DISABLED,font=("メイリオ","10"),bg="white")
        text1.configure(width=40,height=10)
        text1.place(relx=0.74,rely=0.89,relwidth=0.25,relheight=0.1)
        canvas1.grid(row=1,padx=1,pady=1,sticky=tk.W)
        canvas.grid(row=0,padx=2,pady=2)
        
        #hpの表示を修正
        for n in range(self.game_info_data_["PLAYER_HP"]):
         canvas1.create_rectangle(10+n*50,10,40+n*50,70,fill="red")
        
        p_info=self.game_info_data_["PLAYER_INFO_LIST"]
        
        wid=0
        for i in maze:
           hei=0
           for j in i:
                if j==1:
                    canvas.create_rectangle(hei*60,wid*60,(hei+1)*60,(wid+1)*60,fill="black")
                elif j==2:
                    canvas.create_polygon(hei*60+15,wid*60+30,hei*60+30,wid*60+15,hei*60+45,wid*60+30,hei*60+30,wid*60+45,fill="blue")
                elif j==3:
                    for k in p_info:
                        p_posi=k["PLAYER_POSI"]
                        #KeyErrorが出る、理由わからん
                        #p_color=k["PLAYER_COLOR"]
                        if p_posi[1]==wid and p_posi[0]==hei:
                            canvas.create_oval(hei*60+5,wid*60+5,(hei+1)*60-5,(wid+1)*60-5,fill="red")                    
                hei+=1
           wid+=1
        root.mainloop()

    def move_player(self):
          root=tk.Tk()
          root.title("移動コマンド")
          canvas=tk.Canvas(master=root,bg="white",height=300,width=300)
          canvas.grid()
          btn1=tk.Button(master=canvas,command=self.up_move,text="↑",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn1.place(relx=0.33,rely=0,relwidth=0.33,relheight=0.33)
          btn2=tk.Button(master=canvas,command=self.right_move,text="→",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn2.place(relx=0.66,rely=0.33,relwidth=0.33,relheight=0.33)
          btn3=tk.Button(master=canvas,command=self.left_move,text="←",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn3.place(relx=0,rely=0.33,relwidth=0.33,relheight=0.33)
          btn4=tk.Button(master=canvas,command=self.down_move,text="↓",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn4.place(relx=0.33,rely=0.66,relwidth=0.33,relheight=0.33)
          canvas.create_rectangle(100,100,200,200,fill="grey")


    def attack_player(self):
          root=tk.Tk()
          root.title("攻撃コマンド")
          canvas=tk.Canvas(master=root,bg="white",height=300,width=300)
          canvas.grid()
          btn1=tk.Button(master=canvas,command=self.up_attack,text="↑",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn1.place(relx=0.33,rely=0,relwidth=0.33,relheight=0.33)
          btn2=tk.Button(master=canvas,command=selfmgame_info.right_attack,text="→",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn2.place(relx=0.66,rely=0.33,relwidth=0.33,relheight=0.33)
          btn3=tk.Button(master=canvas,command=self.left_attack,text="←",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn3.place(relx=0,rely=0.33,relwidth=0.33,relheight=0.33)
          btn4=tk.Button(master=canvas,command=self.down_attack,text="↓",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn4.place(relx=0.33,rely=0.66,relwidth=0.33,relheight=0.33)
          canvas.create_rectangle(100,100,200,200,fill="grey")


mf = MazeField("1",1)
#mf.move_player()
#mf.attack_player()
#mf.root.mainloop()

mf.locate_bullet()
mf.locate_player()
mf.create_maze(MAZE_LIST[1])