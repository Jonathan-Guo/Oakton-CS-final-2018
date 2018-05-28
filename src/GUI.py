from tkinter import *
import math
root = Tk()
# Tracks the mouse movement and when to color in blocks
xPos = 0.0
yPos = 0.0

# tracks starting nodes
createStarting = 1.0

# creates a 125x125 matrix, representative of our grid
grid_list = [[0 for i in range(125)] for j in range(125)]

# was for debugging purposes
grid_elements = 0

# Vertex class that stores a x and y position
class Vertex:
    x = -1
    y = -1

    # Constructor
    def __init__(self, event_x, event_y ):
        self.x = event_x
        self.y = event_y

    # Accessor
    def get_x(self):
        return self.x

    # Accessor
    def get_y(self):
        return self.y

    # Modifier for x
    def set_x(self, event_x):
        self.x = event_x

    # Modifier for y
    def set_y(self, event_y):
        self.x = event_y


# draws in the black tiles to signify walls
# depends on mouse movement and is binded to mouse movement
# the // represents integer division; we use it to draw the squares precisely
def draw(event):
    global xPos
    global yPos
    global grid_elements

    # grid bounds
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
            # debugging purposes
            grid_elements += 1
        # creates a rectangle using xPos and yPos, multiplies them by 4 to draw the square precisely
        canvas.create_rectangle(xPos * 4, yPos * 4, xPos * 4 + 4, yPos * 4 + 4, fill="black")


# draws a line from (x, y) to (x_2, y_2)
def draw_line(x, y, x_2, y_2):
    canvas.create_line(x, y, x_2, y_2, smooth="true")


# resets xPos and yPos after the use lifts their mouse
def reset_draw(event):
    global xPos
    global yPos
    xPos = 0.0
    yPos = 0.0
    print(grid_elements)


# creates the starting and ending nodes, represented by a red circle (starting) and green circle (ending)
def create_start(event):
    global createStarting
    global start
    global stop
    global line_path
    # floor division to place the circles onto our grid precisely
    pos_x = event.x//4
    pos_y = event.y//4
    # if start does not exist yet
    if createStarting == 1.0:
        canvas.create_oval(pos_x*4-4, pos_y*4-4, pos_x*4 + 4, pos_y*4 + 4, fill="red")
        start = Vertex(pos_x, pos_y)
        print(start.get_x())
        print(start.get_y())
        createStarting = 2.0
    # if start already exists
    elif createStarting == 2.0:
        canvas.create_oval(pos_x*4-4, pos_y*4-4, pos_x*4 + 4, pos_y*4 + 4, fill="green")
        stop = Vertex(pos_x, pos_y)
        createStarting = 0.0
        line_path = canvas.create_line(start.get_x()*4, start.get_y()*4, stop.get_x()*4, stop.get_y()*4, fill="orange")


# runs Dijkstra's algorithm
# calls the A* algorithm, a_star_algo(Bool b) in order to do so
# Note: Dijkstra's is a special case of A*, where h(n), the cost from the current node to the end node is always 0
def dijkstra():
    global start, stop
    points = a_star_algo(True)
    for i in points:
        canvas.create_rectangle(i.get_x()*4, i.get_y()*4, i.get_x()*4+4, i.get_y()*4+4, fill="orange")
    # draws in the path from start to stop
    canvas.create_oval(start.get_x()*4-4, start.get_y()*4-4, start.get_x()*4 + 4, start.get_y()*4 + 4, fill="red")
    canvas.create_oval(stop.get_x()*4-4, stop.get_y()*4-4, stop.get_x()*4 + 4, stop.get_y()*4 + 4, fill="green")


# calls the a_star_algo(Bool b) method

def a_star():
    global start, stop
    points = a_star_algo(False)
    for i in points:
        canvas.create_rectangle(i.get_x()*4, i.get_y()*4, i.get_x()*4+4, i.get_y()*4+4, fill="orange")
    # draws in the path from start to stop
    canvas.create_oval(start.get_x()*4-4, start.get_y()*4-4, start.get_x()*4 + 4, start.get_y()*4 + 4, fill="red")
    canvas.create_oval(stop.get_x()*4-4, stop.get_y()*4-4, stop.get_x()*4 + 4, stop.get_y()*4 + 4, fill="green")


