from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
width = 600
height = 600
listPoint = []


def put4pixel(xc, yc, x, y):
    glVertex3i(x+xc, y+yc, 0)
    glVertex3i(x+xc, -y+yc, 0)
    glVertex3i(xc-x, yc-y, 0)
    glVertex3i(xc-x, yc+y, 0)


def ElipMidPoint(xc, yc, a, b):
    a2, b2 = a*a, b*b
    x, y = 0, b
    p = b2-a2*b+(1/4)*a2
    x0 = (int)(a2/math.sqrt(a2+b2))
    y0 = (int)(b2/math.sqrt(a2+b2))
    glBegin(GL_POINTS)
    while x <= x0:
        put4pixel(xc, yc, x, y)
        if p < 0:
            p += (2*x+3)*b2
        else:
            p += (2*x+3)*b2-2*a2*(y-1)
            y -= 1
        x += 1

    x, y = a, 0
    p = a2-a*b2+(1/4)*b2
    while(y <= y0):
        put4pixel(xc, yc, x, y)
        if p < 0:
            p += a2*(2*y+3)
        else:
            p += (2*y+3)*a2-2*b2*(x-1)
            x -= 1
        y += 1
    glEnd()


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    if len(listPoint) == 3:
        x1, y1 = listPoint[0][0], listPoint[0][1]
        x2, y2 = listPoint[1][0], listPoint[1][1]
        x3, y3 = listPoint[2][0], listPoint[2][1]
        a = math.sqrt((x2-x1)**2+(y2-y1)**2)
        b = math.sqrt((x3-x1)**2+(y3-y1)**2)
        ElipMidPoint(listPoint[0][0], listPoint[0][1], (int)(a), (int)(b))
    glFlush()


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 3:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Lab1-ElipBres")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(myDisplay)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
