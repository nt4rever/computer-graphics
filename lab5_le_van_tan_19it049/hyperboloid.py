from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

width = 600
height = 600

chieu = 1


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def projective(type, P):
    p = Point2D(0, 0)
    if type == 1:
        p.x = P.x
        p.y = P.y
    elif type == 2:
        p.x = P.x
        p.y = P.z
    elif type == 3:
        p.x = P.y
        p.y = P.z
    return p


def draw(a, b, c, depth):
    P = Point3D(0, 0, 0)
    detail_u = 10
    detail_v = 10

    glBegin(GL_LINE_LOOP)
    u = 0
    while u < 10:
        v = 0
        while v < 10:
            u_normal = ((depth * 2 * u / (detail_u - 1)) - depth) / c
            v_normal = 2 * math.pi * v / (detail_v)

            P.x = a * math.sqrt(1 + u_normal**2) * math.cos(v_normal)
            P.y = b * math.sqrt(1 + u_normal**2) * math.sin(v_normal)
            P.z = c * u_normal
            p = projective(chieu, P)
            glVertex2f(p.x, p.y)
            v += 0.1
        u += 0.1
    glEnd()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    draw(10, 20, 10, 60)


def keyPressed(key, x, y):
    global chieu
    if key == b'1':
        chieu = 1
    if key == b'2':
        chieu = 2
    if key == b'3':
        chieu = 3
    glutPostRedisplay()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(640, 640)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("hyperboloid")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()
