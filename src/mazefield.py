
#this is GUI file
import tkinter as tk

def create_line(canvas,x,y,d,l):
    if d=="ver":
        for i in range(l):
            canvas.create_line(x,y,x,y+80*l,fill="black")
    elif d=="flat":
        for i in range(l):
            canvas.create_line(x,y,x+80*l,y,fill="black")
         

root=tk.Tk()
root.title("sample")
root.geometry()

canvas=tk.Canvas(master=root,bg="white",height=320,width=640)

canvas.create_oval(0,0,80,80,fill="orange")
canvas.create_oval(640,320,560,240,fill="blue")
create_line(canvas,80,0,"ver",3)
create_line(canvas,80,240,"flat",1)
create_line(canvas,240,0,"ver",1)
create_line(canvas,160,80,"flat",2)
create_line(canvas,240,160,"ver",1)
create_line(canvas,160,160,"flat",1)
create_line(canvas,320,160,"ver",1)
create_line(canvas,320,240,"flat",1)
create_line(canvas,400,320,"ver",1)
create_line(canvas,400,80,"ver",1)
create_line(canvas,400,80,"flat",1)
create_line(canvas,480,80,"ver",2)
create_line(canvas,560,80,"ver",3)
canvas.create_polygon(((200,0),(160,78),(240,78)),fill="green")
canvas.create_polygon(((440,80),(400,158),(480,158)),fill="green")


canvas.grid(padx=20,pady=20)
root.mainloop()