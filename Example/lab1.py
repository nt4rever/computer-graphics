from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

listPoint = [[0, 0], [100, 100]]


def LineBres(x1, y1, x2, y2):
    Dx = abs(x2-x1)
    Dy = abs(y2-y1)
    x, y = x1, y1
    m = (y2-y1)/(x2-x1)
    if m > 0 and m <= 1:
        const1 = 2*Dy
        const2 = 2*(Dy-Dx)
        P = 2*Dy-Dx
        while(x <= x2):
            glVertex2f(x, y)
            if P < 0:
                P += const1
            else:
                P += const2
                y += 1
            x += 1


def drawLine():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    if len(listPoint) == 2:
        LineBres(listPoint[0][0], listPoint[0][1],
                 listPoint[1][0], listPoint[1][1])
    glEnd()
    glutSwapBuffers()


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
            listPoint.append([x-300, 300-y])
        else:
            listPoint.append([x-300, 300-y])
        print(listPoint)
        glutPostRedisplay()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Lab1")
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 0)
    glutDisplayFunc(drawLine)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
