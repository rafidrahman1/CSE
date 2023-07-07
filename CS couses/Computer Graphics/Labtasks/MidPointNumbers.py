from OpenGL.GL import *


def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
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

# def zero(a,b,c):
#     glBegin(GL_POINTS)
#     glColor3f(1.0, 0.0, 1.0)
    
#     midpoint_line_algorithm(10, 10, 10, 15)
#     midpoint_line_algorithm(10, 5, 10, 10)
#     midpoint_line_algorithm(10, 15, 5, 15)
#     midpoint_line_algorithm(5, 10, 5, 5)
#     midpoint_line_algorithm(5, 5, 10, 5) 
#     midpoint_line_algorithm(5, 10, 5, 15)  

#     glEnd()

'''
def one(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glEnd()
'''
def two(a,b,c):
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    #vertical
    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(a, b, a, a)
    midpoint_line_algorithm(a, a, b, a)     
   
    glEnd()
'''
def three(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()    

def four(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)
   
    glEnd()  

def five(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()    

def six(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()  

def seven(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)
 
    #horizontal
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()

def eight(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical    
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glVertex2f(s, b)
    glVertex2f(s, x)
    
    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)

    glEnd()

def nine(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
  
    glEnd()  
    ''' 