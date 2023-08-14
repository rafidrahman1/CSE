from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

def choose_sign():
    """Asks user to choose sign"""
    sign = ""
    while sign not in ["X", "O"]:
        sign = input("Do you want to be X or O? ").upper()
    return sign


def choose_region(sign):
    """Asks user to choose a region to place their sign"""
    region = None
    while region not in range(1, 10):
        try:
            region = int(input(f"Choose a region (1-9) to place {sign}: "))
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 9.")
    return region




def play_game():
    """Plays the Tic Tac Toe game"""
    sign = choose_sign()
    print(f"You are {sign}.")
    # region = choose_region(sign)
    # print(f"Your chosen region {region}.")

    # while True:
    # player's turn
    for region in range(1, 10):
        region = choose_region(sign)
        print(f"Your chosen region {region}.")

        if (sign == "O"):
            if (region == 1):
                Midpoint_Line_Circle(80, 150, 150)  # Bottom left--1
            elif (region == 2):
                Midpoint_Line_Circle(80, 450, 150)  # Bottom middle--2
            elif (region == 3):
                Midpoint_Line_Circle(80, 700, 150)  # Bottom Right--3
            elif (region == 4):
                Midpoint_Line_Circle(80, 150, 450)  # Middle left--4
            elif (region == 5):
                Midpoint_Line_Circle(80, 450, 450)  # Middle middle--5
            elif (region == 6):
                Midpoint_Line_Circle(80, 700, 450)  # Middle Right--6
            elif (region == 7):
                Midpoint_Line_Circle(80, 150, 700)  # Top left--7
            elif (region == 8):
                Midpoint_Line_Circle(80, 450, 700)  # Top middle--8
            elif (region == 9):
                Midpoint_Line_Circle(80, 700, 700)  # Top Right--9


        if (sign == "X"):
            if (region == 1):
                draw_lines(100, 100, 270, 270)
                draw_lines(100, 270, 270, 100)  # Bottom left--1
            elif (region == 2):
                draw_lines(400, 100, 570, 270)
                draw_lines(400, 270, 570, 100)  # Bottom middle--2
            elif (region == 3):
                draw_lines(620, 100, 770, 270)
                draw_lines(620, 270, 770, 100)  # Bottom right--3
            elif (region == 4):
                draw_lines(100, 400, 270, 570)
                draw_lines(100, 570, 270, 400)  # Middle left--4
            elif (region == 5):
                draw_lines(400, 400, 570, 570)
                draw_lines(400, 570, 570, 400)  # Middle middle--5
            elif (region == 6):
                draw_lines(620, 400, 770, 570)
                draw_lines(620, 570, 770, 400)  # Middle right--6
            elif (region == 7):
                draw_lines(100, 630, 270, 770)
                draw_lines(100, 770, 270, 630)  # Top left--7
            elif (region == 8):
                draw_lines(400, 630, 570, 770)
                draw_lines(400, 770, 570, 630)  # Top middle--8


        # switch to other player's turn
        sign = "O" if sign == "X" else "X"



    #return sign, region



#play_game()
"""
def case():
    sign,region=play_game()

    if (sign=="O"):
        if (region==1):
            Midpoint_Line_Circle(80, 150, 150)  # Bottom left--1
        elif (region==2):
            Midpoint_Line_Circle(80, 450, 150)  # Bottom middle--2
        elif (region==3):
            Midpoint_Line_Circle(80, 700, 150)  # Bottom Right--3
        elif (region==4):
            Midpoint_Line_Circle(80, 150, 450)  # Middle left--4
        elif (region == 5):
            Midpoint_Line_Circle(80, 450, 450)  # Middle middle--5
        elif (region == 6):
            Midpoint_Line_Circle(80, 700, 450)  # Middle Right--6
        elif (region == 7):
            Midpoint_Line_Circle(80, 150, 700)  # Top left--7
        elif (region == 8):
            Midpoint_Line_Circle(80, 450, 700)  # Top middle--8
        elif (region == 9):
            Midpoint_Line_Circle(80, 700, 700)  # Top Right--9

    if (sign == "X"):
        if (region == 1):
            draw_lines(100, 100, 270, 270)
            draw_lines(100, 270, 270, 100)  # Bottom left--1
        elif (region == 2):
            draw_lines(400, 100, 570, 270)
            draw_lines(400, 270, 570, 100)  # Bottom middle--2
        elif (region == 3):
            draw_lines(620, 100, 770, 270)
            draw_lines(620, 270, 770, 100)  # Bottom right--3
        elif (region == 4):
            draw_lines(100, 400, 270, 570)
            draw_lines(100, 570, 270, 400)  # Middle left--4
        elif (region == 5):
            draw_lines(400, 400, 570, 570)
            draw_lines(400, 570, 570, 400)  # Middle middle--5
        elif (region == 6):
            draw_lines(620, 400, 770, 570)
            draw_lines(620, 570, 770, 400)  # Middle right--6
        elif (region == 7):
            draw_lines(100, 630, 270, 770)
            draw_lines(100, 770, 270, 630)  # Top left--7
        elif (region == 8):
            draw_lines(400, 630, 570, 770)
            draw_lines(400, 770, 570, 630)  # Top middle--8
        elif (region == 9):
            draw_lines(620, 630, 770, 770)
            draw_lines(620, 770, 770, 630)  # Bottom right--9
"""


