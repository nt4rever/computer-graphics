from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

width = 600
height = 600
xmin, xmax, ymin, ymax = -100, 200, -100, 200
listPoint = []

def Ma(x, y):
    m = 0
    if x < xmin:
        m |= 1
    if x > xmax:
        m |= 2
    if y < ymin:
        m |= 4
    if y > ymax:
        m |= 8
    return m


def draw(x0, y0, x1, y1):
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2d(x0, y0)
    glVertex2d(x1, y1)
    glEnd()


def BinaryClip(xA, yA, xB, yB):
    if (Ma(xA, yA) | Ma(xB, yB) == 0):
        draw(xA, yA, xB, yB)
    if (Ma(xA, yA) & Ma(xB, yB) != 0):
        return
    if (Ma(xA, yA) != 0) & (Ma(xB, yB) == 0):
        xA, yA, xB, yB = xB, yB, xA, yA
    if (Ma(xA, yA) == 0) & (Ma(xB, yB) != 0):
        xP, yP = xA, yA
        xQ, yQ = xB, yB
        while(abs(xP - xQ) + abs(yP - yQ)) > 2:
            xM, yM = (xP + xQ)/2, (yP + yQ)/2
            if Ma(xM, yM) == 0:
                xP, yP = xM, yM
            else:
                xQ, yQ = xM, yM
        draw(xA, yA, xP, yP)
    if ((Ma(xA, yA) != 0) & (Ma(xB, yB) != 0)) & ((Ma(xA, yA) & Ma(xB, yB)) == 0):
        xP, yP = xA, yA
        xQ, yQ = xB, yB
        xM, yM = (xP + xQ)/2, (yP + yQ)/2
        while Ma(xM, yM) != 0 & (abs(xP - xQ) + abs(yP - yQ)) > 2:
            if Ma(xP, yP) & Ma(xM, yM) != 0:
                xP, yP = xM, yM
            else:
                xQ, yQ = xM, yM
            xM, yM = (xP + xQ)/2, (yP + yQ)/2
        if Ma(xM, yM) == 0:
            BinaryClip(xP, yP, xM, yM)
            BinaryClip(xM, yM, xQ, yQ)


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()
    if len(listPoint) == 2:
        BinaryClip(listPoint[0][0], listPoint[0][1],
                  listPoint[1][0], listPoint[1][1])
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("binary_clip")
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glutInitWindowPosition(10, 10)
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
