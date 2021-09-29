from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
width = 600
height = 600
listPoint = []


def put8pixel(xc, yc, x, y):
    glVertex3i(x+xc, y+yc, 0)
    glVertex3i(y+xc, x+yc, 0)
    glVertex3i(y+xc, -x+yc, 0)
    glVertex3i(x+xc, -y+yc, 0)
    glVertex3i(-x+xc, -y+yc, 0)
    glVertex3i(-y+xc, -x+yc, 0)
    glVertex3i(-y+xc, x+yc, 0)
    glVertex3i(-x+xc, y+yc, 0)


def CirClebres(xc, yc, r):
    x, y = 0, r
    p = 3-2*r
    glBegin(GL_POINTS)
    while x <= y:
        put8pixel(xc, yc, x, y)
        if p < 0:
            p += 4*x+6
        else:
            p += 4*(x-y)+10
            y -= 1
        x += 1
    glEnd()


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    if len(listPoint) == 2:
        x1, y1 = listPoint[0][0], listPoint[0][1]
        x2, y2 = listPoint[1][0], listPoint[1][1]
        r = math.sqrt((x2-x1)**2+(y2-y1)**2)
        CirClebres(listPoint[0][0], listPoint[0][1], (int)(r))
    glFlush()


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
            listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        else:
            listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Lab1-CirCleBres")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(myDisplay)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
