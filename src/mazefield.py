
#this is GUI file
import tkinter as tk
from config import MAZE_LIST
from maze import Maze

def create_line(canvas,x,y,d,l):
    if d=="ver":
        for i in range(l):
            canvas.create_line(x,y,x,y+60*l,fill="black")
    elif d=="flat":
        for i in range(l):
            canvas.create_line(x,y,x+60*l,y,fill="black")

def create_maze(maze):
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
            hei+=1
        wid+=1
         


root=tk.Tk()
root.title("sample")
root.geometry()




create_maze(MAZE_LIST[0])

#canvas.create_oval(0,0,100,100,fill="orange")
#canvas.create_oval(700,700,630,630,fill="blue")
#create_line(canvas,100,0,"ver",3)
#create_line(canvas,100,300,"flat",1)
#create_line(canvas,300,0,"ver",1)
#create_line(canvas,200,100,"flat",2)
#create_line(canvas,300,200,"ver",1)
#create_line(canvas,200,200,"flat",1)
#create_line(canvas,400,200,"ver",1)
#create_line(canvas,400,300,"flat",1)
#create_line(canvas,500,400,"ver",1)
#create_line(canvas,500,100,"ver",1)
#create_line(canvas,500,100,"flat",1)
#create_line(canvas,600,100,"ver",2)
#create_line(canvas,700,100,"ver",3)
#canvas.create_polygon(((250,0),(200,98),(300,98)),fill="green")
#canvas.create_polygon(((550,100),(500,198),(600,198)),fill="green")


root.mainloop()


#############################################################################

#ガイア　こっから本番だべ頼んだ by sunaga

#############################################################################



class MazeField(object):
    '''
        MazeClientオブジェクトが保持するクラス。
        主な目的は現在のゲームの情報の描画とタッチしたUIからコマンドを生成すること。
        一言でいうとUIと中身のつなぎこみを行うクラス。
    '''
    
    def __init__(self,text, game_info):
        '''
            maze_obejctはmaze.pyに入っているMazeクラス
        '''
        self.text_ = text
        self.game_info_ = game_info
        pass


    #########################################################################################ここから下、ガイアが作った関数コピペしたからうまく動かないかも。
    def create_line(canvas,x,y,d,l):
        if d=="ver":
            for i in range(l):
                canvas.create_line(x,y,x,y+60*l,fill="black")
        elif d=="flat":
            for i in range(l):
                canvas.create_line(x,y,x+60*l,y,fill="black")

    def create_maze(maze):
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
                hei+=1
            wid+=1
         


        root=tk.Tk()
        root.title("sample")
        root.geometry()




        create_maze(MAZE_LIST[0])

        #canvas.create_oval(0,0,100,100,fill="orange")
        #canvas.create_oval(700,700,630,630,fill="blue")
        #create_line(canvas,100,0,"ver",3)
        #create_line(canvas,100,300,"flat",1)
        #create_line(canvas,300,0,"ver",1)
        #create_line(canvas,200,100,"flat",2)
        #create_line(canvas,300,200,"ver",1)
        #create_line(canvas,200,200,"flat",1)
        #create_line(canvas,400,200,"ver",1)
        #create_line(canvas,400,300,"flat",1)
        #create_line(canvas,500,400,"ver",1)
        #create_line(canvas,500,100,"ver",1)
        #create_line(canvas,500,100,"flat",1)
        #create_line(canvas,600,100,"ver",2)
        #create_line(canvas,700,100,"ver",3)
        #canvas.create_polygon(((250,0),(200,98),(300,98)),fill="green")
        #canvas.create_polygon(((550,100),(500,198),(600,198)),fill="green")


        root.mainloop()




















