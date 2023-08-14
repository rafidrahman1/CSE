from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Thread import *
from Reel import *
from NightBackground import *
from DayBackground import *
from Kite import *
from CircleThread import * 
from Sun import *
from Star import *

print("Day or Night?(d/n): ")
n=input()
x=0

def iterate():
    glViewport(0, 0, 2000, 2000)#zoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
 
def animate(_):
    global x

    x+=1
    if x==8:
        x=0

    glutPostRedisplay()  # Trigger a redraw

    # Call the animate function again after a delay
    glutTimerFunc(10, animate, 0)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    
    if n=="n":
       NightBackground()
       Star()
       Thread(x)
       Kite(x) 
       Reel()  
       CircleThread(x)  

    elif n=="d": 
       DayBackground()
       Sun(x)
       Thread(x)
       Kite(x) 
       Reel()  
       CircleThread(x)          

    elif n=="johncena":
       DayBackground()
       Sun(x)
       Thread(x)
       Reel()  
       CircleThread(x)

    else :
       DayBackground()
         
       
 

    glutSwapBuffers()
    


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(700, 100)#window position
window = glutCreateWindow(b"Let's fly a kite ez") #window name
glutDisplayFunc(showScreen)

# Start the animation by calling the animate function
glutTimerFunc(10, animate, 0)

# Start the main loop
glutMainLoop()



