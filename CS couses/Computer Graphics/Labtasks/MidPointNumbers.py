from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(20) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1, 0, 1) #color
    glVertex2f(x,y) #jekhane show korbe pixel, Cordinates
    glEnd()

def midpoint_line_algorithm(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy

    while x0 != x1 or y0 != y1:
        draw_points(x0, y0)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    draw_points(x0, y0)

def zero(a,b,c):
    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(a, b, a, a)
    midpoint_line_algorithm(a, a, b, a) 
    midpoint_line_algorithm(a, b, a, c)  

def one(a,b,c):
    midpoint_line_algorithm(a, b, a, c)
    midpoint_line_algorithm(a, a, a, b)
    

def two(a,b,c):

    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(a, b, a, a)
    midpoint_line_algorithm(a, a, b, a)     
   
def three(a,b,c):
    
    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(a, a, b, a)   

def four(a,b,c):
    
    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(a, b, a, c)  

def five(a,b,c):

    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(a, b, a, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(a, a, b, a)    

def six(a,b,c):

    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(a, a, a, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(a, b, a, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(a, a, b, a)     

def seven(a,b,c):

    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(b, c, a, c)
    
def eight(a,b,c):
    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(a, b, a, a)
    midpoint_line_algorithm(a, a, b, a) 
    midpoint_line_algorithm(a, b, a, c)
    midpoint_line_algorithm(a, b, b, b) 

def nine(a,b,c):
    
    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(a, c, b, c)
    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(a, b, a, c)         