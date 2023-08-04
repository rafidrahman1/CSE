from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def plot_symmetric_points(x, y, cx, cy):
    
    glVertex2f(cx + x, cy + y)
    glVertex2f(cx - x, cy + y)
    glVertex2f(cx + x, cy - y)
    glVertex2f(cx - x, cy - y)
    glVertex2f(cx + y, cy + x)
    glVertex2f(cx - y, cy + x)
    glVertex2f(cx + y, cy - x)
    glVertex2f(cx - y, cy - x)
    

def midpoint_circle_algorithm(radius):
    cx, cy = radius, radius
    x, y = 0, radius
    d = 1 - radius

    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    while x <= y:
        plot_symmetric_points(x+50, y+50, cx, cy)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1

        x += 1
    glEnd()

def iterate():
    glViewport(0, 0, 700, 700)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glPointSize(5.0)
    midpoint_circle_algorithm(150)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(500, 125)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()


