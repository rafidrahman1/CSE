from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def midpoint_line_algorithm(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    d = dy - (dx / 2)
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    x = x0
    y = y0
    draw_points(x, y)

    while x < x1:
        x += 1
        if d <= 0:
            # Choose E
            d = d + incrE
        else:
            # Choose NE
            d = d + incrNE
            y += 1

        draw_points(x, y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    # Drawing the number "2"
    midpoint_line_algorithm(100,100, 100, 950)
    
        
   
    glFlush()

def main():
    glutInit()
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"OpenGL Number 2")
    gluOrtho2D(0, 400, 0, 400)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()