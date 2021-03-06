from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


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

    def getN(self, n):
        listP = n.indexFace
        ls = []
        for i in listP:
            p = faceModel.getPoints()[i-1]
            ls.append(p)
        v1 = np.zeros(3)
        v1[0] = ls[1].x-ls[0].x
        v1[1] = ls[1].y-ls[0].y
        v1[2] = ls[1].z-ls[0].z
        v2 = np.zeros(3)
        v2[0] = ls[2].x-ls[0].x
        v2[1] = ls[2].y-ls[0].y
        v2[2] = ls[2].z-ls[0].z
        return np.cross(v1, v2)


listPoint = [[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0.5, 1.5], [
    0, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0.5, 1.5], [1, 0, 1]]

listFace = [
    [1, 2, 7, 6],
    [2, 3, 8, 7],
    [1, 6, 10, 5],
    [7, 8, 9, 10, 6],
    [2, 1, 5, 4, 3],
    [4, 9, 8, 3],
    [5, 10, 9, 4]
]

V = [50, 50, 50]


numVertex = len(listPoint)
numFace = len(listFace)
faceModel = FaceModel(numVertex, numFace)
for p in listPoint:
    point = Point(p[0]*200, p[1]*200, p[2]*200)
    faceModel.addPoint(point)

for id, e in enumerate(listFace):
    face = FaceType(id, e)
    faceModel.addFaceType(face)


def init():
    glOrtho(-320, 320, -320, 320, -320, 320)


def draw():
    for p in faceModel.getFaceTypes():
        k = V@faceModel.getN(p)
        if k >= 0:
            glBegin(GL_LINE_LOOP)
            listP = p.indexFace
            for i in listP:
                p = faceModel.getPoints()[i-1]
                glVertex3f(p.x, p.y, p.z)
            glEnd()
            glFlush()
        else:
            glEnable(GL_LINE_STIPPLE)
            glLineStipple(2, 0xAAA)
            glBegin(GL_LINE_STRIP)
            listP = p.indexFace
            for i in listP:
                p = faceModel.getPoints()[i-1]
                glVertex3f(p.x, p.y, p.z)
            glEnd()
            glDisable(GL_LINE_STIPPLE)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 1, 1)
    draw()



if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(640, 640)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("back_face")
    init()
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(30, 20, 50, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glutDisplayFunc(display)
    glutMainLoop()
