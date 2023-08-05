from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MidPointCircle import *
import array as arr
import math

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
    

    r=200 
    sr=r/2  
    c_x=300
    c_y=300
    MidpointCircle(r, c_x, c_y)

    for i in range(8):
        angle = (2*math.pi * i) / 8
        offset_x = int(r * math.cos(angle))/2
        offset_y = int(r * math.sin(angle))/2
        
        MidpointCircle(sr, c_x + offset_x, c_y + offset_y)
    
    



    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(500, 125)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()



