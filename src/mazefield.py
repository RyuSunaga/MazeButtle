
#this is GUI file
import tkinter as tk
from MazeServer import GameManager 
from config import MAZE_LIST

def create_line(canvas,x,y,d,l):
    if d=="ver":
        for i in range(l):
            canvas.create_line(x,y,x,y+60*l,fill="black")
    elif d=="flat":
        for i in range(l):
            canvas.create_line(x,y,x+60*l,y,fill="black")

def create_maze(maze):
    canvas=tk.Canvas(master=root,bg="white",height=60*len(maze),width=60*len(maze[0]))
    canvas1=tk.Canvas(master=root,bg="white",height=80,width=480)


    canvas2=tk.Canvas(master=root,bg="white",height=80,width=320)
    canvas2.grid(row=1,padx=1,pady=1,sticky=tk.E)
    canvas1.grid(row=1,padx=1,pady=1,sticky=tk.W)
    canvas.grid(row=0,padx=2,pady=2)

    count1=0
    for i in maze:
        count=0
        for j in i:
            if j==1:
                canvas.create_rectangle(count*60,count1*60,(count+1)*60,(count1+1)*60,fill="black")
            count+=1
        count1+=1
         



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