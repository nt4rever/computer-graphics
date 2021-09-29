from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

listPoint = []


def init():
    # glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-320, 320, -320, 320, -1, 1)


vertices = [100, 100, 50, 100, 50, 50, 100, 50]


def trans(x, y):
    midX = ((vertices[0]+vertices[4])/2)
    midY = ((vertices[1]+vertices[5])/2)
    M = np.eye(3)
    M[2, 0] = x - midX
    M[2, 1] = y - midY
    # array([[ 1.,  0.,  0.],
    #       [ 0.,  1.,  0.],
    #       [tx, ty,  1.]])
    # N = Q x M
    for i in range(0, 8, 2):
        N = [vertices[i], vertices[i+1], 1]@M
        vertices[i] = N[0]
        vertices[i+1] = N[1]


def rotate(x, y, alpha):
    M = np.eye(3)
    M[0, 0] = math.cos(alpha)
    M[0, 1] = math.sin(alpha)
    M[1, 0] = -math.sin(alpha)
    M[1, 1] = math.cos(alpha)
    M[2, 0] = (1-math.cos(alpha))*x+math.sin(alpha)*y
    M[2, 1] = -math.sin(alpha)*x+(1-math.cos(alpha))*y
    for i in range(0, 8, 2):
        N = [vertices[i], vertices[i+1], 1]@M
        vertices[i] = N[0]
        vertices[i+1] = N[1]


def reflection(x1, y1, x2, y2):
    k = (y2-y1)/(x2-x1)
    t = -y1/(y2-y1)
    x0 = x1 + t*(x2-x1)
    alpha = math.atan(k)
    rotate(x0, 0, -alpha)

    M = np.eye(3)
    M[1, 1] = -1.0
    for i in range(0, 8, 2):
        N = [vertices[i], vertices[i+1], 1]@M
        vertices[i] = N[0]
        vertices[i+1] = N[1]

    rotate(x0, 0, alpha)


def draw():
    glBegin(GL_POLYGON)
    glVertex2f(vertices[0], vertices[1])
    glVertex2f(vertices[2], vertices[3])
    glVertex2f(vertices[4], vertices[5])
    glVertex2f(vertices[6], vertices[7])
    glEnd()
    glFlush()

def drawLine(x0, y0, x1, y1):
    # glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2d(x0, y0)
    glVertex2d(x1, y1)
    glEnd()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    draw()
    if len(listPoint) == 2:
            x1, y1 = listPoint[0][0], listPoint[0][1]
            x2, y2 = listPoint[1][0], listPoint[1][1] 
            drawLine(x1, y1, x2, y2)    
            


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        # trans(x-320, 320-y)
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([x-320, 320-y])
        if len(listPoint) == 2:
            x1, y1 = listPoint[0][0], listPoint[0][1]
            x2, y2 = listPoint[1][0], listPoint[1][1] 
            reflection(x1, y1, x2, y2)
            glutPostRedisplay()


def keyPressed(key, x, y):
    print(key)
    if key == b'l':
        rotate(math.pi/12)
    elif key == b'r':
        rotate(-math.pi/12)


if __name__== "__main__":
    glutInit()
  
    glutInitWindowSize(640, 640)
    # glutInitWindowPosition(320, 320)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
   
    glutCreateWindow("Reflection")
    init()
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    # glutIdleFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()

