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


    # 2

    draw_lines(50, 400, 100, 400)

    draw_lines(100, 400, 100, 350)

    draw_lines(50, 350, 100, 350)

    draw_lines(50, 300, 100, 300)

    draw_lines(50, 350, 50, 300)


    glColor3f(0.0, 1.0, 1.0)  # konokichur color set (RGB)

    # 0

    draw_lines(120, 400, 170, 400)

    draw_lines(120, 400, 120, 300)

    draw_lines(120, 300, 170, 300)

    draw_lines(170, 300, 170, 400)


    glColor3f(1.0, 0.0, 1.0)  # konokichur color set (RGB)

    # 1

    draw_lines(190, 400, 190, 300)


    glColor3f(0.0, 0.0, 1.0)  # konokichur color set (RGB)

    # 0

    draw_lines(210, 400, 260, 400)

    draw_lines(210, 400, 210, 300)

    draw_lines(210, 300, 260, 300)

    draw_lines(260, 400, 260, 300)


    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)

    # 1

    draw_lines(280, 400, 280, 300)


    glColor3f(0.0, 1.0, 0.0)  # konokichur color set (RGB)

    # 2

    draw_lines(300, 400, 350, 400)

    draw_lines(350, 400, 350, 350)

    draw_lines(300, 350, 350, 350)

    draw_lines(300, 300, 350, 300)

    draw_lines(300, 350, 300, 300)

    glColor3f(1.0, 0.0, 0.0)  # konokichur color set (RGB)



    # 3

    draw_lines(370, 400, 420, 400)

    draw_lines(420, 400, 420, 350)

    draw_lines(370, 350, 420, 350)

    draw_lines(420, 350, 420, 300)

    draw_lines(370, 300, 420, 300)



    glColor3f(0.54, 0.17, 0.89)  # konokichur color set (RGB)

    # 3

    draw_lines(440, 400, 440, 300)







    glutSwapBuffers()








glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()