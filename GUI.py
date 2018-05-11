from tkinter import *

root = Tk()
xPos = 0.0
yPos = 0.0


def draw(event):
    global xPos
    global yPos
    if xPos != 0.0 and yPos != 0.0:
        canvas.create_line(xPos, yPos, event.x, event.y, fill="black")
        xPos = event.x
        yPos = event.y
    else:
        xPos = event.x
        yPos = event.y


def reset(event):
    global xPos
    global yPos
    xPos = 0.0
    yPos = 0.0


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset)
canvas.create_rectangle(0, 0, 500, 500, fill='red')

canvas.pack()
root.mainloop()