# runs A*
def a_star_algo(dijkstra):
    global start, stop

    # calculates the distance between two nodes, which is h(n)
    # this heuristic uses Euclidean distance
    def calc_h(x, y, end):
        return math.sqrt((x - end.get_x())**2 + (y - end.get_y())**2)

    # appends all of the nodes around the current node to a list, if they are not a wall
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

    # contains function for sets
    def contains(node1, set):
        for all in set:
            if node1.get_x() == all.get_x() and node1.get_y() == all.get_y():
                return True
        return False

    # returns the complete path from start to stop
    def path(previous, current):
        node_path = []
        while current in previous.keys():
            current = previous[current]
            node_path.append(current)
        return node_path

    open = set() # initialize open set
    closed = set() # initialize closed set
    current = Vertex(start.get_x(), start.get_y())
    open.add(current) # add start to the open set
    g_values = {current: 0} # track g_values through a dictionary
    f_values = {current: 0} # track f_values through a dictionary
    previous = {} # track the list of nodes through a dictionary
    g_values[current] = 0 # set the intial g_value to be 0
    f_values[current] = calc_h(start.get_x(), start.get_y(), stop) # initialize the f_value of the start node
    while len(open) != 0:
        least_f = 9999
        pop_node = 0
        # finds the node with the lowest f_value
        for k in open:
            if f_values[k] < least_f:
                least_f = f_values[k]
                pop_node = k
        # debugging
        print(pop_node.get_x(), pop_node.get_y(), "pop_node")
        # remove the node from the open set, add to the closed set
        open.remove(pop_node)
        closed.add(pop_node)
        # end condition
        if pop_node.get_x() == stop.get_x() and pop_node.get_y() == stop.get_y():
            return path(previous, pop_node)
        # check for all neighbors of pop_node
        for i in neighbors(pop_node):
            # color this square in to indicate which squares have been visited
            canvas.create_rectangle(i.get_x()*4, i.get_y()*4, i.get_x()*4+4, i.get_y()*4+4, fill="cyan")
            # if already in closed set, we've already visited; we don't need this node
            if contains(i, closed):
                print("closed")
                continue
            # add to open if not in open; means we haven't visited this node yet
            if not contains(i, open):
                open.add(i)
                # debugging purposes
                print(i.get_x(), i.get_y())
                print("appended to open")
            # new cost = old cost(g_value) + new cost to neighbor
            new_g = g_values[pop_node] + calc_h(i.get_x(), i.get_y(), pop_node)
            # if the new cost is greater than the previous ones, we don't need this node
            if i in g_values:
                if new_g > g_values[i]:
                    print("greater g")
                    continue
            # set the path down
            previous[i] = pop_node
            # set the new g_value for this node
            g_values[i] = new_g
            # f(n) = g(n) + h(n) for A*
            if not dijkstra:
                f_values[i] = g_values[i] + calc_h(i.get_x(), i.get_y(), stop)
            else: # h(n) = 0 in Dijkstra's algorithm
                f_values[i] = g_values[i]


# function to clear everything to the original state
def reset_everything():
    global grid_list
    global createStarting
    canvas.delete("all")
    grid_list = [[0 for i in range(125)] for j in range(125)]
    createStarting = 1
    # draw the grid lines
    for i in range(125):
        draw_line(i*4, 0, i*4, 500)
    for i in range(125):
        draw_line(0, i*4, 500, i*4)


# main canvas we draw on
canvas = Canvas(root, width=500, height=500)
# binds to mouse buttons.
canvas.bind("<B1-Motion>", draw) # binds to whenever the left click is held down and moved
canvas.bind("<ButtonRelease-1>", reset_draw) # binds to when the left click is released
canvas.bind("<Button-3>", create_start) # binds to when the right click is pressed

# main canvas creation
canvas.create_rectangle(0, 0, 500, 500, fill='white')

# create the grid lines
for i in range(125):
    draw_line(i*4, 0, i*4, 500)
for i in range(125):
    draw_line(0, i*4, 500, i*4)
# define start and stop points
start = Vertex(0, 0)
stop = Vertex(0, 0)
line_path = 0
# frame to contain all of the buttons
frame = Frame(root)
frame.pack(side=BOTTOM, expand=TRUE, fill=BOTH)
# make all of the buttons and pack them into the frame
dijkstras = Button(frame, text="Dijkstra's", command=dijkstra)
a_star_button = Button(frame, text="A*", command=a_star)
reset = Button(frame, text = "Reset", command = reset_everything)
dijkstras.pack(side=LEFT, expand=True)
a_star_button.pack(side=LEFT, expand=True)
reset.pack(side=LEFT, expand=True)
canvas.pack()
# run the program
root.mainloop()
