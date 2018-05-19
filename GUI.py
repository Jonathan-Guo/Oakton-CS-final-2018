from tkinter import *

#hello2
root = Tk()
xPos = 0.0
yPos = 0.0
createStarting = 1.0
line_list = [[]]


class Vertex:
    x = -1
    y = -1

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


def draw_line(x, y, x_2, y_2):
    canvas.create_line(x, y, x_2, y_2)


def reset_draw(event):
    global xPos
    global yPos
    global line_list
    xPos = 0.0
    yPos = 0.0
    print(line_list)


def create_start(event):
    global createStarting
    global start
    global stop
    global slope_path

    if createStarting == 1.0:
        canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="red")
        start = Vertex(event.x, event.y)
        createStarting = 2.0
    elif createStarting == 2.0:
        canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="green")
        stop = Vertex(event.x, event.y)
        createStarting = 0.0
        slope_path = (stop.get_y() - start.get_y())/(stop.get_x() - start.get_x())


def create_line_representation(event):
    global line_list
    line_list[-1].append(Vertex(event.x, event.y))


def callback():
    global concavityButton
    global line_list
    global start
    global stop
    global slope_path
    mark_1 = Vertex(-1, -1)
    mark_2 = Vertex(-1, -1)
    slopes = []
    for x in range(0, len(line_list)):
        slopes = []
        for i in range(1, len(line_list[x])):
            print(line_list[x][i].get_y())
            print(line_list[x][i-1].get_y())
            print(line_list[x][i].get_x())
            print(line_list[x][i-1].get_x())
            slopes.append((line_list[x][i].get_y() - line_list[x][i-1].get_y())/(line_list[x][i].get_x() - line_list[x][i-1].get_x()))
            print("hello")
        if slope_path >= 0:
            for slope in range(0, len(slopes)):
                if (slopes[slope] <= slope_path) and (mark_1.get_x() == -1):
                    mark_1 = line_list[x][slope]
                elif slopes[slope] <= slope_path:
                    mark_2 = line_list[x][slope]
                    draw_line(mark_1.get_x(), mark_1.get_y(), mark_2.get_x(), mark_2.get_y())
                    canvas.create_line(mark_1.get_x(), mark_1.get_y(), mark_2.get_x(), mark_2.get_y())
                    print("hello world")
                    mark_1 = Vertex(-1, -1)
                    mark_2 = Vertex(-1, -1)


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_draw)
canvas.bind("<Button-3>", create_start)
canvas.create_rectangle(0, 0, 500, 500, fill='white')

start = Vertex(0, 0)
stop = Vertex(0, 0)
slope_path = 0
concavityButton = Button(root, text="Find Concavity", command=callback)

canvas.pack()
concavityButton.pack()
root.mainloop()
