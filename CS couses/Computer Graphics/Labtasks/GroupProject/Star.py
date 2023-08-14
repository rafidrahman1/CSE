from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def Star():
 def draw_points(x, y, a, b, c):
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(a, b, c) #color
    glVertex2f(x,y) #jekhane show korbe pixel, Cordinates
    glEnd()

 for i in range(100):
     n = random.randint(5,170)#random x axis point
     p = random.randint(100,200)#random y axis point
     a = random.randint(0,1)#radom color
     b = random.randint(0,1)
     c = random.randint(0,1)
     draw_points(n,p,a,b,c)