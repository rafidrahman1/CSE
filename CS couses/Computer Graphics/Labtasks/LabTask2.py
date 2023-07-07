from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
from MidPointNumbers import*

def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1, 0, 1) #color
    glVertex2f(x,y) #jekhane show korbe pixel, Cordinates
    glEnd()

def iterate():
    glViewport(0, 0, 5000, 5000)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


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

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
     #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(100, 100)
    # Drawing the number 0
    # midpoint_line_algorithm(10, 10, 10, 15)
    # midpoint_line_algorithm(10, 5, 10, 10)
    # midpoint_line_algorithm(10, 15, 5, 15)
    # midpoint_line_algorithm(5, 10, 5, 5)
    # midpoint_line_algorithm(5, 5, 10, 5) 
    # midpoint_line_algorithm(5, 10, 5, 15)     

    two(5,10,15)  

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(500, 125)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()



