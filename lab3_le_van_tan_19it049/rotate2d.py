from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math


def init():
    # glClearColor(1.1, 1.0, 1.0, 1.0)
    glOrtho(-320, 320, -320, 320, -1, 1)


vertices = [50, 50, -50, 50, -50, -50, 50, -50]


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


def rotate(alpha):
    oldX = ((vertices[0]+vertices[4])/2)
    oldY = ((vertices[1]+vertices[5])/2)
    trans(0, 0)
    M = np.eye(3)
    M[0, 0] = math.cos(alpha)
    M[0, 1] = math.sin(alpha)
    M[1, 0] = -math.sin(alpha)
    M[1, 1] = math.cos(alpha)
    for i in range(0, 8, 2):
        N = [vertices[i], vertices[i+1], 1]@M
        vertices[i] = N[0]
        vertices[i+1] = N[1]
    trans(oldX,oldY)


def draw():
    glBegin(GL_POLYGON)
    glVertex2f(vertices[0], vertices[1])
    glVertex2f(vertices[2], vertices[3])
    glVertex2f(vertices[4], vertices[5])
    glVertex2f(vertices[6], vertices[7])
    glEnd()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    draw()


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        trans(x-320, 320-y)

def keyPressed(key,x,y):
    # print(key)
    if key==b'l':
        rotate(math.pi/12)
    elif key==b'r':
        rotate(-math.pi/12)
        


def main():
    glutInit()
    glutInitWindowSize(640, 640)
    # glutInitWindowPosition(320, 320)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Rotate")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()


main()
