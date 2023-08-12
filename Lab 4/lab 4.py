from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def transform():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(.5, .3, .7)
    glPointSize(5)

    glBegin(GL_LINES)
    glVertex2f(250, 500)
    glVertex2f(250, 0)
    glVertex2f(0, 250)
    glVertex2f(500, 250)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    glVertex2f(200, 300)
    glVertex2f(200, 200)
    glVertex2f(300, 200)
    glVertex2f(300, 300)
    glEnd()











    # Translation
    tx = 30
    ty = 0
    t = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])


    # scaling

    sc = 1
    s = np.array([[sc, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])

    ts = np.matmul(t, s)

    v1 = np.array([[-50],
                   [50],
                   [1]])
    v2 = np.array([[-50],
                   [-50],
                   [1]])
    v3 = np.array([[50],
                   [-50],
                   [1]])
    v4 = np.array([[50],
                   [50],
                   [1]])






    # translation and scaling
    ts = np.matmul(t, s)

    v11 = np.matmul(ts, v1)
    v22 = np.matmul(ts, v2)
    v33 = np.matmul(ts, v3)
    v44 = np.matmul(ts, v4)







    #
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(v11[0][0] + 250, v11[1][0] + 250)
    glVertex2f(v22[0][0] + 250, v22[1][0] + 250)
    glVertex2f(v33[0][0] + 250, v33[1][0] + 250)
    glVertex2f(v44[0][0] + 250, v44[1][0] + 250)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    transform()

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()