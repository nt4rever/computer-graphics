from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys
sys.setrecursionlimit(100000)

def init():
    # glClearColor(2.0, 1.0, 0.0, 0.0)
    glOrtho(0, 640, 0, 480, -1, 1)


def bound_it(x, y, fillColor, bc):
    colorS = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
    color = colorS[0][0]
    if ((color[0] != bc[0] or color[1] != bc[1] or color[2] != bc[2]) and (color[0] != fillColor[0] or color[1] != fillColor[1] or color[2] != fillColor[2])):
        glColor3f(fillColor[0], fillColor[1], fillColor[2])
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        glFlush()
        bound_it(x+1, y, fillColor, bc)
        bound_it(x-1, y, fillColor, bc)
        bound_it(x, y+1, fillColor, bc)
        bound_it(x, y-1, fillColor, bc)


def mouse(btn, state, x, y):
    y = 480-y
    if btn == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            print(x,y)
            bCol = [1, 0, 0]
            color = [0, 0, 1]
            bound_it(x, y, color, bCol)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(254,308)
    glVertex2i(276,346)
    glVertex2i(314,304)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Boundary Fill")
    glutDisplayFunc(myDisplay)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()

main()


