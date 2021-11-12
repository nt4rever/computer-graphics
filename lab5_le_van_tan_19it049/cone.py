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

def projective(type,P):
    p = Point2D(0,0)
    if type == 1:
        p.x = P.x
        p.y = P.y      
    elif type ==2:
        p.x = P.x
        p.y = P.z
    elif type ==3:
        p.x = P.y
        p.y = P.z
    return p
    
def draw(R, h):
    P = Point3D(0,0,0)
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
            p = projective(chieu,P)
            glVertex2f(p.x, p.y)
            v += Delta_V
        u += Delta_U
    glEnd()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    draw(40,80)

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
    glutCreateWindow("cone")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()
