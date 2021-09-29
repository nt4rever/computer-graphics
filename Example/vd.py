from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


n = -1
P = [Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0),
     Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)]


def GT(n):
    gt = 0
    if n == 0:
        gt = 1
    else:
        gt = 1
        for i in range(1, n+1):
            gt = gt*i
    return gt


def LT(coso, mu):
    lt = 0
    if mu == 0:
        lt = 1
    else:
        lt = 1
        for i in range(1, mu+1):
            lt = lt*coso
    return lt


def CKN(n, k):
    gtn = GT(n)
    gtk = GT(k)
    gtnk = GT(n-k)
    ckn = gtn/(gtk*gtnk)
    return ckn


def BNK(t, k, n):
    b = CKN(n, k)*LT(1-t, n-k)*LT(t, k)
    return b


def Tpt(p, n, t):
    pt = Point(0, 0)
    for k in (0, n+1):
        B = BNK(t, k, n)
        pt.x = (long)(pt.x+p[k].x*B)
        pt.y = (long)(pt.y+p[k].y*B)
    return pt


def veBezier(p, n):
    t = 0
    m = 1000
    dt = 1/float(m)
    glBegin(GL_LINE_STRIP)
    for i in (1, m+1):
        pt = Tpt(p, n, t)
        glVertex2i(pt.x, pt.y)
        t = t+dt
    glVertex2i(p[n].x, p[n].y)
    glEnd()


def VeDaGiacKiemSoat(P, n):
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(1, 0xAAA)
    glBegin(GL_LINE_STRIP)
    for i in range(1, n+1):
        glVertex2i(P[i].x, P[i].y)
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def Mydisplay():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    VeDaGiacKiemSoat(P, n)
    glColor3f(1.0, 1.0, 0.0)
    veBezier(P, n)
    glFlush()


def change(n):
    n += 1


def MouseEventHandler(button, state, x, y):
    if(button == GLUT_LEFT_BUTTON and state == GLUT_UP):
        change(n)
        P[n].x = x - 300
        P[n].y = 300-y
        glutPostRedisplay()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Ve duong cong Bezier")
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 0)
    glutDisplayFunc(Mydisplay)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
