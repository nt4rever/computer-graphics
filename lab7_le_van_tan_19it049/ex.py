from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    gluOrtho2D(-320, 320, -320, 320)

listP = [[0,0],[100,0],[100,100],[0,100]]

def draw():
    glBegin(GL_LINE_LOOP)
    for p in listP:
        glVertex2f(p[0],p[1])
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .5, .25)
    draw()

if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(640, 640)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("lambert")
    init()
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glutMainLoop()