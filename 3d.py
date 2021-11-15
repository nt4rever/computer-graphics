from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

X, Y, Z = 0, 0, 0
rotX, rotY, rotZ = 0, 0, 0
rotLx, rotLy, rotLz = 0, 0, 0
rotation = False
old_x, old_y = 0, 0
mousePressed = 1


def init():
    glShadeModel(GL_SMOOTH)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def drawings():
    global rotX, rotY, rotZ
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glRotatef(rotX, 1.0, 0.0, 0.0)
    glRotatef(rotY, 0.0, 1.0, 0.0)
    glRotatef(rotZ, 0.0, 0.0, 1.0)

    if rotation:
        rotX += 0.2
        rotY += 0.2
        rotZ += 0.2
    glTranslatef(X, Y, Z)

    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.50, 0.50, 1.0)
    glVertex3f(3.0, 3.0, -3.0)
    glVertex3f(3.0, -3.0, -3.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, 3.0)
    glVertex3f(3.0, 3.0, -3.0)
    glVertex3f(3.0, -3.0, -3.0)
    glVertex3f(3.0, -3.0, 3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.50, 1.0, 0.50)
    glVertex3f(-3.0, 3.0, 3.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(3.0, 3.0, 3.0)
    glVertex3f(3.0, 3.0, -3.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.50, 0.50)
    glVertex3f(3.0, -3.0, 3.0)
    glVertex3f(3.0, -3.0, -3.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glEnd()
    
    glDisable(GL_LINE_STIPPLE)
    glutPostRedisplay()
    glPopMatrix()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75, w / h, 0.10, 500.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def keyboard(key, x, y):
    global X, Y, Z, rotX, rotY, rotZ, rotLx, rotLy, rotLz, rotation
    if key == b'x':
        rotX += 2.0
    if key == b'X':
        rotX -= 2.0
    if key == b'y':
        rotY -= 2.0
    if key == b'Y':
        rotY += 2.0
    if key == b'z':
        rotZ -= 2.0
    if key == b'Z':
        rotZ += 2.0
    if key == b'j':
        rotLx -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    if key == b"J":
        rotLx += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    if key == b'k':
        rotLy -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    if key == b'K':
        rotLy += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        print(rotLx,rotLy,rotLz)
    if key == b'l':
        if rotLz + 14 >= 0:
            rotLz -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    if key == b'L':
        rotLz += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    if key == b'b':
        rotX += 90.0
    if key == b'B':
        rotX -= 90.0
    if key == b'n':
        rotY -= 90.0
    if key == b'N':
        rotY += 90.0
    if key == b'm':
        rotZ -= 90.0
    if key == b'M':
        rotZ += 90.0
    if key == b'o':
        rotation = False
        X = Y = Z = 0.0
        rotX = rotY =  rotZ = 0.0;
        rotLx = rotLy = rotLz = 0.0;
    glutPostRedisplay()


def specialKey(key, x, y):
    global X, Y, Z, rotation
    if key == GLUT_KEY_LEFT:
        X -= 2.0
    if key == GLUT_KEY_RIGHT:
        X += 2.0
    if key == GLUT_KEY_UP:
        Y += 2.0
    if key == GLUT_KEY_DOWN:
        Y -= 2.0
    if key == GLUT_KEY_PAGE_UP:
        Z -= 2.0
    if key == GLUT_KEY_PAGE_DOWN:
        Z += 2.0
    if key == GLUT_KEY_F2:
        rotation = not rotation
    glutPostRedisplay()


def processMouseActiveMotion(button, state, x, y):
    global mousePressed, old_x, old_y
    mousePressed = button
    old_x = x
    old_y = y


def processMouse(x, y):
    global X, Y
    if mousePressed == 0:
        X = (x - old_x) / 15
        Y = -(y - old_y) / 15
    glutPostRedisplay()


def processMouseWheel(wheel, direction, x, y):
    global Z
    Z += direction
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow("Xauu")
init()
glutReshapeFunc(reshape)
glutDisplayFunc(drawings)
glutKeyboardFunc(keyboard)
glutSpecialFunc(specialKey)
glutMouseFunc(processMouseActiveMotion)
glutMotionFunc(processMouse)
glutMouseWheelFunc(processMouseWheel)
glutMainLoop()
