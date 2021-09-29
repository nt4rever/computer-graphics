from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutCreateWindow("Py")
    glutDisplayFunc(display)
    glutMainLoop()
