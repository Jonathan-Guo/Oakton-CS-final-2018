from tkinter import *

root = Tk()


def draw(event):
    canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="black")


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)

canvas.create_rectangle(0, 0, 500, 500, fill='red')

canvas.pack()
root.mainloop()
