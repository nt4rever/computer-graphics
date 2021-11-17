from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

width = 600
height = 600


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



def draw(R, h):
    P = Point3D(0, 0, 0)
    Delta_U = 0.03
    Delta_V = 0.1
    u = 0
    glBegin(GL_LINE_LOOP)
    while u < 2*math.pi:
        v = 0
        while v < 1:
            P.x = v*R*math.cos(u)
            P.y = v*R*math.sin(u)
            P.z = v*h
            glVertex3f(P.x, P.y, P.z)
            v += Delta_V
        u += Delta_U
    glEnd()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 1, 1)
    draw(60, 100)


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(width, height)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("cone")
    glOrtho(-width/2, height/2, -height/2, width/2, -height/2, width/2)
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 60, 30, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glutMainLoop()
