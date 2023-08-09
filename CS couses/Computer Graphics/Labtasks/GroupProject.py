from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MidPointCircle import *
from MidPointNumbers import *
from Stage import *
import random
import array as arr


# print("Enter your ID: ")
# x = input()
# arr = [int(x) for x in str(x)]

def iterate():
    glViewport(0, 0, 2000, 2000)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
 

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #Natai
    MidpointLine(40, 20, 40, 50)
    MidpointLine(20, 35, 40, 35)
    MidpointLine(135, 20, 135, 50)
    MidpointLine(135, 35, 155, 35)
    x=25
    for i in range(21):
       MidpointLine(40, x, 135, x)
       x+=1
    #Natai er Suta.
    Stages(4)

    


    
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(700, 100)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()



