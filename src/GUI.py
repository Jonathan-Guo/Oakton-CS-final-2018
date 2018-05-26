from tkinter import *
#hello3
#program start
root = Tk()
xPos = 0.0
yPos = 0.0
createStarting = 1.0
grid_list = [[0 for i in range(125)] for j in range(125)]
grid_elements = 0


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


def get_start():
    return start


def get_stop():
    return stop


def draw(event):
    global xPos
    global yPos
    global grid_elements
    xPos = event.x//4
    yPos = event.y//4
    if grid_list[xPos][yPos] != 1:
        grid_list[xPos][yPos] = 1
        grid_elements += 1
    canvas.create_rectangle(xPos * 4, yPos * 4, xPos * 4 + 4, yPos * 4 + 4, fill="black")


def draw_line(x, y, x_2, y_2):
    canvas.create_line(x, y, x_2, y_2, smooth="true")


def reset_draw(event):
    global xPos
    global yPos
    xPos = 0.0
    yPos = 0.0
    print(grid_elements)


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
        line_path = canvas.create_line(start.get_x(), start.get_y(), stop.get_x(), stop.get_y(), fill="orange")


def dijkstra():
    global start, stop


def a_star():
    global start, stop


def JPS():
    global start,stop


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_draw)
canvas.bind("<Button-3>", create_start)
canvas.create_rectangle(0, 0, 500, 500, fill='white')
for i in range(125):
    draw_line(i*4, 0, i*4, 500)
for i in range(125):
    draw_line(0, i*4, 500, i*4)
start = Vertex(0, 0)
stop = Vertex(0, 0)
line_path = 0
dijkstras = Button(root, text="Dijkstra's", command=dijkstra)
a_star_button = Button(root, text="A*", command=a_star)
JPS_button = Button(root, text="JPS", command=JPS)
dijkstras.pack(padx=5, pady=5, side=BOTTOM)
a_star_button.pack(padx=10, pady=5, side=BOTTOM)
JPS_button.pack(padx=15, pady=5, side=BOTTOM)
canvas.pack()
root.mainloop()
