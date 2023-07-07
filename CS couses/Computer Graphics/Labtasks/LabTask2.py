from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MidPointNumbers import*


def iterate():
    glViewport(0, 0, 1000, 1000)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
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



