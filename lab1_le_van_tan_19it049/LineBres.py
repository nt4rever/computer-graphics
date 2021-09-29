from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

listPoint = []
# listPoint = [[0, 0], [100, 100]]
width = 600
height = 600


def LineBres(x1, y1, x2, y2):
    Dx = x2-x1
    Dy = y2-y1
    const1 = 2*Dy
    const2 = 2*(Dy-Dx)
    P = 2*Dy-Dx
    x, y = x1, y1
    glBegin(GL_POINTS)
    while(x <= x2):
        glVertex3i(x, y, 0)
        if P < 0:
            P += const1
        else:
            P += const2
            y += 1
        x += 1
    glEnd()


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
            listPoint.append([(int) (x-width/2), (int) (height/2-y)])
        else:
            listPoint.append([(int) (x-width/2), (int) (height/2-y)])
        print(listPoint)
        glutPostRedisplay()


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    if len(listPoint) == 2:
        LineBres(listPoint[0][0], listPoint[0][1],
                 listPoint[1][0], listPoint[1][1])
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Lab1-LineBres")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(myDisplay)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
