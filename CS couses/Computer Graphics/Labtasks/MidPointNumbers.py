from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1, 0, 1) #color
    glVertex2f(x,y) #jekhane show korbe pixel, Cordinates
    glEnd()


#convert to original zone
def OriginalZone(x,y,zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

#convert to zone zero
def ZoneZero(x, y, zone):
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


def MidpointLine(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    zone=0
      
    #Zone finding
    if ((dx)>(dy)):
        if(dx>0 & dy>0):
            zone= 0
        elif(dx<0 & dy>0):
            zone= 3
        elif(dx>0 & dy<0):
            zone= 7
        elif(dx<0 & dy<0):
            zone= 4

    else:
        if(dx>0 & dy>0):
            zone= 1    
        elif(dx<0 & dy>0):
            zone= 2             
        elif(dx<0 & dy<0):
            zone= 5   
        elif(dx>0 & dy<0):
            zone= 6

    #Convert to zone 0
    x0, y0 = ZoneZero(x0, y0, zone)
    x1, y1 = ZoneZero(x1, y1, zone)

    

    E = 1 if x0 < x1 else -1
    NE = 1 if y0 < y1 else -1
    d = dx - dy

    while x0 != x1 or y0 != y1:
        draw_points(*OriginalZone(x0, y0, zone))
        e2 = 2 * d
        if e2 > -dy:
            d -= dy
            x0 += E
        if e2 < dx:
            d += dx
            y0 += NE

    draw_points(*OriginalZone(x0, y0, zone))

    
        
 
#numbers
def zero(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, b, s, x)
    MidpointLine(s, z, s, b)
    MidpointLine(s, z, a, z) 
    MidpointLine(s, x, a, x)  
    

def one(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(a, z, a, b)
    

def two(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(s, z, s, b)
    MidpointLine(s, b, a, b)
    MidpointLine(s, z, a, z)
    MidpointLine(s, x, a, x)     
    
   
def three(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, b, a, b)
    MidpointLine(s, z, a, z)
    MidpointLine(s, x, a, x)   
    

def four(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(s, b, s, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, b, a, b)  
    

def five(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(s, b, s, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, b, a, b)
    MidpointLine(s, z, a, z)
    MidpointLine(s, x, a, x)    
    

def six(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(s, b, s, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, z, s, b)
    MidpointLine(s, b, a, b)
    MidpointLine(s, z, a, z)
    MidpointLine(s, x, a, x)     

def seven(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, x, a, x)
    
def eight(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, b, s, x)
    MidpointLine(s, z, s, b)
    MidpointLine(s, b, a, b) 
    MidpointLine(s, z, a, z)
    MidpointLine(s, x, a, x) 

def nine(a,b):
    x=b+20
    z=b-20
    s=a-20
    MidpointLine(a, b, a, x)
    MidpointLine(s, b, s, x)
    MidpointLine(a, z, a, b)
    MidpointLine(s, b, a, b)
    MidpointLine(s, z, a, z)  
    MidpointLine(s, x, a, x)        