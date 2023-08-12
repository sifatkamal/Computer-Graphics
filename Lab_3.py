import math
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_points(x, y):

    glPointSize(3)

    glBegin(GL_POINTS)

    glVertex2f(x, y)

    glEnd()

def draw_circle(x0, y0, radius):

    d = 1-radius

    x1 = 0

    y1 = radius

    while x1 < y1:

        x1 += 1

        if d < 0:

            d = d+2*x1+1

        else:

            y1 -= 1

            d = d+2*x1-2*y1+1

        draw_points(x0+x1, y0+y1)

        draw_points(x0-x1, y0+y1)

        draw_points(x0+x1, y0-y1)

        draw_points(x0-x1, y0-y1)

        draw_points(x0+y1, y0+x1)

        draw_points(x0-y1, y0+x1)

        draw_points(x0+y1, y0-x1)

        draw_points(x0-y1, y0-x1)

def iterate():

    glViewport(0, 0, 700, 700)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)

    glMatrixMode (GL_MODELVIEW)

    glLoadIdentity()

def showScreen():

    x0, y0, radius = 350, 350, 250

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    iterate()

    glColor3f(136, 8, 8)

    h = radius//2

    q = math.floor(math.sqrt(((radius/2)**2)/2))

    # Big Circle

    draw_circle(x0, y0, radius)

    # Upper Circle

    draw_circle(x0, y0+h, h)

    # Right Circle

    draw_circle(x0+h, y0, h)

    # Left Circle

    draw_circle(x0-h, y0, h)

    # Lower Circle

    draw_circle(x0, y0-h, h)

    # Upper Right Circle

    draw_circle(x0+q, y0+q, h)

    # Lower Right Circle

    draw_circle(x0+q, y0-q, h)

    # Lower Left Circle

    draw_circle(x0-q, y0-q, h)

    # Upper Left Circle

    draw_circle(x0-q, y0+q, h)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(10, 10)
wind = glutCreateWindow("Circles")
glutDisplayFunc(showScreen)
glutMainLoop()
