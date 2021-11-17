from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width = 800
height = 800

P = []
n = -1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


def Bernstein(t, n, k):
    ckn = fact(n)/(fact(k)*fact(n-k))
    kq = ckn * ((1-t)**(n-k))*(t**k)
    return kq


def TPt(P, t, n):
    p = Point(0, 0)
    for k in range(n+1):
        B = Bernstein(t, n, k)
        p.x = (int)(p.x + P[k].x*B)
        p.y = (int)(p.y + P[k].y*B)
    return p


def draw(n, P):
    if n < 2:
        return
    t = 0
    m = 100
    dt = 1/m
    glBegin(GL_LINE_STRIP)
    for i in range(m+1):
        pt = TPt(P, t, n)
        glVertex2i(pt.x, pt.y)
        t += dt
    glVertex2i(P[n].x, P[n].y)
    glEnd()


def VeDaGiacKiemSoat(P, n):
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(1, 0xAAA)
    glBegin(GL_LINE_STRIP)
    for i in range(n+1):
        glVertex2i(P[i].x, P[i].y)
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def MouseEventHandler(button, state, x, y):
    global n
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        n += 1
        p = Point((int)(x-width/2), (int)(height/2-y))
        P.append(p)
        glutPostRedisplay()


def keyPressed(key, x, y):
    global n
    if key == b'c':
        P.clear()
        n = -1
        glutPostRedisplay()


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(2.0, 0.5, 1.0)
    VeDaGiacKiemSoat(P, n)
    glColor3f(0.5, 1.0, 1.0)
    draw(n, P)
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("LineBezier")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(myDisplay)
    glutMouseFunc(MouseEventHandler)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()
