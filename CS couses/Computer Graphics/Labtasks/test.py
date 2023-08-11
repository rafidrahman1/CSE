from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

# Initialize PyOpenGL
glutInit(sys.argv)

# Set up the display
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Square Translation Example")

# Define the square's properties
square_size = 0.2
initial_x, initial_y = -0.5, -0.5
current_x, current_y = initial_x, initial_y

# Define the translation amount
translation_x = 0.5
translation_y = 0.5

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(current_x, current_y)
    glVertex2f(current_x + square_size, current_y)
    glVertex2f(current_x + square_size, current_y + square_size)
    glVertex2f(current_x, current_y + square_size)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)  # Blue color

    # Perform translation
    global current_x, current_y
    current_x += translation_x
    current_y += translation_y

    # Draw the translated square
    draw_square()

    glFlush()

# Set up the initial state
glClearColor(1.0, 1.0, 1.0, 1.0)  # White background

# Register the display function
glutDisplayFunc(display)

# Start the main loop
glutMainLoop()