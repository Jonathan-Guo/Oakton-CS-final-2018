from tkinter import *
import math
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
    g = 0
    f = 0

    def __init__(self, event_x, event_y, gvalue, fvalue):
        self.x = event_x
        self.y = event_y
        self.g = gvalue
        self.f = fvalue

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_g(self):
        return self.g

    def get_f(self):
        return self.f

    def set_x(self, event_x):
        self.x = event_x

    def set_y(self, event_y):
        self.x = event_y

    def set_g(self, value):
        self.g = value

    def set_f(self, value):
        self.f = value


def get_start():
    return start


def get_stop():
    return stop


def draw(event):
    global xPos
    global yPos
    global grid_elements
    if event.x < 500 and event.y < 500:
        if event.x == 0:
            xPos = 0
        else:
            xPos = event.x//4
        if event.y == 0:
            yPos = 0
        else:
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
    pos_x = event.x//4
    pos_y = event.y//4
    if createStarting == 1.0:
        canvas.create_oval(pos_x*4-4, pos_y*4-4, pos_x*4 + 4, pos_y*4 + 4, fill="red")
        start = Vertex(pos_x, pos_y, 0, 0)
        print(start.get_x())
        print(start.get_y())
        createStarting = 2.0
    elif createStarting == 2.0:
        canvas.create_oval(pos_x*4-4, pos_y*4-4, pos_x*4 + 4, pos_y*4 + 4, fill="green")
        stop = Vertex(pos_x, pos_y, 0, 0)
        createStarting = 0.0
        line_path = canvas.create_line(start.get_x()*4, start.get_y()*4, stop.get_x()*4, stop.get_y()*4, fill="orange")


def dijkstra():
    global start, stop


def a_star():
    global start, stop
    points = a_star_algo()
    for i in range(len(points)-1):
        draw_line(points[i].get_x()*4, points[i].get_y()*4, points[i+1].get_x()*4, points[i+1].get_y()*4)
    draw_line(points[-1].get_x()*4, points[-1].get_y()*4, stop.get_x()*4, stop.get_y()*4)


def a_star_algo():
    global start, stop

    def calc_h(x, y, end):
        return math.sqrt((x - end.get_x())**2 + (y - end.get_y())**2)

    open = set()
    closed = set()
    current = Vertex(start.get_x(), start.get_y(), 0, 0)
    open.add(current)
    neighbor_f = 0
    points = []

    while len(open) != 0:
        least_f = 9999
        pop_node = None
        open_contains = False
        closed_contains = False
        for k in open:
            if k.get_f() < least_f:
                least_f = k.get_f()
                pop_node = k
        open.remove(pop_node)
        print(pop_node)
        print("hello")
        for i in range(pop_node.get_x()-1, pop_node.get_x()+1):
            for j in range(pop_node.get_y()-1, pop_node.get_y()+1):
                if grid_list[i][j] != 1 and i != pop_node.get_x() and j != pop_node.get_y():
                    if grid_list[i] == stop.get_x() and grid_list[j] == stop.get_y():
                        return points
                    neighbor_g = pop_node.get_g() + calc_h(i, j, pop_node)
                    neighbor_h = calc_h(i, j, stop)
                    neighbor_f = neighbor_g + neighbor_h
                    for k in open:
                        if k.get_x() == i and k.get_y() == j and k.get_f() < neighbor_f:
                            open_contains = True
                            print("skipped one")
                    for k in closed:
                        if k.get_x() == i and k.get_y() == j and k.get_f() < neighbor_f:
                            closed_contains = True
                            print("skipped two")
                    if not open_contains and not closed_contains:
                        open.add(Vertex(i, j, neighbor_g, neighbor_f))
                        print("appended")
                        points.append(Vertex(i, j, neighbor_g, neighbor_f))
        closed.add(pop_node)
    return points


#note: this is jump point search
def JPS():
    global start, stop


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_draw)
canvas.bind("<Button-3>", create_start)
canvas.create_rectangle(0, 0, 500, 500, fill='white')
for i in range(125):
    draw_line(i*4, 0, i*4, 500)
for i in range(125):
    draw_line(0, i*4, 500, i*4)
start = Vertex(0, 0, 0, 0)
stop = Vertex(0, 0, 0, 0)
line_path = 0
frame = Frame(root)
frame.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
dijkstras = Button(frame, text="Dijkstra's", command=dijkstra)
a_star_button = Button(frame, text="A*", command=a_star)
JPS_button = Button(frame, text="JPS", command=JPS)
dijkstras.pack(side=LEFT, expand=True)
a_star_button.pack(side=LEFT, expand=True)
JPS_button.pack(side=LEFT, expand=True)
canvas.pack()
root.mainloop()
