from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Thread import *
from Reel import *
from Background import *
from Kite import *
from CircleThread import * 

x=input()

def iterate():
    glViewport(0, 0, 2000, 2000)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
 

def showScreen():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    
    Background()    
    Thread(x)
    Kite(x)    
    Reel()    
    CircleThread(x)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(700, 100)#window position
window = glutCreateWindow(b"Let's fly a kite ez") #window name
glutDisplayFunc(showScreen)
glutMainLoop()



