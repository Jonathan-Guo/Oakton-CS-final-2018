from tkinter import *

root = Tk()
a = 0.0
b = 0.0


def draw(event):
    global a
    global b
    if a != 0.0 and b != 0.0:
        canvas.create_line(a, b, event.x, event.y, fill="black")
        a = event.x
        b = event.y
    else:
        a = event.x
        b = event.y


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)

canvas.create_rectangle(0, 0, 500, 500, fill='red')

canvas.pack()
root.mainloop()
