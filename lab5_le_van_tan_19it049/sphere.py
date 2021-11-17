from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

width = 600
height = 600


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    
def draw(R):
    P = Point3D(0,0,0)
    Delta_U = 0.1
    Delta_V = 0.1
    Pi_2 = math.pi/2
    v = -Pi_2
    
    glBegin(GL_LINE_LOOP)
    while v < Pi_2:
        u = 0
        while u < 2*math.pi:
            P.x = R*math.cos(u)*math.cos(v)
            P.y = R*math.sin(u)*math.cos(v)
            P.z = R*math.sin(v)
            glVertex3f(P.x, P.y, P.z)
            u += Delta_U
        v += Delta_V
    glEnd()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 1, 1)
    draw(80)


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(width, height)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("sphere")
    glOrtho(-width/2, height/2, -height/2, width/2, -height/2, width/2)
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 40, 10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glutMainLoop()
