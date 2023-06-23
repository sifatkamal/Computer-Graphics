from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()\




def draw_lines(x1, y1, x2, y2):
    glPointSize(10)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()


def draw_triangles(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()







def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here

    # roof

    # draw_triangles(200, 400, 400, 400, 300, 500)

    draw_lines(200, 400, 300, 500)

    draw_lines(400, 400, 300, 500)

    draw_lines(200, 400, 400, 400)

    # house

    draw_lines(200, 400, 200, 200)

    draw_lines(200, 200, 400, 200)

    draw_lines(400, 200, 400, 400)

    # window_1

    draw_lines(230, 370, 280, 370)

    draw_lines(230, 320, 280, 320)

    draw_lines(230, 370, 230, 320)

    draw_lines(280, 370, 280, 320)

    # window_2

    draw_lines(320, 370, 370, 370)

    draw_lines(320, 320, 370, 320)

    draw_lines(320, 370, 320, 320)

    draw_lines(370, 370, 370, 320)


    # door

    draw_lines(280, 290, 320, 290)

    draw_lines(280, 290, 280, 200)

    draw_lines(320, 290, 320, 200)


    # Lock

    draw_points(310, 245)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()