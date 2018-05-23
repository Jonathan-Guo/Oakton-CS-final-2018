from tkinter import *
import math

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
    canvas.create_line(x, y, x_2, y_2, smooth="true")


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
        canvas.create_line(start.get_x(), start.get_y(), stop.get_x(), stop.get_y(), fill="orange")
        slope_path = (stop.get_y() - start.get_y())/(stop.get_x() - start.get_x())


def create_line_representation(event):
    global line_list
    line_list[-1].append(Vertex(event.x, event.y))


def callback():
    global start, stop
    path(start, stop)


def path(start1, stop1):
    global line_list
    marks = [start1]
    current_mark = start1
    x = current_mark.get_x()
    y = current_mark.get_y()
    dx = stop1.get_x() - current_mark.get_x()
    dy = stop1.get_y() - current_mark.get_y()
    r = math.sqrt(dx**2 + dy**2)
    angle = math.atan(dy/dx)
    count = 0
    if stop.get_x() - dx == 0:
        slope = 9999
    else:
        slope = (stop.get_y() - dy)/(stop.get_x() - dx)
    while current_mark != stop1:
        intersections = contains(x, y, dx, dy, slope)
        if -1 < len(intersections) <= 1 and count != 0:
            print("hello")
            angle -= 0.0005
            dx = r * math.cos(angle)
            dy = r * math.sin(angle)
            intersections = contains(x, y, dx, dy, slope)
            current_mark = intersections[0]
            marks.append(current_mark)
            x = current_mark.get_x()
            y = current_mark.get_y()
            dx = stop1.get_x() - current_mark.get_x()
            dy = stop1.get_y() - current_mark.get_y()
            r = math.sqrt(dx**2 + dy**2)
            print(angle)
            angle = math.atan(dy/dx)
            print(angle)
            count = 0
        elif len(intersections) == 0 and count == 0:
            current_mark = stop1
            marks.append(stop1)
            print("STOP")
        else:
            angle += 0.0001
            print(math.degrees(angle))
            dx = r * math.cos(angle)
            #print(dx)
            #print(dy)
            dy = r * math.sin(angle)
            count += 1
        if stop.get_x() - dx == 0:
            slope = 9999
        else:
            slope = (dy/dx)
    for i in range(len(marks)-1):
        draw_line(marks[i].get_x(), marks[i].get_y(),  marks[i+1].get_x(), marks[i+1].get_y())
        print("olleh")
    print(marks)


def contains(x, y, dx, dy, m):
    global line_list
    intersections = []
    b = y - m*x
    for i in range(len(line_list)):
        for j in range(len(line_list[i])):
            if m != 9999 and m > 0:
                if line_list[i][j].get_y() > line_list[i][j].get_x() * m + b and x < line_list[i][j].get_x() < dx and y < line_list[i][j].get_y() < dy:
                    intersections.append(line_list[i][j])
            elif m != 9999 and m < 0:
                if line_list[i][j].get_y() > line_list[i][j].get_x() * m + b and dx < line_list[i][j].get_x() < x and y < line_list[i][j].get_y() < dy:
                    intersections.append(line_list[i][j])
            elif m == 9999 and m != 0:
                if line_list[i][j] < x and y < line_list[i][j] < dy:
                    intersections.append(line_list[i][j])
            else:
                if line_list[i][j] < y and x < line_list[i][j] < dx:
                    intersections.append(line_list[i][j])
    return intersections


canvas = Canvas(root, width=500, height=500)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_draw)
canvas.bind("<Button-3>", create_start)
canvas.create_rectangle(0, 0, 500, 500, fill='white')

start = Vertex(0, 0)
stop = Vertex(0, 0)
button = Button(root, text="Path", command=callback)

canvas.pack()
button.pack()
root.mainloop()
