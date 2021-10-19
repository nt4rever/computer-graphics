from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print(self.x, self.y, self.z)


class EdgeType:
    def __init__(self, begin, end):
        self.beginP = begin
        self.endP = end

    def print(self):
        print(self.beginP, self.endP)


class WireFrame:
    Points = []
    EdgeTypes = []

    def __init__(self, numVertex, numEdge):
        self.numVertex = numVertex
        self.numEdge = numEdge

    def getPoints(self):
        return self.Points

    def getEdgeTypes(self):
        return self.EdgeTypes

    def addPoint(self, p):
        self.Points.append(p)

    def addEdgeType(self, e):
        self.EdgeTypes.append(e)

    def getO(self):
        return self.Points[0]


userView = 1
listPoint = [[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0.5, 1.5], [
    0, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0.5, 1.5], [1, 0, 1]]
listEdge = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 7], [7, 8], [8, 9], [
    9, 10], [10, 6], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [2, 5], [1, 3]]

numVertex = len(listPoint)
numEdge = len(listEdge)
wire_frame = WireFrame(numVertex, numEdge)
for p in listPoint:
    point = Point(p[0]*100, p[1]*100, p[2]*100)
    wire_frame.addPoint(point)

for e in listEdge:
    edge = EdgeType(e[0], e[1])
    wire_frame.addEdgeType(edge)


def clear():
    wire_frame.getPoints().clear()
    wire_frame.getEdgeTypes().clear()
    for p in listPoint:
        point = Point(p[0]*100, p[1]*100, p[2]*100)
        wire_frame.addPoint(point)
    for e in listEdge:
        edge = EdgeType(e[0], e[1])
        wire_frame.addEdgeType(edge)


def init():
    glOrtho(-320, 320, -320, 320, -320, 320)


def rotate(phi, theta, R):
    T = np.eye(4)
    T[0, 0] = -math.sin(theta)
    T[0, 1] = -math.cos(theta)*math.sin(phi)
    T[0, 2] = -math.cos(theta)*math.cos(phi)

    T[1, 0] = math.cos(theta)
    T[1, 1] = -math.sin(theta)*math.sin(phi)
    T[1, 2] = -math.sin(theta)*math.cos(phi)

    T[2, 1] = math.cos(phi)
    T[2, 2] = -math.sin(phi)
    T[3, 2] = R
    for p in wire_frame.getPoints():
        N = [p.x, p.y, p.z, 1] @ T
        p.x = N[0]
        p.y = N[1]
        p.z = N[2]

def scale(k):
    T = np.eye(4)
    T[0,0] = k
    T[1,1] = k
    T[2,2] = k
    T[3,3] = k
    for p in wire_frame.getPoints():
        N = [p.x, p.y, p.z, 1] @ T
        p.x = N[0]
        p.y = N[1]
        p.z = N[2]


def draw():
    for p in wire_frame.getEdgeTypes():
        glBegin(GL_LINES)
        p1 = wire_frame.getPoints()[p.beginP-1]
        p2 = wire_frame.getPoints()[p.endP-1]
        if userView == 1:
            glVertex3f(p1.y, p1.z, p1.x)
            glVertex3f(p2.y, p2.z, p2.x)
        elif userView == 2:
            glVertex3f(p1.x, p1.z, p1.y)
            glVertex3f(p2.x, p2.z, p2.y)
        elif userView == 3:
            glVertex3f(p1.y, p1.x, p1.z)
            glVertex3f(p2.y, p2.x, p2.z)
        elif userView == 4:
            glVertex3f(p1.x, p1.y, p1.z)
            glVertex3f(p2.x, p2.y, p2.z)
        elif userView == 5:
            glVertex3f(p1.z, p1.x, p1.y)
            glVertex3f(p2.z, p2.x, p2.y)
        elif userView == 6:
            glVertex3f(p1.z, p1.y, p1.x)
            glVertex3f(p2.z, p2.y, p2.x)
        glEnd()
        glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    draw()


def control(key,  x,  y):
    O = wire_frame.getO()
    R = math.sqrt((O.x)**2+(O.y)**2+(O.z)**2)
    if key == GLUT_KEY_DOWN:
        rotate(math.pi/4, 0, R)
    if key == GLUT_KEY_UP:
        rotate(-math.pi/4, 0, R)
    if key == GLUT_KEY_RIGHT:
        rotate(0, math.pi/2, R)
    if key == GLUT_KEY_LEFT:
        rotate(0, -math.pi/2, R)
    glutPostRedisplay()


def keyPressed(key, x, y):
    global userView
    if key == b'1':
        userView = 1
    elif key == b'2':
        userView = 2
    elif key == b'3':
        userView = 3
    elif key == b'4':
        userView = 4
    elif key == b'5':
        userView = 5
    elif key == b'6':
        userView = 6
    elif key == b'c':
        clear()
    elif key == b'=':
        scale(1.2)
    elif key == b'-':
        scale(0.8)
    glutPostRedisplay()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(640, 640)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Khung_ket_noi")
    init()
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glutSpecialFunc(control)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()