def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def Midpoint_Line_Circle(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius
    circlePoints(x, y, x0, y0)

    while x < y:
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1
        circlePoints(x, y, x0, y0)

def circlePoints (x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)
def FindZone(dx,dy):
    Zone=0
    if (abs(dx)>=abs(dy)):
        if(dx>0 and dy>0):
            Zone=0
        elif(dx<0 and dy>0):
            Zone=3
        elif(dx<0 and dy<0):
            Zone=4
        elif(dx>0 and dy<0):
            Zone=7

    else:
        if(dx>0 and dy>0):
            Zone=1
        elif(dx<0 and dy>0):
            Zone=2
        elif(dx<0 and dy<0):
            Zone=5
        elif(dx>0 and dy<0):
            Zone=6

    #print(Zone)
    return Zone

def ConvertToZone0 (X, Y, Zone):
    if (Zone == 1):
        x = Y
        y = X
    elif (Zone==2):
        x = Y
        y = -X
    elif (Zone==3):
        x = -X
        y = Y
    elif (Zone==4):
        x = -X
        y = -Y
    elif (Zone==5):
        x = -Y
        y = -X
    elif (Zone==6):
        x = -Y
        y = X
    elif (Zone==7):
        x = X
        y = -Y
    elif (Zone==0):
        x = X
        y = Y
    return (x,y)

def MidPoint(x1, y1, x2, y2, Zone):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        # non-vertical line
        d  = (2*dy) - dx
        incE  = 2*dy
        incNE = 2*(dy - dx)
        y = y1

        glPointSize(2)  # pixel size. by default 1 thake
        glBegin(GL_POINTS)
        glVertex2f (x1,y1)

        for x in range(x1+1, x2+1):
            if (d>0):
                d = d + incNE
                y = y + 1
            else:
                d = d + incE

            px, py = OriginalZone(x, y, Zone)
            glVertex2f(px, py)

    else:
        # vertical line
        glPointSize(2)  # pixel size. by default 1 thake
        glBegin(GL_POINTS)
        glVertex2f(x1, y1)

        for y in range(y1+1, y2+1):
            px, py = OriginalZone(x1, y, Zone)
            glVertex2f(px, py)

    glEnd()


def OriginalZone (X, Y, Zone):

    if (Zone == 1):
       x = Y
       y = X
    elif(Zone == 2):
       x = -Y
       y = X
    elif (Zone ==3):
       x = -X
       y = Y
    elif (Zone==4):
        x = -X
        y = -Y
    elif (Zone==5):
        x = -Y
        y = -X
    elif (Zone==6):
        x = Y
        y = -X
    elif (Zone==7):
        x = X
        y = -Y
    elif (Zone==0):
        x = X
        y = Y
    return (x,y)


def draw_lines(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    zone = FindZone(dx, dy)

    px1, py1 = ConvertToZone0( x1, y1, zone)
    px2, py2 = ConvertToZone0( x2, y2, zone)

    MidPoint(px1, py1, px2, py2, zone)





def board():

    glColor3f(1.0,0.3,0.5)
    draw_lines(300, 100, 300, 800)
    draw_lines(600, 100, 600, 800)
    draw_lines(100, 300, 800, 300)
    draw_lines(100, 600, 800, 600)

    """
    #for (O) Case
    Midpoint_Line_Circle(80, 150, 150) #Bottom left--1
    Midpoint_Line_Circle(80, 450, 150) #Bottom middle--2
    Midpoint_Line_Circle(80, 700, 150) #Bottom Right--3

    Midpoint_Line_Circle(80, 150, 450) #Middle left--4
    Midpoint_Line_Circle(80, 450, 450) #Middle middle--5
    Midpoint_Line_Circle(80, 700, 450) #Middle Right--6

    Midpoint_Line_Circle(80, 150, 700) #Top left--7
    Midpoint_Line_Circle(80, 450, 700) #Top middle--8
    Midpoint_Line_Circle(80, 700, 700) #Top Right--9
    
    #for (X) Case
    draw_lines( 100, 100, 270, 270)
    draw_lines( 100,270, 270, 100)  # Bottom left--1

    draw_lines(400, 100, 570, 270)
    draw_lines(400, 270, 570, 100)  # Bottom middle--2

    draw_lines(620, 100, 770, 270)
    draw_lines(620, 270, 770, 100)  # Bottom right--3

    draw_lines(100, 400, 270, 570)
    draw_lines(100, 570, 270, 400)  # Middle left--4

    draw_lines(400, 400, 570, 570)
    draw_lines(400, 570, 570, 400)  # Middle middle--5

    draw_lines(620, 400, 770, 570)
    draw_lines(620, 570, 770, 400)  # Middle right--6

    draw_lines(100, 630, 270, 770)
    draw_lines(100, 770, 270, 630)  # Top left--7

    draw_lines(400, 630, 570, 770)
    draw_lines(400, 770, 570, 630)  # Top middle--8

    draw_lines(620, 630, 770, 770)
    draw_lines(620, 770, 770, 630)  # Bottom right--9
    """








def iterate():
   glViewport(0, 0, 800, 800)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
   glMatrixMode (GL_MODELVIEW)
   glLoadIdentity()

def showScreen():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glLoadIdentity()
   #glFlush()
   iterate()
   # glColor3f(1,0,1.0,1.0) #konokichur color set (RGB)
   #call the draw methods here
   #board()
   #case()
   #refresh()
   #play_game()
   glutSwapBuffers()

def refresh():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1000, 1000) #window size
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"Group project: Team 5") #window name
    glutDisplayFunc(showScreen)
    glutMainLoop()


refresh()
board()
play_game()
refresh()
print("refresh")