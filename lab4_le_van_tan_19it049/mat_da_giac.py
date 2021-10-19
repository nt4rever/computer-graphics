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


class FaceType:
    def __init__(self, nFace, indexface) -> None:
        self.nFace = nFace
        self.indexFace = indexface


class FaceModel:
    Points = []
    FaceTypes = []

    def __init__(self, numVertex, numFace):
        self.numVertex = numVertex
        self.numFace = numFace

    def getPoints(self):
        return self.Points

    def getFaceTypes(self):
        return self.FaceTypes

    def addPoint(self, p):
        self.Points.append(p)

    def addFaceType(self, e):
        self.FaceTypes.append(e)

    def getO(self):
        return self.Points[0]


userView = 1
listPoint = [[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0.5, 1.5], [
    0, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0.5, 1.5], [1, 0, 1]]

listFace = [
    [1, 2, 7, 6],
    [2, 7, 8, 3],
    [1, 6, 10, 5],
    [7, 6, 10, 9, 8],
    [2, 1, 5, 4, 3],
    [4, 3, 8, 9],
    [5, 4, 9, 10]
]

numVertex = len(listPoint)
numFace = len(listFace)
faceModel = FaceModel(numVertex, numFace)
for p in listPoint:
    point = Point(p[0]*100, p[1]*100, p[2]*100)
    faceModel.addPoint(point)

for id,e in enumerate(listFace):
    face = FaceType(id, e)
    faceModel.addFaceType(face)


def clear():
    faceModel.getPoints().clear()
    faceModel.getFaceTypes().clear()
    for p in listPoint:
        point = Point(p[0]*100, p[1]*100, p[2]*100)
        faceModel.addPoint(point)
    for id,e in enumerate(listFace):
        face = FaceType(id, e)
        faceModel.addFaceType(face)


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
    for p in faceModel.getPoints():
        N = [p.x, p.y, p.z, 1] @ T
        p.x = N[0]
        p.y = N[1]
        p.z = N[2]


def scale(k):
    T = np.eye(4)
    T[0, 0] = k
    T[1, 1] = k
    T[2, 2] = k
    T[3, 3] = k
    for p in faceModel.getPoints():
        N = [p.x, p.y, p.z, 1] @ T
        p.x = N[0]
        p.y = N[1]
        p.z = N[2]


def draw():
    for p in faceModel.getFaceTypes():
        glBegin(GL_LINE_LOOP)
        listP = p.indexFace
        for i in listP:
            p = faceModel.getPoints()[i-1]
            if userView == 1:
                glVertex3f(p.y, p.z, p.x)
            elif userView == 2:
                glVertex3f(p.x, p.z, p.y)
            elif userView == 3:
                glVertex3f(p.y, p.x, p.z)
            elif userView == 4:
                glVertex3f(p.x, p.y, p.z)
            elif userView == 5:
                glVertex3f(p.z, p.x, p.y)
            elif userView == 6:
                glVertex3f(p.z, p.y, p.x)
        glEnd()
        glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    draw()


def control(key,  x,  y):
    O = faceModel.getO()
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
    glutCreateWindow("Mat_da_giac")
    init()
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glutSpecialFunc(control)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()
