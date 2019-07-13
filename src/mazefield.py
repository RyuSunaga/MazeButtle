
#this is GUI file
import tkinter as tk
from config import MAZE_LIST
from config import RIGHT_MOVE,LEFT_MOVE,UP_MOVE,DOWN_MOVE
from config import RIGHT_ATTACK,LEFT_ATTACK,UP_ATTACK,DOWN_ATTACK
from config import SERVER_TO_CLIENT_PACKET
from config import RED, BLUE, GREEN, YELLOW
from config import PACKET_TYPE, PLAYER_ID, PLAYER_NAME, PLAYER_COLOR, PLAYER_HP, POSI,MAZE, PLAYER_INFO_LIST, BULLET_INFO_LIST, ITEM_INFO_LIST, TURN,TEXT
#from maze import Maze
import packet
from packet import ClientToServerPacket, ServerToClientPacket
from mazesocket import MazeClientSocketManager
import threading
#############################################################################

#ガイア　こっから本番だべ頼んだ by sunaga

#############################################################################


HOST = '127.0.0.1'
PORT = 50000
BACKLOG = 10
BUFSIZE = 4096
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
                                PLAYER_HP:5,#これはidを見てこのクラスを保持しているクラスのplayer_idと一致するplayerのhpを入れる
                                PLAYER_INFO_LIST:[{PLAYER_ID:1,PLAYER_NAME:"Gaia",PLAYER_COLOR:RED,POSI:[0,0]},
                                                  {PLAYER_ID:2,PLAYER_NAME:"Nojima",PLAYER_COLOR:BLUE,POSI:[9,9]},
                                                  {PLAYER_ID:3,PLAYER_NAME:"Sunaga",PLAYER_COLOR:YELLOW,POSI:[0,9]}],
                                BULLET_INFO_LIST:[{POSI:[0,2]},{POSI:[4,9]},{POSI:[8,1]},{POSI:[9,6]}],
                                ITEM_INFO_LIST:[]
                                }

        self.next_command_=None

        self.HOST_ = HOST
        self.PORT_ = PORT
        self.BACKLOG_ = BACKLOG
        self.BUFSIZE_ = BUFSIZE
        self.ctsp_ = None
        self.maze_client_socket_manager_ = MazeClientSocketManager(
                                self.HOST_,
                                self.PORT_,
                                self.BACKLOG_,
                                self.BUFSIZE_
                                )
    #########################################################################################ここから下、ガイアが作った関数コピペしたからうまく動かないかも。

    def up_move(self):
        print("up")
        packet.ClientToServerPacket().set_next_command(UP_MOVE)
        return UP_MOVE


    def left_move(self):
        print("left")
        packet.ClientToServerPacket().set_next_command(LEFT_MOVE)
        return LEFT_MOVE

    def right_move(self):
        print("right")
        packet.ClientToServerPacket().set_next_command(RIGHT_MOVE)
        return RIGHT_MOVE

    def down_move(self):
        print("down")
        packet.ClientToServerPacket().set_next_command(DOWN_MOVE)
        return DOWN_MOVE

    def up_attack(self):
        print("up")
        packet.ClientToServerPacket().set_next_command(UP_ATTACK)
        return UP_ATTACK

    def left_attack(self):
        print("left")
        packet.ClientToServerPacket().set_next_command(LEFT_ATTACK)
        return LEFT_ATTACK

    def right_attack(self):
        print("right")
        packet.ClientToServerPacket().set_next_command(RIGHT_ATTACK)
        return RIGHT_ATTACK

    def down_attack(self):
        print("down")
        packet.ClientToServerPacket().set_next_command(DOWN_ATTACK)
        return DOWN_ATTACK

    def create_maze(self,maze):
        root=tk.Tk()
        root.title("迷路")
        canvas=tk.Canvas(master=root,bg="white",height=60*len(maze),width=60*len(maze[0]))
        canvas1=tk.Canvas(master=root,bg="white",height=80,width=250)


        label1=tk.Label(master=root,text="Turn1",font=("メイリオ","44"),bg="#cccccc")
        label1.place(relx=0.45,rely=0.89,relwidth=0.5,relheight=0.1)
        canvas1.grid(row=1,padx=1,pady=1,sticky=tk.W)
        canvas.grid(row=0,padx=2,pady=2)

        canvas1.create_rectangle(10,10,40,70,fill="red")
        canvas1.create_rectangle(60,10,90,70,fill="red")
        canvas1.create_rectangle(110,10,140,70,fill="red")
        canvas1.create_rectangle(160,10,190,70,fill="red")
        canvas1.create_rectangle(210,10,240,70,fill="red")
        wid=0
        for i in maze:
           hei=0
           for j in i:
                if j==1:
                    canvas.create_rectangle(hei*60,wid*60,(hei+1)*60,(wid+1)*60,fill="black")
                elif j==2:
                    canvas.create_polygon(hei*60+15,wid*60+30,hei*60+30,wid*60+15,hei*60+45,wid*60+30,hei*60+30,wid*60+45,fill="blue")
                elif j==3:
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
          btn2=tk.Button(master=canvas,command=self.right_attack,text="→",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn2.place(relx=0.66,rely=0.33,relwidth=0.33,relheight=0.33)
          btn3=tk.Button(master=canvas,command=self.left_attack,text="←",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn3.place(relx=0,rely=0.33,relwidth=0.33,relheight=0.33)
          btn4=tk.Button(master=canvas,command=self.down_attack,text="↓",font=("メイリオ","20"),bg="grey",height=100,width=100)
          btn4.place(relx=0.33,rely=0.66,relwidth=0.33,relheight=0.33)
          canvas.create_rectangle(100,100,200,200,fill="grey")



'''
mf = MazeField("1",1)
root = tk.Tk()
mf.move_player()
mf.attack_player()
mf.create_maze(MAZE_LIST[1])
root.mainloop()
'''
