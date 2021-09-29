from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width = 600
height = 600
xmin, xmax, ymin, ymax = -100, 200, -100, 200
listPoint = []


def computeCode(x, y):
    m = 0
    if x < xmin:
        m |= 1
    if x > xmax:
        m |= 2
    if y < ymin:
        m |= 4
    if y > ymax:
        m |= 8
    return m

def draw(x0, y0, x1, y1):
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2d(x0, y0)
    glVertex2d(x1, y1)
    glEnd()

def cohenSutherlandClip(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            if code_out & 8:
                x = x1 + (x2 - x1) * \
                    (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & 4:
                x = x1 + (x2 - x1) * \
                    (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & 2:
                y = y1 + (y2 - y1) * \
                    (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & 1:
                y = y1 + (y2 - y1) * \
                    (xmin - x1) / (x2 - x1)
                x = xmin
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    if accept:
        draw(x1, y1, x2, y2)

def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()
    if len(listPoint) == 2:
        cohenSutherlandClip(listPoint[0][0], listPoint[0][1],
                  listPoint[1][0], listPoint[1][1])
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("cohen_sutherland")
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glutInitWindowPosition(10, 10)
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()