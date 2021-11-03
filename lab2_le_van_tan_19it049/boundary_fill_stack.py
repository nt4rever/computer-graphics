from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

stack = []


def init():
    # glClearColor(2.0, 1.0, 0.0, 0.0)
    glOrtho(0, 640, 0, 480, -1, 1)


def bound_fill(x, y, fillColor, bc):
    colorS = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT)
    color = colorS[0][0]
    if ((color[0] != bc[0] or color[1] != bc[1] or color[2] != bc[2]) and (color[0] != fillColor[0] or color[1] != fillColor[1] or color[2] != fillColor[2])):
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        glFlush()
        stack.append([x, y])


def bound_it(x0, y0, fillColor, bc):
    glColor3f(fillColor[0], fillColor[1], fillColor[2])
    glBegin(GL_POINTS)
    glVertex2i(x0, y0)
    glEnd()
    glFlush()
    stack.append([x0, y0])
    while (len(stack) > 0):
        ls = stack.pop()
        x,y  = ls[0],ls[1]
        bound_fill(x+1, y, fillColor, bc)
        bound_fill(x-1, y, fillColor, bc)
        bound_fill(x, y+1, fillColor, bc)
        bound_fill(x, y-1, fillColor, bc)


def mouse(btn, state, x, y):
    y = 480-y
    if btn == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            print(x, y)
            bCol = [1, 0, 0]
            color = [0, 0, 1]
            bound_it(x, y, color, bCol)


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(250, 300)
    glVertex2i(250, 350)
    glVertex2i(300, 300)
    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Boundary Fill Stack")
    glutDisplayFunc(myDisplay)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()


main()
