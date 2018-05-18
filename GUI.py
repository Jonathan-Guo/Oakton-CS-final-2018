from tkinter import *

root = Tk()
xPos = 0.0
yPos = 0.0
createStarting = 1.0
line_list = [[]]


class Vertex:
    x = 0
    y = 0

    def __init__(self, event_x, event_y):
        self.x = event_x
        self.y = event_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, event_x):
        self.x = event_x

    def set_y(self, event_y):
        self.x = event_y


def draw(event):
    global xPos
    global yPos
    global line_list
    if xPos != 0.0 and yPos != 0.0:
        canvas.create_line(xPos, yPos, event.x, event.y, fill="black")
        xPos = event.x
        yPos = event.y
        line_list[-1].append(Vertex(xPos, yPos))
    else:
        xPos = event.x
        yPos = event.y
        line_list[-1].append(Vertex(xPos, yPos))


def draw_line(x, y):
    canvas.create_line(x, y)


def reset_draw(event):
    global xPos
    global yPos
    xPos = 0.0
    yPos = 0.0


def create_start(event):
    global createStarting
    if createStarting == 1.0:
        canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="red")
        createStarting = 2.0
    elif createStarting == 2.0:
        canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="green")
        createStarting = 0.0


def create_line_representation(event):
    global line_list
    line_list[-1].append(Vertex(event.x, event.y))


def callback():
    global concavityButton
    global line_list
    slopes = []
    for x in line_list:
        for y in line_list[x]:



canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_draw)
canvas.bind("<Button-3>", create_start)
canvas.create_rectangle(0, 0, 500, 500, fill='white')

concavityButton = Button(root, text = "Find Concavity",command = callback())

canvas.pack()
concavityButton.pack()
root.mainloop()
