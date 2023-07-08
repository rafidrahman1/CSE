from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from MidPointNumbers import *
import array as arr

print("Enter your ID: ")
x = input()
arr = [int(x) for x in str(x)]

def iterate():
    glViewport(0, 0, 9000, 9000)#zoom
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
    a=15
    b=20
    c=25
    
    j=len(arr)-2


    for i in range(2):
        if arr[j]==0:
           zero(a,b,c)
        elif arr[j]==1:
            one(a,b,c) 
        elif arr[j]==2:
            two(a,b,c)     
        elif arr[j]==3:
            three(a,b,c)
        elif arr[j]==4:
            four(a,b,c)
        elif arr[j]==5:
            five(a,b,c)
        elif arr[j]==6:
            six(a,b,c)
        elif arr[j]==7:
            seven(a,b,c)
        elif arr[j]==8:
            eight(a,b,c)
        else:
            nine(a,b,c)      

        a+=7
        b+=7
        c+=7
        j+=1
    
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(500, 125)#window position
window = glutCreateWindow(b"500 taka vangti lagbe") #window name
glutDisplayFunc(showScreen)
glutMainLoop()



