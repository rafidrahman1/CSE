from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MidPointNumbers import *
import array as arr

print("Enter your ID: ")
x = input()
arr = [int(x) for x in str(x)]

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
    # Drawing the number 0
    # MidpointLine(10, 10, 10, 15)
    # MidpointLine(10, 5, 10, 10)
    # MidpointLine(10, 15, 5, 15)
    # MidpointLine(5, 10, 5, 5)
    # MidpointLine(5, 5, 10, 5) 
    # MidpointLine(5, 10, 5, 15) 
    j=len(arr)-2
    z=230
    y=285
    for i in range(2):
        if arr[j]==0:
           zero(y,z)
        elif arr[j]==1:
            one(y,z) 
        elif arr[j]==2:
            two(y,z)     
        elif arr[j]==3:
            three(y,z)
        elif arr[j]==4:
            four(y,z)
        elif arr[j]==5:
            five(y,z)
        elif arr[j]==6:
            six(y,z)
        elif arr[j]==7:
            seven(y,z)
        elif arr[j]==8:
            eight(y,z)
        else:
            nine(y,z)      

        y+=30  
        j+=1
    
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(500, 125)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()



