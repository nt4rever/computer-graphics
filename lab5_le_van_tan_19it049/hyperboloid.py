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


def draw(a, b, c, depth):
    P = Point3D(0, 0, 0)
    detail_u = 10
    detail_v = 10

    glBegin(GL_LINE_LOOP)
    u = 0
    while u < 10:
        v = 0
        while v < 10:
            u_normal = ((depth * 2 * u / (detail_u - 1)) - depth) / c
            v_normal = 2 * math.pi * v / (detail_v)

            P.x = a * math.sqrt(1 + u_normal**2) * math.cos(v_normal)
            P.y = b * math.sqrt(1 + u_normal**2) * math.sin(v_normal)
            P.z = c * u_normal
            glVertex3f(P.x, P.y, P.z)
            v += 0.1
        u += 0.1
    glEnd()
    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 1, 1)
    draw(10, 20, 10, 60)


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(width, height)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("hyperboloid")
    glOrtho(-width/2, height/2, -height/2, width/2, -height/2, width/2)
    glMatrixMode(GL_PROJECTION)
    glutDisplayFunc(display)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 40, 10, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glutMainLoop()
