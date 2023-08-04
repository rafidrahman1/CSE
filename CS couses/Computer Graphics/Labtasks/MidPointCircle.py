from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



extend = 150

def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1, 0, 1) #color
    glVertex2f(x,y)
    

    #jekhane show korbe pixel, Cordinates
    glEnd()

def draw_spoints(more_x,more_y,x,y):
    draw_points(more_x + x, more_y + y)
    draw_points(more_x - x, more_y + y)
    draw_points(more_x + x, more_y - y)
    draw_points(more_x - x, more_y - y)
    draw_points(more_x + y, more_y + x)
    draw_points(more_x - y, more_y + x)
    draw_points(more_x + y, more_y - x)
    draw_points(more_x - y, more_y - x)

def sym(x, y, more_x, more_y):
    draw_points(more_x + x, more_y + y)
    draw_points(more_x - x, more_y + y)
    draw_points(more_x + x, more_y - y)
    draw_points(more_x - x, more_y - y)
    draw_points(more_x + y, more_y + x)
    draw_points(more_x - y, more_y + x)
    draw_points(more_x + y, more_y - x)
    draw_points(more_x - y, more_y - x)

def sm_sym(x, y, more_x, more_y,r):
    more_x+=15+150
    more_y+=15+150
    draw_spoints(more_x,more_y,x,y)
    more_x= r
    more_y= r 
    more_x+=85+150
    more_y+=85+150  

    draw_spoints(more_x,more_y,x,y)   
    more_x= r
    more_y= r+150
    more_x+= 50+150
    draw_spoints(more_x,more_y,x,y)
    more_x= r+150
    more_y= r
    more_y+= 50+150
    draw_spoints(more_x,more_y,x,y)
    more_x= r
    more_y= r
    more_x+= 100+150
    more_y+= 50+150
    draw_spoints(more_x,more_y,x,y)
    more_x= r
    more_y= r
    more_x+= 50+150
    more_y+= 100+150
    draw_spoints(more_x,more_y,x,y) 
    more_x= r
    more_y= r
    more_x+= 85+150
    more_y+= 15+150
    draw_spoints(more_x,more_y,x,y)
    more_x= r
    more_y= r
    more_x+= 15+150
    more_y+= 85+150
    draw_spoints(more_x,more_y,x,y)


def MidpointCircle(r):
    more_x= r+150
    more_y= r+150
    d= 1-r
    x= 0
    y= r
    sr=r/2 #small circle
    while x<=y:
        sym(x,y,more_x,more_y)
        if(d<0):
            #choose E
            d= d+ 2*x +3
            x+=1

        else:
            #choose SE
            d= d+ 2*x - 2*y +5
            x+=1
            y-=1

def MidpointSmallCircle(r):
    more_x= r
    more_y= r
    d= 1-r
    x= 0
    y= r
    while x<=y:
        sm_sym(x,y,more_x,more_y,r)
        if(d<0):
            #choose E
            d= d+ 2*x +3
            x+=1

        else:
            #choose SE
            d= d+ 2*x - 2*y +5
            x+=1
            y-=1
      



                



