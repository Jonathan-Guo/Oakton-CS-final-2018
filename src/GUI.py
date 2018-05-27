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

    def __init__(self, event_x, event_y ):
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
        start = Vertex(pos_x, pos_y)
        print(start.get_x())
        print(start.get_y())
        createStarting = 2.0
    elif createStarting == 2.0:
        canvas.create_oval(pos_x*4-4, pos_y*4-4, pos_x*4 + 4, pos_y*4 + 4, fill="green")
        stop = Vertex(pos_x, pos_y)
        createStarting = 0.0
        line_path = canvas.create_line(start.get_x()*4, start.get_y()*4, stop.get_x()*4, stop.get_y()*4, fill="orange")


def dijkstra():
    global start, stop


def a_star():
    global start, stop
    points = a_star_algo()
    for i in points:
        canvas.create_rectangle(i.get_x()*4, i.get_y()*4, i.get_x()*4+4, i.get_y()*4+4, fill="orange")
    canvas.create_oval(start.get_x()*4-4, start.get_y()*4-4, start.get_x()*4 + 4, start.get_y()*4 + 4, fill="red")
    canvas.create_oval(stop.get_x()*4-4, stop.get_y()*4-4, stop.get_x()*4 + 4, stop.get_y()*4 + 4, fill="green")


def a_star_algo():
    global start, stop

    def calc_h(x, y, end):
        return math.sqrt((x - end.get_x())**2 + (y - end.get_y())**2)

    def neighbors(node):
        global stop
        neighbors_list = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if grid_list[i+node.get_x()][j+node.get_y()] != 1 and \
                        not(i == 0 and j == 0):
                    if (i == -1 or i == 1) and (j == -1 or j == 1):
                        neighbors_list.append(Vertex(i + node.get_x(), j + node.get_y()))
                    else:
                        neighbors_list.append(Vertex(i + node.get_x(), j + node.get_y()))
        return neighbors_list

    def contains(node1, set):
        for all in set:
            if node1.get_x() == all.get_x() and node1.get_y() == all.get_y():
                return True
        return False

    def path(previous, current):
        node_path = []
        while current in previous.keys():
            current = previous[current]
            node_path.append(current)
        return node_path

    open = set()
    closed = set()
    current = Vertex(start.get_x(), start.get_y())
    open.add(current)
    g_values = {current: 0}
    f_values = {current: 0}
    previous = {}
    g_values[current] = 0
    f_values[current] = calc_h(start.get_x(), start.get_y(), stop)
    while len(open) != 0:
        least_f = 9999
        pop_node = 0
        for k in open:
            if f_values[k] < least_f:
                least_f = f_values[k]
                pop_node = k
        print(pop_node.get_x(), pop_node.get_y(), "pop_node")
        open.remove(pop_node)
        closed.add(pop_node)
        if pop_node.get_x() == stop.get_x() and pop_node.get_y() == stop.get_y():
            return path(previous, pop_node)
        for i in neighbors(pop_node):
            canvas.create_rectangle(i.get_x()*4, i.get_y()*4, i.get_x()*4+4, i.get_y()*4+4, fill="cyan")
            if contains(i, closed):
                print("closed")
                continue
            if not contains(i, open):
                open.add(i)
                print(i.get_x(), i.get_y())
                print("appended to open")
            new_g = g_values[pop_node] + calc_h(i.get_x(), i.get_y(), pop_node)
            if i in g_values:
                if new_g > g_values[i]:
                    print("greater g")
                    continue
            previous[i] = pop_node
            g_values[i] = new_g
            f_values[i] = g_values[i] + calc_h(i.get_x(), i.get_y(), stop)


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
start = Vertex(0, 0)
stop = Vertex(0, 0)
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
