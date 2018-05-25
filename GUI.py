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


def get_line_list():
    return line_list


def get_start():
    return start


def get_stop():
    return stop


def draw(event):
    global xPos
    global yPos
    global line_list
    if xPos != 0.0 and yPos != 0.0:
        canvas.create_line(xPos, yPos, event.x, event.y, fill="black")
        xPos = event.x
        yPos = event.y
        canvas.create_oval(xPos, yPos, xPos + 3, yPos + 3, fill="yellow")
        line_list[-1].append(Vertex(xPos, yPos))
    else:
        xPos = event.x
        yPos = event.y
        line_list[-1].append(Vertex(xPos, yPos))


def draw_line(x, y, x_2, y_2):
    canvas.create_line(x, y, x_2, y_2, smooth="true")


def reset_draw(event):
    global xPos
    global yPos
    global line_list
    xPos = 0.0
    yPos = 0.0
    print(line_list)
    print(len(line_list[0]))


def create_start(event):
    global createStarting
    global start
    global stop
    global line_path

    if createStarting == 1.0:
        canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="red", tag="point")
        start = Vertex(event.x, event.y)
        createStarting = 2.0
    elif createStarting == 2.0:
        canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="green", tag="point")
        stop = Vertex(event.x, event.y)
        createStarting = 0.0
        line_path = canvas.create_line(start.get_x(), start.get_y(), stop.get_x(), stop.get_y(), fill="orange", tag="line")


def create_line_representation(event):
    global line_list
    line_list[-1].append(Vertex(event.x, event.y))


def callback():
    global start, stop
    #path(start, stop)


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_draw)
canvas.bind("<Button-3>", create_start)
canvas.create_rectangle(0, 0, 500, 500, fill='white')

start = Vertex(0, 0)
stop = Vertex(0, 0)
line_path = 0
button = Button(root, text="Path", command=callback)
canvas.pack()
button.pack()
root.mainloop()
