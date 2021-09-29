from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


myPoly = [Point(0,0),Point(1,0),Point(1,1)]


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for p in myPoly:
        glVertex2f(p.x, p.y)
    glEnd()
    glFlush()


def mouseEvent(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            print(x, ",", y)
            if len(myPoly) == 4:
                myPoly.clear()
            myPoly.append(Point(x, y))
            print(len(myPoly))
            if len(myPoly) == 4:
                glutPostRedisplay()


if __name__ == "__main__":
    glutInit()
    glutCreateWindow("Py")
    glutDisplayFunc(display)
    glutMouseFunc(mouseEvent)
    glutMainLoop()
