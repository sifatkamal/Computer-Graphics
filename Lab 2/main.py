from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def find_zone(dx, dy):

    if dx > -1 and dy > -1:

        if abs(dx) >= abs(dy):

            return 0

        else:

            return 1

    elif dx < 0 and dy > -1:

        if abs(dx) < abs(dy):

            return 2

        else:

            return 3

    elif dx < 0 and dy < 0:

        if abs(dx) >= abs(dy):

            return 4

        else:

            return 5

    else:

        if abs(dx) < abs(dy):

            return 6

        else:

            return 7

def zone0_conversion(x1, y1, x2, y2, zone):


    if zone == 0:

        x1, y1 = x1, y1

        x2, y2 = x2, y2

    elif zone == 1:

        x1, y1 = y1, x1

        x2, y2 = y2, x2



    elif zone == 2:

        x1, y1 = y1, -x1

        x2, y2 = y2, -x2




    elif zone == 3:

        x1, y1 = -x1, y1

        x2, y2 = -x2, y2



    elif zone == 4:

        x1, y1 = -x1, -y1

        x2, y2 = -x2, -y2



    elif zone == 5:

        x1, y1 = -y1, -x1

        x2, y2 = -y2, -x2


    elif zone == 6:

        x1, y1 = -y1, x1

        x2, y2 = -y2, x2


    elif zone == 7:

        x1, y1 = x1, -y1

        x2, y2 = x2, -y2

    return x1, y1, x2, y2



def DrawLine(x1, y1, x2, y2):

    dx = x2 - x1

    dy = y2 - y1

    zone = find_zone(dx, dy)

    x1, y1, x2, y2 = zone0_conversion(x1, y1, x2, y2, zone)

    X0 = []

    Y0 = []

    D = []



    dx = x2 - x1

    dy = y2 - y1

    d = 2*dy-dx



    D = D + [d]

    incE = 2 * dy

    incNE = 2 * (dy - dx)

    x = x1

    y = y1


    while x<=x2:

        tempx = x

        tempy = y

        X0+=[x]

        Y0 += [y]

        tempx, tempy = convert_to_origin_zone(tempx, tempy, zone)

        draw_points(tempx, tempy)

        x+=1

        if (d > 0):

            d = d + incNE

            y = y + 1

        else:

            d = d + incE

            D+=[d]

def convert_to_origin_zone(x, y, zone):

    if zone == 0:

        return x, y

    elif zone == 1:

        return y, x

    elif zone == 2:

        return -y, x

    elif zone == 3:

        return -x, y

    elif zone == 4:

        return -x, -y

    elif zone == 5:

        return -y, -x

    elif zone == 6:

        return y, -x

    elif zone == 7:

        return x, -y



# ===========================================================================


def top(x):

  DrawLine(x+50, 400, x+100, 400)

def mid(x):

  DrawLine(x+50, 350, x+100, 350)

def bottom(x):

  DrawLine(x+50, 300, x+100, 300)

def left_above(x):

  DrawLine(x+50, 400, x+50, 350)

def left_bottom(x):

  DrawLine(x+50, 350, x+50, 300)

def right_above(x):

  DrawLine(x+100, 400, x+100, 350)

def right_bottom(x):

  DrawLine(x+100, 350, x+100, 300)





# Output

def output(value, x):

    if value == "0":

        top(x)

        right_above(x)

        right_bottom(x)

        left_above(x)

        left_bottom(x)

        bottom(x)

    elif value == "1":

        right_above(x)

        right_bottom(x)

    elif value == "2":

        top(x)

        right_above(x)

        mid(x)

        left_bottom(x)

        bottom(x)

    elif value == "3":

        top(x)

        right_above(x)

        mid(x)

        right_bottom(x)

        bottom(x)

    elif value == "4":

        left_above(x)

        mid(x)

        right_above(x)

        right_bottom(x)


    elif value == "5":

        top(x)

        left_above(x)

        mid(x)

        right_bottom(x)

        bottom(x)


    elif value == "6":

        top(x)

        left_above(x)

        left_bottom(x)

        mid(x)

        right_bottom(x)

        bottom(x)

    elif value == "7":

        top(x)

        right_above(x)

        right_bottom(x)

    elif value == "8":

        top(x)

        left_above(x)

        left_bottom(x)

        mid(x)

        right_above(x)

        right_bottom(x)

        bottom(x)

    elif value == "9":

        top(x)

        left_above(x)

        mid(x)

        right_above(x)

        right_bottom(x)

        bottom(x)



# ===========================================================================


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
   glColor3f(1.0, 1.0, 0.0)





   student_id = "20101223"

   list(student_id)

   digit = student_id[-2] + student_id[-1]

   distance = 0

   for i in digit:

       output(i, distance)

       distance += 70




   glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)

glutMainLoop()

















